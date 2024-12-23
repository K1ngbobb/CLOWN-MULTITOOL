import requests
import os
import fade
import time

os.system("title CLOWN")

def main():
    os.system("cls")
    logo = """
   █████████ █████         ███████  █████   ███   ██████████   █████
  ███░░░░░██░░███        ███░░░░░██░░███   ░███  ░░██░░██████ ░░███ 
 ███     ░░░ ░███       ███     ░░██░███   ░███   ░███░███░███ ░███ 
░███         ░███      ░███      ░██░███   ░███   ░███░███░░███░███ 
░███         ░███      ░███      ░██░░███  █████  ███ ░███ ░░██████ 
░░███     ███░███      ░░███     ███ ░░░█████░█████░  ░███  ░░█████ 
 ░░█████████ ███████████░░░███████░    ░░███ ░░███    █████  ░░█████
  ░░░░░░░░░ ░░░░░░░░░░░   ░░░░░░░       ░░░   ░░░    ░░░░░    ░░░░░ 

"""
    print(fade.purplepink(logo))
    menu1 = """
                    ║═════════════════════════║
                    ║  ~$ [1] TOKEN SPAMMER   ║
                    ║  ~$ [2] WEBHOOK SPAMMER ║
                    ║  ~$ [3] IP PINGER       ║
                    ║  ~$ [4] IP SHOWER       ║
                    ║  ~$ [5] CALCULATOR      ║
                    ║═════════════════════════║
"""
    print(fade.purplepink(menu1))

    choice = input("\033[0;35m~~$ ")
    if choice=="1":
        token()
    if choice=="2":  
        webhook() 
    if choice=="3":
        ipping()   
    if choice=="4":    
        ipconfig() 
    if choice=="5":
        calculator()


def token():
    os.system("cls")
    logo = """
   █████████ █████         ███████  █████   ███   ██████████   █████
  ███░░░░░██░░███        ███░░░░░██░░███   ░███  ░░██░░██████ ░░███ 
 ███     ░░░ ░███       ███     ░░██░███   ░███   ░███░███░███ ░███ 
░███         ░███      ░███      ░██░███   ░███   ░███░███░░███░███ 
░███         ░███      ░███      ░██░░███  █████  ███ ░███ ░░██████ 
░░███     ███░███      ░░███     ███ ░░░█████░█████░  ░███  ░░█████ 
 ░░█████████ ███████████░░░███████░    ░░███ ░░███    █████  ░░█████
  ░░░░░░░░░ ░░░░░░░░░░░   ░░░░░░░       ░░░   ░░░    ░░░░░    ░░░░░ 

"""
    print(fade.purplepink(logo))
    author = input("\033[0;35m~~$ Enter the token: ")

    url = input("\033[0;35m~~$ Enter channel id: ")

    message = input("\033[0;35m~~$ Enter the message: ")

    amount = int(input("\033[0;35m~~$ Enter how many times u wanna spam: "))
    
    delay = float(input("\033[0;35m~~$ Enter the delay between the messages: "))

    channel = f"https://discord.com/api/v9/channels/{url}/messages"

    payload = {
        'content': message
        }

    header = {
        'authorization': author
        }

    for i in range(amount):
        requests.post(channel, data=payload, headers=header)
        print("")
        print(f"\033[0;35m[!] NUKING: {i}/{amount - 1}.")
        time.sleep(delay)
        
    os.system("pause >nul")    
    main()    

def webhook():
    os.system("cls")
    logo = """
   █████████ █████         ███████  █████   ███   ██████████   █████
  ███░░░░░██░░███        ███░░░░░██░░███   ░███  ░░██░░██████ ░░███ 
 ███     ░░░ ░███       ███     ░░██░███   ░███   ░███░███░███ ░███ 
░███         ░███      ░███      ░██░███   ░███   ░███░███░░███░███ 
░███         ░███      ░███      ░██░░███  █████  ███ ░███ ░░██████ 
░░███     ███░███      ░░███     ███ ░░░█████░█████░  ░███  ░░█████ 
 ░░█████████ ███████████░░░███████░    ░░███ ░░███    █████  ░░█████
  ░░░░░░░░░ ░░░░░░░░░░░   ░░░░░░░       ░░░   ░░░    ░░░░░    ░░░░░ 

"""
    print(fade.purplepink(logo))
    webhook = input("\033[0;35m~~$ Webhook: ")
    message1 = input("\033[0;35m~~$ Message: ")
    amount1 = int(input("\033[0;35m~~$ Amount: "))
    delay1 = int(input("\033[0;35m~~$ Delay:"))
    print("")

    payload = {
        'content': message1
    }

    for i in range(amount1):
        requests.post(webhook, json=payload)
        print(f"\033[0;35m[!] Webhook spamming: {i}/{amount1 - 1}.")
        time.sleep(delay1)

    os.system("pause >nul")  
    main()      

def ipping():
    os.system("start pinger.bat")
    main()

def ipconfig():
    os.system("cls")
    logo = """
   █████████ █████         ███████  █████   ███   ██████████   █████
  ███░░░░░██░░███        ███░░░░░██░░███   ░███  ░░██░░██████ ░░███ 
 ███     ░░░ ░███       ███     ░░██░███   ░███   ░███░███░███ ░███ 
░███         ░███      ░███      ░██░███   ░███   ░███░███░░███░███ 
░███         ░███      ░███      ░██░░███  █████  ███ ░███ ░░██████ 
░░███     ███░███      ░░███     ███ ░░░█████░█████░  ░███  ░░█████ 
 ░░█████████ ███████████░░░███████░    ░░███ ░░███    █████  ░░█████
  ░░░░░░░░░ ░░░░░░░░░░░   ░░░░░░░       ░░░   ░░░    ░░░░░    ░░░░░ 

"""
    print(fade.purplepink(logo))
    print("")
    os.system("ipconfig")
    input1 = input("\033[0;35m~~$ Press enter to go to menu...")
    main()



def calculator():
    os.system("cls")
    logo = """
   █████████ █████         ███████  █████   ███   ██████████   █████
  ███░░░░░██░░███        ███░░░░░██░░███   ░███  ░░██░░██████ ░░███ 
 ███     ░░░ ░███       ███     ░░██░███   ░███   ░███░███░███ ░███ 
░███         ░███      ░███      ░██░███   ░███   ░███░███░░███░███ 
░███         ░███      ░███      ░██░░███  █████  ███ ░███ ░░██████ 
░░███     ███░███      ░░███     ███ ░░░█████░█████░  ░███  ░░█████ 
 ░░█████████ ███████████░░░███████░    ░░███ ░░███    █████  ░░█████
  ░░░░░░░░░ ░░░░░░░░░░░   ░░░░░░░       ░░░   ░░░    ░░░░░    ░░░░░ 

"""
    print(fade.purplepink(logo))
    print("")
    n1 = float(input("\033[0;35m~~$ Num 1: "))
    sec = input("\033[0;35m~~$ Calculation: ")
    n2 = float(input("\033[0;35m~~$ Num 2: "))

    if sec=="+":
        print("")
        print(n1 + n2)
        input1 = input("\033[0;35m~~$ Press enter to go to menu...")
        main()  
    if sec=="-":
        print("")
        print(n1 - n2)
        input1 = input("\033[0;35m~~$ Press enter to go to menu...")
        main()  
    if sec=="*":
        print("")
        print(n1 * n2)
        input1 = input("\033[0;35m~~$ Press enter to go to menu...")
        main()  
    if sec=="/":
        print("")
        print(n1 / n2)
        input1 = input("\033[0;35m~~$ Press enter to go to menu...")
        main()    
    if sec=="%":
        print("")
        print(n1 % n2)
        input1 = input("\033[0;35m~~$ Press enter to go to menu...")
        main()    
  
main()