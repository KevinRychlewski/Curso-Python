# como podemos criar listas?
# criar lista usando loops e range()
numeros = []
for i in range(5):
    numeros.append(i)
print(numeros)
# map
nomes = ['larissa','rafael','marcus','john']
def aprovar_pessoa(nome):
    # logico mais complexa
    return nome + ' APROVADO'
print(list(map(aprovar_pessoa,nomes)))
# DESAFIO
pinturas = [
    ['Pintura Classica', 'Azul', 1857],
    ['Pintura Medieval', 'Vermelha', 1867],
    ['Pintura Moderna', 'Verde', 1897]
]
def quadro(cor):
    return cor 
print(list(map(quadro,pinturas)))