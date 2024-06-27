# *arg: significa q podemos receber uma quantidade variavel de valores
def somar (*valores, b):
    print(valores)
    for valor in valores:
        b += valor
    print(b)
somar(10,20,5, b=5)
# ** significa: quando queremos receber uma quantidade infinita de argumentos nomeados
def concatenar(**palavras):
    frase = ''
    for palavra in palavras.values():
        frase += palavra + ' '
    print(frase)
concatenar(a='nos',b='somos',c='pythonistas',d='profissionais')
