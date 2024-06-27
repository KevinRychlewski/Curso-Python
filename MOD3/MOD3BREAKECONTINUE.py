# continue, ignorar/pular
for numero in range(100):
    if numero % 2 == 0:
        print(numero)
    else:
        continue
# break, para interromper a iteracao
for numero in range(100):
    if numero % 2 == 0:
        print(numero)
    else:
        break
frutas = ['maca', 'manga', 'laranja', 'morango']
for fruta in frutas:
    if fruta == 'manga':
        break
    print(f'{fruta} adicionada a dieta')
# DESAFIO 1
estilos = ['Hip-Hop','Rock','Rap','Pop']
for estilo in estilos:
    if estilo == 'Rap':
        continue
    print(f'{estilo}')
# DESAFIO 2
estilos = ['Hip-Hop','Rock','Rap','Pop']
for estilo in estilos:
    if estilo == 'Rock':
        break
    print(f'{estilo}')

