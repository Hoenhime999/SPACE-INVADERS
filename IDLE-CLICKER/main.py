
from audioop import mul
import pygame
import os

pygame.init()
WIDTH = 800
HEIGHT = 600
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)


money = 0
has_factory = False
factory_income = 1
click_income = 10
multiplier = 1
factory_num = 0

multiplierdict = {
    "1x": True,
    "2x": False,
    "3x": False,
    "4x": False,
    "5x": False,
    "6x": False,
    "7x": False,
    "8x": False,
    "9x": False,
    "10x": False,
    "11x": False,
    "12x": False,
    "13x": False,
    "14x": False,
    "15x": False,
    "16x": False,
    "17x": False,
    "18x": False,
    "19x": False,
    "20x": False,


}


pygame.display.set_caption("IDLE CLICKER")

ICON = pygame.image.load(os.path.join("assets", "wait.png"))
pygame.display.set_icon(ICON)

MINERIMG = pygame.image.load(os.path.join("assets", "oil-pump.png"))

MULTIPLIERIMG = pygame.image.load(os.path.join("assets", "multiplier.png"))

FACTORYIMG = pygame.image.load(os.path.join("assets", "FACTORY ICON.png"))

BG = pygame.image.load(os.path.join("assets", "BG.png"))

BG = pygame.transform.scale(BG, (int(WIN.get_width()), int(WIN.get_height())))


class Miner(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        super().__init__()

        self.x = x
        self.y = y
        self.img = img
        self.w = 200
        self.h = 200
        self.img = pygame.transform.scale(self.img, (200, 200))
        self.rect = self.img.get_rect()

    def draw(self):
        WIN.blit(self.img, (self.x, self.y))

    def redraw(self, neww, newh):
        self.w = neww
        self.h = newh
        self.img = pygame.transform.scale(self.img, (self.w, self.h))

    def original_Size(self):
        self.w = 200
        self.h = 200
        self.img = pygame.transform.scale(self.img, (self.w, self.h))


class Button():
    def __init__(self, img, x, y, w, h):
        self.img = img
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self):
        WIN.blit(self.img, (self.x, self.y))


MINER = Miner(WIN.get_width()//2 - MINERIMG.get_width()/2,
              WIN.get_height()//2 - MINERIMG.get_height()//2, MINERIMG)

FACTORY = Button(FACTORYIMG, 30,
                 WIN.get_height() - WIN.get_height() * 0.1 * 0.9, 64, 64)

MULTIPLIER = Button(MULTIPLIERIMG, 60 + FACTORY.w,
                    WIN.get_height() - WIN.get_height() * 0.1 * 0.9, 64, 64)


def collide(a_x, a_y, a_width, a_height, b_x, b_y, b_width, b_height):
    return (a_x + a_width > b_x) and (a_y + a_height > b_y) and (b_x + b_width > a_x) and (b_y + b_height > a_y)


def draw_button_area():
    global button_area
    button_area = pygame.Rect(0, WIN.get_height() *
                              0.9, WIN.get_width(), WIN.get_height() * 0.1)
    pygame.draw.rect(WIN, (255, 255, 255), button_area)


def draw_stats_area():
    global stats_area
    stats_area = pygame.Rect(WIN.get_width() * 0.8, 0,
                             WIN.get_width() * 0.2, WIN.get_height())
    pygame.draw.rect(WIN, (255, 255, 255), stats_area)


def Factory_func():
    global money
    global has_factory
    global factory_income

    if has_factory:
        money += (multiplier * factory_income * factory_num)/60

         


def miner_click():
    global money
    global multiplier
    global click_income

    money += click_income * multiplier
    


def multiplier_func():
    global money
    global multiplier

    if money >= 10000 and multiplierdict["2x"] != True:
        multiplierdict["2x"] = True
        multiplier = 2
        money -=10000

    if money >= 20000 and multiplierdict["3x"] != True:
        multiplierdict["3x"] = True
        multiplier = 3
        money -=20000

    if money >= 30000 and multiplierdict["4x"] != True:
        multiplierdict["4x"] = True
        multiplier = 4
        money -=30000

    if money >= 40000 and multiplierdict["5x"] != True:
        multiplierdict["5x"] = True
        multiplier = 5
        money -=40000

    if money >= 50000 and multiplierdict["6x"] != True:
        multiplierdict["6x"] = True
        multiplier = 6
        money -=50000

    if money >= 60000 and multiplierdict["7x"] != True:
        multiplierdict["7x"] = True
        multiplier = 7
        money -=60000

    if money >= 70000 and multiplierdict["8x"] != True:
        multiplierdict["8x"] = True
        multiplier = 8
        money -=70000

    if money >= 80000 and multiplierdict["9x"] != True:
        multiplierdict["9x"] = True
        multiplier = 9
        money -=80000

    if money >= 90000 and multiplierdict["10x"] != True:
        multiplierdict["10x"] = True
        multiplier = 10
        money -=90000

    if money >= 100000 and multiplierdict["11x"] != True:
        multiplierdict["11x"] = True
        multiplier = 11
        money -=100000

    if money >= 1100000 and multiplierdict["12x"] != True:
        multiplierdict["12x"] = True
        multiplier = 12
        money -=1100000

    if money >= 1200000 and multiplierdict["13x"] != True:
        multiplierdict["13x"] = True
        multiplier = 13
        money -=1200000

    if money >= 1300000 and multiplierdict["14x"] != True:
        multiplierdict["14x"] = True
        multiplier = 14
        money -=1300000

    if money >= 1400000 and multiplierdict["15x"] != True:
        multiplierdict["15x"] = True
        multiplier = 15
        money -=1400000

    if money >= 1500000 and multiplierdict["16x"] != True:
        multiplierdict["16x"] = True
        multiplier = 16
        money -=1500000

    if money >= 1600000 and multiplierdict["17x"] != True:
        multiplierdict["17x"] = True
        multiplier = 17
        money -=1600000

    if money >= 1700000 and multiplierdict["18x"] != True:
        multiplierdict["18x"] = True
        multiplier = 18
        money -=1700000

    if money >= 1800000 and multiplierdict["19x"] != True:
        multiplierdict["19x"] = True
        multiplier = 19
        money -=1800000

    if money >= 1900000 and multiplierdict["20x"] != True:
        multiplierdict["20x"] = True
        multiplier = 20
        money -=1900000


def lable():
    money_lable = MAIN_FONT.render(f"Money: {int(money)}", 1, (0, 0, 0))
    multiplier_lable = MAIN_FONT.render(
        f"Multiplier: {multiplier}", 1, (0, 0, 0))
    factory_income_lable = MAIN_FONT.render(
        f"Num of Factorys: {factory_num}", 1, (0, 0, 0))
    click_income_lable = MAIN_FONT.render(
        f"Click Income: {click_income * multiplier}/click", 1, (0, 0, 0))

    WIN.blit(money_lable, (WIN.get_width() - stats_area.width * 0.9, 10))
    WIN.blit(multiplier_lable, (WIN.get_width() -
             stats_area.width * 0.9, money_lable.get_height()+10))
    WIN.blit(factory_income_lable, (WIN.get_width() - stats_area.width *
             0.9, multiplier_lable.get_height() + money_lable.get_height()+10))
    WIN.blit(click_income_lable, (WIN.get_width() - stats_area.width * 0.9,
             factory_income_lable.get_height() + multiplier_lable.get_height() + money_lable.get_height()+10))


def main():
    global MAIN_FONT
    global BG
    global fps_clock
    global money
    global has_factory
    global factory_income
    global factory_num

    run = True
    fps_clock = pygame.time.Clock()

    while run:
        MAIN_FONT = pygame.font.SysFont(
            "monospace", int(WIN.get_width() * 0.015))

        MINER = Miner(20, WIN.get_height()//2 -
                      MINERIMG.get_height()//4, MINERIMG)

        BG = pygame.transform.scale(
            BG, (int(WIN.get_width()), int(WIN.get_height())))

        FACTORY = Button(FACTORYIMG, 30,
                         WIN.get_height() - WIN.get_height() * 0.1 * 0.9, 64, 64)

        MULTIPLIER = Button(MULTIPLIERIMG, 60 + FACTORY.w,
                    WIN.get_height() - WIN.get_height() * 0.1 * 0.9, 64, 64)

        WIN.blit(BG, (0, 0))

        fps_clock.tick(FPS)

        MINER.draw()

        

        draw_button_area()

        draw_stats_area()

        FACTORY.draw()

        MULTIPLIER.draw()

        pos=pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                run=False

            if event.type == pygame.MOUSEBUTTONDOWN:

                if collide(MINER.x, MINER.y, MINER.w, MINER.h, pos[0], pos[1], 0, 0):

                    MINER.redraw(0.98 * 200, 0.98 * 200)
                    miner_click()
                    MINER.draw()

                if collide(FACTORY.x, FACTORY.y, FACTORY.w, FACTORY.h, pos[0], pos[1], 0, 0):
                    if money >= 5000 and has_factory != True:
                        has_factory=True
                        money -= 5000
                        factory_num += 1
                    if money >= 5000 and has_factory == True:

                        money -= 5000
                        factory_num += 1

                if collide(MULTIPLIER.x, MULTIPLIER.y, MULTIPLIER.w, MULTIPLIER.h, pos[0], pos[1], 0, 0):
                    multiplier_func()

            if event.type == pygame.MOUSEBUTTONUP:

                MINER.original_Size()

        Factory_func()

        lable()
        pygame.display.update()

    pygame.quit()


main()
