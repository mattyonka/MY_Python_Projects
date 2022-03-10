import random
import pygame
import keyboard
"""This program is a simple test on using and applying Pygame concepts to move a character around and get the apple using the arrow keys"""
#moves the character based on keyboard input
def move(xpos,ypos,screen_width,screen_height):
    #defining variables
    
    step_x = 0
    step_y = 0

    #how fast character moves
    scale = 5
    
    
    #move on x,y axis
    if keyboard.is_pressed("up"):
        step_y = step_y - scale
    if keyboard.is_pressed("down"):
        step_y = step_y + scale
    if keyboard.is_pressed("left"):
        step_x = step_x - scale
    if keyboard.is_pressed("right"):
        step_x = step_x + scale


    #if out of bounds don't move
    if xpos > screen_width-32 and step_x > 0 :
        step_x = 0
    if xpos < 0 and step_x < 0 :
        step_x = 0
    if ypos > screen_height-32 and step_y > 0 :
        step_y = 0
    if ypos < 0 and step_y < 0 :
        step_y = 0
        
        
    return(step_x,step_y)

#checks if the apple and banana collide
def is_score(xpos,ypos,a_xpos,a_ypos):
    if abs(xpos-a_xpos) <= 16 and abs(ypos-a_ypos) <= 16:
        return(True)
    else:
        return(False)

#places the apple randomly (Does not protect againt placing it in the same area, maybe fix later if I care)
def get_apple(screen_width,screen_height):
    rand_x,rand_y = random.randrange(32,screen_width-32),random.randrange(32,screen_height-32)
    return(rand_x,rand_y)
    
def main():
    pygame.init()
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("Simple Game Test - Get Apple")
    
    
    screen_width = 480
    screen_height = 360
    fill_color = [108,158,93]
    screen = pygame.display.set_mode((screen_width,screen_height))
    running = True

    #main loop

    #Starting Position
    xpos = int((screen_width/2)-16)
    ypos = int((screen_height/2)-16)
    
    #apple starting position
    a_xpos,a_ypos = get_apple(screen_width,screen_height)
    
    #step
    step_x = 0
    step_y = 0
    score = 0
    clock = pygame.time.Clock()
    
    #loading images
    image = pygame.image.load("testnanner.png")
    apple = pygame.image.load("apple.png")
    
    #establishing Screen
    screen.fill(fill_color)
    screen.blit(image,(50,50))
    screen.blit(apple,(a_xpos,a_ypos))
    pygame.display.flip()
    pygame.font.init()


    #establishes gameplay loop
    while running:
        #sets framerate to 30? 
        clock.tick(30)

        

        
        
        #sets step to 0 then calls the move function to see if they changed positions
        step_x,step_y =(0,0)
        step_x,step_y = move(xpos,ypos,screen_width,screen_height)
        
        xpos += step_x
        ypos += step_y

        
        #redrawing screen every frame
        screen.fill(fill_color)
        screen.blit(apple,(a_xpos,a_ypos))
        screen.blit(image,(xpos,ypos))

        #checks if apple colides with banana
        if is_score(xpos,ypos,a_xpos,a_ypos) == True:
            score += 1
            a_xpos,a_ypos = get_apple(screen_width,screen_height)
            
            
        
        #draws score
        score_str = str(score)
        default_font = pygame.font.get_default_font()
        score_font = pygame.font.Font(default_font,12)
        screen.blit(pygame.font.Font.render(score_font,"Score = ",1,(0,0,0)),(12,12))
        screen.blit(pygame.font.Font.render(score_font,score_str,1,(0,0,0)),(60,12))


        


        #Completes screen draw
        pygame.display.flip()


        #quit command if x is clicked on window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                

if __name__ == "__main__":
    main()



