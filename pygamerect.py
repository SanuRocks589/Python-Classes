import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
done = False
points = [(250,100), (200,300), (300,300)]

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen, (64, 224, 208), pygame.Rect(30,30,60,60))
    pygame.draw.circle(screen, (127,0,255), (180, 100), 50)
    pygame.draw.circle(screen, (255,0,0), (180, 100), 50, 4)
    pygame.draw.polygon(screen, (5,80,130), points)
    pygame.display.flip()