class Camera:
    def __init__(self, marca, megapixels):
        self.marca = marca
        self.megapixels = megapixels
    def tirar_foto(self):
        print(f'foto tirada com a camera {self.marca} com a qualidade de {self.megapixels} megapixels')
class CameraCelular(Camera):
    pass
class CameraCelular(Camera):
    def __init__(self, marca, megapixels, quantidade_de_cameras):
        super().__init__(marca,megapixels)
        self.quantidade_de_cameras = quantidade_de_cameras
    def aplicar_filtro(self, filtro):
        print(f'aplicanto filtro {filtro}')
    def tirar_foto(self,camera_a_utilizar):
        print(f'foto tirada com a camera {self.marca} com a qualidade de {self.megapixels} megapixels, utilizando camera {camera_a_utilizar}')
camera_celular = CameraCelular('sony','25mp',4)
camera_celular.aplicar_filtro('azul')
camera_celular.tirar_foto(2)
class CameraSeguranca(Camera):
    def __init__(self, marca, megapixels, horas_maxima_de_gravacao):
        super().__init__(marca,megapixels)
        self.horas_maxima_de_gravacao = horas_maxima_de_gravacao
    def rotacionar(Self,direcao):
        print(f'rotacionando a camera para {direcao}')
camera_segurancao = CameraSeguranca('sony','5mp',10)
camera_segurancao.rotacionar('direita')
'''print(issubclass(CameraCelular,Camera))
print(issubclass(CameraSeguranca,Camera))'''
class CameraIphone(Camera):
    def __init__(self, marca, megapixels, espaco_sobrando):
        super().__init__(marca, megapixels)
        self.espaco_sobrando = espaco_sobrando
    def espaco(self,espaco):
        print(f'ainda tem {espaco}')
camera_iphone = CameraIphone('sony','5mp',90)
camera_iphone.espaco(90)
class Usuario:
    def __init__(self,nome,idade,altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
    def contar(self,funcionario):
        print(f'novo funcionario {self.nome} {funcionario} com a idade de {self.idade} e a altura de {self.altura}')
usuario = Usuario('kevin','17','1,60')
usuario.contar(1)

