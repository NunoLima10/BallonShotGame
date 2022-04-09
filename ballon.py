
import pygame


WIDTH, HEIGHT = 1080,720

class Ballon:
    def __init__(self,color,radius,position) -> None:
        super().__init__()

        #ballon 1
        self.color = color
        self.radius = radius 

        self.position_x ,self.position_y = position

        # ballon 2
        self.ballon2_radius = radius / 2.5
        self.ballon2_position_x = self.position_x
        self.ballon2_position_y = self.position_y + self.radius

        # ballon line
        self.line_color = (0,0,0)
        self.line_size = 40 
        self.line_end = (self.position_x ,self.position_y + self.line_size * 3)

        #state
        self.on_focus = False

        #last
        self.end_position = self.ballon2_position_y + self.ballon2_radius * 2


    def move(self, speed_x, speed_y)-> None:
        self.position_x -= speed_x
        self.position_y -= speed_y

        self.ballon2_position_x = self.position_x
        self.ballon2_position_y = self.position_y + self.radius

        self.line_end = (self.position_x ,self.position_y + self.line_size * 3)

        self.end_position = self.ballon2_position_y + self.ballon2_radius  * 2


    def mouse_trigger(self, event) -> None:
        return event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.on_focus
         

    def is_on_focus(self, position) -> bool:
        deltaX = (self.position_x - position[0]) ** 2
        deltaY = (self.position_y - position[1]) ** 2
        ballon1 = self.radius > (deltaX + deltaY) ** 0.5

        ballon2_deltaX = (self.ballon2_position_x - position[0]) ** 2
        ballon2_deltaY = (self.ballon2_position_y - position[1]) ** 2
        ballon2 = self.radius > (deltaX + deltaY) ** 0.5

        self.on_focus = ballon1 or ballon2


    def update(self,surface,speed,mouse_postion)-> None:
        self.move(0,speed)
        self.is_on_focus(mouse_postion)
        pygame.draw.line(surface, self.line_color, (self.position_x, self.position_y), self.line_end)
        pygame.draw.circle(surface, self.color, (self.position_x, self.position_y), self.radius)
        pygame.draw.circle(surface, self.color, (self.ballon2_position_x, self.ballon2_position_y), self.ballon2_radius)
        