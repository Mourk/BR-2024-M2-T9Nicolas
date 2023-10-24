import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager

FONT_STYLE = "freesansbold.ttf"


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.high_score = 0
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.score = 0
        self.death_count = 0

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()  

        pygame.display.quit()
        pygame.quit()          

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.record_death()
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()
        self.power_up_manager.update(self)

    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 2

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()  
        self.draw_high_score()
        self.draw_score()      
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed   

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()   

    def draw_high_score(self):
        self.draw_text(f"High Score: {self.high_score}", (1000, 30))

    def record_death(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.death_count += 1

    def draw_text(self, message, center_pos, font_size=22):
        font = pygame.font.Font(FONT_STYLE, font_size)
        text = font.render(message, True, (0, 0, 0))
        self.screen.blit(text, text.get_rect(center=center_pos))

    def draw_score(self):
        self.draw_text(f"Score: {self.score}", (1000, 60))

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show > 0:
                self.draw_text(f"{self.player.type.capitalize()} enabled for {time_to_show} seconds", (500, 50), 18)
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def reset_game(self):
        self.score = 0
        self.game_speed = 10
        self.player.type = DEFAULT_TYPE
        
    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()   

    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2

        if self.death_count == 0:
            self.draw_text("Press any key to start", half_screen)
        else:
            self.reset_game()
            self.screen.blit(ICON, (half_screen[0] - 20, half_screen[1] - 140))
            self.draw_text("Press any key to restart", (half_screen[0], half_screen[1] + 50))
            self.draw_text(f"Deaths: {self.death_count}", (half_screen[0], half_screen[1] + 90))
            self.draw_text(f"High Score: {self.high_score}", half_screen)

        pygame.display.update()
        self.handle_events_on_menu()