print('by Leonardo Cois\n' + '_' * 20 + '\n')
from time import*
from random import*

from colorama import init, Fore, Back, Style
init(convert=True)
import ctypes
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

tab1 = 80
ply = {}
data = []

print(Fore.RED + '=' * tab1)
print(f'{" AUTO DRAW - DICE GAME ":-^{tab1}}')
print('=' * tab1)
print()
print('I\'ll roll a dice for each player.')

while True:
    qst1 = str(input('>> How many players? ')).strip()
    qst3 = str(input('>> How many sides for the dice? [press enter - default 6 sides] ')).strip()
    if qst3 == '':
        qst3 = 6
    qst2 = len(qst1)
    try:
        qst1 = int(qst1)
        qst3 = int(qst3)
        break
    except ValueError:
        print('>> Error, try again')
        print()

print()
print(Fore.GREEN + '-' * tab1)
for c in range(1, qst1 + 1):
    ply['Player'] = c
    ply['dice'] = randint(1, qst3)
    sleep(0.5)
    print(f'>> Player({ply["Player"]:0{qst2}d}) took in dice: {ply["dice"]}')
    if data == []:
        data.append(ply.copy())
    else:
        for p, v in enumerate(data):
            if ply['dice'] < v['dice'] and p + 1 == len(data):
                data.append(ply.copy())
                break
            elif ply['dice'] < v['dice']:
                pass                
            else:
                data.insert(p, ply.copy())
                break
print(Fore.GREEN + '-' * tab1)
print('   --== RANKING POSITION ==--   ')
print()

pos = 1
post = '1st'
sps = 0
clr = Fore.YELLOW

for p, v in enumerate(data):
    sleep(.5)
    if p == 0:
        print(clr + '   ' + '-' * sps + f'{post} Position: Player({v["Player"]:0{qst2}d}) | dice: {v["dice"]}')
    elif v['dice'] == data[p - 1]['dice']:
        print(clr + '   ' + '-' * sps + f'{post} Position: Player({v["Player"]:0{qst2}d}) | dice: {v["dice"]}')
    else:
        pos += 1
        if pos == 1:
            post = '1st'
            clr = Fore.LIGHTYELLOW_EX
        elif pos == 2:
            post = '2nd'
            clr = Fore.LIGHTBLUE_EX
            sps += 2
        elif pos == 3:
            post = '3rd'
            clr = Fore.LIGHTMAGENTA_EX
            sps += 2
        else:
            post = str(pos) + 'th'
            clr = Fore.LIGHTWHITE_EX
            sps += 2
        if pos == 4:
            print(clr + '-' * len(clr + '   ' + '-' * sps + f'{post} Position: Player({v["Player"]:0{qst2}d}) | dice: {v["dice"]}'))
        print(clr + '   ' + '-' * sps + f'{post} Position: Player({v["Player"]:0{qst2}d}) | dice: {v["dice"]}')
print(Style.RESET_ALL + '-' * tab1)
print()
ex = input('press enter to exit...')
