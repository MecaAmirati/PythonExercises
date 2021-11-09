import pygame
pygame.init()
pygame.mixer.music.load('xs021.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()):pass
