import cv2
import pygame
import time

# Initialize Pygame and set up the display
pygame.init()
screen = pygame.display.set_mode((1920, 1080))

image143 = pygame.image.load('lightbluegem.png')
image144 = pygame.image.load('pinkgem.png')
image145 = pygame.image.load('rubygem.png')
image146 = pygame.image.load('heartgem.png')
image147 = pygame.image.load('diamondgem.png')
image148 = pygame.image.load('purplegem.png')
image149 = pygame.image.load('darkbluegem.png')

running = True
while running:
    screen.fill((0,0,0))
    screen.blit(image143, (490, 230))
    screen.blit(image144, (590, 230))
    screen.blit(image145, (690, 230))
    screen.blit(image146, (790, 230))
    screen.blit(image147, (590, 330))
    screen.blit(image148, (590, 430))
    screen.blit(image149, (590, 530))
    pygame.display.update()
