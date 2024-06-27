from datetime import datetime
import random

#1. Obtenha o nome do usuário
nome = str(input('digite seu nome'))

#2. Obtenha a idade do usuário
idade = int(input('digite sua idade'))

#3. Registre de forma automática a data do cadastro do usuário, usando a data do registro como data de registro
data = datetime.now()
data2 =  data.strftime('%d/%m/%Y')
#4. Para cada novo funcionário que é registrado na empresa, ele recebe um dos seguintes cartões, que é sorteado de forma aleatória:


cartoes = ['R$50,00','R$250,00','R$120,00']
cartoes2 = (random.choice(cartoes))

#5. Guarde informações sobre a data de aniversário do funcionário(dd/mm/aaaa)
aniversario = datetime.strptime(input('digite a data do seu aniversario'),'%d/%m/%Y')
aniversario1 = aniversario.strftime('%d/%m/%Y')
print(aniversario1)

## Módulo 2 - Gerar apresentação do usuário

### Funcionalidades do módulo 2 - Mensagem de boas vindas!
print(f'''Ola {nome}, seu registro foi concluido com sucesso no dia {data2}
Parabens, houve um sorteio e voce ganhou um cartao de compras no valor de {cartoes2}''')
