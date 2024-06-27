# metodos comuns
class Computador:
    sistema_operacional = 'windows 10'
    def __init__(self,marca,memoria,placa):
        self.marca = marca
        self.memoria = memoria
        self.placa = placa
    def exibir_dados_do_computador(self):
        print(self.marca, self.memoria,
              self.placa, self.sistema_operacional)
# metodos de uma classe
    @classmethod
    def computador_escritorio(cls, memoria):
        return cls('dell',memoria,'placa de video - baixo custo')
    @classmethod
    def computador_configuracao_pesado(cls,memoria):
        return cls('dell',memoria,'placa de video - alto nivel')
    @staticmethod
    def roda_programa(memoria):
        if memoria >8:
            return True
        else:
            return False
print(Computador.roda_programa(7))
    # computador1 = Computador.computador_escritorio('8gb')
    # computador2 = Computador.computador_configuracao_pesado('16gb')
    # computador1.exibir_dados_do_computador()
    # computador2.exibir_dados_do_computador()  
    # metodos estaticos
