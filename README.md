# Keygen95
A Windows 95 Key Generator written in Python.

# Download
Both Windows Defender and Google Chrome sadly flags the executable as malicious, which means that downloading the compiled version is almost impossible ;(, but the executable is 100% safe! The problem is propably caused by PyInstaller. I'll try to fix it soon. As of right now, the only option is to download the python script and run it that way.

# Windows 95 OEM Key Format
Thanks to research I was able to figure out the Windows 95 OEM key format, which looks like this:

DDDYY-OEM-MMMMMMM-RRRRR

DDD - Day from 001 to 366 (for example 034 is 3rd of Febuary) <br>
YY - Last 2 digits of the year 1995 to 2002 (for example 98 is 1998) <br>
"-OEM-" - Stays the same <br>
MMMMMMM - This is the most complex part of the key. First digit is always 0, other digits must equal 0 when added to themself, and put into the modulo function. <br>
RRRRR - These are just random numbers (for example 69420 :) )
