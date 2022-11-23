import pygame 
pygame.init() 

screen = pygame.display.set_mode((600,600)) 
run =True 
while run: 
    screen.fill((144, 201, 120)) 
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT : 
            run = False
    
    pygame.display.update()