# Como podemos criar listas?
# Criar listas usando Loops e Range()
numeros = []
for i in range(5):
    numeros.append(i)
print(numeros)
# # Map
nomes = ['Larissa','Rafael','Maria','John']
from pprint import pprint


def aprovar_pessoa(nome):
    return nome + ' APROVADO'
    
# print(list(map(aprovar_pessoa,nomes)))

# Como usar list compreheension
nova_lista = [2 * i for i in range(10)]
# [expressao for membro in iterável]
print(nova_lista)
nomes = ['Larissa','Rafael','Maria','John']
print([nome + ' APROVADO' for nome in nomes])
print([aprovar_pessoa(nome) for nome in nomes])
'''1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5'''
pprint([[i for i in range(1,6)]for x in range(5)])
# Usar condicionais em list compreheension
# [expressao for membro in iterável (condicional if)]
print([aprovar_pessoa(nome) for nome in nomes if nome != 'Rafael'])
# Valores numéricos
def eh_numero_par(numero):
    valor = numero % 2
    if valor == 0:
        return True
    else:
        return False
print([i for i in range(20)if eh_numero_par(i)])
# A condicioanl é flexível
# [expressao (condicional if) for membro in iterável]
participantes = ['Larissa','Rafael','Maria','John']
ganhadores = ['Maria','John']
print([i + ' GANHADOR' if i in ganhadores else i + ' NAO SELECIONADO' for i in participantes])
# DESAFIO 1
print([i for i in range(11) if eh_numero_par(i)])
# DESAFIO 2 - nao consegui resolver 
cores = ['vermelho','azul','verde','amarelo','rosa','preto']
pprint([str(cores.index(i)+1) + ' - ' + i for i in cores])
# DESAFIO 3
participantes = ['joel','jessica','maria','cris','Larissa','rafael','marcus','john']
pagamento_realizado = ['joel','jessica','maria','cris']
print([i + ' PAGO' if i in pagamento_realizado else i + ' PAGAMENTO N FEITO' for i in participantes])


