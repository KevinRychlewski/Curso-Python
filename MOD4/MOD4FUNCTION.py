
'''def nome_da_funcao(parametros):
    #comandos'''
def dar_boas_vindas():
    print('bem vindo')

dar_boas_vindas()

def dar_boas_vindas_personalizada(nome):
    print(f'bem vindo {nome}')
dar_boas_vindas_personalizada('jhonatan')
# valor padrao
def apresentar_lugar(horario_de_funcionamento,lugar ='nossa loja'):
    print(f'conheca {lugar}, horario de funcionamento das {horario_de_funcionamento}')
apresentar_lugar('08:00 as 18:00')
# DESAFIO 1
def gerar_nome_completo(nome):
    print(f'bem vindo {nome}')
gerar_nome_completo('kevin')
# DESAFIO 2
def calculas_valores(preco, quantidade=1):
    print(preco*quantidade)
calculas_valores(10,2)