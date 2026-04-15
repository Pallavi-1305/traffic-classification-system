from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

stats = {"TCP":0, "UDP":0, "ICMP":0, "OTHER":0}

def _handle_PacketIn(event):
    data = event.ofp.data

    if len(data) < 24:
        return

    # Ethernet type bytes 12-13
    eth_type = int.from_bytes(data[12:14], byteorder='big')

    # IPv4
    if eth_type == 0x0800 and len(data) >= 24:
        proto = data[23]

        if proto == 1:
            stats["ICMP"] += 1
            log.info("ICMP Packet Detected")

        elif proto == 6:
            stats["TCP"] += 1
            log.info("TCP Packet Detected")

        elif proto == 17:
            stats["UDP"] += 1
            log.info("UDP Packet Detected")

        else:
            stats["OTHER"] += 1
            log.info("Other IP Packet")

    else:
        stats["OTHER"] += 1
        log.info("Non-IP Packet")

    log.info("Stats: %s", stats)

    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg)

def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    log.info("Traffic Classification Started")
