import random
import pygame
from dino_runner.components.power_ups.power_up import ExtraLifePowerUp
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.utils.constants import SHIELD_TYPE
from dino_runner.components.power_ups.shield import Shield

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0

    def generate_power_up(self, score):
        if len(self.power_ups) == 0:
            if score != 0:
                if score % 500 == 0:
                    self.power_ups.append(Hammer())
                elif score % 1000 == 0:
                    self.power_ups.append(ExtraLifePowerUp())
                elif self.when_appears == score:
                    self.when_appears += random.randint(200, 300)
                    self.power_ups.append(Shield())

    def update(self, game):
        self.generate_power_up(game.score)
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)

            if isinstance(power_up, Hammer):
                if game.player.dino_rect.colliderect(power_up.rect):
                    game.player.has_hammer = True
                    self.power_ups.remove(power_up)
                    power_up.start_time = pygame.time.get_ticks()
                    game.player.power_up_time = power_up.start_time + 3000

            elif isinstance(power_up, Shield):
                if game.player.dino_rect.colliderect(power_up.rect):
                    game.player.has_power_up = True
                    game.player.type = SHIELD_TYPE
                    self.power_ups.remove(power_up)
                    power_up.start_time = pygame.time.get_ticks()
                    game.player.power_up_time = power_up.start_time + 3000

            elif isinstance(power_up, ExtraLifePowerUp):
                if game.player.dino_rect.colliderect(power_up.rect):
                    game.player.extra_lives += 1
                    self.power_ups.remove(power_up)


    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen) 

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 300)
