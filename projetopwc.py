
def inverter_texto(texto):

    texto_dividido = texto.split()
    invertido = texto_dividido[::-1]
    pronto = ' '.join(invertido)

    return pronto


string = "Hello, World! OpenAI is amazing"
inve = inverter_texto(string)

print(inve)
