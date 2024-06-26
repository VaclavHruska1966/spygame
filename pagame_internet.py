# import pygame module in this program  
import pygame 
  
# activate the pygame library .   
# initiate pygame and give permission   
# to use pygame's functionality.   
pygame.init() 
  
# create the display surface object   
# of specific dimension..e(500, 500).   
win = pygame.display.set_mode((1000, 1000)) 
  
# set the pygame window name  
pygame.display.set_caption("Naše první hra") 
  
# object current co-ordinates  
x = 480
y = 450
  
# dimensions of the object  
width = 20
height = 20
  
# velocity / speed of movement 
vel = 10
  
# Indicates pygame is running 
run = True
clock= pygame.time.Clock()
# infinite loop  
while run: 
    # creates time delay of 10ms  
    pygame.time.delay(10) 
      
    # iterate over the list of Event objects   
    # that was returned by pygame.event.get() method.   
    for event in pygame.event.get(): 
          
        # if event object type is QUIT   
        # then quitting the pygame   
        # and program both.   
        if event.type == pygame.QUIT: 
              
            # it will make exit the while loop  
            run = False
    # stores keys pressed  
    keys = pygame.key.get_pressed() 
      
    # if left arrow key is pressed 
    if keys[pygame.K_LEFT] and x>0: 
          
        # decrement in x co-ordinate 
        x -= vel 
          
    # if left arrow key is pressed 
    if keys[pygame.K_RIGHT] and x<1000-width: 
          
        # increment in x co-ordinate 
        x += vel 
         
    # if left arrow key is pressed    
    if keys[pygame.K_UP] and y>0: 
          
        # decrement in y co-ordinate 
        y -= vel 
          
    # if left arrow key is pressed    
    if keys[pygame.K_DOWN] and y<1000-height: 
        # increment in y co-ordinate 
        y += vel 
         
              
    # completely fill the surface object   
    # with black colour   
    win.fill((0, 0, 0)) 
      
    # drawing object on screen which is rectangle here  
    pygame.draw.rect(win, (255, 255, 255), (x, y, width, height)) 
      
    # it refreshes the window 
    pygame.display.update()  
    clock.tick(60)
# closes the pygame window  
pygame.quit() 