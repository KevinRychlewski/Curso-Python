class Usuario:
    def __init__(self, nome, salario, profissao):
        self.nome = nome
        self.salario = salario
        self.profissao = profissao
    def registrar_funcionario(self):
        print(f'cadastrando usuario {self.nome}')
        
class Gestor:
    def __init__(self,nome,salario,profissao,setor_responsavel):
        super().__init__(nome, salario, profissao)
        self.setor_responsavel = setor_responsavel
        
    def definir_setor(self,setor):
        print(f'definindo setor para {setor}')
        
usuario1 = Usuario('camila',5000,'analista de software')
gestor = Gestor('roberta',7000,'gestora','gestao de projetos')


# heranca multinivel
# primeiro problema
class Veiculo:
    pass
class VeiculoDeRodas(Veiculo):
    pass
class Carro(VeiculoDeRodas):
    pass
class CarroEletrico(Carro):
    pass
class CarroEletricoDuasPortas(CarroEletrico):
    pass
