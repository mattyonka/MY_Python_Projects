import random
import pygame
import keyboard

"""This game is inspired from the classic game, Snake, made from memory.
This program lets you control snake with the arrow keys and get the apples, the game gets faster as you get more apples.
Currently still has the debug position lists displayed"""
class screen:
    width = 512
    height = 512

    def __init__(self):
        "null"
        
#snake class(object)
class player:
    #
    speed = 30
    direction = 1
    score = 0
    image = pygame.image.load("greensquare.png")
    image2 = pygame.image.load("lightgreensquare.png")
    xpos = 256
    ypos = 256
    xpos_old = xpos
    ypos_old = ypos
    trail_x = [0]
    trail_y = [0]

    
#default values
    def default(self):
        self.speed = 30
        self.direction = 1
        self.score = 0
        self.xpos = 256
        self.ypos = 256
        self.trail_x = [0]
        self.trail_y = [0]
        
    def __init__(self):
        "temp"

    #changes speed if a score is found
    def speedUp(self):
        if self.speed <= 2:
            return
        else:
            self.speed -= 1
        
    #changes direction based on keyboard input
    def changeDirection(self):

        #1-4 clockwise, 1 = up, 2 = right, 3 = down, 4 = left
        if keyboard.is_pressed("up"):
            self.direction = 1
        if keyboard.is_pressed("right"):
            self.direction = 2
        if keyboard.is_pressed("down"):
            self.direction = 3
        if keyboard.is_pressed("left"):
            self.direction = 4

    #checks if running into a wall (or later, self) and restarts game 
    def collision(self):
        if self.xpos > screen.width or self.xpos < 0:
            self.default()
        if self.ypos > screen.height or self.ypos < 0:
            self.default()
            
            #checks if self collides with any position in its trail
        for i in range(0,len(self.trail_x)-1,1):

            if self.xpos == self.trail_x[i] and self.ypos == self.trail_y[i]:
                self.default()

            
    #moves based on direction from changeDirection
    def move(self):
        self.xpos_old = self.xpos
        self.ypos_old = self.ypos
        
        if self.direction == 1:
            self.ypos -= 32
        if self.direction == 2:
            self.xpos += 32
        if self.direction == 3:
            self.ypos += 32
        if self.direction == 4:
            self.xpos -= 32


        self.collision()
        self.trail()
        """
        Bug here, collision asks for a position potentially out of its range because the trail doesn't update first
        need to change how that interactin works? Simply swapping them doesn't help because then the collision updates 
        before the new movement value is applied
        """

    #tracks last n positions where n = score to draw/collide snake chain
    def trail(self):
        
##      for n in range(self.score+1,1,1):
##            
##      self.trail_x[n] = self.trail_x[n-1]
##      self.trail_y[n] = self.trail_x[n-1]
        #fills first spot with
        length = len(self.trail_x)
        
        for n in range(len(self.trail_x)-1,0,-1):
            self.trail_x[n] = self.trail_x[n-1]
            self.trail_y[n] = self.trail_y[n-1]
            
        self.trail_x[0] = self.xpos
        self.trail_y[0] = self.ypos


         
        
    def didScore(self):
    
        self.score += 1
        print(self.score)
        self.speedUp()
        self.trail_x.append(self.xpos_old)
        self.trail_y.append(self.ypos_old)
            
class apple():
    xpos = 0
    ypos = 0
    img = pygame.image.load("apple.png")
    def __init__(self):
        "null"

        #gives random apple position, does not protect against placing in same spot
        # or under player (for the time being)
        
    def get(self):
        #fills old positions
        xpos_old = self.xpos
        ypos_old = self.ypos

        # checks if the position is a duplicate, if not repeats self.get() to get a unique position
        while ypos_old == self.ypos and xpos_old == self.xpos:
            self.xpos = random.randrange(0, 15, 1) * (screen.height / 16)
            self.ypos = random.randrange(0, 15, 1) * (screen.height / 16)



    

def main():
    running = True
    pygame.init()
    clock = pygame.time.Clock()
    snake = player()
    #renaming apple to obj 
    obj = apple()
    
    frame = 1
    movecount = 1
    

    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("Snake Game Test")
    
    screen_width = 512
    screen_height = 512
    background = pygame.image.load("512by32_orange.png")
    screen = pygame.display.set_mode((screen_width,screen_height))

    #Starting Position
    snake.default()

    #Starting Speed (FOR TESTING ONLY, DEFAULT 60)
    snake.speed = 30
    #apple starting position
    obj.get()
    
    
    #loading images
    apple_img = pygame.image.load("apple.png")
    
    #establishing Screen
    screen.fill([0,0,0])
    screen.blit(background,(0 ,0))
    
    screen.blit(snake.image,(snake.xpos,snake.ypos))
    screen.blit(obj.img,(apple.xpos,apple.ypos))
    pygame.display.flip()
    pygame.font.init()






    

    
    while running == True:
        clock.tick(60)
        
        snake.changeDirection()
        #print(frame)
        #print(movecount)
        #print(snake.direction)
        
        
        


        #snake move check
        if movecount == snake.speed:
            snake.move()
            print(snake.direction)
           # print("snake xpos",snake.xpos)
            #print("snake ypos",snake.ypos)
            #print("apple xpos",obj.xpos)
            #print("apple ypos",obj.ypos)
            print("snake trail_x", snake.trail_x)
            print("snake trail_y", snake.trail_y)
            movecount = 1
        elif movecount < snake.speed:
            movecount += 1


        #score condition 
        if abs(snake.xpos - obj.xpos) <= 16 and abs(snake.ypos - obj.ypos) <= 16:
            snake.didScore()
            obj.get()
            print(snake.score)
            print("speed:",snake.speed)
            

        
        #rendering screen
        screen.blit(background,(0,0))
        screen.blit(obj.img,(obj.xpos,obj.ypos))
        screen.blit(snake.image,(snake.xpos,snake.ypos))
        #renders snake trail
        for j in range(1,len(snake.trail_x),1):
            screen.blit(snake.image2,(snake.trail_x[j],snake.trail_y[j]))
        
        #render complete
        pygame.display.flip()
        
        #frame counter for testing game operations, keep this last besides quit 
        if frame == 60:
            frame = 1
        elif frame < 60:
            frame += 1

        #quit command if x is clicked on window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        
if __name__ == "__main__":
    main()
