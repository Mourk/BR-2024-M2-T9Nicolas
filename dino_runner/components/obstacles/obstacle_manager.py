import random
import pygame
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
            
    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(random.choice([Cactus(), Bird()]))
            
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.has_hammer:
                    self.obstacles.remove(obstacle)
                elif not game.player.has_power_up:
                    pygame.time.delay(500)
                    game.game_over()
                    game.playing = False
                    game.death_count += 1
                    break

    def reset_obstacles(self):
        self.obstacles = []

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)