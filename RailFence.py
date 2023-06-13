def criptografar(texto, chave):
    # Criar a matriz para cifrar o texto plano,
    # chave = linhas, len(texto) = colunas
    # Preenchendo a matriz de cercas para distinguir
    # espaços preenchidos de espaços em branco
    cerca = [['\n' for i in range(len(texto))]
             for j in range(chave)]

    # Encontrar a direção do fluxo e inverter a direção
    # se acabamos de preencher a cerca superior ou inferior
    dir_descer = False
    linha, coluna = 0, 0

    for i in range(len(texto)):
        if (linha == 0) or (linha == chave - 1):
            dir_descer = not dir_descer

        # Preencher a letra correspondente
        cerca[linha][coluna] = texto[i]
        coluna += 1

        # Encontrar a próxima linha usando a
        # flag de direção
        if dir_descer:
            linha += 1
        else:
            linha -= 1

    # Agora podemos construir o texto cifrado
    # usando a matriz de cercas
    resultado = []
    for i in range(chave):
        for j in range(len(texto)):
            if cerca[i][j] != '\n':
                resultado.append(cerca[i][j])
    return "".join(resultado)

# Função que recebe o texto cifrado e a chave e retorna o texto original após a descriptografia
def descriptografar(cifra, chave):
    # Criar a matriz para cifrar o texto plano,
    # chave = linhas, len(texto) = colunas
    # Preenchendo a matriz de cercas para distinguir
    # espaços preenchidos de espaços em branco
    cerca = [['\n' for i in range(len(cifra))]
             for j in range(chave)]

    # Encontrar a direção do fluxo
    dir_descer = None
    linha, coluna = 0, 0

    # Marcar os espaços com '*'
    for i in range(len(cifra)):
        if linha == 0:
            dir_descer = True
        if linha == chave - 1:
            dir_descer = False

        # Colocar o marcador
        cerca[linha][coluna] = '*'
        coluna += 1

        # Encontrar a próxima linha
        # usando a flag de direção
        if dir_descer:
            linha += 1
        else:
            linha -= 1

    # Agora podemos construir a matriz de cercas
    indice = 0
    for i in range(chave):
        for j in range(len(cifra)):
            if (cerca[i][j] == '*') and (indice < len(cifra)):
                cerca[i][j] = cifra[indice]
                indice += 1

    # Agora ler a matriz em forma de zig-zag
    # para construir o texto resultante
    resultado = []
    linha, coluna = 0, 0
    for i in range(len(cifra)):
        # Verificar a direção do fluxo
        if linha == 0:
            dir_descer = True
        if linha == chave - 1:
            dir_descer = False

        # Colocar o marcador
        if cerca[linha][coluna] != '*':
            resultado.append(cerca[linha][coluna])
            coluna += 1

        # Encontrar a próxima linha
        # usando a flag de direção
        if dir_descer:
            linha += 1
        else:
            linha -= 1

    return "".join(resultado)