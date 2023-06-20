# Keygen95
A Windows 95 Key Generator written in Python.

# Download
Currently download is unavailable due to PyInstaller having problems with his executables being flagged as malicious and a major bug in the code. The download of the source code will be available soon along side the 1.0.0 release!

# Windows 95 RTM Key Format
**BBB-MMMMMMM**

BBB - Just a Blacklist: 222, 333, 444, 555, 666, 777, 888 and 999 are banned <br>
MMMMMMM - Simillar to the OEM's mod7 function. The only diffrence is that you don't need to put 0 on the beginning.

Notes:
The dash (-) can be replased! The code doesn't check if it's there, so you can make a key, that looks like this: 'YOLO7777777', and it will pass the check!

# Windows 95 OEM Key Format
**DDDYY-OEM-MMMMMMM-RRRRR**

DDD - Day from 001 to 366 (for example 034 is 3rd of Febuary) <br>
YY - Last 2 digits of the year 1995 to 2002 (for example 98 is 1998) <br>
"-OEM-" - Stays the same <br>
MMMMMMM - This is the most complex part of the key called "mod7". First digit is always 0, other digits must equal 0 when added to themself, and put into the modulo function. <br>
RRRRR - These are just random numbers (for example 69420 haha)
