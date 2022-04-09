
import pygame
from math import floor

pygame.init()

class CursorPointer:
    def __init__(self, color: tuple, size: int) -> None:
        self.color = color
        self.size = size
        self.surface = pygame.Surface((self.size, self.size))
        self.surface.set_colorkey((0,0,0))
        self.center_position = self.surface.get_rect().center

        #circle
        self.radius = size / 4
        self.circle_with = floor(size / 10)

        #lines

        self.horizontal_line_start_L = (self.center_position[0] - self.radius * 2, self.center_position[1])
        self.horizontal_line_end_L = (self.center_position[0] - self.radius , self.center_position[1])

        self.horizontal_line_start_R = (self.center_position[0] + self.radius * 2, self.center_position[1])
        self.horizontal_line_end_R = (self.center_position[0] + self.radius , self.center_position[1])

        self.vertical_line_start_U = (self.center_position[0] , self.center_position[1] - self.radius * 2)
        self.vertical_line_end_U = (self.center_position[0] , self.center_position[1] - self.radius )

        self.vertical_line_start_B = (self.center_position[0] , self.center_position[1] + self.radius * 2)
        self.vertical_line_end_B = (self.center_position[0] , self.center_position[1] + self.radius)

        #animation
        self.animation_speed = 0.1
        self.animation_index = 1


    def shot_animate(self, event) -> None:
        if event.button == 1:
            self.animation_index = 0
       
        
    def animate(self) -> None:
        if self.animation_index <= 1:
            self.animation_index += self.animation_speed

    def draw(self) -> None:
        radius = self.radius if  self.animation_index <= 1 else self.radius * 2 

        pygame.draw.circle(self.surface, self.color, self.center_position, radius, self.circle_with)

        pygame.draw.line(self.surface, self.color, self.horizontal_line_start_L, self.horizontal_line_end_L, self.circle_with)
        pygame.draw.line(self.surface, self.color, self.horizontal_line_start_R, self.horizontal_line_end_R, self.circle_with)
        pygame.draw.line(self.surface, self.color, self.vertical_line_start_U, self.vertical_line_end_U, self.circle_with)
        pygame.draw.line(self.surface, self.color, self.vertical_line_start_B, self.vertical_line_end_B, self.circle_with)
        
           
    def get_cursor(self):

        self.surface.fill((0,0,0))
        self.draw()

        return pygame.cursors.Cursor(self.center_position, self.surface)


      

       