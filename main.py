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

katakana =  [
        [('a', 'ア'), ('i', 'イ'), ('u', 'ウ'), ('e','エ'), ('o', 'オ')],
        [('ka', 'カ'), ('ki', 'キ'), ('ku', 'ク'), ('ke', 'ケ'), ('ko', 'コ')],
        [('sa', 'サ'), ('shi', 'シ'), ('su', 'ス'), ('se', 'セ'), ('so', 'ソ')],
        [('ta', 'タ'), ('chi', 'チ'), ('tsu', 'ツ'), ('te', 'テ'), ('to', 'ト')],
        [('na', 'ナ'), ('ni', 'ニ'), ('nu', 'ヌ'), ('ne', 'ネ'), ('no', 'ノ')],
        [('ha', 'ハ'), ('hi', 'ヒ'), ('fu', 'フ'), ('he', 'へ'), ('ho', 'ホ')],
        [('ma', 'マ'), ('mi', 'ミ'), ('mu', 'ム'), ('me', 'メ'), ('mo', 'モ')],
        [('ya', 'ヤ'), ('yu', 'ユ'), ('yo', 'ヨ')],
        [('ra', 'ラ'), ('ri', 'リ'), ('ru', 'ル'), ('re', 'レ'), ('ro', 'ロ')],
        [('wa', 'ワ'), ('o/wo', 'ヲ')],
        [('n', 'ン')]
        ]

rows = len(hiragana)
lower_bound = 0
reverse = False
is_hiragana = True

def print_table():
    i = 1
    print('-'*35)
    kana = 'hiragana' if is_hiragana else 'katakana'
    for row in globals()[kana]:
        print(i, ' '.join([el[1] for el in row]), '-', ' '.join([el[0] for el in row]))
        i += 1
    print('-'*35)


def get_input():
    while (True):
        print('Do you wanna learn katakana or hiragana (h - hiragana, k - katakana):', end=' ')
        inp = input()
        if inp == 'h':
            break
        elif inp == 'k':
            globals()['is_hiragana'] = False
            break
        else:
            print("I'm sorry, but this is invalid input", end='\n')

    print_table()
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
        kana_temp = []
        for j in range(rows):
            kana_temp.append(hiragana[j].copy() if globals()['is_hiragana'] else katakana[j].copy())
        while any(kana_temp):
            row = randint(lower_bound, len(kana_temp) - 1)
            sign = kana_temp[row].pop(randint(0, len(kana_temp[row]) - 1))
            if kana_temp[row] == []:
                kana_temp.pop(row)

            print(i, sign[first_sign], end='')
            input()
            print('\x1b[1A\x1b[2K', str(i)+'.', sign[first_sign], sign[second_sign])
            i += 1
        print('Again? (Y/n)', end=' ')
        again = True if input() != 'n' else False
    print('Bye!')


if __name__ == '__main__':
    get_input()
    # print('\n'.join(['-'*35 for i in range(4)]))
    globals()['first_sign'] = 0 if not reverse else 1
    globals()['second_sign'] = 1 if not reverse else 0
    main_block()
