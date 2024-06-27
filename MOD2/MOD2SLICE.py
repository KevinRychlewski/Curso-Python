teclado ='teclado'
print(teclado[-1])# normal
print(teclado.index('l'))# segundo jeito
print(teclado[teclado.index('l')])# jeito dinamico
frase = 'Clean Code'
print(frase.rindex('C'))# como acessar o ultimo caracter dentro de uma string
# Acessando partes de um string
link = 'facebook.com/devaprender'
print(link[0])# acessar o primeiro item de um string
print(link[-1])# acessar o ultimo string
print(link[0:5])# onde ele vai comecar e onde ele vai acabar
print(link[0:])# vai inicar do comeco ate o final
print(link[-5:])# vai ate o final e vai voltar 5 indices
print(link[5:])# vai do indice especificado ate o final
print(link[:-5])# vai do 0  ate a posicao final q vc colocou
# DESAFIO
biblioteca = 'Biblioteca'
print(biblioteca[biblioteca.index('o')])
# DESAFIO 2
des = 'Desenvolvimento De Aplicações'
print(des[16:])