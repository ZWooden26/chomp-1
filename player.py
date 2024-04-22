import pygame
from game_parameters import *

# Load the sound effects
chomp = pygame.mixer.Sound("assets/sounds/chomp.wav")
hurt = pygame.mixer.Sound("assets/sounds/hurt.wav")

class Player:
    def __init__(self, x, y, color):
        self.color = color
        self.size = MINIMUM_SIZE
        self.x = x
        self.y = y
    
    def set_position(self, x, y):
        if x == -1 or y == -1:
            return # ignore invalid positions
        self.x = x
        self.y = y
        

    def draw(self, screen):
        if self.color == 'red':
            color = PLAYER_RED
        else:
            color = PLAYER_BLUE
        pygame.draw.circle(screen, color, (self.x, self.y), self.size)

    def collide(self, dot):
        if pygame.math.Vector2(self.x, self.y).distance_to(pygame.math.Vector2(dot.x, dot.y)) < self.size:
            if self.color == dot.color:
                self.size += SIZE_INCREMENT
                pygame.mixer.Sound.play(chomp)
            else:
                self.size = max(MINIMUM_SIZE, self.size - SIZE_INCREMENT)
                pygame.mixer.Sound.play(hurt)
            return True
        return False