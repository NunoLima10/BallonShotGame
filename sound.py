import pygame
from pygame import mixer

sound_sfx ={
    "game_over":mixer.Sound('assets/game_over.mp3'),
    "gun_shot":mixer.Sound('assets/gun_shot.mp3'),
    "pop":mixer.Sound('assets/pop.mp3'),
}

def play_bg_music()-> None:
    mixer.music.load('assets/bg_music.mp3')
    mixer.music.play(-1)

def stop_bg_music()-> None:
    mixer.music.fadeout(1000)


def play_sound_sfx(sound) -> None:
    if sound in sound_sfx:
        sound_sfx[sound].play(fade_ms=100)
