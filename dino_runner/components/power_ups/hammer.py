from dino_runner.utils.constants import HAMMER, DEFAULT_TYPE
from dino_runner.components.power_ups.power_up import PowerUp

class Hammer(PowerUp):
    def __init__(self):
        self.image = HAMMER
        self.type = DEFAULT_TYPE
        super().__init__(self.image, self.type)
