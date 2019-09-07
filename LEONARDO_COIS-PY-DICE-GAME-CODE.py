print('by Leonardo Cois\n' + '_' * 20 + '\n')

# define printing for dice results
def dice_print(clr, sps, post, qst2, v):
    print(clr + '   ' + '-' * sps + f'{post} Position: Player({v["Player"]:0{qst2}d}) | dice: {v["dice"]}')


from time import*
from random import*

from colorama import init, Fore, Back, Style
init(convert=True)
import ctypes
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

# setting tabulation length and db
tab1 = 80
ply = {}
data = []

# header
print(Fore.RED + '=' * tab1)
print(f'{" AUTO DRAW - DICE GAME ":-^{tab1}}')
print('=' * tab1)
print()
print('I\'ll roll a dice for each player.')

while True:
    # asking for inputs
    qst1 = str(input('>> How many players? ')).strip()
    qst3 = str(input('>> How many sides for the dice? [press enter - default 6 sides] ')).strip()
    
    # testing inputs
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

# roll dice, add to dic
print()
print(Fore.GREEN + '-' * tab1)
for c in range(1, qst1 + 1):
    ply['Player'] = c
    ply['dice'] = randint(1, qst3)
    sleep(0.5)
    print(f'>> Player({ply["Player"]:0{qst2}d}) took in dice: {ply["dice"]}')
    
    # add data from dict to db/list and ranking
    # if is empty
    if data == []:
        data.append(ply.copy())
    else:
        for p, v in enumerate(data):
            # check if first item
            if ply['dice'] < v['dice'] and p + 1 == len(data):
                data.append(ply.copy())
                break
            # roll over the list to find position
            elif ply['dice'] < v['dice']:
                pass
            # insert in correct ranking pos
            else:
                data.insert(p, ply.copy())
                break
# header for ranking
print(Fore.GREEN + '-' * tab1)
print('   --== RANKING POSITION ==--   ')
print()

# setting variables
pos = 1
post = '1st'
sps = 0
clr = Fore.YELLOW

for p, v in enumerate(data):
    sleep(.5)
    # building colored and tabulated list by it position
    if p == 0:
        dice_print(clr, sps, post, qst2, v)
    elif v['dice'] == data[p - 1]['dice']:
        dice_print(clr, sps, post, qst2, v)
    else:
        # ordinal number
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
            print(clr + '-' * len(dice_print(clr, sps, post, qst2, v)))
        dice_print(clr, sps, post, qst2, v)
print(Style.RESET_ALL + '-' * tab1)
print()
ex = input('press enter to exit...')
