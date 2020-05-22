import pygame       #pygame for everything
from pygame import mixer        #Mixer for music

import random       #for random movements of alians

import math       #for calculating the distance 

# Initialize the pygame
pygame.init()      #Important

# create the window
(width, height) = (800, 600)
screen = pygame.display.set_mode((width,height))     #window for game width x height

#Backgroung 
background = pygame.image.load('background.png')     #to make the background of game 

#Background Sound
mixer.music.load('background.wav')     #for playing the background music
mixer.music.play(-1)      #to make the background music repeate 


# Title and Icon
pygame.display.set_caption("Space Invader")     #to display the game name @ caption
icon = pygame.image.load('spaceship.jpg')       #to store the game logo, the image
pygame.display.set_icon(icon)    #to display the game logo loaded above

#player
playerImg = pygame.image.load('spacehero.png')    #player image
playerX = 368    #player position on x axis
playerY = 480    #player position on y axis
playerX_change = 0    #to move the player in x direction @ player speed in x direction
playerY_change = 0    #to move the player in y direction @ player speed in y direction

#Enemy
'''
all these lists for creating multiple enemies

'''

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemy = 6

for i in range(num_of_enemy):    #for storing all the enemy data on different lists
    
    enemyImg.append(pygame.image.load('enemy.png'))   #load enemy image
    enemyX.append(random.randint(0,735))     #to determine the random x position for enemy
    enemyY.append(random.randint(30,150))    #to determine the random y position for enemy
    enemyX_change.append(5)     #to determine the movement of the enemies in x direction @ speed in x direction
    enemyY_change.append(40)    #to determine the movement of the enemies in y direction @ speed in y direction


#Bullet
# Ready - You cant see the bullet on the screen @ you can fire it 
# Fire - The bullet is currently moving @ you can't fire it
bulletImg = pygame.image.load('bullet32.png')   #load the bullet image 
bulletX = 0
bulletY = 480
bulletX_change = 0     #to determine the fired position of bullet in x direction @ before it is fired
bulletY_change = 10     #to determine the movement of bullet in y direction @ speed of bullet in y direction @ after it is fired
bullet_state = "ready"    #first storing the bullet state in ready position @ you cant see the bullet on the screen @ you can fire it 

#Score
score_value = 0  #initially storing the score of player as 0 which increments as enemy gets killed
font = pygame.font.Font('freesansbold.ttf', 32)   #storing the font style and font size as font for rendering the score of player later


# Game over text
over_font = pygame.font.Font('freesansbold.ttf', 96)     #storing the font style and font size as over_font for rendering the game over text after the player gets killed

def game_over_text():     #game_over_text for displaying the game is over after the player gets killed 
    over_text = over_font.render("GAME OVER", True, (255,255,255))    #storing the rendered game over text in over_text for displaying 
    screen.blit(over_text, (100, 200))   #it draws/prints/displays the over_text on screen after the player gets distroyed at position (100, 200)
    
    

def show_current_score():   #function for displaying the current score of the player
    score = font.render("Score: " + str(score_value), True, (255,255,255))   #storing the rendered score text in score for displaying 
    screen.blit(score, (10, 10))     #it draws/prints/displays the score on screen after the player gets each point at position (10, 20)

def player(x, y):   #function for displaying the player in its current position
    #blit = draw
    screen.blit(playerImg,(x, y))   #it draws/prints/displays the player at position (x, y) 
    
def enemy(x, y, i):    #function for displaying the enemy [i] in its current position
    screen.blit(enemyImg[i], (x, y))     #it draws/prints/displays the enemy[i] at position (x, y) 

def fire_bullet(x,y):    #function for displaying the bullet in its current position and maintaining its state
    global bullet_state    #import the global variable bullet_state
    bullet_state = "fire"   #changes the state of bullet from ready to fire for preventing the bullet from firing again
    screen.blit(bulletImg,(x+16, y+10))    #it draws/prints/displays the bullet at its corrent position and changes on its y position causes it to move up
    
def isCollision(enemyX, enemyY, bulletX, bulletY):    #this function is to detect whether the bullet has hit the alien or not 
    distance = math.sqrt((math.pow(enemyX-bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))    #calculate the distance between the bullet and each alien at different instance 
    if distance < 40:    #when the distance between the bullet and any alien is less than 40 than it is considered as hit 
        return True    #returns true when it is less than 40
    else:
        return False     #returns false when it is more than 40
    
def isGameOver(enemyX, enemyY, playerX, playerY):
    over_distance = 0
    over_distance = math.sqrt((math.pow(enemyX-playerX, 2)) + (math.pow(enemyY - playerY, 2)))    #calculate the distance between the player and each alien at different instance to check for collision
    if over_distance < 40:     #when the distance between the player and any alien is less than 40 than it is considered as hit 
        return True      ##returns true when it is less than 40
    else:
        return False     #returns false when it is more than 40
    

    
# Game Loop
#The python game main part must be written inside the whiler loop 


running = True
while running:    #Loop Starts
    
    # RGB = RED GREEN BLUE
    screen.fill((0, 0, 0))   #this is for changing the background colour of the screen of the game window
    
    #background image
    screen.blit(background,(0,0))   #it need to be written so the the background image continuous to be drawn 
    
    for event in pygame.event.get():   #this loop is for the quit event in pygame, whenever we press the cross the window and game closes
        if event.type == pygame.QUIT:
            running = False
        
        # if key stroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:    #checking if key is pressed 
            
            
            if event.key == pygame.K_LEFT:   #chicking if its left arrow key
                playerX_change = -5     #if pressed making playerX_change to -6 so that it goes to left direction
            
            if event.key == pygame.K_RIGHT:    #chicking if its right arrow key
                playerX_change = 5     #if pressed making playerX_change to 6 so that it goes to right direction
                
            if event.key == pygame.K_UP:     #checking if its up arrow
                playerY_change = -5
                
            if event.key == pygame.K_DOWN:    #checking if its down arrow
                playerY_change = +5
                        
            
            if event.key == pygame.K_SPACE:    #chicking if its space arrow key
                                
                
                if bullet_state == "ready":     #if pressed chicking the state of bullet so that multiple bullet doesnot get fire at a time
                    
                    #Get the current X cooridinate of spaceship
                    bulletX = playerX    #setting playerX positio in bullet X so that position of bullet does not chance as the ship moves in x direction
                    fire_bullet(bulletX,bulletY)   #firing the bullet
                    bullet_sound = mixer.Sound("laser.wav")    #storing the sound file in bullet.sound
                    bullet_sound.play()   #playing the sound when the bullet is fired
                
        
        # removal of key stroke
        if event.type == pygame.KEYUP:    #checking if the key stroke is removed to stop the ship moving in x direction
            
            
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:   #checking if the removed key is left or right key or some other key because you dont wanna stop the ship if some other key is removed
                playerX_change = 0
                
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:     #checking if the removed key is up or down key or some other key because you dont wanna stop the ship if some other key is removed
                playerY_change = 0
                            
                
    #after screen.fill
    # checking for boundaries of spaceship so it doesnt go out of bounds
    playerX += playerX_change
    playerY += playerY_change
    
    '''
    #for limiting the movement of spaceship
    '''
    
    if playerX <= 0:     #0 pixels in left direction
        playerX = 0
    elif playerX >= 736:    #736 pixels in righ direction
        playerX = 736
        
    if playerY >= 536:    #0 pixels in downside
        playerY = 536
    elif playerY <= 0:    #0 pixels in upside 
        playerY = 0
        
    #Enemy Movement
    for i in range(num_of_enemy):     #need to use for loop because you have more than one enemy
        
        '''
        GAME OVER
        '''
        
        if isGameOver(enemyX[i], enemyY[i], playerX, playerY):    #the game gets over when the distance between player and enemy is less than 40 pixels                     
            for j in range(num_of_enemy):    #again need to use for loop for multiple enemies
                enemyY[j] = 2000     #changing the y coordinate of every enemies to 2000 so that all of them go below the screen of game and no longer are seen, hence the score if player remains constant because it cannot hit any targets
            game_over_text()     #when the y coorfinate of any enemy gets below 440 pixels means the game is over, hence displaying the game over text
            break     #breaks of the current for loop 
        
        
        #code for enemy movement starts
        enemyX[i] += enemyX_change[i]    #changing/continuing the movement of each enemy in different X position
        
        if enemyX[i] <= 0:     #keeping the enemies in bounds
            enemyX_change[i] = 5    #when if x coordinate of any enemy is less than 0, setting enemyX_change to 6 so that it starts moving in right direction
            enemyY [i] += enemyY_change[i]   #updating the moviment parameter of enemies
            
        elif enemyX[i] >= 736:      #keeping the enemies in bounds
            enemyX_change[i] = -5     #when if x coordinate of any enemy is less than 736, setting enemyX_change to -6 so that it starts moving in left direction
            enemyY[i] += enemyY_change[i]     #updating the moviment parameter of enemies
            
        #Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)     #chacking whether the bullet has hit the enemy and storing the result as a boolean in collision
        if collision:   #id collision has occured
            bullet_sound = mixer.Sound("explosion.wav")    #storing the explosion sound in bullet_sound
            bullet_sound.play()    #olaying the explosion sound
            bulletY = 480    #resetting the t value of bullet to the y coordinate of the spaceship so that it is ready to fire the bullet again
            bullet_state = "ready"    #setting the bullet state to ready from "fire"
            score_value += 1    #as the bullet has hit a target, increasing the score of player
            
            enemyX[i] = random.randint(0,735)     #regenerstoring the random X coordinate of enemy after getting killed
            
        enemy(enemyX[i], enemyY[i], i)    #regenerating the killed enemy in different random position 
        
    #bullet Movement
    if bulletY <= 0:     #this is for making the bullet ready to fire again of it missed the target
        bulletY = playerY   #setting he bullet y position to 480 
        bullet_state = "ready"    #and making it ready to fire again
        
    if bullet_state == "fire":    #this is for maintaining the movement if bullet after it has been fired so that it continuous to move in its straight path
        fire_bullet(bulletX,bulletY)   #calling the fire bullet to fire maintaining it 
        bulletY -= bulletY_change    #maintaining the bullet in its straight path and move it in upward position
    
        
    if enemyY[i] >= 2000:     #for displaying the Game Over text even after the above loop breaks and the game ends
        game_over_text()      #this is what gets the text printed
        
    
    
    
    player(playerX,playerY)    #for drawing the player in its desired position on the screen
    
    show_current_score()     #for displaying the current score of the player
    
    
    pygame.display.update()    #This is very very important, it always need to be written so that the screen gets updated after each iteration of the loop
        


pygame.quit()    #this is for quitting the pygame window and always needs to be written so that the system doesnot get hang and python starts not responding

'''

NOW THIS IS HOW YOY MAKE SPACE INVADER GAME :)

'''

           