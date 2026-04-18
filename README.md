# Traffic Analysis System using SDN (POX + Mininet)

## Objective
The objective of this project is to classify network traffic into TCP, UDP, ICMP, and OTHER packets, monitor live traffic metrics, detect traffic spikes, and generate comparative reports before and after high traffic conditions.

---

## Tools Used
- Ubuntu Virtual Machine
- Mininet
- POX Controller
- OpenFlow
- iperf
- GitHub

---

## Topology Used
- 1 Switch (`s1`)
- 3 Hosts (`h1`, `h2`, `h3`)
- 1 Remote Controller (`c0`)

---

## Project File
- `traffic_classification.py`

---

# Execution Steps with Screenshots

## 1. Updated Code File
Screenshot of the final controller code with live metrics and report logic.

![Updated Code](code_updated.png)

<img width="894" height="846" alt="image" src="https://github.com/user-attachments/assets/d961e9ea-9e4c-492f-a27f-4c7bb2031b4c" />

<img width="869" height="790" alt="image" src="https://github.com/user-attachments/assets/548b7be6-540a-459d-8dbc-7aa2ac596c34" />

<img width="879" height="772" alt="image" src="https://github.com/user-attachments/assets/88e69d4e-3cb8-4b91-8866-b1bcaa6bf9a7" />

<img width="978" height="431" alt="image" src="https://github.com/user-attachments/assets/107c27e2-04b9-4f1e-b35a-347c08c89b77" />

---

## 2. Controller Started
Started the POX controller successfully.

![Controller Started](controller_started.png)

<img width="1184" height="359" alt="image" src="https://github.com/user-attachments/assets/3c4523ff-5b31-45eb-b86e-fc1261f67be0" />


---

## 3. Mininet Started
Started the Mininet topology.

![Mininet Started](mininet_started.png)

<img width="919" height="482" alt="image" src="https://github.com/user-attachments/assets/566d3ee2-f486-47fc-be8a-d179264bac8f" />


---

## 4. Nodes Output
Displayed all nodes in the topology.

![Nodes](nodes.png)

<img width="543" height="156" alt="image" src="https://github.com/user-attachments/assets/d8498cd1-b160-43bd-a302-a54918243153" />


---

## 5. Pingall Test (Before Spike)
Tested connectivity between all hosts.

![Pingall](pingall.png)

<img width="737" height="194" alt="image" src="https://github.com/user-attachments/assets/79a77388-207f-4f16-9c47-5a2d812eea48" />


---

## 6. Live Metrics During Before Phase
Displayed packet type, packets/sec, and bytes/sec during normal traffic.

![Before Metrics](before_live_metrics.png)

<img width="1008" height="777" alt="image" src="https://github.com/user-attachments/assets/5cac08d8-c4b8-4c03-942b-9e7193853fe4" />


---

## 7. TCP Traffic Test using iperf
Generated TCP traffic spike.

![TCP Test](tcp_test.png)

<img width="985" height="210" alt="image" src="https://github.com/user-attachments/assets/e5acac08-b994-4dab-95f4-3fb5ab13a031" />


---

## 8. Live Metrics After Spike (TCP)
Displayed live metrics during high TCP traffic.

![After TCP Metrics](after_tcp_metrics.png)

<img width="1020" height="663" alt="image" src="https://github.com/user-attachments/assets/a48baef1-edcc-40b9-a928-139246f008bd" />


---

## 9. UDP Traffic Test using iperf
Generated UDP traffic.

![UDP Test](udp_test.png)

<img width="1002" height="471" alt="image" src="https://github.com/user-attachments/assets/ea23578b-d32b-4e31-88d2-a22bf9364445" />

---

## 10. Live Metrics for UDP
Displayed UDP packet metrics.

![UDP Metrics](udp_metrics.png)

<img width="1128" height="523" alt="image" src="https://github.com/user-attachments/assets/a90eb20f-cdaf-4c6b-b870-57f5e8938209" />


---

## 11. Final Before Spike Report Table
Summary table for traffic before spike.

![Before Table](before_table.png)

<img width="955" height="208" alt="image" src="https://github.com/user-attachments/assets/c0e5670e-d8b3-4ac3-96ca-e58815e4a15c" />

---

## 12. Final After Spike Report Table
Summary table for traffic after spike.

![After Table](after_table.png)

---<img width="884" height="153" alt="image" src="https://github.com/user-attachments/assets/4ba0be4d-9e14-4e8e-a04f-fcfecbffdf93" />


## 13. Switch Details
Displayed Open vSwitch details.

![Switch Details](switch_details.png)

<img width="1194" height="735" alt="image" src="https://github.com/user-attachments/assets/c3aead78-36af-45b5-be49-1ed6a858addb" />

---

## 14. Cleanup
Cleaned old Mininet configuration.

![Cleanup](cleanup.png)

<img width="1190" height="617" alt="image" src="https://github.com/user-attachments/assets/4c69afd7-9aa4-47b7-9986-86e6b22c37e9" />

---

# Features Implemented
- Packet classification (TCP, UDP, ICMP, OTHER)
- Live traffic monitoring
- Packets per second calculation
- Bytes per second calculation
- Automatic traffic spike detection
- Before and After traffic comparison tables
- Traffic percentage analysis

---

# Working Principle
When a packet reaches the switch, it is sent to the POX controller using PacketIn. The controller checks the packet protocol type and classifies it. It calculates live traffic metrics such as packets per second and bytes per second. When heavy traffic starts using iperf, the system automatically detects the spike and moves to the after-spike phase. Finally, it prints two analysis tables comparing traffic before and after the spike.

---

# Results
- Successfully detected TCP, UDP, ICMP, and OTHER packets
- Displayed live metrics during traffic flow
- Detected traffic spike after iperf execution
- Generated before and after comparison reports
- Demonstrated SDN-based traffic monitoring system

---

# Conclusion
This project successfully implemented a Traffic Analysis System using SDN concepts with POX and Mininet. It classified packets, measured live performance, detected traffic spikes, and generated useful traffic reports.
