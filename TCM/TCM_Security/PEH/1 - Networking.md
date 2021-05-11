# Networking
## IP Addresses
 
OSI Layer 3  
IPv4:  
32 bits -> 4 bytes  
4 x 8 bits -> 4 bytes  
128 64 32 16 8 4 2 1  
1 1 1 1 1 1 1 1 -> 255  
Classes:  
Class A: 10.0.0.0 255.0.0.0 : 126 Number of Networks and 16 646 144 Hosts  
Class B: 172.16.0.0-172.31.0.0 255.255.0.0 : 16 383 Number of Networks and 65 024 Hosts  
Class C: 192.168.0.0-192.168.255.255 255.255.255.0 : 2 097 151 Number of Networks and 254 Hosts  
IPv6:  
128 bits -> 16 bytes  
uses Hexadeximal numbers  
  
  
NAT:  
Network address translation

### Linux Command to view configuration
~~~bash
ifconfig -view ip configuration
~~~

---
## MAC Addresses

OSI Layer 2  
NIC - Network Interface Card  
First 3 Pair is the identifiers

---
## TCP, UDP and The Three-Way Handshake

OSI Layer 4:  
TCP - Transmission Control Protocol  
UDP- User Datagram Protocol  
  
TCP - highly reliable  
	-FTP  
	-HTTP-HTTPS  
	-SSH  
  
UDP  
	-DNS  
	-Streaming  
	-Voice over IP (VoIP)  
  
Three-Way Handshake:  
	SYN > SYN ACK > ACK  
	Hello > Hello > GoodToGo  
SYN:  
	ACK: Acknowledge  
  
Example:  
	You send you want to connect  
		if host is up and port is open, it send back a response  
			if you want to connect, you send an ACK  
  
Tool:  
	Wireshark
	
---
## Common Ports and Protocols 

### TCP
 FTP - 21 - File Transfer Protocol  
SSH - 22 - Secure Shell  
Telnet - 23 - Log in to a computer  
SMTP - 25 - Mail  
DNS - 53 - Domain Name System  
HTTP - 80 - WebSite (non secure)  
HTTPS - 443 - WebSite (encrypted)  
POP3 - 110 - Mail  
SMB - 139 and 443 - File Shares (Samba)  
IMAP 143 - Mail

### UDP
DNS - 53 - Domain Name System  
DHCP - 67 or 68 - Dynamic Host Control Protocol  
TFTP - 69 - Trivial FTP  
SNMP - 161 - Simple Network Managment Protocol

---
## OSI Model

Layer 1 - P - Physical Layer - data cables  
Layer 2 - D - Data Layer - Switching, MAC addresses  
Layer 3 - N - Network Layer - IP addresses, routing  
Layer 4 - T - Transport Layer - TCP/UDP  
Layer 5 - S - Session Layer - session management  
Layer 6 - P - Presentation Layer - WMV, JPEG, MOV  
Layer 7 - A - Application Layer - HTTP, HTTPS, SMTP  
  
Please do not throw sausage pizza away  
  
Troubleshooting -  
From 1 - 7

---
## Subnetting
![https://github.com/FGabi01/TCM_Security/blob/main/TCM/TCM_Security/Pictures/subnetting.png]
www.ipaddressguide.com/cidr
---
