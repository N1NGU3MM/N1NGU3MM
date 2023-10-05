import pygame
pygame.init()

x= 500
y= 500
speed = 20
#PS = 60

surface = pygame.display.set_mode((1000,1000))
pygame.display.set_caption('criando jogo')

windows_open = True
while windows_open:
    pygame.time.delay(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            windows_open = False
            
    command = pygame.key.get_pressed()
    if command[pygame.K_UP]:
       y -= speed
    if command[pygame.K_DOWN]:
       y += speed    
    if command[pygame.K_LEFT]:
        x -= speed
    if command[pygame.K_RIGHT]:
        x += speed         

    
    
    surface.fill((0,0,0))

    pygame.draw.circle(surface,(0,255,0),(x,y),60)
    pygame.display.update()
    
pygame.quit()

# o 
