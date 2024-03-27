import math
import random
import time
import pygame
pygame.init()
# Pixels for the screen size
WIDTH, HEIGHT = 600, 400
# Display window screen
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# name of the window
pygame.display.set_caption("Aim Trainer")
# Manipulates the targets in game
class Target:
    MAX_SIZE = 30
    GROWTH_Ratte = 0.2
    Color = "red"
    SECOND_COLOR = "white"
# Constructor for targets
def __init__(self,x,y):
    self.x = x
    self.y = 0
    self.size = 0
    self.grow = True
# Updates targets size (Makes targets grow and shrink)
def update(self):
    if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
        self.grow = False

    if self.grow:
        self.size += self.GROWTH_RATE  
    else:
        self.size -= self.GROWTH_RATE   
        #    Draws cirles to window
def draw(self, win):
    pygame.draw.circle(win,self.COLOR,(self.x,self.y), self.size)
    pygame.draw.circle(win,self.SECOND_COLOR,(self.x,self.y), self.size * 0.8)
    pygame.draw.circle(win,self.COLOR,(self.x,self.y), self.size * 0.6)
    pygame.draw.circle(win,self.SECOND_ COLOR,(self.x,self.y), self.size * .04)


# main function keeps game playing
def main():
    run = True

while run:
        # looks for "event"(quiting game X) during game in order to quit
    for event in pygame.event.get():
           if event.type == pygame.QUIT:
              run = False
              break
           
pygame.quit()
# Ensure we only run the main function
if __name__ == "__main__":
   main()
