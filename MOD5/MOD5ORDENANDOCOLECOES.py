from operator import itemgetter
# ordenar por propriedades
nomes = ['zack','camilla','julius','romer']
valores = [31,23,6,36,21,33,37,7,20,23]
pessoas = [
    {'nome': 'john',
     'idade': 32,
     'nivel_acesso': 2},
    {'nome': 'carol',
     'idade': 18,
     'nivel_acesso': 3},
    {'nome': 'thomas',
     'idade': 45,
     'nivel_acesso': 5},
    {'nome': 'amanda',
     'idade': 23,
     'nivel_acesso': 1},   
]
pessoas.sort(key=itemgetter('nome'))
print(pessoas)
produtos = [
    ('celular', 750),
    ('bicicleta', 1500),
    ('microfone', 550),
]
produtos.sort(key=itemgetter(0), reverse=True)
print(produtos)
matriz = [[5,10], [15,21], [1,5]]
matriz.sort(key=itemgetter(1))
print(matriz)
# DESAFIO 1
produtos = [
    {'nome': 'Celular',
     'preco': 1500
     },
    {'nome': 'Monitor',
     'preco': 500
     },
    {'nome': 'Microfone',
     'preco': 300
     }
]
produtos.sort(key=itemgetter('preco'))
print(produtos)
# DESAFIO 2
equipamento_filmagem = [
    ('Tripé', 300),
    ('Câmera', 1700),
    ('Iluminação', 200),
]
equipamento_filmagem.sort(key=itemgetter(1), reverse=True)
print(equipamento_filmagem)
# DESAFIO 3
cotacao_moedas = [['usd', 5.25], ['brl', 1.56], ['eur', 6.47]]
cotacao_moedas.sort(key=itemgetter(1))
print(cotacao_moedas)
