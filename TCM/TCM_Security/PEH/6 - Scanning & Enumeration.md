# Scanning and Enumeration
## Resources
- Kioptrix  
- nmap  
- nikto -to scan web vulnerabilities --doesn't work if the website has good websecurity 
- smbclient

---

## Enumerating HTTP/HTTPS
- 80/443 - 192.168.1.3 - 10:36am
- Default webpage - Apache - PHP
- dirbuster/gobuster to scan for files and directories

---
## Enumerating SMB 
- Using metasploit module:
~~~bash
msfconsole start
use auxiliary/scanner/smb/smb_version
~~~
---
# Additional Scanning Tools
## [Masscan](https://github.com/robertdavidgraham/masscan.git)
Sometimes faster than nmap
~~~bash
#usage
masscan -p1-65535 IP$
~~~
---
## Metasploit
~~~bash
#usage
msfconsole
~~~
---
## Nessus
It is a vulnarability scanner
Access through web interface - port number 8834
~~~bash 
# After install
sudo /etc/init.d/nessusd start
# Then open webbrowser ei. https://localhost:8834
~~~

There are several scans offered
The pro version costs around $2400 - $4000 a year

---
