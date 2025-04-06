import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
while True:
    for x in pygame.event.get():
        if x.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()
    