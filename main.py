import math
import random
import time
import pygame
pygame.init()
# Current problem (Make Targets appear)
# Pixels for the screen size
WIDTH, HEIGHT = 600, 400
# Display window screen
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# name of the window
pygame.display.set_caption("Aim Trainer")

# Time for tagets to appear
TARGET_INCREMENT = 400
TARGET_EVENT = pygame.USEREVENT
TARGET_PADDING = 30 
# RGB color
BG_COLOR = (0, 25, 40)

# Manipulates the targets in game
class Target:
    MAX_SIZE = 30
    GROWTH_RATE = 0.2
    COLOR = "red"
    SECOND_COLOR = "white"

# Constructor for targets
    def __init__(self, x, y):
        self.x = x
        self.y = y
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
        #    Draws cirles to window and makes them dynamic
    def draw(self, win):
        pygame.draw.circle(win,self.COLOR,(self.x,self.y), self.size)
        pygame.draw.circle(win,self.SECOND_COLOR,(self.x,self.y), self.size * 0.8)
        pygame.draw.circle(win,self.COLOR,(self.x,self.y), self.size * 0.6)
        pygame.draw.circle(win,self.SECOND_COLOR,(self.x,self.y), self.size * .04)
# Collision for targets
    def collide(self, x, y):
        dis = math.sqrt((x - self.x)**2 + (y - self.y)**2)
        return dis <= self.size
# clears screen and then add new targets onto screen
def draw(win, targets):
    win.fill(BG_COLOR)
# Loops in all targets
    for target in targets:
        target.draw(win)
# Draws targets onto screen
    pygame.display.update()    


# main function keeps game playing
def main():
    run = True
    targets = []
    clock = pygame.time.Clock()
# Click variables
    target_pressed = 0
    clicks = 0
    misses = 0
    start_time = time.time()


# Triggers target event 
    pygame.time.set_timer(TARGET_EVENT, TARGET_INCREMENT)

    while run:
        # runs while loop at 60 fps
        clock.tick(60)
        click = False
        mouse_pos = pygame.mouse.get_pos()
        # looks for "event"(quiting game X) during game in order to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              run = False
              break
        #    creates event with specific parameters and esures targets remain on screen
            if event.type == TARGET_EVENT:
               x =  random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
               y = random.randint(TARGET_PADDING, HEIGHT - TARGET_PADDING)
               target = Target(x, y)
               #    pushes target obj into list
               targets.append(target) 
        # Enables clicks
            if event.type ==  pygame.MOUSEBUTTONDOWN:
                click = True
                clicks += 1  
    #    Updates targets before we draw them
        for target in targets:
            target.update()
                # Removes target size when reaches 0
            if target.size <= 0:
                targets.remove(target)
                misses += 1
            # Click collision on targets
            if click and target.collide(*mouse_pos):
               targets.remove(target)
               target_pressed += 1 
    #    Calls draw function
        draw(WIN, targets)   
    # Quits game
    pygame.quit()    
           
# Ensure we only run the main function
if __name__ == "__main__":
    main()
