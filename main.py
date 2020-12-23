## https://www.youtube.com/watch?v=UEO1B_llDnc
# Python Hangman Tutorial #1 - Learn to Make Games with Pygame
# Tech With Tim
# Created: 2020-12-23

import pygame
import os

# setup display
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

# load images
images = []
for i in range(6):
    images.append(pygame.image.load("images/hangman" + str(i)+ ".png"))

# game variables
hangman_status  = 0 # which image to draw

#colors
WHITE = (255,255,255)

# setup game loop
FPS = 60
clock = pygame.time.Clock()
run = True

while run:
    clock.tick(FPS)
    
    win.fill(WHITE)
    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)


pygame.quit()
