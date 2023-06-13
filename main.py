import os
import random
import string


import RailFence

codes = {}

def get_code(letter):
    if letter not in codes:
        code = ''.join(random.choices(string.ascii_lowercase + string.digits, k=3))
        codes[letter] = code
    return codes[letter]

def get_letter(code):
    for letter, c in codes.items():
        if c == code:
            return letter
    return ''

def encrypt(message,key):
    encrypted = ''
    for letter in message:
        encrypted += get_code(letter)
    # print(f'Antes: {encrypted}')
    encrypted = RailFence.criptografar(encrypted,key)
    # print(f'Depois: {encrypted}')
    return encrypted

def decrypt(message,key):
    decrypted = ''
    rail = RailFence.descriptografar(message,key)
    codes = [rail[i:i+3] for i in range(0, len(rail), 3)]
    for code in codes:
        letter = get_letter(code)
        decrypted += letter
    return decrypted

while True:
    print('\n---------------------------')
    print('        Criptografia')
    print('---------------------------')
    print('1. Criptografar')
    print('2. Descriptografar')
    print('0. Sair\n')
    option = int(input('Escolha uma opção: '))

    if option == 1:
        message = input('Digite uma mensagem: ')
        while True:
            key = input('Digite a chave (int): ')
            try:
                key = int(key)
                break
            except ValueError:
                print('Chave inválida. Digite um número inteiro.')

        encrypted_message = encrypt(message,key)
        print(f'\n\n{encrypted_message}')

        print('\nConteúdo do dicionário :\n')
        for key, value in codes.items():
            print(f'{key}: {value}')

    elif option == 2:
        message = input('Digite uma mensagem criptografada: ')
        while True:
            key = input('Digite a chave: ')
            try:
                key = int(key)
                break
            except ValueError:
                print('Chave inválida. Digite um número inteiro.')

        decrypted_message = decrypt(message,key)
        print(f'\n\n{decrypted_message}')


    elif option == 0:
        break
    else:
        print('Opção inválida')

