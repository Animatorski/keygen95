import random,os,keyboard
def mod7rtm():
    x = 'a';y = 1
    while x == 'a' or y % 7 != 0:
        x = '{:0>7}'.format(random.randint(0,9999999))
        y = int(x[0])+int(x[1])+int(x[2])+int(x[3])+int(x[4])+int(x[5])+int(x[6])
    return x
def mod7oem():
    x = 'a';y = 1
    while x == 'a' or y % 7 != 0:
        x = '{:0>6}'.format(random.randint(0,999999))
        y = int(x[0])+int(x[1])+int(x[2])+int(x[3])+int(x[4])+int(x[5])
    return '0'+x
def gen_oem():
    x = '{:0>3}'.format(random.randint(95,102))
    return '{:0>3}'.format(random.randint(0,366))+x[1]+x[2]+'-OEM-'+mod7oem()+'-'+'{:0>5}'.format(random.randint(0,99999))
def gen_rtm():
    x = 'a'
    while x == '222' or x == '333' or x == '444' or x == '555' or x == '666' or x == '777' or x == '888' or x == '999' or x == 'a':
        x = '{:0>3}'.format(random.randint(0,999))
        if x == '222' or x == '333' or x == '444' or x == '555' or x == '666' or x == '777' or x == '888' or x == '999':
            pass
        else:
            return x+'-'+mod7rtm()
def main():
    os.system('cls')
    print('Keygen95 by Animatorski\nhttps://github.com/Animatorski/keygen95/\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\n[*] What key to generate?\n[1] Windows 95 RTM\n[2] Windows 95 OEM')
    while True:
        if keyboard.is_pressed('1'):
            print('\n[i] Generating RTM key, please wait...')
            print('[i] Done! Key: '+gen_rtm()+'\nPress Enter to exit...')
            keyboard.wait('enter')
            os._exit(0)
        elif keyboard.is_pressed('2'):
            print('\n[i] Generating OEM key, please wait...')
            print('[i] Done! Key: '+gen_oem()+'\nPress Enter to exit...')
            keyboard.wait('enter')
            os._exit(0)
main()