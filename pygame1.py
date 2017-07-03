import pygame      
from random import randint
import math

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

class Characters(object):
    def __init__(self, charImage, positionX, positionY, screen, width, height):
        self.width = width
        self.height = height
        self.charImage = charImage
        self.hero_x = positionX
        self.hero_y = positionY
        self.monster_x = randint(50, 440)
        self.monster_y = randint(50, 440)
        self.screen = screen
    
    def Hero(self):

        if self.hero_x > self.width - 30:
            self.hero_x = self.width - 30
        if self.hero_x < 0:
            self.hero_x = 0
        if self.hero_y > self.height - 35:
            self.hero_y = self.height - 35
        if self.hero_y < 0:
            self.hero_y = 0

    def HeroUpdate(self, screen):

        pos = self.charImage.get_rect().move(self.hero_x, self.hero_y)
        screen.blit(self.charImage, pos,)

    def updateMonster(self, direction, change_dir_countdown):
        self.change_dir_countdown = change_dir_countdown
        self.direction = direction
        if self.change_dir_countdown == 0:
            self.change_dir_countdown = 120
            self.direction = randint(0,3)
        
        if self.direction == 0:
            self.monster_y-=1
        if self.direction == 1:
            self.monster_x+=1
        if self.direction == 2:
            self.monster_y+=1
        if self.direction == 3:
            self.monster_x-=1
        
        self.screen.blit(self.charImage, (self.monster_x, self.monster_y))

        if self.monster_x > self.width - 30:
            self.monster_x = 30
        if self.monster_x < 0:
            self.monster_x = self.width -30
        if self.monster_y > self.height - 30:
            self.monster_y = 30
        if self.monster_y < 0:
            self.monster_y = self.height - 30
        #countdown to monster direction change
        self.change_dir_countdown-=1

        return self.change_dir_countdown, self.direction

def main():
    # set game size
    width = 510
    height = 480
    
    # initialize pygame framework
    pygame.init()
    pygame.font.init()

    # screen and window caption
    screen = pygame.display.set_mode((width, height))
    
    # images
    background = pygame.image.load('background.png')
    backgroundRect = background.get_rect()
    screen.blit(background, backgroundRect)
    monster_image = pygame.image.load('monster.png')
    hero_image = pygame.image.load('heroimage.png')
    # screen.blit(hero_image,(100, 100))
    pygame.display.set_caption('Rogue Monsters')

    # clock
    clock = pygame.time.Clock()

    # GAME INITIALIZATION
    change_dir_countdown = 0
    direction = 0
    lost = False
    level = 1

    myHero = Characters(hero_image, 255, 140, screen, width, height)    
    myMonster = Characters(monster_image, 240, 100, screen, width, height)
    # myHero.Hero()
    stop_game = False
    
    def won_game(won, level):
        if won == True:
            level+=1
            return level
    def scoreChange(level):
        f2 = open('highscore.txt', 'r')
        v = f2.read()
        f2.close()
        v = v.split(' ')
        oldScore = int(v[0])
        if level > oldScore:
            f = open('highscore.txt', 'r')
            lines = f.readlines()
            f.close()
            f = open("highscore.txt", "w")
            lines = str(level)
            f.write(lines)
            f.close()
            oldScore = level

    # while not stop_game:  

    #     f2 = open('highscore.txt', 'r')
    #     v = f2.read()
    #     f2.close()
    #     v = v.split()
    #     oldScore = int(v[0])

        catch = math.sqrt((myHero.hero_x - myMonster.monster_x)**2 + (myHero.hero_y - myMonster.monster_y)**2)
        screen.blit(background, backgroundRect)
        myHero.Hero()
        myHero.HeroUpdate(screen)
        myMonster.updateMonster(change_dir_countdown, direction)
        
        if catch >= 25:

            for event in pygame.event.get():
            
            # Event handling
                if event.type == pygame.KEYDOWN:
                    if event.key == KEY_DOWN:
                        myHero.hero_y += 20
                    elif event.key == KEY_UP:
                        myHero.hero_y -= 20
                    elif event.key == KEY_LEFT:
                        myHero.hero_x -= 20
                    elif event.key == KEY_RIGHT:
                        myHero.hero_x += 20
            
                if event.type == pygame.QUIT:
                
                    stop_game = True

        if catch >= 25:
            # screen.blit(background_image, (0, 0))
            # screen.blit(textsurfaceLevel,(0,0))
            # screen.blit(textsurfaceLevel,(0,20))
            lvl = pygame.font.SysFont("Comic Sans MS", 30)
            high = pygame.font.SysFont("Comic Sans MS", 30)
            change_dir_countdown, direction = myMonster.updateMonster(change_dir_countdown, direction)
            myHero.Hero()
            myHero.HeroUpdate(screen)
        
        for i in range(len(updateMonster)):
            #detect if hero collides with goblin and set lost to True
            lose = math.sqrt((myHero.Hero_x - updateMonster[i].monster_x)**2 + (myHero.Hero_y - updateMonster[i].monster_y)**2)
            if lose < 25:
                lost = True
        
        # if lost == True:

        #     lvl = pygame.font.SysFont("Comic Sans MS", 30)
        #     textsurface = lvl.render("Level: %d" % (level), False, (255, 255, 255))
        #     screen.blit(textsurface,(0,0))
        #     high = pygame.font.SysFont("Comic Sans MS", 30)
        #     textsurfaceLevel = high.render("Highscore: %d" % (oldScore), True, (255, 255, 255))
        #     screen.blit(textsurfaceLevel,(0,20))
            
            
            
            # Game logic

#         # Draw background                       

#         # Game display

        pygame.display.update()
        
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
