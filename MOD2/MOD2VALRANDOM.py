import random
# Valores aleatórios com random
print(random.random())# gera um valor de 0.0 a 1.0
# gera um valor decimal de valor minimo ao valor maximo
print(random.uniform(4, 10))# gera um valor quebrado aleatorio de quatro ate 10
print(random.randint(4,10))# gera um valor inteiro aleatorio 
cores = ['verde', 'vermelho', 'azul']# escolher opcao aleatorio
print(random.choice(cores,))# para fazer random com variaveis usar choice 
cartas = ['carta1', 'carta2', 'carta3', 'carta4']# embaralhar uma lista
print(random.shuffle(cartas))# shuffle para embaralhar as cartas
print(cartas)
# DESAFIO 1
moeda = ['cara', 'coroa']
print(random.choice(moeda))
# DESAFIO 2
nomes = ['kevin', 'jeferson', 'mario', 'herique', 'soraia']
print(random.choice(nomes))
# DESAFIO 3
print(random.randint(10, 100))