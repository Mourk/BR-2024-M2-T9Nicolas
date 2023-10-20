import random
import pygame
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus #Remoção da constante "SMALL CACTUS"


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(random.choice([Cactus(), Bird()])) #Adicionei aleatóriedade nos obstáculos
            

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)