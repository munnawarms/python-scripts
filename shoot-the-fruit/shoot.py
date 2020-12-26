from random import randint
apple = Actor("apple")

def draw():
    screen.clear()
    apple.draw()

def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)

def on_mouse_down(pos):
    
     
    score = 0
    if apple.collidepoint(pos):
        
        score = + 1
        print("Good shot!")
        print(score)
        place_apple()
    else:
       print("You missed!")
       quit()

place_apple()       
            
