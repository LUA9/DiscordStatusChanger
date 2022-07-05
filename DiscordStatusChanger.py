import os
import json
import time
import colorama # pip install colorama
import requests # pip install requests

from itertools import cycle

configuration = json.load(open('config.json', 'r', encoding='UTF-8'))
words = open('words.txt', 'r', encoding='UTF-8').read()
words = words.splitlines()

def ClearConsole():
    if os.name == 'nt': # Check OS is windows. (Only Windows uses cls command for clear console.)
        return os.system('cls')
    else:
        return os.system('clear') # If OS is not Windows, use clear command.

def RunForever():
    try:
        while True: pass
    except KeyboardInterrupt:
        exit(1)

ClearConsole() # Cleaning console before main part starts.
print(f'{colorama.Fore.LIGHTYELLOW_EX}Thanks for use this program.{colorama.Fore.RESET}')
print(f'{colorama.Fore.LIGHTYELLOW_EX}Discord ID: 766078556392390696{colorama.Fore.RESET}')
print(f'{colorama.Fore.LIGHTYELLOW_EX}You can search me at https://discord.id/ (Discord Lookup){colorama.Fore.RESET}')
print(f'{colorama.Fore.RED}We are not scamming to people.{colorama.Fore.RESET}')

token = configuration['DiscordAuthorization']

if not token:
    from getpass import getpass # Security input for get Discord TOKEN.
    token = getpass(f'{colorama.Fore.GREEN}Enter your Discord Authorization TOKEN (Security input): {colorama.Fore.RESET}')
    configuration['DiscordAuthorization'] = token
    with open('config.json', 'w', encoding='UTF-8') as configuration_file:
        json.dump(configuration, configuration_file, indent=4)
    configuration_file.close()

token = configuration.get('DiscordAuthorization') # Update it.
delay = configuration.get('DiscordStatusChangeDelay')
status = configuration.get('DiscordStatus')

if not words:
    print(f'{colorama.Fore.RED}Add words in words.txt (separate with indent.){colorama.Fore.RESET}')
    RunForever()

words = cycle(words)

for word in words:
    response = requests.patch(
        'https://canary.discord.com/api/v9/users/@me/settings',
        json={'custom_status': {'text': word}, 'status': status},
        headers={'Content-Type': 'application/json', 'Authorization': token}
    )

    time.sleep(delay)
