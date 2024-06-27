# polimorfismo
print(10 + 20)
print('ola' + 'dev')
print(len('livro'))
print(len([25,20,30]))
print(len({'titulo': 'livro1','lancamento': '2010','categoria': 'lifestyle'}))
class Carro:
    def ligar(self):
        print('ligando')
class Moto:
    def ligar(self):
        print('ligando')
def iniciar(veiculo):
    veiculo.ligar()
carro = Carro()
moto = Moto()
iniciar(carro)
iniciar(moto)
class Pessoa:
    def apresentar(self,nome,idade=None,profissao=None):
        if idade and profissao != None:
            print(f'{nome}, {idade}, {profissao}')
        elif idade != None:
            print(f'{nome}, {idade}')    
        elif profissao != None:
            print(f'{nome}, {profissao}')
        else:
            print(nome)
pessoa = Pessoa()
pessoa.apresentar('amanda')
pessoa.apresentar('amanda',18)
pessoa.apresentar('amanda',18,"programadora")