# heranca multipla
class Pessoa:
    nome = 'sou adalberto'
    def convidar(self):
        print('ola, vamos ao evento?')
class Profissional:
    nome = 'profissional'
    def convidar2(self):
        print('ola, vamos ao evento profissional?')
class AtorProfissional(Pessoa,Profissional):
    pass
ator = AtorProfissional()
ator.convidar()
