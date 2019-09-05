print('by Leonardo Cois\n' + '_' * 20 + '\n')
from time import*
from random import*

from colorama import init, Fore, Back, Style
init(convert=True)
import ctypes
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

tab1 = 50
ct1 = 1

print(Fore.CYAN + '=' * tab1)
print('{:^{}}'.format('LOTTO GAME DRAW', tab1))
print('=' * tab1, '\n')
print('Numbers from 1 to 60')
while True:
    qst = str(input('How many games to draw? ')).strip()
    try:
        qst = int(qst)
        break
    except ValueError:
        print('Error, please input an integer number.')
print()
print('=' * tab1)
disp = f'RAFFLING {qst} GAMES'
print(f'{disp:-^{tab1}}')
print()
cl1 = 0
while ct1 < qst + 1:
    l1 = []
    for i in range(0, 6):
        rnd = randint(1, 60)
        while rnd in l1:
            rnd = randint(1, 60)
        l1.append(rnd)
        l1.sort()
    if cl1 == 0:
        print(Fore.BLACK + Back.LIGHTGREEN_EX + f'>> Game {ct1:>2}: ', end='')
        cl1 = 1
    else:
        print(Fore.BLACK + Back.LIGHTYELLOW_EX + f'>> Game {ct1:>2}: ', end='')
        cl1 = 0
    for c in l1:
        print(f'{c:>2}', end='   ')
    print()    
    ct1 += 1
    sleep(.5)
print(Style.RESET_ALL)
disp = ' GOOD LUCK ! '
print(f'{disp:-^{tab1}}')
ex = input('press enter to exit...')
