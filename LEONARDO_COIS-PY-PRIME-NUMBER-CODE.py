print('by Leonardo Cois\n' + '_' * 20 + '\n')
from time import*
from random import*

from colorama import init, Fore, Back, Style
init(convert=True)
import ctypes
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

tab1 = 60
print('=' * tab1)
print(f'{" PRIME NUMBERS ":-^{tab1}}')
print('=' * tab1)
n = 0
l = []
while True:
    x = str(input('>> Enter a integer number: '))
    spaces = len(x)
    if spaces < 3:
        print('>> Hey, let\'s do something fun, please try a bigger one, like 100')
    else:
        try:
            x = int(x)
            break
        except ValueError:
            print('>> Error, please enter a integer number.')
    print()
print('=' * tab1)
print()
# change for the tabulation
tab = 10
for c in range(1, x + 1):
    sleep(0.05)
    if c % tab == 0:
        ee = '\n'
        leftm = '  |'
        rightm = ''
    elif c % tab == 1:
        ee = ' '
        leftm = ''
        rightm = '|  '
    else:
        ee = ' '
        leftm = ''
        rightm = ''
    if x % c == 0:
        print(f'{rightm}\033[1;32m{c: >{spaces}}\033[m{leftm}', end=ee)
        n += 1
        l.append(c)
    elif x % c != 0:
        print(f'{rightm}\033[1;31m{c: >{spaces}}\033[m{leftm}', end=ee)
l = '| ' + str(l)[1:-1].replace(',', ' |') + ' |'
print()
print('=' * tab1)
print()
if n == 1:
    res = '\033[1;34mIS PRIME NUMBER\033[m'
    s = ''
elif n == 2:
    res = '\033[1;34mIS PRIME NUMBER\033[m'
    s = 's'
else:
    res = '\033[1;34mISN\'T PRIME NUMBER\033[m'
    s = 's'
print('\nThe number {} is divisible {} time{} by:\n\n'
      '{} \n'
      '>> It means that {} {}'.format(x, n, s, l, x, res))
print()
print('=' * tab1)
print()
ex = input('press enter to exit...')
