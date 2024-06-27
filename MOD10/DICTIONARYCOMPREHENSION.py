# Dictionary compreheension
# [expressao for membro in iterável]
# {chave:expressao for membro in iterável}
from pprint import pprint
# pprint({i: i for i in range(20)})
# Popular um dicionario com valores
produtos = ['produto 1','produto 2','produto 3','produto 4','produto 5']
pprint({produto: 1 for produto in produtos})
# Gerar uma matriz de valores de teste
pprint({produto: [0 for i in range(5)] for produto in produtos})
# [expressão for membro in iterável]
pprint({produto: [i*2 for i in range(5)] for produto in produtos})
# Gerar valores de teste
import random
pprint({produto: [random.randint(1000,15000) for i in range(5)] for produto in produtos})
# DESAFIO 1
import random
sorteios = ['sorteio1','sorteio2','sorteio3']
participantes = ['joel','jessica', 'maria','cris','Larissa', 'rafael', 'marcus', 'john']
pprint({sorteio: random.choice(participantes) for sorteio in sorteios})
# DESAFIO 2
grupos = ['grupo 1', 'grupo 2', 'grupo 3']
pprint({grupo: [random.randint(1,101) for i in range(5)] for grupo in grupos})