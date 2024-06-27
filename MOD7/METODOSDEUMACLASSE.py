# metodos de uma classe -> ligar,desligar,exibir dados do computador
class Computador:
    def __init__(self,marca,memoria,placa):
        self.marca = marca
        self.memoria = memoria
        self.placa = placa
    def ligar(self):
        print('estou ligadno')
    def desligar(self):
        print('estou desligando')
    def exibir_dados_do_computador(self):
        print(
            f'Computador da marca {self.marca}, com {self.memoria} de memoria ram e que usa a placa de video {self.placa}')
    
computador1 = Computador('asus','32gb','nvidia')
computador1.desligar()
computador1.ligar()
computador1.exibir_dados_do_computador()
computador2 = Computador('dell','8gb','nvidia')
computador2.ligar()
computador2.desligar()
computador2.exibir_dados_do_computador()