from rich.console import Console 
import pyfiglet, platform, os, random, sys

os.system('cls' if os.name == 'nt' else 'clear')
os_ = platform.system()
osname = os.name
console = Console()


console.print(f'{os_}@{osname.capitalize()}', end='')
inp = input('')

if inp == 'ls': 
    console.print('test success!')