#!/bin/bash
#https://stackoverflow.com/questions/4904067/get-live-hosts-mac-in-local-network


#HOSTS=$(nmap -sP -n -oG - 192.168.1.1-10 | grep "Up" | awk '{print $2}')

HOSTS=$(nmap -sn -n -oG - 10.0.0.1/24 | grep "Up" | awk '{print $2}')

for host in ${HOSTS}; do
  arp -an | grep ${host} | awk '{print $2 $4}'
done


# Currently doesn't work, just do 
#nmap -PR ip_of_router/24
# ARP sweep of nmap
# http://nmap.org/book/man-host-discovery.html
