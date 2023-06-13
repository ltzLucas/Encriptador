def get_letter(code):
    letters = {
        'h12j': 'A',
        'y18j': 'B',
        'f47k': 'C',
        't59s': 'D',
        'a89f': 'E',
        'l32d': 'F',
        'm56s': 'G',
        't54a': 'H',
        'y22z': 'I',
        'ç90e': 'J',
        't02h': 'K',
        'e45d': 'L',
        'u17i': 'M',
        'f49g': 'N',
        'k00s': 'O',
        'm83v': 'P',
        'a37y': 'Q',
        'w25l': 'R',
        'q82h': 'S',
        'r52t': 'T',
        'b67f': 'U',
        'j99k': 'V',
        'h35j': 'W',
        'o52k': 'X',
        'i71l': 'Y',
        'g97h': 'Z',
        'e90e': 'Ç',
        'h13j': 'Á',
        'y17j': 'À',
        'f43k': 'Ã',
        't56s': 'Â',
        'a87f': 'É',
        'l36d': 'Ê',
        'm54s': 'Í',
        't50a': 'Ó',
        'y25z': 'Ô',
        'ç96e': 'Õ',
        't13h': 'Ú',
        'e49d': 'Ü',
        'y91z': ' '
    }
    return letters.get(code, '')

    

def get_code(letter):
    codes = {
        'A': 'h12j',
        'B': 'y18j',
        'C': 'f47k',
        'D': 't59s',
        'E': 'a89f',
        'F': 'l32d',
        'G': 'm56s',
        'H': 't54a',
        'I': 'y22z',
        'J': 'ç90e',
        'K': 't02h',
        'L': 'e45d',
        'M': 'u17i',
        'N': 'f49g',
        'O': 'k00s',
        'P': 'm83v',
        'Q': 'a37y',
        'R': 'w25l',
        'S': 'q82h',
        'T': 'r52t',
        'U': 'b67f',
        'V': 'j99k',
        'W': 'h35j',
        'X': 'o52k',
        'Y': 'i71l',
        'Z': 'g97h',
        'Ç': 'e90e',
        'Á': 'h13j',
        'À': 'y17j',
        'Ã': 'f43k',
        'Â': 't56s',
        'É': 'a87f',
        'Ê': 'l36d',
        'Í': 'm54s',
        'Ó': 't50a',
        'Ô': 'y25z',
        'Õ': 'ç96e',
        'Ú': 't13h',
        'Ü': 'e49d',
        ' ': 'y91z'
    }
    return codes.get(letter, '')

#
def encrypt(message, chave):
    encrypted = ''
    for letter in message:
        encrypted += get_code(letter)
    encrypted = encrypted[chave:] + encrypted[:chave]
    return encrypted

def decrypt(message, chave):
    decrypted = ''
    message = message[-chave:] + message[:-chave]
    codes = [message[i:i+4] for i in range(0, len(message), 4)]
    for code in codes:
        letter = get_letter(code)
        decrypted += letter
    return decrypted

while True:
    print('---------------------------')
    print('        Criptografia')
    print('---------------------------')
    print('1. Criptografar')
    print('2. Descriptografar')
    print('0. Sair')
    option = int(input('Escolha uma opção: '))

    if option == 1:
        while True:
            chave_input = input('Digite a chave: ')
            try:
                chave = int(chave_input)
                break
            except ValueError:
                print('Chave inválida. Digite um número inteiro.')

        message = input('Digite uma mensagem: ').upper()
        encrypted_message = encrypt(message, chave)
        print(encrypted_message)

    elif option == 2:
        message = encrypted_message
        while True:
            chave_input = chave_input
            try:
                chave = int(chave_input)
                break
            except ValueError:
                print('Chave inválida. Digite um número inteiro.')

        decrypted_message = decrypt(message, chave)
        print(decrypted_message)

    elif option == 0:
        break
    else:
        print('Opção inválida')