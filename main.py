
import pygame
from ballon import generate_new_ballon
from label import Label
from cursor_pointer import CursorPointer
from sound import play_bg_music,play_sound_sfx, stop_bg_music

pygame.init()
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1080,720
FPS = 60
BG_COLOR = (105,121,219)
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('BallonShot')

def main():

    #Game initial setup
    speed = 1
    points = 0
    label_color = (255,255,255)
    max_ballons = 5

    play_bg_music()

    cursor = CursorPointer((230,230,230),25)       
    pygame.mouse.set_cursor(cursor.get_cursor())

    #labels
    label_points = Label("Pontuação:",label_color,(30,30))
    label_final = Label("Voce perdeu a sua pontuação é ",label_color,(300,360))
    label_final.set_visible(False)
    label_speed = Label("Speed:",label_color,(30,60))
    
    for i in range (max_ballons):
       ballons = generate_new_ballon()
     

    while True:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                 exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for ballon in ballons:
                    if ballon.mouse_trigger(event):
                        ballons.remove(ballon)
                        play_sound_sfx("pop")
                        ballons = generate_new_ballon(ballons)
                        points += 1

                cursor.shot_animate(event)
                if event.button == 1:
                   play_sound_sfx("gun_shot")
                   

        screen.fill(BG_COLOR)
        mouse_position = pygame.mouse.get_pos()
        speed += 0.001

        #labels

        label_points.label_add_text(f"{points}")
        label_points.draw(screen)

        label_speed.label_add_text(f"{round(speed,3)}")
        label_speed.draw(screen)
        
        label_final.draw(screen)

        #cursor
        cursor.animate()
        pygame.mouse.set_cursor(cursor.get_cursor())

        for ballon in ballons:
            ballon.update(screen,speed,mouse_position)
           
            if ballon.bottom < 0:
                ballons.clear()

                label_speed.set_visible(False)
                label_points.set_visible(False)

                label_final.label_add_text(f"{points}")
                label_final.set_visible(True)

                stop_bg_music()
                play_sound_sfx("game_over")



        
        
        pygame.display.update()


if __name__ == "__main__":
    main()  