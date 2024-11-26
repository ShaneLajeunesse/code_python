import pygame

pygame.init()

## Game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
LOWER_MARGIN = 100
SIDE_MARGIN = 300

screen = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN))
pygame.display.set_caption('Level Editor')


## Load images
plx_1_img = pygame.image.load('Background/plx_1').convert_alpha()
plx_2_img = pygame.image.load('Background/plx_2').convert_alpha()
plx_3_img = pygame.image.load('Background/plx_3').convert_alpha()
plx_4_img = pygame.image.load('Background/plx_4').convert_alpha()
plx_5_img = pygame.image.load('Background/plx_5').convert_alpha()

def draw_bg():
    screen.blit(plx_5_img, (0,0))

## Error code with above code:
## Traceback (most recent call last):
  ## File "c:\Users\shane\OneDrive\Desktop\Programs\level_editor1.py", line 16, in <module>
    ## plx_1_img = pygame.image.load('Background/plx_1').convert_alpha()
          ##      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
## FileNotFoundError: No file 'Background/plx_1' found in working directory 'C:\Users\shane'.


## Game loop
run = True
while run:

## Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()