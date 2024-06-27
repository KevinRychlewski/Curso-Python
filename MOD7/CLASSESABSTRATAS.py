# classes abstratas
# criar um contrato(esqueleto) -> que deve ser implementado na classe que a herda
from abc import ABC, abstractclassmethod
'''# abstractcclassmethod = para q qualquer classe posterior a primeira classe 
seja obrigada a definir as funcoes da primeira''' 

class Camera(ABC):
    @abstractclassmethod
    def definir_tamanho_lente(self,tamanho):
        pass
class CameraProfissional(Camera):
    def definir_tamanho_lente(self,tamanho):
        print(f'alterando a lente para {tamanho}')
    
camera_profissional = CameraProfissional()
camera_profissional.definir_tamanho_lente(5)
# DESAFIO
class Monitor(ABC):
    @abstractclassmethod
    def aumentar_claridade(self,valor):
        pass
    @abstractclassmethod
    def diminuir_claridade(self,valor):
        pass
class MonitorFullHD(Monitor):
    def aumentar_claridade(self,valor):
        print(f'aumentando a claridade em {valor}')
    def diminuir_claridade(self,valor):
        print(f'diminuindo a calridade em {valor}')
monitor_full_hd = MonitorFullHD()
monitor_full_hd.aumentar_claridade(5)
monitor_full_hd.diminuir_claridade(5)