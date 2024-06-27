class Computador:
    sistema_operacional = 'windows 10'
    def __init__(self,marca,memoria,placa):
        self.marca = marca
        self.memoria = memoria
        self.placa = placa
        
    def ligar(self):
        print('estou ligando')
Computador.sistema_operacional = 'windows'
# computador.marca nao fuciona
computador = Computador('dell','8gb','nvidia')
computador.marca = 'asus'
print(computador.marca)
print(computador.sistema_operacional)
Computador.sistema_operacional = 'mac'
computador2 = Computador('asus','2gb','ati')
print(computador2.sistema_operacional)