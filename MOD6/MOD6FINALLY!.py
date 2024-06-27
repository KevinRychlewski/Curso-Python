internet = None
try:
    print('fazendo conexao com a ' + internet)
except TypeError as erro:
    print('nao ha conexao com a internet')
finally:
    print('desfazendo a compra')
try:
    valor = int(input('digite um valor'))
    print(valor / 0)
except ZeroDivisionError as erro:
    print('nao é possivel dividir por zero')
except ValueError as erro:
    print('favor digitar apenas numeros')
finally:
    print('a operacao foi cancelada')

    