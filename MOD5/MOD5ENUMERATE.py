# enumerate
for indice, numero in enumerate(range(1,11),1):
    print(indice,numero)
    if indice == 5:
        print('estamos na metade da lista')       
nomes = ['nome 1','nome 2','nome 3','nome 4','nome 5']
for indice,nome in enumerate(nomes,1):
    print(indice,nome)
    if indice == 3:
        print('ja temos 3 pessoas registradas')
# DESAFIO
frutas = ['maca','laranja','morango','limao']
for indice,fruta in enumerate(frutas,0):       
    if indice == 3:
        print(f'{indice} {fruta} EM PROMOCAO')
    else:
        print(indice, fruta)