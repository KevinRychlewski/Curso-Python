# loop aninhados
# pais + estacao
paises = ['brasil', 'india', 'estados unidos']
estacoes = ['primavera', 'verao', 'outono', 'inverno']
for pais in paises:
    for estacao in estacoes:
        print(f'{pais} {estacao}')
for x in range(1,11):
    for y in range(1,6):
        print(f'valor externo {x} e interno de {y}')
# DESAFIO
celulares = ['Asus', 'Samsung', 'Sony', 'IPhone']
versoes = ['Plus', 'Premium Plus', 'Premium Deluxe', 'Plus Premium Ultra']
for celular in celulares:
    for verso in versoes:
        print(f'{celular} {verso}')
