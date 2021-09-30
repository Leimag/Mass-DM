import json
import discord
import time
import colorama
from colorama import Fore
colorama.init()


client = discord.Client()



print(F"{Fore.LIGHTBLUE_EX}██████╗░██████╗░███████╗░█████╗░███╗░░░███╗")
time.sleep(0.1)
print(F"{Fore.WHITE}██╔══██╗██╔══██╗██╔════╝██╔══██╗████╗░████║")
time.sleep(0.1)
print(F"{Fore.LIGHTBLUE_EX}██║░░██║██████╔╝█████╗░░███████║██╔████╔██║")
time.sleep(0.1)
print(F"{Fore.WHITE}██║░░██║██╔══██╗██╔══╝░░██╔══██║██║╚██╔╝██║")
time.sleep(0.1)
print(F"{Fore.LIGHTBLUE_EX}██████╔╝██║░░██║███████╗██║░░██║██║░╚═╝░██║")
print(F"{Fore.YELLOW}Made by Leimag with love!")
time.sleep(2)
msg = input("Message ---> ")

@client.event
async def on_connect():
    for friend in client.user.friends:
        try:
            await friend.send(msg)
            print(f"{Fore.GREEN}[+]Sent {msg} to {friend.name}!")
        except:
            print(f"{Fore.RED}[-]Couldnt message {friend.name}!")
    print("Done!")


with open('config.json') as f:
        config = json.load(f)
token = config.get('token') 

client.run(token, bot=False)

