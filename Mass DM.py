import json
import discord
from discord import DMChannel
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
print(F"{Fore.CYAN}Made by Leimag with love!")
print(f"{Fore.WHITE}Choose:")
print(f"{Fore.WHITE}1 > Mass DM ID")
print(f"{Fore.WHITE}2 > Mass DM Friends")

time.sleep(2)
op = input ("Option ---> ")
msg = input("Message ---> ")

@client.event
async def on_connect(): 
        if op == '2':
            while True:
                for friend in client.user.friends:
                    try:
                        await friend.send(msg)
                        print(f"{Fore.GREEN}[+]Sent {msg} to {friend.name}!")
                    except:
                        print(f"{Fore.RED}[-]Couldnt message {friend.name}!")
        if op == '1':
            id = input("ID ---> ")
            user = await client.fetch_user(id)
            while True:
                await DMChannel.send(user, msg)
                print(f"{Fore.GREEN}[+]Sent {msg} to {id}!")
        else:
            print("Not a valid option!")


with open('config.json') as f:
        config = json.load(f)
token = config.get('token') 

client.run(token, bot=False)

