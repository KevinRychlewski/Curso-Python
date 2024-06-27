# codigo solto
marca = input('digite a marca do seu computador')
memoria = input('digite a quantidade de memoria ram')
placa = input('digite o nome da placa de video')
print(f'seu computador é da marca {marca}')
print(f'seu computador possui {memoria} de memoria')
print(f'seu computador posui uma placa de video {placa}')
# funcoes
def exibir_informacoes_do_computador():
    marca = input('digite a marca do seu computador')
    memoria = input('digite a quantidade de memoria ram')
    placa = input('digite o nome da placa de video')
    print(f'seu computador é da marca {marca}')
    print(f'seu computador possui {memoria} de memoria')
    print(f'seu computador posui uma placa de video {placa}')
exibir_informacoes_do_computador()
# classes
class Computador:
    def __init__(self, marca,memoria,placa):
        self.marca = marca
        self.memoria = memoria
        self.placa = placa
# marca, memoria ram, placa de video
computador1 = Computador('asus','8gb','nvidia')
print(computador1.marca)
print(computador1.memoria)
print(computador1.placa)
computador2 = Computador('dell','4gb','ati')
print(computador2.marca)
print(computador2.memoria)
print(computador2.placa)

