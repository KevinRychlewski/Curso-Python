class Pessoa:
    def __init__(self):
        self.nome = 'sou uma pessoa'
        self.habilidade = ['habilidade 1','habilidade 2','habilidade 3']
    # representacao para programadores(chamado com metodo repr(pessoa))
    def __repr__(self):
        return 'classe pessoa com propriedades nome e habilidade'
    # '''o que deve ser mensurado para determinar o quantidade daqulea classe
    # (chamada com metodo(len(pessoa)))'''
    def __len__(self):
        return len(self.habilidades)
    def __str__(self):
        return f'{self.nome} com as habilidades {self.habilidade}'
pessoa = Pessoa()
print(pessoa.nome)
print(repr(pessoa))
print(len(pessoa))
print(pessoa)
print(dir(pessoa))