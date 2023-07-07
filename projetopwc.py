

# 1.Faça um codigo que reverta a ordem das palavras nas frases, mantendo a ordem das palavaras.
def inverter_texto(texto):

    # Divide o texto pelos caracteres de espaço, criando uma nova lista.
    texto_dividido = texto.split()

    # inverte os elementos da nova lista.
    invertido = texto_dividido[::-1]

    # Junta os elementos criando uma nova String separada por espaços.
    pronto = ' '.join(invertido)

    return pronto


string1 = "Hello, World! OpenAI is amazing"
texto = inverter_texto(string1)
print(texto)


# 2 Remova todos os caracteres duplicados da string abaixo.
def remove_duplicado(texto):

    # string vazia
    sem_duplicado = ""

    # percorre todos os caracteres da string
    for caracter in texto:

        # Confere se o caracter já existe na nova string (String vazia) e adiciona se não existir.
        if caracter not in sem_duplicado:
            sem_duplicado += caracter

    return sem_duplicado


string2 = "Hello, World!"
texto = remove_duplicado(string2)
print(texto)


# 3 Encontre a substring palindromo mais longa na string abaixo.


def achar_palindromo(texto):

    # Deixa a string com letras minúsculas
    texto_minus = texto.lower()

    # separa a string pelos caracteres de espaço e depois junta a sring com o join sem espaços.
    texto_separado = texto_minus.split()
    texto_junto = ''.join(texto_separado)

    texto_junto = len(texto)
    palindromo = ''

    for letra in range(texto_junto):
        for ultima in range(letra+1, texto_junto+1):
            substring = texto[letra:ultima]
            if substring == substring[::-1] and len(substring) > len(palindromo):
                palindromo = substring

    return palindromo


string3 = "babad"
texto = achar_palindromo(string3)
print(texto)

#
