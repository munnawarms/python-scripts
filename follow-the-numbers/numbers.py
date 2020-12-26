# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 15:02:40 2020

@author: abdul
"""
from random import randint

WIDTH = 400

HEIGHT = 400

dots = []
lines = []

next_dot = 0

for dot in range(0, 10):
    actor = Actor("dot")
    actor.pos = randint(20, WIDTH -20), \
    randint(20, HEIGHT - 20) 
    dots.append(actor)
    
def draw():
    screen.fill("black")
    number = 1
    for dot in dots:
        screen.draw.text(str(number), \
                          (dot.pos[0],dot.pos[1] + 12))
    
        dot.draw()
        number = number + 1
    for line in lines:
        screen.draw.line(line[0], line[1], (100, 0, 0))
        
def on_mouse_down(pos):
    global next_dot 
    global lines
    if dots[next_dot].collidepoint(pos):
        if next_dot:
            lines.append((dots[next_dot - 1].pos, dots[next_dot].pos))
        next_dot = next_dot + 1
    else:
        lines = []
        next_dot = 0
        
