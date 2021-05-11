# Information Gathering
## (Reconnaissance)

## Passive Reconnaissance Overview
Types:
1.  Physical/Social
   - Location Information
      - Satellite images
      - Drone recon
      - Building layout (badge readers, break areas, security, fencing)
			
   - Job Information
       - Employees (name, job title, phone number, manager, etc.)
       -  Pictures (badge photos, desk photos, computer photos, etc)
            
   2. Web / Host
        - Target Validation  
           - WHOIS, nslookup, dnsrecon
            
        - Finding Subdomain
           - Google Fu, dig, Nmap, Sublist3r, Bluto, crt.sh, etc.
        
        - Fingerprinting
           - Nmap, Wappalyzer, WhatWeb, BuiltWith, Netcat
        
        - Data Breaches
           -  HaveIBeenPwned, Breach-Parse, WeLeakInfo

--------------------------------------------

## Identifying Our Target
*For the course, tesla will be in scope  
Everyime you search for a program at bugcrowd.com read the program details carefully, to see what pages is in scope, and what is out of scope*

--------------------------------------------

## E-mail Address Gathering using Hunter.io
Login creds for [hunter.io](https://hunter.io):
     forgacsgabor01(gmail):YesterdayWasABeautifulDayToSayTheTruth
	 With a free account we are limited for 50 search
	 
--------------------------------------------

## Gathering Breached Credentials with Breach-Parse
 [breach-parse](https://github.com/hmaverickadams/breach-parse)  
44 Gib  
used to go through the files and search for credentials

--------------------------------------------

## Utilizing theharvester
~~~bash
theharvester -d tesla.com -l 500 -b google
~~~

--------------------------------------------

## Hunting Subdomains
#### Passive information gathering
- Tool sublist3rt
- website: crt.sh
- [OWASP/Amass](https://github.com/OWASP/Amass)
- [httprobe](https://github.com/tomnomnom/httprobe)

--------------------------------------------

## Identifying Website Technologies
- [builtwith.com](https://builtwith.com)
- wappalyzer - addon
- whatweb - built in tool in kali linux
 
--------------------------------------------