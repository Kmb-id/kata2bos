#!/usr/bin/python2
# coding=utf-8
# Haiyo.... ngapain loe
# By KMB. ID [ L4.ERRORS ]
# copyright 2019 - 2022


import os,sys,time,datetime,random

### Exit
def keluar():
	os.sys.exit()
	
### Animasi gerak 1
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.01)

### Animasi gerak 2
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
		
### LOGO HOME #####
logo = ("""\n\n\033[1;96m     _____________________________/\.\033[1;91mMO \033[1;93mTI \033[1;92mVA \033[1;95mSI
\033[1;96m    / `---`___________----_______/--] \033[91m• • •\033[97m ░▒▓D
\033[1;96m   /_|;;;;;;;;;|_______.:/ \033[93m FOLLOW \033[94m@\033[97mL4eroor.id
\033[1;96m    ), ---.( \( ) /\033[1;91m╔═══════════════════════════╗
\033[1;96m   // (..)),,----` \033[1;91m║  \033[1;93m★\033[4;45;97m Admin & Design Art \033[0m\033[1;93m★   \033[1;91m║
\033[1;96m  //___//          \033[1;91m║    \033[1;93m KMB•ID\033[1;92m【L4•EROOR】    \033[91m║
\033[1;96m //___//           \033[1;91m╚═══════════════════════════╝
\033[1;96m ╚═════╝ \033[1;91m[\033[1;93mUPDATE\033[1;91m] \033[1;94mKATA \033[1;92mKATA \033[1;91m/ \033[0mBAC😁TAN \033[1;92mHARI \033[1;95mINI """)

### LOGO L4
logo_l4 = ("""\n\n\x1b[00m\x1b[1;96m ╔══════════════════════════════╦════════════════╗
 ║ \x1b[1;91m╦ ╦ ╦   ╔═╗ ╔═╗ ╔═╗ ╔═╗ ╔═╗  \x1b[1;96m║\x1b[1;41;92m    KMB • ID    \x1b[0m\x1b[1;96m║
 ║ \x1b[1;91m║ ╚-╣ • ╠╣  ║   ║ ║ ║ ║ ║    \x1b[1;96m╠\x1b[1;41;96m════🛡️══════🛡️════\x1b[0m\x1b[96m╣
 ║ \x1b[1;97m╩╝  ╩   ╚═╝ ╩   ╚═╝ ╚═╝ ╩ \x1b[93m404\x1b[1;96m║\x1b[1;47;91m© \x1b[1;94mcopyright \x1b[1;95m2019\x1b[0m\x1b[1;96m║
 ╚══════════════════════════════╩════════════════╝""")

def tik():
    animation = '|1/-2\\3'
    for i in range(24):
        time.sleep(0.5)
        sys.stdout.write('\r\033[1;36m[!] \x1b[1;32mWaitt gan \x1b[1;97m' + animation[(i % len(animation))])
        sys.stdout.flush()

def titik():
    titik = [
     '.   ', '..  ','... ']
    for o in titik:
        print ('\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92mLoading \x1b[1;97m') + o,
        sys.stdout.flush()
        time.sleep(0.009)

def jalan2(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.09)
		
### Siapa Kamu ###
def siapa():
	os.system('clear')
	jalan ("""🔴🟢🔵""")
	jalan ("""\n\n\x1b[00m\x1b[1;96m ╔══════════════════════════════╦════════════════╗
 ║ \x1b[1;91m╦ ╦ ╦   ╔═╗ ╔═╗ ╔═╗ ╔═╗ ╔═╗  \x1b[1;96m║\x1b[1;41;92m    KMB • ID    \x1b[0m\x1b[1;96m║
 ║ \x1b[1;91m║ ╚-╣ • ╠╣  ║   ║ ║ ║ ║ ║    \x1b[1;96m╠\x1b[1;41;96m════🛡️══════🛡️════\x1b[0m\x1b[96m╣
 ║ \x1b[1;97m╩╝  ╩   ╚═╝ ╩   ╚═╝ ╚═╝ ╩ \x1b[93m404\x1b[1;96m║\x1b[1;47;91m© \x1b[1;94mcopyright \x1b[1;95m2019\x1b[0m\x1b[1;96m║
 ╚══════════════════════════════╩════════════════╝""")

	jalan ('''\n\x1b[00m     ▓▀██      ▒█████    ▄████  ▀▀▓ ███▄   ▀█▓
      ▓██▒    ▒██▒  ██▒ ██▒ ▀█▒▓██▒ ██ ▀█   █▓
      ▒██░    ▒██░  ██▒▒██░▄▄▄░▒██▒▓██  ▀█ ██▒
      ▒██░    ▒██   ██░░▓█  ██▓░██░▓██▒  ▐▌██▒
      ░█▄▄██▀▒░ ████▓▒░░▒▓███▀▒░██░▒██░   ▓██░
      ░ ▒░▓  ░░ ▒░▒░▒░  ░▒   ▒ ░▓  ░ ▒░   ▒ ▒
      ░ ░\x1b[00m\033[3;93;41m C R E A T E  U S E R  L O G I N \033[00m\x1b[1;00m░ ░
        ░ ░   ░   ░    ░ ░   ░    ░   ░   ░
         ▒     ░        ░        ░       ▒''')
	nama = raw_input("\x1b[1;96m╔═════\033[44;1;93m Please enter your data for confirmation \x1b[0m\n\x1b[1;96m║\n\x1b[1;96m╚══▶ \x1b[1;4;97mYour Name \x1b[1;91mOR \x1b[1;97mYour Nick \033[1;91m:\x1b[0m \033[5;41;92m ")
	print ("\x1b[0m")
	if nama =="":
		print ("\033[1;96m[!] \033[1;91mIsi yang benar")
		time.sleep(4)
		siapa()
	else:
		time.sleep(2)
		tik()
		os.system('clear')
		jalan ("""🔴🟢🔵""")
		print (logo_l4)
		jalan("\n\x1b[00m\033[1;93m            Selamat datang \033[41;92m MR." +nama+ " \n\x1b[0m\033[1;93m⏩ Terimakasih telah menyaksikan story ini !! ⏪\n    👹👹 Enjoy in your life \033[41;92m MR." +nama+" \x1b[0m 👹👹\n\x1b[1;97m\n\n\x1b[1;41;96m💰 NOOBY TEAM INDONESIA ,\x1b[1;47;91m KMB • ID {L4•ERROR} 💰\x1b[0m")
		time.sleep(4)
		titik()
		time.sleep(2)
		os.system('clear')
		print(logo)
		jalan("\n\x1b[1;91m╔"+46*"═"+"╗")
		jalan("\x1b[1;91m║\x1b[1;97m"+11*' '+"Motivasi by \x1b[1;93m:\x1b[1;92m "+nama+ (21 - len(nama)) * "\x1b[1;91m " + "║")
		jalan("\x1b[1;91m╚"+46*"═"+"╝")
		tik()
		jalan2('''\n\x1b[1;95m iNFO KATA-KATA BOSS ... !!!\n''')
		jalan2('''\x1b[1;41;97m▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂ 
▂▂▂▂▂▂▂▂▂▂▂▂▂╭━╮▂▂▂▂▂▂▂▂▂▂▂▂▂▂ 
▂▂▂▂▂▂▂▂▂▂▂▂▂┣━┫▂▂▂▂▂▂▂▂▂▂▂▂▂▂ 
▂▂▂▂▂▂▂▂▂▂▂▂▂┃╭┃▂▂▂▂▂▂▂▂▂▂▂▂▂▂ 
▂▂▂▂▂▂▂▂▂▂▂╭━┫┈┣━╮▂▂▂▂▂▂▂▂▂▂▂▂ \x1b[0m\x1b[1;47;91m
▂▂▂▂▂▂▂▂▂╭━┃╭┃╭┃╭┃━╮▂▂▂▂▂▂▂▂▂▂ 
▂▂▂▂▂▂▂▂▂┃.        ┃▂▂▂▂▂▂▂▂▂▂ 
▂▂▂▂▂▂▂▂▂\.        /▂▂▂▂▂▂▂▂▂▂ \x1b[0m\n''')
		time.sleep(1)
		jalan2('''\x1b[1;94m👉YAKIN\n👉GAS\n👉MAINKAN\n👉dan JADILAH \x1b[1;92mPEMAIN\n\n\x1b[1;97mKALO\n\x1b[1;93m👉RAGU = \x1b[1;41;96m SKIP AJA \x1b[00m \x1b[1;97m!!!!\n\x1b[1;95m👉 Selamat MENONTON saja & DO'A kan KAMI SUKSES''')
		jalan("\n\x1b[1;91m╔"+46*"═"+"╗")
		jalan("\x1b[1;91m║\x1b[1;97m"+6*' '+"SALAM PEMULUNG RECEH \x1b[1;92m "+nama+ (18 - len(nama)) * "\x1b[1;91m " + "║")
		jalan("\x1b[1;91m╚"+46*"═"+"╝")
		time.sleep(2)

        
if __name__ == '__main__':
	siapa()
