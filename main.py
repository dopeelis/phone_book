import json
import os.path


class MyAction:
    FIND = '1'
    ADD = '2'
    DELETE = '3'
    CHANGE = '4'
    EXIT = '5'


class MyChoice:
    NUMBER = '1'
    NAME = '2'
    RETURN = '3'


if os.path.isfile('phone_book.json'):
    with open('phone_book.json', 'r', encoding='UTF-8') as file:
        phone_book = json.load(file)
else:
    phone_book = {}


def get_name(object, value):
    for name, number in object.items():
        if number == value:
            return name


action = ''

while action != MyAction.EXIT:
    print(f'Menu: \n {MyAction.FIND}) Find number \n {MyAction.ADD}) Add number \n' 
          f' {MyAction.DELETE}) Delete number \n {MyAction.CHANGE}) Change number \n {MyAction.EXIT}) Exit')
    action = input('What do you want to do? ')
    if action == MyAction.FIND:
        print(f'Searching by: \n {MyChoice.NUMBER}) Number \n {MyChoice.NAME}) Name \n {MyChoice.RETURN}) Return')
        request = input('1 or 2? ')
        if request == MyChoice.NUMBER:
            number = input('Enter the number: ')
            if number in phone_book.values():
                name = get_name(phone_book, number)
                print(f'\n Number {number} belongs to: {name} \n')
            else:
                print(f'\n There is no one with number:{number} \n')
        elif request == MyChoice.NAME:
            name = input('Enter the name: ')
            if name in phone_book:
                print(f'\n {name}`s number is: {phone_book[name]} \n')
            else:
                print(f'\n There is no one with name: {name} \n')
        elif request == MyChoice.RETURN:
            continue
        else:
            print('\n Incorrect request. Try again \n')
            continue
    elif action == MyAction.ADD:
        name = input('Enter the name: ')
        number = input('Enter the number: ')
        if name not in phone_book and number not in phone_book.values():
            phone_book[name] = number
            print('\n The contact has been added \n')
            with open('phone_book.json', 'w', encoding='UTF-8') as file:
                json.dump(phone_book, file)
        else:
            if name in phone_book:
                print('\n Name already in use. Choose another one \n')
            if number in phone_book.values():
                print('\n Number already in use. Enter another one \n')
    elif action == MyAction.DELETE:
        print(f'Delete by: \n {MyChoice.NUMBER}) Number \n {MyChoice.NAME}) Name \n {MyChoice.RETURN}) Return')
        request = input('1 or 2? ')
        if request == MyChoice.NUMBER:
            number = input('Enter the number: ')
            if number in phone_book.values():
                name = get_name(phone_book, number)
                phone_book.pop(name)
                print('\n The contact has been deleted \n')
                with open('phone_book.json', 'w', encoding='UTF-8') as file:
                    json.dump(phone_book, file)
            else:
                print(f'\n There is no one with number:{number} \n')
        elif request == MyChoice.NAME:
            name = input('Enter the name: ')
            if name in phone_book:
                phone_book.pop(name)
                print('\n The contact has been deleted \n')
                with open('phone_book.json', 'w', encoding='UTF-8') as file:
                    json.dump(phone_book, file)
            else:
                print(f'\n There is no one with name: {name} \n')
        elif request == MyChoice.RETURN:
            continue
        else:
            print('\n Incorrect request. Try again \n')
            continue
    elif action == MyAction.CHANGE:
        print(f'What do you want to change: \n {MyChoice.NUMBER}) Number \n' 
              f' {MyChoice.NAME}) Name \n {MyChoice.RETURN}) Return')
        request = input('1 or 2? ')
        if request == MyChoice.NUMBER:
            number = input('Enter the number to be changed: ')
            new_number = input('Enter new number: ')
            if number in phone_book.values():
                phone_book[get_name(phone_book, number)] = new_number
                print(f'\n Number {number} was replaced by {new_number} \n')
                with open('phone_book.json', 'w', encoding='UTF-8') as file:
                    json.dump(phone_book, file)
            else:
                print(f'\n There is no one with number:{number} \n')
        elif request == MyChoice.NAME:
            name = input('Enter the name to be changed: ')
            new_name = input('Enter new name: ')
            if name in phone_book:
                phone_book[new_name] = phone_book.pop(name)
                print(f'\n Name {name} was replaced by {new_name} \n')
                with open('phone_book.json', 'w', encoding='UTF-8') as file:
                    json.dump(phone_book, file)
            else:
                print(f'\n There is no one with name: {name} \n')
        elif request == MyChoice.RETURN:
            continue
        else:
            print('\n Incorrect request. Try again \n')
            continue
    else:
        print('\n Till we meet again, my friend!')
