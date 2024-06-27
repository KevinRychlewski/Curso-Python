# filter
nomes = ['larissa','rafael','marcus','john']
def pessoa_aprovada(pessoa):
    if pessoa == 'marcus':
        return True
    else:
        return False
print(list(filter(pessoa_aprovada,nomes)))
print(list(map(pessoa_aprovada,nomes)))
pinturas =[
    ['Pintura Classica', 'Azul', 1857],
    ['Pintura Medieval', 'Vermelha', 1867],
    ['Pintura Moderna', 'Verde', 1897]
]
def eh_antiguidade(pintura):
    if pintura[2] < 1890:
        return True
    else:
        False
print(list(filter(eh_antiguidade,pinturas)))
print(list(map(eh_antiguidade,pinturas)))
# DESAFIO 
vagas = [
    ['vaga 1', 1200],
    ['vaga 2', 2550],
    ['vaga 3', 5000]
]     
def salario(vaga):
    if vaga[1] > 2500:
        return True
    else:
        return False
print(list(filter(salario,vagas)))