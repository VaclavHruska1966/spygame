import pygame

# Inicializace pygame

pygame.init()


#Vytvoření obrazovky
width = 1000
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Naše první hra")
# Hlavní herní cyklus

player = pygame.Rect((300,250,50, 50))

lets_continue = True



while lets_continue:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255,0,0), player)
    
    keys=pygame.key.get_pressed()
    if keys[pygame.K_a]:
        move_player=-10
    
    
    
    
    for event in pygame.event.get():
        print(event)
        
        
        if event.type == pygame.QUIT:
            lets_continue = False

    pygame.display.update()
#Ukončení hry
pygame.quit()
