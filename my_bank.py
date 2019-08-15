import os
import getpass

import my_bank.bank_system as bank

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


clear()

while True:
    print('#######################################')
    print('#######                          ######')
    print('#######          myBank  v. 2    ######')
    print('#######                          ######')
    print('#######################################')
    print(' ')
    print('(C) by bear All rights reserved')
    print(' ')
    print('1. Log in')
    print('2. Exit')
    choose = input('Choose action: ')
    if choose == '1':
        bank.bank_system()
    elif choose == '2':
        break
    else:
        print('You entered incorrect character!')
        input('Press enter to continue...')
    clear()
