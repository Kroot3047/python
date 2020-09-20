#import os
#import pygame
#surface = pygame.display.set_mode((100, 100), 0, 32)
#surface.fill((255, 255, 255))
#pygame.draw.circle(surface, (0, 0, 0), (10, 10), 15, 0)
#pygame.display.update()
#pygame.image.save(surface, os.path.expanduser("~/Desktop/pic.png"))
#pygame.image.save(surface, 'E:\py\Python Project\sc\pic.png')

import PIL.ImageGrab
import time

time.sleep(3)
im = PIL.ImageGrab.grab()  # box = (0, 0, 300, 300)   
#im.show()
im.save("sc.jpg")