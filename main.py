from rich.console import Console 
from pathlib import Path
import pyfiglet, platform, os, random, sys

os.system('cls' if os.name == 'nt' else 'clear')
os_ = platform.system()
osname = os.name
console = Console()


while True:
    print(pyfiglet.figlet_format('TERMIFY'))
    console.print(f'{os_.lower()}@{osname}')
    inp = input('')
    if inp == 'ls': 
        for i in os.listdir(): 
            try: 
                if i == '.git': continue
            except Exception: continue
            if os.path.isfile(i): console.print('[dark_cyan]--file-- ', end='')
            if os.path.isdir(i): console.print('[purple4]--dir-- ', end='')
            console.print(i)

    if inp.startswith('cd '):
        nextDir = inp.split()
        if inp.split('cd')[1] == '..': ...

        os.chdir(nextDir)

    if inp.startswith('dl '): 
        deleteDir = inp.split()[1]
        
        if os.path.isdir(deleteDir): Path.rmdir(deleteDir)
        if os.path.isfile(deleteDir): os.remove(deleteDir)

        console.print('success!')

    if inp.startswith('mkd '): 
        dirToBeCreated = inp.split()[1]
        os.mkdir(dirToBeCreated)

        console.print('success')

    if inp.startswith('echo '):
        echoed = inp.split()[1]
        console.print(f'{echoed}')

    if inp.startswith('touch '):
        filename = inp.split()[1]
        console.print()
        with open(filename, 'w') as f: f.write('')

    if inp.startswith('find '):
        filename =  inp.split()[1]
        if os.path.exists(filename)
        