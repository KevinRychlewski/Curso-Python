# processar vs retornar
#funcao q apenas processa dados
'''print('ola')
# funcoes q retornam dados
cidade = input('qual é a sua cidade')'''
# como escolher entre duncoes que prcessam vs retornam dados?
'''eu vou precisar de usar essa informacao na logica do meu programa ainda?
ou so preicso processar esse dado, mas nao irei utilizar mais ele depois?'''
def exibir_cotacao_do_dia(moeda):
    if moeda == 'usd':
        print(5.47)
exibir_cotacao_do_dia('usd')
def obter_cotacao_do_dia(moeda):
    if moeda == 'usd':
        return 5.47
cotacao = obter_cotacao_do_dia('usd')
if cotacao > 5:
    print('investir em acoes americanas ')
else:
    print('cotacao nao favoravel')