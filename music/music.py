import time
import sys
import pygame

#pygame.init()
pygame.mixer.init()
print("play:\n")
#screen = pygame.display.set_mode([480,320])
track = pygame.mixer.music.load('NumberVoc/music.mp3')
pygame.mixer.music.set_volume(1.0)
while True:	
	if pygame.mixer.music.get_busy() == False:
		pygame.mixer.music.play()
#time.sleep(10)
#pygame.mixer.music.stop()
