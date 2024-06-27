trabalho_terminado = False
if trabalho_terminado == True:
    print('bora sair')
else:
    print('nao posso')
numero = 2
if numero >=3:
    print('diretoria')
elif numero == 2:
    print('essa é sua segunda falta')
elif numero == 1:
    print('essa é sua primeira falta')
else:
    print('pode entrar')
# chaining
multa = 55
if multa >=51 and multa <= 60:
#if 51 <= multa <= 60:
    print('multa = 2')
elif multa >=61 and multa <= 75:
    print('multa = 3')
else:
    print('multa = 7')
# DESAFIO
cabelo = 10
if cabelo <=20:
    print('50')
elif cabelo >=21 and cabelo <= 30:
    print('70')
elif cabelo >=31 and cabelo <= 50:
    print('100')
else:
    print('consultar na recepcao')