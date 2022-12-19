
import pygame
import sys
import random
import os

pygame.init()

WIDTH = 800
HEIGHT = 620
FPS = 60
LOSTFPS = 30

start = True
run = False
paused = False
Lost = False

ICON = pygame.image.load(os.path.join("assets","startup.png"))
pygame.display.set_icon(ICON)

CAPTION = pygame.display.set_caption("SPACE INVADERS")

PLAYERIMG = pygame.image.load(os.path.join("assets","space-invaders.png"))
PLAYERIMG = pygame.transform.scale(PLAYERIMG, (64, 64))

redship = pygame.image.load(os.path.join("assets","pixel_ship_red_small.png"))
redship = pygame.transform.scale(redship, (64, 64))
blueship = pygame.image.load(os.path.join("assets","pixel_ship_blue_small.png"))
blueship = pygame.transform.scale(blueship, (64, 64))
greenship = pygame.image.load(os.path.join("assets","pixel_ship_green_small.png"))
greenship = pygame.transform.scale(greenship, (64, 64))

lives = 3
lvl = 0
wave = 0
enemies = []

main_font = pygame.font.SysFont("Auror", 35)

BG1 = pygame.image.load(os.path.join("assets","download.jpeg"))
BG1 = pygame.transform.scale(BG1, (800, 620))
BG2 = pygame.image.load(os.path.join("assets","download (10).jpeg"))
BG2 = pygame.transform.scale(BG2, (800, 620))


CLOCK = pygame.time.Clock()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))


class Ship():
    def __init__(self, x, y, img, health=100):
        self.x = x
        self.y = y
        self.img = img
        self.health = health

    def draw(self):
        WIN.blit(self.img, (self.x, self.y))


class Player(Ship):
    def __init__(self, x, y, img, health=100):
        super().__init__(x, y, img, health)
        self.x = x
        self.y = y
        self.health = health
        self.img = img

    def move(self):
        self.xchange = 0
        self.ychange = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.xchange = -4
        if keys[pygame.K_d]:
            self.xchange = 4
        if keys[pygame.K_w]:
            self.ychange = -4
        if keys[pygame.K_s]:
            self.ychange = 4

        self.x += self.xchange
        self.y += self.ychange

        if self.x < 0:
            self.x = 10
        if self.x > 750:
            self.x = 750
        if self.y < 0:
            self.y = 10
        if self.y > 580:
            self.y = 570


class Alien(Ship):
    color_map = {
        "red": redship,
        "blue": blueship,
        "green": greenship
    }

    def __init__(self, x, y, img, health):
        super().__init__(x, y, img, health)
        self.x = x
        self.y = y
        self.health = health
        self.img = self.color_map[img]

    def move(self):
        self.y += 1


class Background():
    def __init__(self, img, width, heigth):
        self.height = heigth
        self.width = width
        self.img = img

    def draw_Bg(self):
        WIN.blit(self.img, (0, 0))


def upd():
    pygame.display.update()


def upd_lable():
    lives_lable = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
    wave_lable = main_font.render(f"Wave: {wave}", 1, (255, 255, 255))
    levels_lable = main_font.render(f"Level: {lvl}", 1, (255, 255, 255))
    WIN.blit(lives_lable, (20, 20))
    WIN.blit(levels_lable, (700, 20))


def gen_enemies():
    global BG
    if len(enemies) == 0:
        global lvl
        global wave
        global lives
        lvl = lvl + 1

        wave = wave + 5
        lives = lives + 2
        for i in range(wave):
            enemy = Alien(random.randrange(30, 750), random.randrange(-1500, -100),
                          random.choice(["red", "blue", "green"]), random.randrange(50, 101))
            enemies.append(enemy)
        BG = random.choice([BG1, BG2])


def draw_alien():

    for enemy in enemies:
        enemy.draw()


def move_alien():
    for enemy in enemies:
        enemy.move()


def alien_remove():
    for enemy in enemies:
        if enemy.y > 700:
            enemies.remove(enemy)


def pause_quit():
    global run
    global lives
    global lvl
    global wave
    global enemies
    global paused
    keys = pygame.key.get_pressed()
    if keys[pygame.K_l]:
        run = False
        lives = 3
        lvl = 0
        wave = 0
        enemies = []
        PLAYER.x, PLAYER.y = WIDTH//2, HEIGHT-100

    if keys[pygame.K_p]:
        run = False
        paused = True


def game_over():
    global Lost
    global run
    global lives
    global lvl
    global wave
    global enemies
    global paused
    if lives == 0:
        Lost = True
        run = False
        lives = 3
        lvl = 0
        wave = 0
        enemies = []
        PLAYER.x, PLAYER.y = WIDTH//2, HEIGHT-100


def collide_check():
    global lives
    PLAYERMASK = pygame.mask.from_surface(PLAYERIMG)
    for enemy in enemies:
        enemy_mask = pygame.mask.from_surface(enemy.img)
        offset = (int(PLAYER.x - enemy.x), int(PLAYER.y - enemy.y))
        collousion = PLAYERMASK.overlap(enemy_mask, offset)
        if collousion:
            lives = lives - 1
            enemies.remove(enemy)


PLAYER = Player(WIDTH//2, HEIGHT-100, PLAYERIMG)

BACKGROUND = Background([BG1, BG2], 800, 620)


def main():

    global run

    CLOCK.tick(FPS)

    while run:

        CLOCK.tick(FPS)

        gen_enemies()

        WIN.blit(BG, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        upd_lable()

        PLAYER.move()

        PLAYER.draw()

        draw_alien()

        move_alien()

        alien_remove()

        collide_check()

        pause_quit()

        game_over()

        upd()


def main_menu():
    global start
    global run
    global paused
    global Lost
    
    while start:
        if paused == False:
            STARTGAMELABLE = main_font.render(
                "Click to start", 1, (255, 255, 255))
        if paused == True:
            STARTGAMELABLE = main_font.render(
                "Game paused click to resume", 1, (255, 255, 255))
        if Lost == True:
            STARTGAMELABLE = main_font.render(
                "Game OVER click to play again", 1, (255, 255, 255))

        WIN.fill((0, 0, 0))
        WIN.blit(STARTGAMELABLE, (WIDTH//2 - STARTGAMELABLE.get_width() //
                 2, HEIGHT//2 - STARTGAMELABLE.get_height()//2))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = True
                paused = False
                Lost = False
                main()
        upd()
    pygame.quit()


if __name__ == "__main__":

    main_menu()
