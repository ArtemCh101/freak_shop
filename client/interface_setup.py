import pygame
import sys
from random import *
from time import *
from pygame.locals import *
from math import *

BackgroundColor = (178, 102, 255)
RegistrationBackgroundColor = (255, 188, 0)
RegistrationButtonColor = (178, 102, 255)
MessageBackgroundColor = (51, 153, 255)
ScreenWidth = 1920
ScreenHeight = 1080
MaxLoginLength = 25
MaxPasswordLength = 25
Task_Descriptions = [
    ["Игрок получает 5 очков за каждый номинал,",
     "карт которого у него больше, чем у остальных",
     "   (при равенстве - очки получают оба)      "],

    ["Игрок получает 3 очка за каждые 10 очков",
     "в сумме номиналов его карт"],

    ["Игрок получает очки за каждую тройку карт",
     "одного номинала: 3 очка за номиналы 1,2,3",
     "5 очков за 4,5,6 и 7 очков за 7,8,9,10"],

    ["Игрок получает очки за каждую пару карт",
     "одного номинала: 2 очка за номиналы 1,2,3",
     " 4 очка за 4,5,6 и 5 очков за 7,8,9,10"],

    ["         Игрок получает 3 очка   ",
     "за каждый номинал в своём поместье"],

    ["  Игрок получает 3 очка за каждый номинал",
     "в своей самой длинной последовательности",
     "         (например 3-4-5-6-7)           "],

    ["  Игрок получает 3 очка за каждую карту",
     "своего самого многочисленного номинала",
     "(при равенстве выбирается наименьший)"],

    ["Игрок получает очки за каждую последовательность",
     "         длины 3: 3 очка если номиналы меньше 4,     ",
     "                5 если меньше 8, и 7 иначе            "],

    ["       Игрок получает 2 очка за каждый номинал",
     "             который у него есть, если",
     "среди карт этого номинала нет товаров по акции"],

    ["  Игрок получает очки в замисимости от количества",
     "   товаров по акции(от меньшего к большему):10-6-3",
     "(при равенстве количества, оба игрока получают очки)"],

    ["       Игрок получает 2 очка за каждый номинал",
     "              который у него есть, если",
     "среди карт этого номинала есть товары по акции"],

    ["  Игрок получает очки в замисимости от количества",
     "   товаров по акции(от большего к меньшему):10-6-3",
     "(при равенстве количества, оба игрока получают очки)"]
]
pygame.init()
pygame.display.set_caption("Freak Shop")
clock = pygame.time.Clock()
pygame.font.init()
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))

TextFont = pygame.font.SysFont('Comic Sans MS', 40)
TaskFont = pygame.font.SysFont('Comic Sans MS', 25)
RegistrationFont = pygame.font.SysFont('Comic Sans MS', 80)
