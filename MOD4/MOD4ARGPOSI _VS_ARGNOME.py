def exibir_preco(*,nome_produto, preco):
    print(f'{nome_produto} esta no valor de: {preco}')
# argumentos posicionais
exibir_preco(nome_produto='iphone', preco=5000)
# argumentos nomeados
exibir_preco(nome_produto='iphone', preco=5000)
exibir_preco(preco=5000, nome_produto='iphone')
# DESFIO 1
def gerar_objeto_personalizado(cor,*,altura,formato):
    print(f'{cor} {altura} {formato}')
gerar_objeto_personalizado('vermelho', altura=1, formato='quadrado')
