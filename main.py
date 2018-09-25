from random import randint
from time import sleep
from os import system


hiragana = [
        [('a', 'あ'), ('i', 'い'), ('u', 'う'), ('e','え'), ('o', 'お')],
        [('ka', 'か'), ('ki', 'き'), ('ku', 'く'), ('ke', 'け'), ('ko', 'こ')],
        [('sa', 'さ'), ('si', 'し'), ('su', 'す'), ('se', 'せ'), ('so', 'そ')],
        [('ta', 'た'), ('ti', 'ち'), ('tu', 'つ'), ('te', 'て'), ('to', 'と')],
        [('na', 'な'), ('ni', 'に'), ('nu', 'ぬ'), ('ne', 'ね'), ('no', 'の')],
        [('ha', 'は'), ('hi', 'ひ'), ('hu', 'ふ'), ('he', 'へ'), ('ho', 'ほ')],
        [('ma', 'ま'), ('mi', 'み'), ('mu', 'む'), ('me', 'め'), ('mo', 'も')],
        [('ya', 'や'), ('yu', 'ゆ'), ('yo', 'よ')],
        [('ra', 'ら'), ('ri', 'り'), ('ru', 'る'), ('re', 'れ'), ('ro', 'ろ')],
        [('wa', 'わ'), ('o/wo', 'わ')],
        [('n', 'ん')]
        ]

rows = len(hiragana)
lower_bound = 0

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
    if inp != '':
        globals()['rows'] = int(inp) if int(inp) <= 11 else rows


if __name__ == '__main__':
    print_table()
    get_input()
    system('clear')
    # print('\n'.join(['-'*35 for i in range(4)]))
    hiragana = hiragana[0: rows]
    i = 1
    while any(hiragana):
        row = randint(lower_bound, len(hiragana) - 1)
        sign = hiragana[row].pop(randint(0, len(hiragana[row]) - 1))
        if hiragana[row] == []:
            hiragana.pop(row)
        print(i, sign[0], end='')
        input()
        print('\x1b[1A\x1b[2K', str(i)+'.', sign[0], sign[1])
        i += 1


