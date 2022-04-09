

import pygame
from random import randint,choice
WIDTH, HEIGHT = 1080,720

ballons_colors =[(61,219,98),(83,219,115),(219,61,75),(219,185,72)]


def generate_new_ballon(ballons = []) -> list:
    position = (randint(10,1070), randint(720,760))
    radius = (randint(50,60),randint(60,90))
    color = choice(ballons_colors)
    
    ballon = Ballon(color,position,radius)
    ballons.append(ballon)
    return ballons



class Ballon:
    def __init__(self,color:tuple, position:tuple, radius:tuple) -> None:
        super().__init__()

        self.color = color
        self.position_x ,self.position_y = position
        self.radius_x, self.radius_y = radius

        self.rect = pygame.Rect(position,radius)

        self.bottom = self.position_y + self.radius_y
        

        # ballon line
        self.line_color = (0,0,0)
        self.line_size = self.radius_y * 2
        self.line_end = (self.position_x ,self.position_y + self.line_size * 3)

        #state
        self.on_focus = False
        

    def move(self, speed_x, speed_y)-> None:
        self.position_x -= speed_x
        self.position_y -= speed_y

        self.rect = pygame.Rect((self.position_x, self.position_y),(self.radius_x, self.radius_y))

        self.line_end = (self.rect.centerx ,self.rect.centery + self.line_size)

        self.bottom = self.position_y + self.radius_y

    def mouse_trigger(self, event) -> None:
        return event.button == 1 and self.on_focus
         

    def is_on_focus(self, position) -> None:
       self.on_focus = self.rect.collidepoint(position)


    def update(self,surface,speed,mouse_postion)-> None:
        self.move(0,speed)
        self.is_on_focus(mouse_postion)
        pygame.draw.line(surface, self.line_color, self.rect.center, self.line_end)
        pygame.draw.ellipse(surface,self.color,self.rect)
        
        
        