import pygame

class Label:
    def __init__(self, label_text:str, color:tuple, position:tuple) -> None:
        
        self.defaut_label= label_text
        self.label = label_text
        self.font = "monospace"
        self.font_size = 25
        self.font_color = color
        self.postion = position
        self.is_visible = True


    def draw(self, surface) -> None:
        if self.is_visible:
            text_font = pygame.font.SysFont(self.font, self.font_size)
            text = text_font.render(self.label, 1, self.font_color)
            text_rect = text.get_rect()
            text_rect.topleft = self.postion
            surface.blit(text,text_rect)

    def label_add_text(self,text):
       self.label = self.defaut_label + text   
    
    def set_visible(self,state):
        self.is_visible = state
