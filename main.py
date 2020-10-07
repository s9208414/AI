#Pacman Ghost Algorithm - www.101computing.net/pacman-ghost-algorithm/
from math import atan, cos, sin ,asin ,acos
from processing import *
#import turtle
#screen = turtle.Screen()
#set the screen background
#screen.bgpic("down.jpg")

WIDTH=480
HEIGHT=420
pacman_X = 30
pacman_Y = 30
delay = 1

ghost_X = 10
ghost_Y = 10

def setup():
    strokeWeight(3)
    frameRate(20)
    size(WIDTH,HEIGHT)
    

def moveGhost():    
  global ghost_X,ghost_Y,pacman_X,pacman_Y
  fill(255,255,255)
  stroke(0,0,0)
  
  #Find out the direction (angle) the Ghost needs to move towards
  #Using SOH-CAH-TOA trignometic rations
  opposite=pacman_Y-ghost_Y
  adjacent=pacman_X-ghost_X
  angle = atan(opposite/adjacent)

  
  #Use this angle to calculate the velocity vector of the Ghost
  #Once again using SOH-CAH-TOA trignometic rations
  velocity=3 #pixels per frame
  
  vx = velocity * cos(angle)
  vy = velocity * sin(angle)
  
  #Apply velocity vector to the Ghost coordinates to move/translate the ghost
  ghost_X = ghost_X + vx/delay*2
  ghost_Y = ghost_Y + vy/delay*2
  
  #Draw Ghost  
  ellipse( ghost_X,ghost_Y,50,50)
    
def movePacman():
    global pacman_X, pacman_Y

    fill(0,255,255)
    stroke(0,0,0)
    fc = environment.frameCount

    #Pacman follows the mouse cursor
    pacman_X += (mouse.x-pacman_X)/delay*0.1;
    pacman_Y += (mouse.y-pacman_Y)/delay*0.1;
    
    #Draw Pacman
    ellipse(pacman_X,pacman_Y,30,30)

def playGame():
  background(50,50,150)
  movePacman()
  moveGhost()

draw = playGame
run()
