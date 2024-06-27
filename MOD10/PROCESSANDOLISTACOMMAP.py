# Como podemos criar listas?
# Criar listas usando Loops e Range()
numeros = []
for i in range(5):
    numeros.append(i)
print(numeros)
# Map
nomes = ['Larissa','Rafael','Maria','John']
def aprovar_pessoa(nome):
    return nome + ' APROVADO'
    
print(list(map(aprovar_pessoa,nomes)))