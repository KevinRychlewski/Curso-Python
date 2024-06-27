nome_curso = '  edicao de video '
print(nome_curso.upper()) # DEIXA TODAS AS STRINGS EM MAISCULA 
print(nome_curso.lower()) # DEIXA TODAS AS STRINGS EM MINUSCULA
print(nome_curso.strip()) # REMOVE TODOS OS ESPACOS EM BRANCO
print(nome_curso.lstrip())# REMOVE APEANS OS ESPACOS EM BRANCOS DA ESQUERDA
print(nome_curso.rstrip())# REMOVE APENAS OS ESPACOS EM BRANCO DA DIREITA
print(nome_curso.find('cao'))# MOSTRA EM QUAL INDICE COMECA A PALAVRA Q VC QUISER
print(nome_curso.replace('video', 'musica'))# SUBSTITUI A PRIMEIRA PALAVRA Q VC COLOCAR PELA SEGUNDA Q VC COLOCAR
print('https://sc.olx.com.br/?o=90&q=relogio'.replace('relogio', 'carro'))# PODE USAR O REPLACE PRA MUDAR O TIPO DE PESQUISA TBM, DE VEZ RELOGIO POR CARRO
# DESAFIO
a = 'é'
b = 'MELHOR'
c = 'QUE'
d = 'feito'
e = 'perfeito'
print(f'{a.upper()} {b.lower()} {d.upper()} {c.lower()} {e.upper()}')