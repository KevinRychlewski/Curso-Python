# trabalhando com multiplas listas
from itertools import zip_longest
a_lista = ['A', 'B', 'C', 'D', 'E']
b_lista = [1,2,3,4,6]
for a,b in zip(a_lista,b_lista):
    print(a)
    print(b)
produtos = ['produto 1', 'produto 2', 'produto 3', 'produto 4', 'produto 5']
precos = [250,150,220,550,50]
for a,b in zip(produtos, precos):
    print(f'salvando produto {a} valor R$ {b}')
titulos = ['titulo 1','titulo 2','titulo 3','titulo 4']
descricoes = ['descricao 1','descricao 2','descricao 3']
for a,b in zip_longest(titulos, descricoes):
    print(f'encontramos o {a} descricao: {b}')
# DESAFIO 
produtos = ['Produto 1', 'Produto 2', 'Produto 3', 'Produto 4', 'Produto 5']
precos = ['R$500,00', 'R$1500,00', 'R$2700,00', 'R$5000,00']
for a,b in zip_longest(produtos,precos):
    print(f'produto: {a} encontrado no valor de {b}')