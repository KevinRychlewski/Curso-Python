# caso a idade seja maior ou igual a 18 anos, essa pessoa é maior de idade, caso contrario ela é menor de idade
idade = 15
if idade >= 18:
    print('maior de idade')
else:
    print('menor de idade')
idade1 = 25
print('maior de idade') if idade1 >= 18 else print('menor de idade')
#expressao = if condicao else expressao
possui_passaporte = True
print('Favor embarcar') if possui_passaporte else print('favor tirar passaporte')
# DESAIO
velocidade = 200
print('voce foi multado' if velocidade >=100 else print('siga em frente'))