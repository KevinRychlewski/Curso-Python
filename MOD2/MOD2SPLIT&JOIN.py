frase = 'Ola, bem-vindo a este treinamento'
print(frase.split())
print(frase.split(','))
print(frase.split('-'))
nomes = 'jhonatan, rafael, carol, amanda, jefferson'
print(nomes.split())
print(nomes.split(','))
hashtags = 'music #guitar #game #codar #python'
print(hashtags.split())
print(hashtags.split('#'))
print(hashtags.split('#', 3))
# como concatenar(combinar) strings
hashtags_separadas_por_espaco = hashtags.split(' ')
print(hashtags_separadas_por_espaco)
print(','.join(hashtags_separadas_por_espaco))
print('.'.join(hashtags_separadas_por_espaco))
print(' '.join(hashtags_separadas_por_espaco))
# DESAFIO 1
frase1 = 'Desafio manipulacao de strings'
frase2 = 'jhonatan,rafael,carol,camilla'
palavras1 = frase1.split()
palavras2 = frase2.split(',')
print(','.join(palavras1))
print(' & '.join(palavras2))


