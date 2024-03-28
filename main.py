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
# Lives in game
LIVES = 3
# Top bar
TOP_BAR_HEIGHT = 50
# Font for the game analytics
LABEL_FONT = pygame.font.SysFont("comicsans", 24)

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
   
# Formats time counter
def format_time(secs):
    milli = math.floor(int(secs * 1000 % 1000) / 100)
    seconds = int(round(secs % 60, 1))
    minutes = int(secs // 60)
    # Allows for two digits in counter
    return f"{minutes:02d}:{seconds:02d}.{milli}"
# Game analytics
def draw_top_bar(win, elapsed_time, targets_pressed, misses):
    pygame.draw.rect(win, "grey", (0,0, WIDTH, TOP_BAR_HEIGHT))
    # Renders font and time
    time_label = LABEL_FONT.render(f"Time: {format_time(elapsed_time)}", 1, "black")
    
    speed = round(targets_pressed / elapsed_time, 1)
    speed_label = LABEL_FONT.render(f"Speed: {speed} t/s", 1, "black")

    hits_label = LABEL_FONT.render(f"Hits: {targets_pressed} ", 1, "black")
    
    lives_label = LABEL_FONT.render(f"Lives: {LIVES - misses} ", 1, "black")

    # Displays label and position
    win.blit(time_label,(5,5))
    win.blit(speed_label,(200,5))
    win.blit(hits_label,(450,5))
    win.blit(lives_label,(650,5))

# main function keeps game playing
def main():
    run = True
    targets = []
    clock = pygame.time.Clock()
# Click variables
    targets_pressed = 0
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
        elapsed_time = time.time() - start_time
        # looks for "event"(quiting game X) during game in order to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              run = False
              break
        #    creates event with specific parameters and esures targets remain on screen
            if event.type == TARGET_EVENT:
               x =  random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
               y = random.randint(TARGET_PADDING + TOP_BAR_HEIGHT, HEIGHT - TARGET_PADDING)
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
               targets_pressed += 1 
# Function ends game if misses greater than lives
        if misses >= LIVES:
            pass    
    #    Calls draw function
        draw(WIN, targets) 
        draw_top_bar(WIN, elapsed_time, targets_pressed, misses )
            # Draws targets onto screen
        pygame.display.update() 
    # Quits game
    pygame.quit()    
           
# Ensure we only run the main function
if __name__ == "__main__":
    main()
