

from math import radians
import pygame

from random import randint,choice
from ballon import Ballon
from label import Label

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 1080,720
FPS = 60
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('BallonShot')


ballons_colors =[(61,219,98),(83,219,115),(219,61,75),(219,185,72)]
backgound_color = (105,121,219)

def generate_ballon(ballons):
    position = (randint(10,1070),randint(720,760))
    color = choice(ballons_colors)
    radius = randint(30,40)
    ballon = Ballon(color ,radius, position)
    ballons.append(ballon)
    return ballons

def main():
    speed = 1
    click = 0
    playing = True
    label = Label("Pontuação:",(255,255,255),(30,30))
    label_final = Label("Voce perdeu a sua pontuação é ",(255,255,255),(350,360))
    label_final.set_visible(False)
    

    ballons = []
    for i in range (5):
       ballons = generate_ballon(ballons)
     

    while True:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                 exit()
            for ballon in ballons:
                if ballon.mouse_trigger(event):
                    ballons.remove(ballon)
                    ballons = generate_ballon(ballons)
                    click += 1

           


        screen.fill(backgound_color)
        mouse_position = pygame.mouse.get_pos()
        speed += 0.001

        label_final.draw(screen)

        label.draw(screen)
        label.label_text(f"{click}")

        for ballon in ballons:
            ballon.update(screen,speed,mouse_position)
            if ballon.end_position < 0:
                label.set_visible(False)
                label_final.label_text(f"{click}")
                label_final.set_visible(True)
                ballons.clear()

        pygame.display.update()


if __name__ == "__main__":
    main()  