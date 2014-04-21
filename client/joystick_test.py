import os
import pygame, sys
from pygame.locals import *
import socket
import time

pygame.init()

### Tells the number of joysticks/error detection
joystick_count = pygame.joystick.get_count()
print ("There is ", joystick_count, "joystick/s")
if joystick_count == 0:
    print ("Error, I did not find any joysticks")
else:
    my_joystick = pygame.joystick.Joystick(0)
    my_joystick.init()

screen = pygame.display.set_mode((450, 250))
pygame.display.set_caption('Basic Pygame program')

# Fill background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

clock = pygame.time.Clock()

# Display some text
font = pygame.font.Font(None, 36)

# Connect to the vehicle
HOST, PORT = "localhost", 9002
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


sock.connect((HOST, PORT))

prev_s1x = 0.0
prev_s1y = 0.0
prev_s2x = 0.0
prev_s2y = 0.0


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        
    stick1_x = my_joystick.get_axis(0)
    stick1_y = -1.0*my_joystick.get_axis(1)
    stick2_x = my_joystick.get_axis(3)
    stick2_y = -1.0*my_joystick.get_axis(4)

    stick1_x = round(stick1_x, 2)
    stick1_y = round(stick1_y, 2)
    stick2_x = round(stick2_x, 2)
    stick2_y = round(stick2_y, 2)

    if (prev_s1x, prev_s1y, prev_s2x, prev_s2y) == (stick1_x, stick1_y, stick2_x, stick2_y):
      continue

    prev_s1x = stick1_x
    prev_s1y = stick1_y
    prev_s2x = stick2_x
    prev_s2y = stick2_y

    sock.sendall("/set_thrust %.2f,%.2f,%.2f,%.2f\n" % (stick1_x, stick1_y, stick2_x, stick2_y))

    background.fill((250, 250, 250))
    text = font.render(str(stick1_x), 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centery = 30.0
    textpos.centerx = background.get_rect().centerx

    background.blit(text, textpos)

    text = font.render(str(stick1_y), 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centery = 80.0
    textpos.centerx = background.get_rect().centerx

    background.blit(text, textpos)


    text = font.render(str(stick2_x), 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centery = 130.0
    textpos.centerx = background.get_rect().centerx

    background.blit(text, textpos)

    text = font.render(str(stick2_y), 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centery = 180.0
    textpos.centerx = background.get_rect().centerx

    background.blit(text, textpos)

    screen.blit(background, (0, 0))
    pygame.display.flip()
    
    pygame.time.delay(50)
    #clock.tick(60) 


sock.close()
