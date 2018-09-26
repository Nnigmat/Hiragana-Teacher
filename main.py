from random import randint
from time import sleep
from os import system
import signal


hiragana = [
        [('a', 'あ'), ('i', 'い'), ('u', 'う'), ('e','え'), ('o', 'お')],
        [('ka', 'か'), ('ki', 'き'), ('ku', 'く'), ('ke', 'け'), ('ko', 'こ')],
        [('sa', 'さ'), ('shi', 'し'), ('su', 'す'), ('se', 'せ'), ('so', 'そ')],
        [('ta', 'た'), ('chi', 'ち'), ('tsu', 'つ'), ('te', 'て'), ('to', 'と')],
        [('na', 'な'), ('ni', 'に'), ('nu', 'ぬ'), ('ne', 'ね'), ('no', 'の')],
        [('ha', 'は'), ('hi', 'ひ'), ('fu', 'ふ'), ('he', 'へ'), ('ho', 'ほ')],
        [('ma', 'ま'), ('mi', 'み'), ('mu', 'む'), ('me', 'め'), ('mo', 'も')],
        [('ya', 'や'), ('yu', 'ゆ'), ('yo', 'よ')],
        [('ra', 'ら'), ('ri', 'り'), ('ru', 'る'), ('re', 'れ'), ('ro', 'ろ')],
        [('wa', 'わ'), ('o/wo', 'を')],
        [('n', 'ん')]
        ]

rows = len(hiragana)
lower_bound = 0
reverse = False

def print_table():
    i = 1
    print('-'*35)
    for row in hiragana:
        print(i, ' '.join([el[1] for el in row]), '-', ' '.join([el[0] for el in row]))
        i += 1
    print('-'*35)


def get_input():
    print('Enter number of rows you want to learn:', end=' ')
    inp = input().strip('\n')
    if '-r' in inp:
        globals()['reverse'] = True
        inp = inp.split(' ')[0]
    if inp != '':
        globals()['rows'] = int(inp) if int(inp) <= 11 else rows

def main_block():
    again = True
    while again:
        system('clear')
        i = 1
        hira_temp = []
        for j in range(rows):
            hira_temp.append(hiragana[j].copy())
        while any(hira_temp):
            row = randint(lower_bound, len(hira_temp) - 1)
            sign = hira_temp[row].pop(randint(0, len(hira_temp[row]) - 1))
            if hira_temp[row] == []:
                hira_temp.pop(row)

            print(i, sign[first_sign], end='')
            input()
            print('\x1b[1A\x1b[2K', str(i)+'.', sign[first_sign], sign[second_sign])
            i += 1
        print('Again? (Y/n)', end=' ')
        again = True if input() != 'n' else False
    print('Bye!')


if __name__ == '__main__':
    print_table()
    get_input()
    # print('\n'.join(['-'*35 for i in range(4)]))
    globals()['first_sign'] = 0 if not reverse else 1
    globals()['second_sign'] = 1 if not reverse else 0
    main_block()
