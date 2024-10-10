import pygame 
pygame.init()
print('Teste')
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()