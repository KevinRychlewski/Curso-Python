'''# como criar e modificar arquivos:
'r' -> usado somente para ler algo
'w' -> usado somente para escrever algo
'r+' -> usado para ler e escrever algo
'a' -> usado para acrescentar algo
'''
import os
with open('celulares.txt','w') as arquivo:
    arquivo.write('celular 1')
nomes = ['lucas', 'carol', 'jeff','douglas']
numeros = [1,2,3,4,5,6]
with open('numeros.txt','a', newline='') as arquivo:
     for numero in numeros:
         arquivo.write(str(numero) + os.linesep)
with open('nomes.txt', 'r') as arquivo:
     for linha in arquivo:
         print(linha)
with open('numeros.txt','r+') as arquivo:
     for linha in arquivo:
         print(linha)
     arquivo.write('9000')
# DESAFIO 1
frutas = ['maca','banana','melancia','pera','abacaxi']
cores = ['vermelho','azul','preto','amarelo','verde']
linguagens = ['python','java','sql','php','javascript']
with open('frutas.txt','w', newline='') as arquivo:
     for fruta in frutas:
        arquivo.write(fruta + os.linesep)
        print(fruta)
# DESAFIO 2
with open ('frutas.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)
with open('frutas.txt','a', newline='') as arquivo:
    for cor in cores:
        arquivo.write(os.linesep + cor)
        print(cor)
with open('top 5 linguagens.txt','w',newline='') as arquivo:
    for lingua in linguagens:
        arquivo.write(lingua + os.linesep)
        print(lingua)
arquivos =  ['musica.mp3', 'foto.jpg', 'senhas.txt', 'relatorio.pdf']
for arquivo in arquivos:
    with open(arquivo,'w') as arquivo:
        pass