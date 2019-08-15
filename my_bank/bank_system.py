import os
import getpass

from my_bank.banking_provider import MYSQLBankingProvider

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')



def bank_system():
    bank = MYSQLBankingProvider()
    clear()

    print('#######################################')
    print('#######                          ######')
    print('#######          myBank  v. 2    ######')
    print('#######                          ######')
    print('#######################################')
    print(' ')
    print('(C) by bear All rights reserved')
    print(' ')
    login = input('Login: ')
    password = getpass.getpass('Password: ')
    print(bank.log_in(login, password))
    input('Press enter to continue...')
    if bank.check_if_logged():
        while True:
            clear()
            print('#######################################')
            print('#######                          ######')
            print('#######          myBank  v. 2    ######')
            print('#######                          ######')
            print('#######################################')
            print(' ')
            print('(C) by bear All rights reserved')
            print(' ')
            print(bank.get_account_data(login))
            print('\n1. Transfer money')
            print('2. Log out')
            choose = input('Choose action: ')
            if choose == '1':
                amount = input('Enter amount to transfer: ')
                target = input('Enter target account number: ')
                print(bank.transfer(login, amount, target))
                input('Press enter to continue...')
            elif choose == '2':
                break
            else:
                print('You entered incorrect character!')
                input('Press enter to continue...')
            clear()