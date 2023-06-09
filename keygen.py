import random,os,keyboard
def mod7():
    x = 'a'
    y = 1
    while x == 'a' or y % 7 != 0:
        x = '{:0>6}'.format(random.randint(0,999999))
        y = int(x[0])+int(x[1])+int(x[2])+int(x[3])+int(x[4])+int(x[5])
    return '0'+x
def gen_oem():
    x = '{:0>3}'.format(random.randint(0,366))
    y = '{:0>3}'.format(random.randint(95,102))
    y = y[1]+y[2]
    z = mod7()
    i = '{:0>5}'.format(random.randint(0,99999))
    return x+y+'-OEM-'+z+'-'+i
os.system('cls')
print('Keygen95 by Animatorski\nhttps://github.com/Animatorski/keygen95/\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\n[*] Generating OEM key, please wait...\n[*] Done! Key: '+gen_oem()+'\nPress Enter to exit...')
keyboard.wait('enter')
os.quit()
