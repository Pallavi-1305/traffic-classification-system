from pox.core import core
import pox.openflow.libopenflow_01 as of
import time

log = core.getLogger()

types = ["TCP", "UDP", "ICMP", "OTHER"]

before_stats = {t: 0 for t in types}
after_stats = {t: 0 for t in types}

phase = "before"
packet_counter = 0
SPIKE_START_AFTER = 50

start_before = time.time()
start_after = None

last_time = time.time()
sec_packets = 0
sec_bytes = 0

def classify_raw(data):
    if len(data) < 14:
        return "OTHER"

    eth_type = int.from_bytes(data[12:14], "big")

    if eth_type == 0x0800 and len(data) >= 24:
        proto = data[23]

        if proto == 1:
            return "ICMP"
        elif proto == 6:
            return "TCP"
        elif proto == 17:
            return "UDP"

    return "OTHER"

def print_table(title, stats, duration):
    total = sum(stats.values())

    log.info(" ")
    log.info("========== %s ==========", title)
    log.info("%-8s %-12s %-12s %-12s", "TYPE", "TOTAL", "PERCENT", "AVG PPS")

    for t in types:
        count = stats[t]
        percent = (count / total * 100) if total > 0 else 0
        avgpps = (count / duration) if duration > 0 else 0

        log.info("%-8s %-12d %-11.2f %-12.2f",
                 t, count, percent, avgpps)

def _handle_PacketIn(event):
    global phase, packet_counter, start_after
    global last_time, sec_packets, sec_bytes

    data = event.ofp.data
    ptype = classify_raw(data)
    size = len(data)

    packet_counter += 1
    sec_packets += 1
    sec_bytes += size

    # Live packet analysis
    now = time.time()
    diff = now - last_time

    if diff >= 1:
        pps = sec_packets / diff
        bps = sec_bytes / diff

        log.info("Time: %.2f | Phase: %s | Type: %s", now, phase.upper(), ptype)
        log.info("Packets/sec: %.2f | Bytes/sec: %.2f", pps, bps)

        sec_packets = 0
        sec_bytes = 0
        last_time = now

    # Auto spike detect
    if phase == "before" and packet_counter > SPIKE_START_AFTER:
        phase = "after"
        start_after = time.time()
        log.info("===== IPERF SPIKE DETECTED : AFTER PHASE STARTED =====")

    if phase == "before":
        before_stats[ptype] += 1
    else:
        after_stats[ptype] += 1

    # Forward packet
    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg)

def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)

    log.info("Traffic Analysis with Live Metrics Started")
    log.info("Run pingall first, then run iperf TCP/UDP.")
    log.info("Press Ctrl+C to print final tables.")

    def shutdown_handler():
        end_time = time.time()

        before_dur = (start_after - start_before) if start_after else (end_time - start_before)
        after_dur = (end_time - start_after) if start_after else 0

        print_table("BEFORE SPIKE", before_stats, before_dur)
        print_table("AFTER SPIKE", after_stats, after_dur)

    core.addListenerByName("DownEvent", lambda e: shutdown_handler())
