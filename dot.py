from game_parameters import *
import pygame
import random

class Dot:
    def __init__(self):
        self.color = random.choice(['red','blue'])
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
    
    def draw(self, screen):
        if self.color == 'red':
            color = DOT_RED
        else:
            color = DOT_BLUE
        pygame.draw.circle(screen, color, (self.x, self.y), DOT_SIZE)