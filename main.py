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

# button variables
RADIUS = 20
GAP = 15
letters = []
startX = round((WIDTH - (RADIUS *2 +GAP) *13) / 2)
startY = 400
for i in range(26):
  x = startX + GAP * 2 + (RADIUS * 2 + GAP) * (i % 13)
  y = startY + (RADIUS * 2 + GAP) * (i // 13)
  letters.append([x, y, chr(65 + i)])

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)

# fonts
LETTER_FONT = pygame.font.Sysfont('comicsans', 40)

# setup game loop
FPS = 60
clock = pygame.time.Clock()
run = True

def draw():
  win.fill(WHITE)
  
  # draw buttons
  for pos in letters:
    x, y, letter = pos
    pygame.draw.circle(win, BLACK, (x,y), RADIUS, 3)
    text = LETTER_FONT.render(letter, 1, BLACK)
    win.blit(text, (x,y))
  
  win.blit(images[hangman_status], (150, 100))
  pygame.display.update()
  
  
while run:
    clock.tick(FPS)
    
    # display    
    draw()
    
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)


pygame.quit()
