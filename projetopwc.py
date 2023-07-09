# 1.Faça um código que reverta a ordem das palavras nas frases, mantendo a ordem das palavras.
def inverter_texto(texto):

    # Divide o texto pelos caracteres de espaço, criando uma nova lista.
    texto_dividido = texto.split()

    # inverte os elementos da nova lista.
    invertido = texto_dividido[::-1]

    # Junta os elementos criando uma nova String separada por espaços.
    pronto = " ".join(invertido)

    return pronto

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

# 3 Encontre a substring palindromo mais longa na string abaixo.
def achar_palindromo(texto):

    # Deixa a string com letras minúsculas
    texto_minus = texto.lower()

    # separa a string pelos caracteres de espaço e depois junta a string com o join sem espaços extras.
    texto_junto = ''.join(texto.strip().split())
    
    # Define o tamanho que vamos percorrer com o for.
    tamanho = len(texto_junto)

    # Variavel que recebe o maior palindromo.
    palindromo = ""

    # Loop que percorre cada letra da frase.
    for letra in range(tamanho):
        # Loop que percorre as letras passando a posição da variavel "letra" para variavel "ultimo", aumentando de um em um a posição.
        for ultima in range(letra + 1, tamanho + 1):
            # Substring que recebe a frase nova com a posição da "Letra" e a posição "ultima" formando uma nova frase.
            substring = texto_junto[letra:ultima]
            # confere se a substring é um palindromo e se o tamanho dela é maior que a ultima substring armazenada.
            if substring == substring[::-1] and len(substring) > len(palindromo):
                palindromo = substring

    return palindromo

# 4 Coloque em maiúsculo a primeira letra de cada frase na string.
def primeira_maiuscula(texto):

    # separa a string pelos caracteres de espaço e depois junta a string com o join sem espaços extra.
    texto_sem_espaco = ' '.join(texto.strip().split())    

    # difine o tamanho que vamos percorrer              
    tamanho = len(texto_sem_espaco)-1
    novo_texto = ""
    i = 0
    
    # loop para formatar a frase para que sempre tenha espaços depois dos caracteres " . ! ? :"
    for i in range(tamanho):
        # Adiciona os elementos se não houver o espaço depois de um dos caracteres
        if (texto_sem_espaco[i] == "." or texto_sem_espaco[i] == ":" or texto_sem_espaco[i] == "?" or texto_sem_espaco[i] == "!") and texto_sem_espaco[i+1] != " ":
            x = texto_sem_espaco[i]
            novo_texto += x + " "
        else:
            # Adiciona normalmente se estiver com espaço
            x = texto_sem_espaco[i]
            novo_texto += x
    x = texto_sem_espaco[i+1]
    novo_texto += x
    
    # Coloca o novo texto formatado em uma nova variavel e define o tamanho que vamos percorrer.
    texto_formatado = novo_texto
    novo_tamanho = len(texto_formatado)
    texto_pronto = ""

    # Loop que confere se temos um espaço e um ponto antes de uma letra.
    for i in range(novo_tamanho):
        # Substitui o caracter para um maiúsculo se temos um espaço e um ponto antes de uma letra e se for a primeira letra da frase.
        if i == 0 or texto_formatado[i-1] == " " and (texto_formatado[i-2] == "." or texto_formatado[i-2] == "?" or texto_formatado[i-2] == "!" or texto_formatado[i-2] == ":"):
            texto_pronto += texto_formatado[i].upper()        
        else:
            # Se não houver adiciona ele normalmente.
            x = texto_formatado[i]
            texto_pronto += x

    return texto_pronto

# 5 Verificar se a string é um anagrama de um palindromo:
def verifica_anagrama(texto):
    
    # contador de impares. (para saber se a palavra pode ser um anagrama de um palindromo vemos se ela tem uma unica letra com uma ocorrência impar)
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


# Criando MENU.
tam = 50
opcoes = {
    "1": "inverter frase",
    "2": "Remover caracteres duplicados",
    "3": "substring palindromo mais longa",
    "4": "Maiúsculo na primeira letra de cada frase",
    "5": "Verificar anagrama de um palindromo",
    "0": "para sair",
}

while True:

    # Cria um Menu com um tamanho ajustavel.
    print(f"+{'-' * tam}+")
    print(f"|{'MENU':^{tam}}|")
    print(f"+{'-' * tam}+")
    for (numero,texto,) in opcoes.items():
        print(f"|{f' {numero} - {texto}':{tam}}|")
    print(f"+{'-' * tam}+")

    # pede ao usuario uma opção.
    op = input("Digite o NÚMERO da sua opção desejada: ")

    # Avisa se a opção não estiver na lista.
    if op not in opcoes:
        print("\n\033[1;30;41mOpção invalida!!!\033[m\n")
        continue

    # se 1 chama a função inverter_texto.
    if op == "1":

        print(f"\n+{'-' * tam}+")

        # Mostra exemplo.
        print("1.Faça um codigo que reverta a ordem das palavras nas frases, mantendo a ordem das palavaras.\nExemplo: ")
        string1 = "Hello, World! OpenAI is amazing"
        print(string1)
        print(inverter_texto(string1))

        # Pede uma frase ao usuario e chama a função para inverter a frase.
        frase = input("\nDigite a sua frase:\n")
        invertida = inverter_texto(frase)
        print(invertida)

        print(f"+{'-' * tam}+\n")

        continue

    # se 2 chama a função remove_duplicado.    
    if op == "2":
         
        print(f"\n+{'-' * tam}+")

        # Mostra exemplo.
        print("2 Remova todos os caracteres duplicados da string abaixo\nExemplo:")
        string2 = "Hello, World!"
        print(string2)
        print(remove_duplicado(string2))

        # Pede uma frase ao usuario e chama a função para remover letras duplicadas.
        frase = input("\nDigite a sua frase:\n")
        sem_duplicada = remove_duplicado(frase)
        print(sem_duplicada)

        print(f"+{'-' * tam}+\n")


        continue

    #  chama a 3 chama a função substring palindromo mais longa.
    if op == "3":

        print(f"\n+{'-' * tam}+")

        # Mostra exemplo.
        print("3 Encontre a substring palindromo mais longa na string abaixo.\nExemplo:")
        string3 = "babad"
        print(string3)
        print(achar_palindromo(string3))    

        # Pede uma frase ao usuario e chama a função para achar palindromo.
        frase = input("\nDigite a sua frase ou palavra:\n")
        palindromo = achar_palindromo(frase)
        print(palindromo)

        print(f"+{'-' * tam}+\n")

        continue

    #  chama a 4 chama a função que coloca em maiúsculo a primeira letra da frase.
    if op == "4":

        print(f"\n+{'-' * tam}+")

        # Mostra exemplo
        print("4 Coloque em maiúsculo a primeira letra de cada frase na string.\nExemplo:")
        string4 = "hello. how are you? i'm fine, thank you."
        print(string4)
        print(primeira_maiuscula(string4))
 
        # Pede uma frase ao usuario e chama a função para achar palindromo.
        frase = input("\nDigite a sua frase:\n")
        primeira = primeira_maiuscula(frase)
        print(primeira)

        print(f"+{'-' * tam}+\n")

        continue
       
    # chama a 5 chama a função que Verificar se a string é um anagrama de um palindromo. 
    if op == "5":

        print(f"\n+{'-' * tam}+")

        # Mostra exemplo.
        print("5 Verificar se a string é um anagrama de um palindromo e retorna True or False :\nExemplo:")
        string5 = "racecar"
        print(string5)
        print(verifica_anagrama(string5))
 
        # Pede uma frase ao usuario e chama a função para Verificar se a string é um anagrama de um palindromo.
        frase = input("\nDigite a sua frase:\n")
        anagrama_palindromo = verifica_anagrama(frase)
        print(anagrama_palindromo)

        print(f"+{'-' * tam}+\n")

        continue

    # fecha o programa.    
    if op == "0":
        break
