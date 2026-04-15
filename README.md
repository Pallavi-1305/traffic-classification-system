# Traffic Classification System

## Objective
Classify TCP, UDP and ICMP traffic using POX controller.

## Tools Used
Ubuntu VM, Mininet, POX, OpenFlow

## Topology
Single switch with 3 hosts

## Commands Used
python3 pox.py forwarding.traffic_classification
sudo mn --topo single,3 --controller remote
pingall
h1 iperf -s &
h2 iperf -c h1
h1 iperf -s -u &
h2 iperf -c h1 -u

## Result
Traffic classification executed successfully.
