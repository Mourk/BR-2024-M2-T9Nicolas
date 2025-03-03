import pygame
import os

# Global Constants
TITLE = "Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 60
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/DinoRunShield1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/DinoRunShield2.png")),
]

RESET_BUTTON = pygame.image.load(os.path.join(IMG_DIR, 'Other/reset.png'))


RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/DinoRunHammer1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/DinoRunHammer2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/Jump/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/Jump/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/Jump/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Ducking/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Ducking/DinoDuck2.png")),
    
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Ducking/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Ducking/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Ducking/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Ducking/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/arvore1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/arvore2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/arvore3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/arvore4.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/passaro1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/passaro2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/passaro3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/passaro4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/passaro5.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOVer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
