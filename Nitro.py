import requests
import time
import string 
from colorama import init, Fore, Back, Style
import os,threading
from os import name,system
from pycenter import center
import random



def clear():
    system("cls" if name == "nt" else "clear")


if name == "nt":
    system("mode 140, 30")    


init(convert=True)
valid = 0
invalid = 0


characters = string.ascii_letters +  string.digits
 



 


print(f"""
{Fore.RED}{Fore.MAGENTA}     

 ██ ▄█▀▓██   ██▓ ▒█████  ▄▄▄█████▓ ▒█████       ▄████ ▓█████  ███▄    █ 
 ██▄█▒  ▒██  ██▒▒██▒  ██▒▓  ██▒ ▓▒▒██▒  ██▒    ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
▓███▄░   ▒██ ██░▒██░  ██▒▒ ▓██░ ▒░▒██░  ██▒   ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
▓██ █▄   ░ ▐██▓░▒██   ██░░ ▓██▓ ░ ▒██   ██░   ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
▒██▒ █▄  ░ ██▒▓░░ ████▓▒░  ▒██▒ ░ ░ ████▓▒░   ░▒▓███▀▒░▒████▒▒██░   ▓██░
▒ ▒▒ ▓▒   ██▒▒▒ ░ ▒░▒░▒░   ▒ ░░   ░ ▒░▒░▒░     ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
░ ░▒ ▒░ ▓██ ░▒░   ░ ▒ ▒░     ░      ░ ▒ ▒░      ░   ░  ░ ░  ░░ ░░   ░ ▒░
░ ░░ ░  ▒ ▒ ░░  ░ ░ ░ ▒    ░      ░ ░ ░ ▒     ░ ░   ░    ░      ░   ░ ░ 
░  ░    ░ ░         ░ ░               ░ ░           ░    ░  ░         ░ 
        ░ ░                                                             

{Fore.RED} {Fore.MAGENTA}
                                                                                     
""")



lines = open('proxies.txt').read().splitlines()
def title():
    global valid
    global invalid
    while True:
        os.system(f"title Kyoto Nitro Gen Valid : [{valid}]  Invalid : [{invalid}]")

def nitro():
    global valid
    global invalid
    while True:
        os.system(f"title Kyoto Nitro Gen Valid : [{valid}]  Invalid : [{invalid}]") 
        proxy =random.choice(lines)
        if proxytype == "https":
            proxies = {'https': 'https://%s' % (proxy)}
        elif proxytype == "http":
            proxies = {'http': 'http://%s' % (proxy)}
        else:
            print(" > INVALID PROXY TYPE GIVEN, RESTART REQUIRED!")
            continue
        gift = "".join(random.choice(characters) for i in range(24))
        print(f"{Fore.CYAN}[?] Testing discord.gift/{gift.upper()}")
        try:
            r = requests.get(f"https://ptb.discordapp.com/api/v6/entitlements/gift-codes/{gift}", proxies = proxies)
            if r.status_code == 404:
                print(f"{Fore.RED}[-] discord.gift/{gift.upper()} - Invalid")
                invalid += 1
            elif r.status_code == 429:
                print(f"{Fore.RED}[-] discord.gift/{gift.upper()} - Ratelimited ")
                invalid += 1
                time.sleep(5)
            elif r.status_code == 200: 
                print(f"{Fore.GREEN}[-] discord.gift/{gift.upper()} -Valid Code - Saved to valid.txt")
                f = open("valids.txt", "a")
                valid += 1
                f.write("https://discord.gift/"+gift)
                f.close()
        except:
            pass

threading.Thread(target = title).start()
threadcount = int(input(" > Number of threads?\n > "))
proxytype = input(" > HTTP or HTTPS\n > ").lower()
for kieronia in range(threadcount):
    threading.Thread(target = nitro).start()
    time.sleep(0.1)