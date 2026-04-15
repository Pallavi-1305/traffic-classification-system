# Traffic Classification System using SDN (POX + Mininet)

## Objective
The objective of this project is to classify network traffic based on protocol type using Software Defined Networking (SDN). The controller identifies and maintains statistics for:

- TCP Packets
- UDP Packets
- ICMP Packets
- Other Packets

The project demonstrates controller-switch communication, packet handling, and traffic monitoring using POX and Mininet.

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
- Remote Controller (`c0`)

---

## Project Files

- `traffic_classification.py`
- `README.md`

---

# Execution Steps with Screenshots

---

## 1. Cloning POX Repository

Downloaded the POX controller using Git.

![Cloning POX](Screenshot%201.png)
<img width="962" height="1027" alt="Screenshot 1" src="https://github.com/user-attachments/assets/ddafc511-71a0-4e78-a954-e1341c017978" />

---

## 2. Creating Controller Code File

Created `traffic_classification.py` inside the forwarding folder.

### Code Screenshot - Part 1

![Code Part 1](Screenshot%20-21.png)
<img width="1053" height="766" alt="Screenshot -22" src="https://github.com/user-attachments/assets/12759795-1bf5-4554-88b5-3943c8316707" />

### Code Screenshot - Part 2

![Code Part 2](Screenshot%20-22.png)
<img width="1053" height="766" alt="Screenshot -22" src="https://github.com/user-attachments/assets/5e91d5b4-dbeb-4c20-b760-84300e24c958" />

---

## 3. Running POX Controller

Started the custom traffic classification controller.

![POX Running](Screenshot%20-31.png)
<img width="1097" height="347" alt="Screenshot -31" src="https://github.com/user-attachments/assets/1cfc18a2-3a51-4e07-97ee-3d30aec51995" />

---

## 4. Starting Mininet Topology

Started Mininet with 1 switch and 3 hosts using remote controller.

![Mininet Started](Screenshot%20-41.png)
<img width="1057" height="745" alt="Screenshot -41" src="https://github.com/user-attachments/assets/bd2e3d32-6aed-46e0-8958-6c02264577a0" />

---

## 5. Testing Connectivity using Ping

All hosts successfully communicated with each other.

![Ping Test](Screenshot%20-51.png)
<img width="648" height="247" alt="Screenshot -51" src="https://github.com/user-attachments/assets/013f007f-1bd2-478d-84d9-f5b05011c00a" />

---

## 6. ICMP Detection Logs

Controller detected ICMP packets and updated statistics.

![ICMP Logs](Screenshot%20-61.png)
<img width="1052" height="882" alt="Screenshot -61" src="https://github.com/user-attachments/assets/c23b5e0c-28cd-48da-9285-006b260362ed" />

---

## 7. TCP Traffic Test using iperf

Generated TCP traffic between hosts.

![TCP Test](Screenshot%20-71.png)
<img width="997" height="232" alt="Screenshot -71" src="https://github.com/user-attachments/assets/d4eb4026-5bdb-4c90-918c-678eeca56c87" />

---

## 8. TCP Detection Logs

Controller detected TCP packets successfully.

![TCP Logs](Screenshot%20-81.png)
<img width="888" height="502" alt="Screenshot -91" src="https://github.com/user-attachments/assets/1911ad79-e473-4372-9e11-eb454bea25e7" />

---

## 9. UDP Traffic Test using iperf

Generated UDP traffic between hosts.

![UDP Test](Screenshot%20-91.png)
<img width="888" height="502" alt="Screenshot -91" src="https://github.com/user-attachments/assets/b730db8c-c147-46c6-ad57-65bc37639cfb" />

---

## 10. UDP Detection Logs

Controller detected UDP packets and updated statistics.

![UDP Logs](Screenshot%20-10.png)
<img width="1002" height="788" alt="Screenshot -10" src="https://github.com/user-attachments/assets/00b1d054-16af-4da0-868a-316f7a479b2c" />

---

## Switch Details / OpenFlow Proof

Verified switch `s1` and active ports.

![Switch Details](Screenshot%20-11.png)
<img width="1212" height="721" alt="temp" src="https://github.com/user-attachments/assets/7baea2c1-54a9-4ab7-8323-f0036598c15b" />


---

## 12. Exiting Mininet

Closed the running topology successfully.

![Exit Mininet](Screenshot%20-12.png)
<img width="526" height="252" alt="Screenshot -12" src="https://github.com/user-attachments/assets/fb2009f8-4aed-48ba-8f18-a60b867be62f" />

---

## 13. Cleanup Command

Removed old Mininet configurations and cleaned the environment.

![Cleanup](Screenshot%20-13.png)
<img width="1192" height="527" alt="Screenshot -13" src="https://github.com/user-attachments/assets/d8c631f0-35c6-4fd1-9076-64f9b71183be" />

---

# Controller Logic Summary

The POX controller performs the following tasks:

- Receives packets from switch
- Checks protocol type
- Classifies as TCP / UDP / ICMP / Other
- Updates live statistics
- Floods packets for connectivity

---

# Test Scenarios

## Scenario 1: ICMP Traffic
Used `pingall` to generate ICMP packets.

## Scenario 2: TCP Traffic
Used `iperf` to generate TCP packets.

## Scenario 3: UDP Traffic
Used `iperf -u` to generate UDP packets.

---

# Results

- Successfully detected ICMP traffic
- Successfully detected TCP traffic
- Successfully detected UDP traffic
- Maintained packet statistics dynamically
- Demonstrated SDN controller and switch communication

---

# Conclusion

This project successfully implemented a Traffic Classification System using SDN concepts with POX controller and Mininet. The controller classified packets based on protocol type and displayed real-time statistics.

---
