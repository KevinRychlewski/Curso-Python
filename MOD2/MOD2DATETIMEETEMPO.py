from datetime import datetime

print(datetime.now())# para saber a hora exata do dia de hj
print(datetime.now().day)# para saber o dia
print(datetime.now().month)# para saber o mes
print(datetime.now().year)# para saber o ano

# Criar uma data
lancamento = datetime(2024,8,25)
print(lancamento)
# Quero receber a data de lancamento do meu aplicativo
# 25/08/2024
data = datetime.strptime(input('quando devemos lancar o aplicativo?'),'%d/%m/%Y')# como extrair a data do seu usuario
print(data)
print(type(data))
# Calcular o intervalo entre datas
data1 = datetime.now()
prazo = data1 - data
print(prazo.days)
# DESAFIO
aniversario = datetime(2024,8,25)
diasparaaniversario = aniversario - datetime.now()
print(diasparaaniversario)