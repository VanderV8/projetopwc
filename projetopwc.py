import re


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

    # Define o tamanho que vamos percorrer com o for.
    tamanho = len(texto_junto)

    # Variavel que recebe o maior palindromo.
    palindromo = ''

    # Loop que percorre cada letra da frase.
    for letra in range(tamanho):
        # Loop que percorre as letras passando a posição da variavel "letra" para variavel "ultimo", aumentando de um em um a posição.
        for ultima in range(letra+1, tamanho+1):
            # Substring que recebe a frase nova com a posição da "Letra" e a posição "ultima" formando uma nova frase.
            substring = texto_junto[letra:ultima]
            # confere se a substring é um palindromo e se o tamanho dela é maior que a ultima substring armazenada.
            if substring == substring[::-1] and len(substring) > len(palindromo):
                palindromo = substring

    return palindromo


string3 = "banana"
texto = achar_palindromo(string3)
print(texto)


# 4 Coloque em maiusculo a primeira letra de cada frase na string.

def primeira_maiuscula(texto):

    # Padrões de caracteres que vão dividir a frase em uma nova lista.
    padrao = r"[.!?]+[\s]*"
    # Nova lista que procura os padrões dentro da frase.
    lista_palavras = re.split(padrao, texto)

    # Varivel que resebe a nova frase.
    maiuscula = ''

    # loop que passa pelas palavras da lista_palavras
    for palavra in lista_palavras:
        # Coloca a palavra em maiúsculo
        palavra_formatada = palavra.capitalize()
        # Costroi a frase com as palavras formatadas e com os espaçoes.
        maiuscula += palavra_formatada + '. '

    texto_junto = ''.join(maiuscula)
    return texto_junto


string4 = "hello. how are you? i'm fine, thank you"
texto = primeira_maiuscula(string4)
print(texto)


# 5 Verificar se a string é um anagrama de um palindromo:

def verifica_anagrama(texto):

    # contador de impares. (para saber se a palavra pode ser um anagrama vemos se ela tem uma unica letra impar)
    contagem = {}

    # Conta quantos letras temos na string e adiciona ela em um dicionario.
    for letra in texto:
        if letra in contagem:
            contagem[letra] += 1
        else:
            contagem[letra] = 1

    # Variavel que recebe o numeros impares.
    num_impares = 0

    # Loop que passa pelos valores da biblioteca.
    for count in contagem.values():
        # confere se o numero é impar.
        if count % 2 != 0:
            num_impares += 1
            # confere se temos mais de um numero impar na biblioteca e retorna falso.
            if num_impares > 1:
                return False

    return True


string5 = "racecar"
print(verifica_anagrama(string5))
