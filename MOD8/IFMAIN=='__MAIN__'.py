from carro import ligar_carro
from moto import ligar_moto

ligar_carro()
ligar_moto()
if __name__ == '__main__':
    print('ligando veiculos')
    print(f'estamos no arquivo {__name__}')