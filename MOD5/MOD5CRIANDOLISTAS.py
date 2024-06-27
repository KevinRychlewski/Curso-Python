# listas
precos = [10,20,30, 40, 50, 60, 100, 250, 560, 23, 74]
print(precos[2])# indice
print(precos[precos.index(100)])
# listas no python sao dinamicas(aceitam qualquer tipo de dado)
itens = [1,3,6,'ola','cafe',True, 10.6]
print(itens[itens.index('ola')])
# maneiras diferentes de gerar uma lista
# multiplicacao de valores(repeticao)
lista_de_noves = [9] * 10
print(lista_de_noves)
# usando gerador range(sequencia)
# 1 a 29
faixa_de_numeros = list(range(30))
print(faixa_de_numeros)
# gerar a partir de strings
lista2 = list('abuble')
print(lista2)
#lista de lista (matriz)
matriz_de_nomes = [['carol',30],['marcus',50]]
print(matriz_de_nomes[0])
print(matriz_de_nomes[0][0])
print(matriz_de_nomes[1][0])
# DESAFIO 1
lista = ['celular', 'pc', 'fone']
print(lista)
# DESAFIO 2
lista2 = list(range(10,132))
# DESAFIO 3
lista3 = lista + lista2
print(lista3)
# DESAFIO 4
lista_de_matriz = [['celular', 1000],['pc', 2000],['fone', 500]]
print(lista_de_matriz[1][0])