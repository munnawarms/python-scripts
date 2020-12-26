# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 15:48:44 2020

@author: abdul
"""
from random import randint

DEVELOPERMODE = True

WIDTH = 800

HEIGHT = 600


score = 0

game_over = False


fox = Actor("fox")
fox.pos = 100, 100


coin = Actor("coin")
coin.pos = 200, 200

def draw():
    
    
    screen.fill("royalblue")
    fox.draw()
    coin.draw()
    
    screen.draw.text("Score: " + str(score), color="black" , topleft=(10, 10))
    screen.draw.text("Dudeslayer Creations", color="black", topleft=(10,30))
    
    
    if game_over:
        
        screen .fill ("firebrick")
        
        screen.draw.text("Times Up! :( ", topleft=(10,60), fontsize=60)
        
        screen.draw.text("Final Score: " + str(score), color="black", topleft=(10,10), fontsize=60)
        
        screen.draw.text("R.I.P You died!", topleft=(10,1))
		
        
    
def place_coin():
    coin.x = randint (20, (WIDTH - 20))
    coin.y = randint (20, (HEIGHT - 20))
   
def time_up():
	global game_over
	game_over = True
	place_coin()


    
def update():
    global score
    
    speed = 10
    
    if keyboard.left:
        fox.x = fox.x - speed
        fox.image = "fox"
        
    if keyboard.right:
        fox.x = fox.x + speed
        fox.image = "fox"
        
    if keyboard.up:
        fox.y = fox.y - speed

    if keyboard.down:
        fox.y = fox.y + speed
 
    coin_collected = fox.colliderect(coin)
    
    if coin_collected:
        score = score + 10
        place_coin()
        sounds.piccoin.play()
        
        speed = speed - .2
  

clock.schedule(time_up, 15.0)
place_coin()    

# if _main_ =='_main_':
#     main()

