import random

from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS
from dino_runner.components.obstacles.obstacle import Obstacle


class Cactus(Obstacle):

    CACTUS = [
        (LARGE_CACTUS, 300),
        (SMALL_CACTUS, 325), #adicionei a lista de cactos
    ]
    def __init__(self): #removi "image" já que no terminal o erro indicava que não havia um diretório para imagem, adicionei a variável "cactus_pos"
        image, cactus_pos = self.CACTUS[random.randint(0, 1)]
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)

        self.rect.y = cactus_pos