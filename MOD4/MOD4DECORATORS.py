from datetime import datetime
def depositar():
    print('depositando dinheiro')
    
    def depositando_dolar():
        print('depositando dolares')
     
    def depositando_reais():
        print('depositando reais')
    
    depositando_dolar()
    depositando_reais()
    
depositar()

def pai(numero):
    def filho_1():
        print('sou filho 1')
    def filho_2():
        print('sou filho 2')
    if numero == 1:
        return filho_1
    elif numero == 2:
        return filho_2
resultado = pai(1)
resultado()
# decorators
def meu_decorator(funcao):
    def wrapper():
        print('antes')
        funcao()
        print('depois')
    return wrapper
@meu_decorator
def parabenizar():
    print('parabens')
    
parabenizar()
# DESAFIO 
def meu_decorator(funcao):
    def wrapper():
        print (datetime.now())
        funcao()
        print(datetime.now())
    return wrapper
@meu_decorator
def horas():
    print('horas')
    
horas()
def decorator(funcao):
    def hora():
        print(datetime.now())
        funcao()
        print(datetime.now())
    return hora
@decorator
def horas():
    print('horas')
horas()        
        
