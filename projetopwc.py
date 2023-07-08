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

    tamanho = len(texto_junto)
    palindromo = ''

    for letra in range(tamanho):
        for ultima in range(letra+1, tamanho+1):
            substring = texto_junto[letra:ultima]
            if substring == substring[::-1] and len(substring) > len(palindromo):
                palindromo = substring

    return palindromo


string3 = "banana"
texto = achar_palindromo(string3)
print(texto)


# 4 Coloque em maiusculo a primeira letra de cada frase na string.

def primeira_maiuscula(texto):

    padrao = r"[.!?]+[\s]*"
    lista_palavras = re.split(padrao, texto)

    maiuscula = ''

    for palavra in lista_palavras:
        frase_formatada = palavra.capitalize()
        maiuscula += frase_formatada + '. '

    texto_junto = ''.join(maiuscula)
    return texto_junto


string4 = "hello. how are you? i'm fine, thank you"
texto = primeira_maiuscula(string4)
print(texto)


