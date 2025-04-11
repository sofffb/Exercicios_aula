# como reproduzir um arquivo MP3
# primeiro ter um aquivo com um nome simples, pequeno, sem caracteres
# adicionar o arquivo ao pycharm

import pygame
pygame.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
