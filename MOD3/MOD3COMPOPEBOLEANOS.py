# vamos pensar por exemplo no seguinte
'''idade = 21
possui_convite = False
filho_do_dono = True
print(idade >= 21) and (possui_convite == True)
print(idade >= 21 or possui_convite == True)
# maior de 21 e possui o convite ou seja filho do dono
print(idade > 21 and possui_convite == True) or (filho_do_dono == True)
# exemplo
maior_idade = True
possui_carteira_de_trabalho = True
esta_trabalhando_atualmente = True
possui_veiculo_proprio = False
# voce so pode trabalhar aqui se for maior de idade e possuir carteira de trabalho
print(maior_idade == True and possui_carteira_de_trabalho == True)
print(maior_idade and possui_carteira_de_trabalho )
# queremos contratar pessoas que ainda nao possuem um veiculo proprio,mas ja possuam uma carteira de trabalho
print(possui_carteira_de_trabalho == True and not possui_veiculo_proprio == False)'''
# DESAFIO 1
possui_passaporte = False
passagem_comprada = False
menor_de_idade = False
print(possui_passaporte and passagem_comprada and not menor_de_idade)
# DESAFIO 2
print(possui_passaporte or passagem_comprada and not menor_de_idade)
# DESAFIO 3
print(possui_passaporte or passagem_comprada and not menor_de_idade)
# DESAFIO 4
print(not possui_passaporte or passagem_comprada or not menor_de_idade)
# DESAFIO 5
print(possui_passaporte and passagem_comprada and menor_de_idade)
