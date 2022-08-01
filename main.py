import requests
import random
from colorama import *
numb = True
for i in range(30):
    letters = [
                    'a', 'e', 'i', 'o', 'u',
                    'b', 'c', 'd', 'f', 'g',
                    'h', 'j', 'k', 'l', 'm',
                    'n', 'p', 'q', 'r', 's',
                    't', 'v', 'w', 'x', 'z'
                    ]
    if numb == True:
        i = 0
        for c in range(10):
            g = str(i)
            letters.append(g)
            i += 1
    username = "".join(random.choices(letters,k = 3)) /// here you chance the number of letters of the Name in k=3...
    url = f"https://api.mojang.com/users/profiles/minecraft/{username}?at=0"
    proxy_info = open('proxy.txt', 'r').read().splitlines()
    proxy = random.choice(proxy_info)
    proxies = {
            'http': f'http://{proxy}',
            'https':f'http://{proxy}'
            }
    print(f"Checking Username: {username}:")
    try:
        r = requests.get(url, proxies=proxies, timeout=5)
    except:
        print(Fore.LIGHTYELLOW_EX + "Proxy Rate Limited")
    if r.text.contains("id"):
        a = r.json()["id"]
        print(Fore.LIGHTRED_EX + f"Username Taken, UUID: {a}\n" + Fore.RESET)
    else:
        print(Fore.GREEN + "Username its Avaible\n" + Fore.RESET)
