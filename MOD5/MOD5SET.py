# set
numeros = [2,2,5,8]
frutas = ['maca','uva','banana','maca','morango']
# convertendo para set
set_numeros = (set(numeros))
set_frutas = (set(frutas))
print(set_numeros)
print(set_frutas)
# adicionando novos valores
set_numeros.add(10)
print(set_numeros)
# conjuntos
numeros = [2,2,5,8]
numeros2 = [2,2,3,9]
a = set(numeros)
b = set(numeros2)
# ver os valores q tem em um e nao tem em outro
print(a.symmetric_difference(b))
# ver os valores q se repetem
print(a.intersection(b))
# remove todos os numeros duplicados
print(a.union(b))