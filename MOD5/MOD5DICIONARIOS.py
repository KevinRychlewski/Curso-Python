# dicionarios
pessoa = ['carol',18,1.60,'mike',50,1.80]
#dicionario(chave,valor)
dicionario_pessoa = {'nome':'carol','idade':18,'altura':1.60}
print(dicionario_pessoa)
pessoa2 = dict(nome='carol',idade=18,altura=1.60)
print(pessoa2['idade'])
# ver todas as chaves
print(dicionario_pessoa.keys())
# ver os valores 
print(dicionario_pessoa.values())
# par de chave e valor
print(dicionario_pessoa.items())
# iterar sobre um dicionario
for item in dicionario_pessoa.items():
    print(item)
    print(item[1])

