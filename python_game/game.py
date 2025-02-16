import pygame
from pygame.locals import *
import sys
import os
import math
import random
import cv2
pygame.init()
pygame.mixer.init()
import json
import string
########################################################################################################################
########################################################################################################################
def resource_path(relative_path):
    if getattr(sys, 'frozen', False):  # Running as an .exe
        base_path = sys._MEIPASS
    else:  # Running as a script
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
########################################################################################################################
########################################################################################################################
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHTBLUE = (102, 255, 255)
PURPLE = (127, 0, 255)
LIGHTGREEN = (102, 255, 180)
PINK = (255, 153, 255)
GREY = (192, 192, 192)
YELLOW = (255, 255, 51)
DARKGREEN = (51, 102, 0)
GOLD = (255, 197, 46)
SKYBLUE = (204, 255, 255)
TAN = (245, 197, 135)
DARKRED = (108, 5, 5)
DARKPURPLE = (130,20,255)
AQUA = (0, 247, 255)
EMERALD = (67, 192, 148)
ORANGEDESERT = (241, 99, 1)
LIGHTYELLOW = (255, 255, 153)
SWAMPGREEN = (0, 51, 0)
DARKGEMBLUE = (0, 0, 51)
VELVET = (102, 0, 51)
LIME = (102, 255, 102)
PINPPINK = (255, 102, 102)
MURKY = (51, 51, 0)
CLOUD = (204, 229, 255)
SLEEPPURPLE = (204, 153, 255)

menu1_active = True
menu2_active = False
cutscene1 = False

FaderBool = True
Fader = 1.00
textFader = 0
characterName = ''

itemboughtswitch = False
firsttimepaimon = True
firsttimeblackmarket = True
gold = 0
gem = 0
itemlist = []
level = 1
miningspeed = 0
miningefficiency = 0
time = 0
luck = 0
spawnchance = 0
specialefficiency = 0
alchemylevel = 0
alchemyexp = 0
guildtutorial = 0
########################################################################################################################
########################################################################################################################
imagebeast1 = pygame.image.load(resource_path('images/f1.png'))
imagebeast2 = pygame.image.load(resource_path('images/f2.png'))
imagebeast3 = pygame.image.load(resource_path('images/f3.png'))
imagebeast4 = pygame.image.load(resource_path('images/f4.png'))
imagebeast5 = pygame.image.load(resource_path('images/f5.png'))
imagebeast6 = pygame.image.load(resource_path('images/f6.png'))
imagebeast7 = pygame.image.load(resource_path('images/f7.png'))
imagebeast8 = pygame.image.load(resource_path('images/f8.png'))
imagebeast9 = pygame.image.load(resource_path('images/f9.png'))
imagebeast10 = pygame.image.load(resource_path('images/f10.png'))
imagebeast11 = pygame.image.load(resource_path('images/f11.png'))
imagebeast12 = pygame.image.load(resource_path('images/f12.png'))
imagebeast13 = pygame.image.load(resource_path('images/f13.png'))
imagebeast14 = pygame.image.load(resource_path('images/f14.png'))
imagebeast15 = pygame.image.load(resource_path('images/f15.png'))
imagebeast16 = pygame.image.load(resource_path('images/f16.png'))
imagebeast17 = pygame.image.load(resource_path('images/f17.png'))
imagebeast18 = pygame.image.load(resource_path('images/f18.png'))
imagebeast19 = pygame.image.load(resource_path('images/f19.png'))
imagebeast20 = pygame.image.load(resource_path('images/f20.png'))
imagebeast21 = pygame.image.load(resource_path('images/f21.png'))
imagebeast22 = pygame.image.load(resource_path('images/f22.png'))
imagebeast23 = pygame.image.load(resource_path('images/f23.png'))
imagebeast24 = pygame.image.load(resource_path('images/f24.png'))
imagebeast25 = pygame.image.load(resource_path('images/f25.png'))
imagebeast26 = pygame.image.load(resource_path('images/f26.png'))
imagebeast27 = pygame.image.load(resource_path('images/f27.png'))
imagebeast28 = pygame.image.load(resource_path('images/f28.png'))
imagebeast29 = pygame.image.load(resource_path('images/f29.png'))
imagebeast30 = pygame.image.load(resource_path('images/f30.png'))
imagebeast31 = pygame.image.load(resource_path('images/f31.png'))
imagebeast32 = pygame.image.load(resource_path('images/f32.png'))
imagebeast33 = pygame.image.load(resource_path('images/f33.png'))
imagebeast34 = pygame.image.load(resource_path('images/f34.png'))
imagebeast35 = pygame.image.load(resource_path('images/f35.png'))
imagebeast36 = pygame.image.load(resource_path('images/f36.png'))
imagebeast37 = pygame.image.load(resource_path('images/f37.png'))
imagebeast38 = pygame.image.load(resource_path('images/f38.png'))
imagebeast39 = pygame.image.load(resource_path('images/f39.png'))
imagebeast40 = pygame.image.load(resource_path('images/f40.png'))
imagebeast41 = pygame.image.load(resource_path('images/f41.png'))
imagebeast42 = pygame.image.load(resource_path('images/f42.png'))
imagebeast43 = pygame.image.load(resource_path('images/f43.png'))
imagebeast44 = pygame.image.load(resource_path('images/f44.png'))
imagebeast45 = pygame.image.load(resource_path('images/f45.png'))
imagebeast46 = pygame.image.load(resource_path('images/f46.png'))
imagebeast47 = pygame.image.load(resource_path('images/f47.png'))
imagebeast48 = pygame.image.load(resource_path('images/f48.png'))
imagebeast49 = pygame.image.load(resource_path('images/f49.png'))
imagebeast50 = pygame.image.load(resource_path('images/f50.png'))
imagebeast51 = pygame.image.load(resource_path('images/f51.png'))
imagebeast52 = pygame.image.load(resource_path('images/f52.png'))
imagebeast53 = pygame.image.load(resource_path('images/f53.png'))
imagebeast54 = pygame.image.load(resource_path('images/f54.png'))
imagebeast55 = pygame.image.load(resource_path('images/f55.png'))
imagebeast56 = pygame.image.load(resource_path('images/f56.png'))
imagebeast57 = pygame.image.load(resource_path('images/f57.png'))
imagebeast58 = pygame.image.load(resource_path('images/f58.png'))
imagebeast59 = pygame.image.load(resource_path('images/f59.png'))
imagebeast60 = pygame.image.load(resource_path('images/f60.png'))
imagebeast61 = pygame.image.load(resource_path('images/f61.png'))
imagebeast62 = pygame.image.load(resource_path('images/f62.png'))
imagebeast63 = pygame.image.load(resource_path('images/f63.png'))
imagebeast64 = pygame.image.load(resource_path('images/f64.png'))
imagebeast65 = pygame.image.load(resource_path('images/f65.png'))
imagebeast66 = pygame.image.load(resource_path('images/f66.png'))
imagebeast67 = pygame.image.load(resource_path('images/f67.png'))
imagebeast68 = pygame.image.load(resource_path('images/f68.png'))
imagebeast69 = pygame.image.load(resource_path('images/f69.png'))
imagebeast70 = pygame.image.load(resource_path('images/f70.png'))
imagebeast71 = pygame.image.load(resource_path('images/f71.png'))
imagebeast72 = pygame.image.load(resource_path('images/f72.png'))
imagebeast73 = pygame.image.load(resource_path('images/f73.png'))
imagebeast74 = pygame.image.load(resource_path('images/f74.png'))
imagebeast75 = pygame.image.load(resource_path('images/f75.png'))
imagebeast76 = pygame.image.load(resource_path('images/f76.png'))



beasts = [imagebeast1,imagebeast2,imagebeast3,imagebeast4,imagebeast5,imagebeast6,imagebeast7,imagebeast8,imagebeast9,imagebeast10,
imagebeast11,imagebeast12,imagebeast13,imagebeast14,imagebeast15,imagebeast16,imagebeast17,imagebeast18,imagebeast19,imagebeast20,
imagebeast21,imagebeast22,imagebeast23,imagebeast24,imagebeast25,imagebeast26,imagebeast27,imagebeast28,imagebeast29,imagebeast30,
imagebeast31,imagebeast32,imagebeast33,imagebeast34,imagebeast35,imagebeast36,imagebeast37,imagebeast38,imagebeast39,imagebeast40,
imagebeast41,imagebeast42,imagebeast43,imagebeast44,imagebeast45,imagebeast46,imagebeast47,imagebeast48,imagebeast49,imagebeast50,
imagebeast51,imagebeast52,imagebeast53,imagebeast54,imagebeast55,imagebeast56,imagebeast57,imagebeast58,imagebeast59,imagebeast60,
imagebeast61,imagebeast62,imagebeast63,imagebeast64,imagebeast65,imagebeast66,imagebeast67,imagebeast68,imagebeast69,imagebeast70,
imagebeast71,imagebeast72,imagebeast73,imagebeast74,imagebeast75,imagebeast76]

smallBeasts = [pygame.transform.scale(image, (60, 60)) for image in beasts]


#Each element corresponds to the following
# spawn level, hp, defense strength, spec attack, speed, Tier, Name, image location with beast[], move1, move2, move3, move4, type, exp
beastattributes = [
    [1, 4, 4, 4, 4, 4, 1, "gallo", 0, 171, 172, 'empty', 'empty', 'normal'],
    [25, 4, 4, 4, 4, 4, 2, "gallodus", 1, 94, 176, 180, 175, 'normal'],
    [1, 7, 12, 6, 3, 5, 1, "Krillith", 2, 88, 149, 'empty', 'empty', 'ground'],
    [1, 4, 4, 9, 9, 7, 1, "Lux", 3, 88, 97, 'empty', 'empty', 'poison'],
    [1, 8, 13, 5, 3, 2, 1, "Verdescent", 4, 172, 141, 'empty', 'empty', 'ground'],
    [1, 7, 3, 5, 7, 7, 1, "axo", 5, 72, 71, 'empty', 'empty', 'water'],
    [1, 5, 5, 5, 10, 6, 1, "PoisonLight Goop", 6, 75, 93, 'empty', 'empty', 'poison'],
    [1, 4, 3, 3, 3, 12, 1, "Aether Terror", 7, 117, 117, 'empty', 'empty', 'normal'],
    [1, 5, 3, 9, 3, 13, 1, "Mimi", 8, 218, 172, 'empty', 'empty', 'lightning'],
    [1, 5, 11, 1, 3, 1, 1, "Nauty", 9, 125, 124, 'empty', 'empty', 'nature'],
    [1, 5, 9, 2, 7, 4, 1, "Pearlos", 10, 75, 189, 'empty', 'empty', 'water'],
    [1, 7, 5, 5, 5, 4, 1, "Dust Pill", 11, 75, 75, 'empty', 'empty', 'ground'],
    [1, 10, 3, 2, 10, 2, 1, "Assimule", 12, 17, 75, 'empty', 'empty', 'darkness'],
    [1, 4, 6, 7, 7, 8, 1, "Crowpeck", 13, 200, 214, 'empty', 'empty', 'lightning'],
    [1, 8, 5, 9, 2, 7, 1, "Depthtracer", 14, 190, 181, 'empty', 'empty', 'ice'],
    [1, 6, 4, 11, 1, 6, 1, "Nautizark", 15, 72, 76, 'empty', 'empty', 'water'],
    [1, 5, 3, 1, 12, 6, 1, "Ripple", 16, 72, 76, 'empty', 'empty', 'water'],
    [1, 5, 4, 6, 7, 4, 1, "Marene", 17, 4, 75, 'empty', 'empty', 'darkness'],
    [1, 3, 14, 6, 2, 3, 1, "Scalex", 18, 57, 58, 'empty', 'empty', 'fire'],
    [1, 5, 4, 8, 9, 9, 1, "Abyssal Newt", 19, 6, 14, 'empty', 'empty', 'darkness'],
    [1, 7, 3, 11, 3, 3, 1, "Hollow Mimic", 20, 4, 6, 'empty', 'empty', 'darkness'],
    [1, 4, 4, 7, 7, 4, 1, "Corpse Puppet", 21, 6, 7, 'empty', 'empty', 'darkness'],
    [1, 8, 8, 5, 5, 1, 1, "Amica", 22, 120, 141, 'empty', 'empty', 'normal'],
    [1, 3, 3, 5, 3, 6, 1, "Noodle", 23, 75, 120, 'empty', 'empty', 'normal'],
    [1, 6, 4, 5, 5, 8, 1, "Weiner", 24, 190, 181, 'empty', 'empty', 'ice'],
    [1, 7, 6, 7, 10, 7, 1, "Gleamfin", 25, 78, 85, 'empty', 'empty', 'water'],
    [1, 6, 6, 10, 7, 9, 1, "Mistfin", 26, 75, 219, 'empty', 'empty', 'wind'],
    [1, 6, 7, 7, 10, 7, 1, "Magmafin", 27, 57, 50, 'empty', 'empty', 'fire'],
    [25, 7, 6, 7, 10, 7, 2, "AquaWalker", 28, 172, 77, 98, 80, 'water'],
    [25, 6, 7, 7, 10, 7, 2, "MagmaWalker", 29, 172, 62, 215, 48, 'fire'],
    [25, 7, 3, 5, 7, 7, 2, "Axolus", 30, 73, 177, 189, 172, 'water'],
    [50, 7, 3, 5, 7, 7, 3, "Axoluminous", 31, 167, 87, 193, 165, 'water'],
    [25, 7, 7, 7, 7, 7, 2, "Sacred Lumenous", 32, 33, 22, 36, 66, 'light'],
    [25, 8, 13, 5, 3, 2, 2, "Terra Verdescence", 33, 176, 139, 134, 171, 'ground'],
    [1, 6, 6, 13, 13, 9, 1, "Snowblossom", 34, 189, 41, 'empty', 'empty', 'ice'],
    [25, 5, 5, 5, 10, 6, 2, "PoisonLight Carp", 35, 3, 82, 100, 104, 'poison'],
    [25, 10, 3, 2, 10, 2, 2, "Assimilation", 36, 6, 4, 94, 1, 'darkness'],
    [25, 8, 5, 9, 2, 7, 2, "DepthWing", 37, 189, 200, 204, 182, 'ice'],
    [25, 5, 11, 1, 3, 1, 2, "Nautileous", 38, 127, 6, 32, 126, 'nature'],
    [25, 5, 3, 1, 12, 6, 2, "Ripshade", 39, 120, 112, 87, 104, 'water'],
    [25, 6, 4, 11, 1, 6, 2, "Hydrosark", 40, 120, 84, 111, 67, 'water'],
    [25, 5, 4, 6, 7, 4, 2, "Marenara", 41, 0, 7, 84, 13, 'darkness'],
    [25, 3, 14, 6, 2, 3, 2, "Scalex Ripper", 42, 137, 50, 145, 52, 'fire'],
    [25, 7, 3, 11, 3, 3, 2, "Ethereal Mimic", 43, 65, 3, 64, 0, 'darkness'],
    [1, 4, 5, 5, 5, 4, 1, "Undead Soul", 44, 6, 14, 'empty', 'empty', 'darkness'],
    [1, 7, 7, 5, 12, 11, 1, "Cinderfrost", 45, 76, 189, 'empty', 'empty', 'ice'],
    [1, 7, 7, 7, 7, 7, 1, "Sacred Lumen", 46, 75, 76, 'empty', 'empty', 'light'],
    [1, 10, 10, 7, 1, 4, 1, "FrostTip", 47, 190, 141, 'empty', 'empty', 'ice'],
    [1, 10, 5, 14, 1, 3, 1, "Cryolo", 48, 141, 143, 'empty', 'empty', 'ground'],
    [1, 3, 3, 13, 3, 8, 1, "minnowClaw", 49, 204, 179, 'empty', 'empty', 'lightning'],
    [25, 5, 3, 9, 3, 13, 2, "Clyrix", 50, 174, 204, 165, 201, 'lightning'],
    [50, 4, 4, 9, 9, 7, 3, "Luxerous", 51, 96, 109, 108, 80, 'poison'],
    [25, 8, 8, 8, 4, 4, 2, "Seafrost", 52, 190, 141, 139, 192, 'ice'],
    [25, 10, 5, 14, 1, 3, 2, "Cryolodon", 53, 182, 113, 204, 211, 'ground'],
    [25, 5, 3, 9, 3, 13, 2, "Shadow Wing", 54, 140, 201, 217, 153, 'wind'],
    [1, 8, 5, 3, 8, 5, 1, "Shade Wing", 55, 218, 220, 'empty', 'empty', 'wind'],
    [50, 3, 3, 13, 3, 8, 3, "Brineclaw", 56, 169, 215, 25, 208, 'lightning'],
    [25, 3, 3, 13, 3, 8, 2, "SereneClaw", 57, 218, 200, 203, 174, 'lightning'],
    [50, 10, 10, 7, 1, 4, 3, "FrostHyperion", 58, 196, 138, 199, 133, 'ice'],
    [25, 10, 10, 7, 1, 4, 2, "Frosthorn", 59, 139, 192, 189, 191, 'ice'],
    [25, 7, 7, 5, 12, 11, 3, "Cinderglace", 60, 187, 185, 86, 193, 'ice'],
    [50, 5, 5, 5, 10, 6, 3, "PoisonLight Wyvern", 61, 106, 108, 67, 109, 'poison'],
    [25, 5, 5, 1, 9, 5, 2, "Sirenyx", 62, 159, 92, 158, 161, 'psychic'],
    [75, 7, 7, 7, 7, 7, 4, "Opheus The Forbidden", 63, 83, 119, 31, 26, 'light'],
    [50, 5, 4, 8, 9, 9, 3, "Abyssal Basilisk", 64, 15, 144, 19, 12, 'darkness'],
    [50, 4, 4, 7, 7, 4, 3, "Corpse Puppet King", 65, 15, 16, 21, 98, 'darkness'],
    [50, 8, 5, 9, 2, 7, 3, "Depth Lord", 66, 194, 175, 185, 179, 'ice'],
    [50, 6, 6, 10, 7, 9, 3, "Mistrace", 67, 214, 119, 213, 216, 'wind'],
    [50, 6, 6, 13, 13, 9, 3, "Phoenix of Death", 68, 8, 151, 19, 20, 'darkness'],
    [50, 6, 6, 13, 13, 9, 3, "Phoenix of Life", 69, 59, 151, 118, 130, 'fire'],
    [50, 7, 7, 7, 7, 7, 3, "Sacred Oceanix", 70, 116, 29, 83, 119, 'light'],
    [50, 7, 6, 7, 10, 7, 3, "Aqua Dragon", 71, 140, 86, 87, 159, 'water'],
    [50, 6, 7, 7, 10, 7, 3, "Flame Dragon", 72, 44, 54, 55, 143, 'fire'],
    [25, 5, 4, 8, 9, 9, 2, "Abyssal Viper", 73, 4, 161, 3, 0, 'darkness'],
    [25, 4, 5, 5, 5, 4, 2, "Undead Emperor", 74, 181, 16, 197, 200, 'darkness'],
    [50, 9, 9, 9, 9, 9, 3, "Gigantorok", 75, 140, 107, 134, 153, 'ground']
]


#Each element corresponds to the following
# Move name, Damage, special effect, buff/debuff to enemy, buff/debuff to yourself, type of attack, PP
moves = [
    ["Nightveil Slash", 60, "empty", "empty", "empty", "attack", 10],
    ["Dreadspire Maelstrom", 85, "empty", "speed-1", "empty", "spec", 10],
    ["Abyssal Surge", 100, "empty", "empty", "empty", "spec", 3],
    ["Blackthorn Rupture", 75, "empty", "empty", "empty", "attack", 5],
    ["Soulshadow Lament", 50, "empty", "empty", "empty", "spec", 10],
    ["Nocturne Fang", 75, "empty", "empty", "empty", "attack", 10],
    ["Void Lash", 40, "empty", "empty", "empty", "attack", 5],
    ["Nightfall", 60, "empty", "empty", "empty", "spec", 5],
    ["Netherstrike Touch", "random", "fire", "empty", "empty", "attack", 5],
    ["Oblivion Bloom", 85, "empty", "empty", "empty", "spec", 5],
    ["Soul Harvest", 100, "empty", "empty", "empty", "spec", 3],
    ["Reaper Death Seal", 300, "userdeath", "empty", "empty", "spec", 1],
    ["Blood Sacrifice", 150, "empty", "empty", "defense-2", "spec", 2],
    ["Weeping Skull", 60, "empty", "empty", "empty", "attack", 5],
    ["Soul Tie", 50, "empty", "attack-1", "attack-1", "spec", 7],
    ["Void Drain", 70, "heal1", "empty", "empty", "spec", 7],
    ["Blood Magic", 80, "empty", "empty", "defense-1", "spec", 5],
    ["Wraith", 50, "poison", "empty", "accuracy+1", "spec", 10],
    ["Essence", 0, "heal2", "empty", "defense-1", "empty", 10],
    ["Bloodmoon", 110, "empty", "empty", "empty", "spec", 3],
    ["Black Lotus", 120, "fire", "empty", "empty", "spec", 3],
    ["Netherpulse", 90, "empty", "empty", "empty", "spec", 3],
    ["Celestial Javelin", 80, "empty", "empty", "empty", "attack", 10],
    ["Aurora Veil", 0, "empty", "empty", "specattack+2", "spec", 5],
    ["Judgement", 140, "empty", "empty", "specattack-1", "spec", 3],
    ["Heavenly Eclipse", 110, "empty", "empty", "empty", "spec", 3],
    ["Starpiercer Bolt", 90, "empty", "empty", "empty", "attack", 7],
    ["Sanctum Barrier", 0, "empty", "attack-1", "defense+2", "empty", 5],
    ["Moonfire", 85, "empty", "empty", "empty", "spec", 5],
    ["Fatebreaker", 100, "empty", "empty", "empty", "attack", 3],
    ["Celestial Cascade", 50, "empty", "empty", "empty", "spec", 10],
    ["Light Blade", 95, "empty", "empty", "empty", "attack", 5],
    ["Holy Embrace", 0, "heal2", "empty", "empty", "empty", 5],
    ["Light Bringer", 45, "empty", "empty", "empty", "spec", 10],
    ["Love", 0, "heal1", "attack-1", "empty", "empty", 10],
    ["Quintessence", 0, "heal2", "empty", "defense+1", "empty", 3],
    ["Smite", "random", "fire", "empty", "empty", "spec", 10],
    ["Holy Smite", "superrandom", "fire", "empty", "empty", "spec", 5],
    ["Requiem of Life", 100, "empty", "empty", "empty", "spec", 3],
    ["Lumina Pulse", 95, "empty", "empty", "empty", "spec", 7],
    ["Prismstrike", 95, "empty", "empty", "empty", "attack", 7],
    ["Luminspire", 55, "empty", "empty", "accuracy+1", "attack", 10],
    ["Skyshard Barrage", 110, "empty", "empty", "empty", "attack", 3],
    ["Love Potion", 0, "heal2", "empty", "empty", "empty", 10],
    ["Pyroclasmic Surge", 80, "empty", "empty", "empty", "attack", 5],
    ["Phoenix Volley", 75, "empty", "empty", "empty", "spec", 10],
    ["Infernal Arc", 75, "fire", "empty", "empty", "attack", 10],
    ["Dragon Aura", 0, "empty", "empty", "specattack+2", "empty", 10],
    ["Dragons Breathe", 75, "empty", "empty", "empty", "spec", 5],
    ["Draco Meteor", 110, "empty", "empty", "empty", "attack", 3],
    ["Pyro breath", 60, "empty", "empty", "empty", "spec", 5],
    ["Will of Fire", 90, "fire", "defense-1", "empty", "spec", 5],
    ["Flamestorm Spiral", 75, "empty", "empty", "empty", "attack", 5],
    ["Burning Crescence", 95, "empty", "empty", "empty", "spec", 5],
    ["Crimson Fang Slash", 80, "empty", "empty", "empty", "attack", 5],
    ["Supernova", 100, "empty", "empty", "empty", "spec", 3],
    ["Sunlord", 120, "empty", "empty", "empty", "spec", 3],
    ["Wisp", 30, "empty", "empty", "accuracy+1", "spec", 10],
    ["Flare", 0, "empty", "accuracy-2", "empty", "empty", 10],
    ["Sunfire", 100, "fire", "empty", "empty", "spec", 3],
    ["Magma Quake", 95, "empty", "empty", "empty", "attack", 7],
    ["Horizon", 95, "empty", "empty", "empty", "spec", 7],
    ["Solarclaw", 70, "empty", "empty", "empty", "attack", 10],
    ["Volcanic Strike", 85, "fire", "empty", "empty", "attack", 5],
    ["Fireheart", 0, "heal1", "empty", "attack+1", "empty", 5],
    ["Ashstorm", "random", "empty", "empty", "empty", "empty", 5],
    ["Crystal Tempest", 95, "empty", "empty", "empty", "attack", 5],
    ["Spiritbound Vortex", 75, "empty", "speed-1", "empty", "spec", 7],
    ["Aqua Surge", 60, "empty", "empty", "empty", "attack", 7],
    ["Rising Tide Strike", 50, "riptide", "empty", "empty", "attack", 10],
    ["Ocean Requiem", 100, "empty", "empty", "empty", "spec", 3],
    ["Plunge", 50, "empty", "empty", "empty", "attack", 7],
    ["Watergun", 45, "empty", "empty", "empty", "attack", 7],
    ["Hurricane", "random", "riptide", "empty", "empty", "spec", 10],
    ["Hydro Cannon", 65, "empty", "empty", "empty", "attack", 5],
    ["Splash", 10, "empty", "empty", "empty", "spec", 20],
    ["Bubblebeam", 50, "empty", "empty", "empty", "spec", 7],
    ["Coral Spike", 45, "empty", "empty", "empty", "attack", 10],
    ["Ocean Voice", 0, "heal1", "empty", "speed+1", "empty", 10],
    ["Wavepool", 30, "empty", "empty", "empty", "spec", 10],
    ["Stormbound", 0, "riptide2", "empty", "empty", "empty", 10],
    ["Hydrolash", 55, "empty", "empty", "attack+1", "attack", 5],
    ["Rift", 55, "empty", "empty", "empty", "attack", 5],
    ["Hydronova", 110, "empty", "empty", "empty", "spec", 3],
    ["Brine Edge", 75, "empty", "empty", "empty", "attack", 5],
    ["Seafoam Barrage", 60, "empty", "empty", "empty", "spec", 5],
    ["Crystalwave", 95, "freeze", "empty", "empty", "spec", 5],
    ["Oceans Embrace", 0, "heal1", "attack-1", "defense+1", "empty", 7],
    ["Venomdance", 0, "empty", "empty", "specattack+2", "empty", 10],
    ["Phantom Reaver", 0, "empty", "specattack-2", "empty", "empty", 10],
    ["Toxic Vortex", 35, "poison", "empty", "empty", "spec", 7],
    ["Shadow Venom", 0, "poison2", "empty", "empty", "empty", 5],
    ["Serpent's Spite", 55, "empty", "attack-1", "empty", "attack", 10],
    ["coil", 45, "empty", "empty", "empty", "attack", 10],
    ["poison bite", 60, "poison", "empty", "empty", "attack", 7],
    ["venomshock", 60, "poison", "empty", "attack+1", "spec", 7],
    ["Erosion", 80, "empty", "empty", "empty", "spec", 3],
    ["Venom Trap", 45, "poison", "empty", "empty", "attack", 5],
    ["Paralyze", 0, "paralyze", "empty", "empty", "empty", 10],
    ["Poison Beak", 50, "empty", "empty", "empty", "attack", 10],
    ["Chemical Burn", 75, "empty", "empty", "empty", "spec", 5],
    ["Mustard Gas", "superrandom", "empty", "defense-1", "empty", "spec", 5],
    ["Dao of Poison", 100, "poison2", "empty", "empty", "spec", 3],
    ["Purple Lotus", 120, "fire", "empty", "empty", "spec", 3],
    ["Miasma", 90, "paralyze", "empty", "empty", "spec", 5],
    ["Corrosive Swipe", 65, "empty", "empty", "empty", "attack", 5],
    ["Fangs of Decay", 75, "empty", "empty", "empty", "attack", 7],
    ["Putrid", 0, "bloom2", "empty", "empty", "empty", 7],
    ["Corrosive Requiem", 100, "empty", "empty", "empty", "spec", 3],
    ["Plaguestorm", 95, "empty", "defense-1", "empty", "spec", 5],
    ["Mana Bloom", 60, "empty", "empty", "empty", "attack", 10],
    ["Nature’s Wrath", 100, "bloom", "empty", "empty", "spec", 7],
    ["Verdant Slash", 60, "empty", "empty", "empty", "attack", 10],
    ["Ivybind", 40, "paralyze", "empty", "empty", "spec", 10],
    ["Leaf Tempest", 95, "empty", "empty", "empty", "spec", 7],
    ["Grass Knot", 0, "paralyze", "attack-1", "empty", "attack", 10],
    ["Natures Embrace", 0, "empty", "empty", "empty", "empty", 10],
    ["Spore Zone", 30, "empty", "empty", "empty", "attack", 10],
    ["Terra Devestation", 150, "empty", "empty", "attack-2", "attack", 2],
    ["Call of the Spirits", 0, "heal1", "empty", "speed+1", "empty", 10],
    ["Mud", 0, "empty", "speed-2", "empty", "empty", 10],
    ["Jungle Gym", 0, "empty", "empty", "attack+2", "empty", 10],
    ["heal", 0, "heal1", "empty", "empty", "empty", 7],
    ["Jungle Juice", 0, "heal1", "empty", "attack+1", "empty", 5],
    ["Petalstrike", 65, "empty", "empty", "empty", "attack", 7],
    ["Foliage", 0, "empty", "empty", "empty", "empty", 10],
    ["Bloomveil", 50, "bloom", "empty", "empty", "spec", 7],
    ["Wildflare", 70, "empty", "empty", "empty", "spec", 7],
    ["Thornburst", 80, "empty", "empty", "empty", "attack", 7],
    ["Budstrike", 60, "bloom", "empty", "empty", "spec", 7],
    ["Thorns of Ruin", 100, "empty", "empty", "empty", "attack", 5],
    ["Verdescence", 120, "empty", "empty", "empty", "spec", 3],
    ["Titan’s Fist", 130, "gravity", "empty", "speed-1", "attack", 1],
    ["Earthspike Rupture", 90, "empty", "empty", "empty", "spec", 7],
    ["Quakebreaker Slam", 90, "empty", "empty", "empty", "attack", 7],
    ["Shatterstrike", 85, "paralyze", "empty", "empty", "attack", 5],
    ["Creeping Death", 80, "empty", "empty", "empty", "spec", 5],
    ["Earth Barrier", 0, "empty", "speed-1", "defense+1", "empty", 10],
    ["Harden", 0, "empty", "empty", "defense+1", "empty", 10],
    ["Stone Barricade", 0, "empty", "attack-1", "defense+1", "empty", 10],
    ["Earth Spike", 85, "empty", "empty", "empty", "attack", 7],
    ["Stomp", 45, "empty", "empty", "empty", "attack", 10],
    ["New Earth", 130, "empty", "defense-1", "defense-1", "spec", 1],
    ["Bedrock", 120, "empty", "empty", "empty", "attack", 3],
    ["Gravelstrike", "superrandom", "empty", "empty", "empty", "attack", 10],
    ["Tremor", 40, "empty", "empty", "empty", "spec", 10],
    ["Faultline", 100, "empty", "empty", "empty", "spec", 5],
    ["Geospike", 100, "empty", "empty", "empty", "attack", 5],
    ["Seismic Crush", 80, "gravity", "empty", "empty", "attack", 5],
    ["Sediment", 20, "empty", "accuracy-1", "empty", "spec", 10],
    ["Terraburst", 85, "empty", "empty", "empty", "spec", 5],
    ["Meteor Impact", 110, "empty", "empty", "accuracy-1", "attack", 3],
    ["Torterra", 120, "empty", "empty", "empty", "attack", 3],
    ["Duststorm", "random", "empty", "speed-1", "empty", "empty", 5],
    ["Voidflare Rift", 90, "empty", "empty", "empty", "spec", 5],
    ["Mind Burst", "superrandom", "empty", "empty", "empty", "spec", 3],
    ["Timefracture", 130, "empty", "empty", "accuracy-1", "spec", 3],
    ["Echoing Frenzy", 0, "gravity2", "empty", "empty", "empty", 10],
    ["Soulpierce Shot", 75, "paralyze", "empty", "empty", "spec", 5],
    ["Spectral Bolt", 75, "empty", "empty", "empty", "spec", 7],
    ["Astral Coil", 60, "empty", "empty", "empty", "spec", 10],
    ["Dreambreaker", "random", "empty", "empty", "empty", "spec", 10],
    ["Etherwave", 50, "empty", "empty", "empty", "spec", 10],
    ["Memory Wipe", 0, "empty", "specattack-2", "empty", "empty", 5],
    ["Enlightenment", "superrandom", "heal1", "empty", "specattack+2", "empty", 5],
    ["Lionheart Lunge", 80, "gravity", "empty", "empty", "attack", 5],
    ["Arrowstorm", 80, "empty", "empty", "empty", "attack", 5],
    ["Echo Strike", 75, "empty", "empty", "empty", "spec", 5],
    ["Phantom Edge", 75, "empty", "empty", "empty", "spec", 5],
    ["Bladestorm Spiral", "random", "empty", "empty", "empty", "attack", 7],
    ["Slash", 70, "empty", "empty", "empty", "attack", 7],
    ["Crunch", 70, "empty", "empty", "empty", "attack", 7],
    ["Leer", 0, "empty", "accuracy-1", "empty", "empty", 10],
    ["Workout", 0, "empty", "accuracy-1", "attack+1", "empty", 10],
    ["Sword Soul", 0, "gravity", "empty", "specattack+2", "empty", 7],
    ["Aura", 0, "empty", "attack-1", "attack+1", "empty", 7],
    ["Headbutt", 50, "empty", "empty", "empty", "attack", 7],
    ["jab", 50, "paralyze", "empty", "empty", "attack", 7],
    ["Frenzy", 0, "empty", "empty", "attack+1", "empty", 10],
    ["Trueform", 0, "empty", "empty", "specattack+2", "empty", 10],
    ["empty", 90, "empty", "empty", "empty", "spec", 5],
    ["Howl", 0, "empty", "speed-1", "empty", "empty", 10],
    ["Frostfang Missile", 75, "empty", "empty", "empty", "attack", 7],
    ["Crystal Tempest", 100, "empty", "empty", "empty", "spec", 5],
    ["Frozen Starlight", 135, "freeze", "defense+1", "empty", "spec", 3],
    ["Shatterfang", 75, "paralyze", "empty", "empty", "attack", 5],
    ["Aurora", 0, "empty", "empty", "defense+2", "empty", 10],
    ["Ice Heart", 0, "heal2", "empty", "empty", "empty", 10],
    ["Frozen World", 120, "freeze", "empty", "empty", "spec", 5],
    ["Icicle", 35, "empty", "empty", "empty", "attack", 10],
    ["Frostshard", 35, "empty", "empty", "empty", "spec", 10],
    ["Icevein", 0, "freeze2", "empty", "specattack+1", "empty", 10],
    ["Tundrashard", 75, "empty", "empty", "empty", "spec", 10],
    ["Cryoshard", 95, "empty", "empty", "empty", "spec", 7],
    ["Subzero", 0, "freeze", "speed-2", "empty", "empty", 10],
    ["Polarveil", 0, "empty", "empty", "defense+1", "empty", 10],
    ["Icefang Tempest", 95, "empty", "empty", "empty", "attack", 7],
    ["Frozen Reqiuem", 100, "freeze", "empty", "empty", "spec", 5],
    ["Stormbreaker", 110, "empty", "empty", "empty", "spec", 5],
    ["Thunderstrike", 95, "empty", "empty", "empty", "attack", 5],
    ["Lightning Surge", 60, "empty", "empty", "empty", "spec", 7],
    ["Arcburst", 90, "empty", "empty", "empty", "attack", 7],
    ["Electrify", 0, "paralyze", "defense-1", "empty", "empty", 10],
    ["Cloudlash", 60, "empty", "empty", "empty", "spec", 7],
    ["Thunderpulse", 40, "empty", "empty", "empty", "spec", 10],
    ["Lightningcry", 0, "paralyze2", "empty", "empty", "empty", 10],
    ["Blitz", 110, "empty", "empty", "accuracy-1", "attack", 5],
    ["Tempest", 120, "empty", "empty", "empty", "spec", 5],
    ["Sky Sunder", 140, "empty", "empty", "speed-1", "attack", 3],
    ["Storm Lord", 150, "empty", "speed+1", "attack-1", "spec", 1],
    ["Tribulation Lightning", "superrandom", "paralyze", "defense-1", "defense-1", "spec", 5],
    ["Agile", 0, "empty", "speed-1", "speed+2", "empty", 10],
    ["Zephyr", 130, "empty", "empty", "accuracy-1", "attack", 3],
    ["Feather Tornado", 70, "empty", "empty", "empty", "attack", 7],
    ["Windshear", 70, "empty", "empty", "empty", "attack", 7],
    ["Skybound", 0, "empty", "empty", "accuracy+2", "empty", 10],
    ["Sky Breaker", 120, "empty", "empty", "empty", "attack", 3],
    ["Airstream", 60, "gravity", "empty", "empty", "attack", 10],
    ["Winglash", 45, "empty", "empty", "empty", "attack", 10],
    ["Gust", 40, "empty", "empty", "empty", "empty", 10],
    ["Aerial Ace", "superrandom", "empty", "empty", "attack+1", "attack", 5]
    ]

moves_lore = [
    "Nightveil Slash: A shadowy blade technique forged in the depths of the Nightveil, said to sever the soul from the body.",
    "Dreadspire Maelstrom: A chaotic vortex of dark energy that consumes all light and hope, originating from the cursed Dreadspire Tower.",
    "Abyssal Surge: A surge of power from the Abyss, capable of drowning enemies in an ocean of despair.",
    "Blackthorn Rupture: A devastating strike that summons thorny vines from the underworld to entangle and pierce foes.",
    "Soulshadow Lament: A mournful cry that manipulates shadows to drain the life force of those who hear it.",
    "Nocturne Fang: A bite infused with the essence of eternal night, paralyzing enemies with fear.",
    "Void Lash: A whip of pure void energy that disrupts the fabric of reality, leaving chaos in its wake.",
    "Nightfall: A catastrophic event summoned by dark mages, plunging the battlefield into eternal darkness.",
    "Netherstrike Touch: A touch that channels the corrupting energy of the Nether, withering all it contacts.",
    "Oblivion Bloom: A dark flower that blooms once every millennium, releasing a wave of annihilation.",
    "Soul Harvest: A forbidden technique that steals the souls of the fallen to empower the user.",
    "Reaper Death Seal: A pact with the Reaper, sealing the fate of a target with an inescapable curse.",
    "Blood Sacrifice: A ritual that sacrifices the user's blood to summon immense dark power.",
    "Weeping Skull: A cursed skull that weeps tears of poison, spreading decay and despair.",
    "Soul Tie: A binding spell that links the life force of two beings, ensuring shared fate.",
    "Void Drain: A technique that siphons energy from the Void, restoring the user at the cost of the environment.",
    "Blood Magic: A dangerous art that uses the user's blood as a catalyst for destructive spells.",
    "Wraith: A spectral form that allows the user to phase through attacks and strike from the shadows.",
    "Essence: A move that extracts the essence of an enemy, weakening them and empowering the user.",
    "Bloodmoon: A lunar event that amplifies dark powers, turning the tide of battle in favor of shadow users.",
    "Black Lotus: A rare flower that blooms in darkness, releasing a cloud of toxic spores.",
    "Netherpulse: A pulse of energy from the Netherworld, destabilizing the battlefield and weakening enemies.",
    "Celestial Javelin: A spear of pure starlight, hurled from the heavens to smite evil.",
    "Aurora Veil: A protective barrier woven from the light of the auroras, shielding allies from harm.",
    "Judgement: A divine verdict delivered by the gods, striking down the unworthy with righteous fury.",
    "Heavenly Eclipse: A celestial event that channels the power of the sun and moon to obliterate darkness.",
    "Starpiercer Bolt: A bolt of cosmic energy that pierces through any defense.",
    "Sanctum Barrier: An impenetrable shield blessed by the gods, guarding against all evil.",
    "Moonfire: A radiant flame fueled by lunar energy, burning away corruption.",
    "Fatebreaker: A move that defies destiny, allowing the user to rewrite their fate in battle.",
    "Celestial Cascade: A waterfall of starlight that heals allies and purges darkness.",
    "Light Blade: A sword forged from pure light, cutting through shadows with ease.",
    "Holy Embrace: A comforting embrace of divine energy, restoring health and hope.",
    "Light Bringer: A beacon of hope that dispels darkness and inspires allies.",
    "Love: A pure and powerful emotion that manifests as a radiant aura, healing and protecting.",
    "Quintessence: The essence of creation itself, used to restore balance and harmony.",
    "Smite: A divine strike that punishes the wicked with unrelenting force.",
    "Holy Smite: A sacred blast of energy that purifies the battlefield.",
    "Requiem of Life: A song of life that revives fallen allies and strengthens the living.",
    "Lumina Pulse: A pulse of light energy that radiates healing and protection.",
    "Prismstrike: A dazzling attack that refracts light into a spectrum of destructive energy.",
    "Luminspire: A spire of light that rises from the ground, banishing darkness and empowering allies.",
    "Skyshard Barrage: A rain of crystalline shards infused with celestial energy.",
    "Love Potion: A magical elixir that restores health and strengthens bonds between allies.",
    "Pyroclasmic Surge: A surge of molten energy that engulfs the battlefield in flames.",
    "Phoenix Volley: A barrage of fiery feathers that reignite the user's strength upon impact.",
    "Infernal Arc: A sweeping arc of hellfire that incinerates all in its path.",
    "Dragon Aura: An aura of draconic power that enhances the user's fire-based abilities.",
    "Dragons Breathe: A torrent of flame unleashed from the mouth of a dragon.",
    "Draco Meteor: A meteor shower summoned by dragon magic, raining destruction from above.",
    "Pyro Breath: A concentrated blast of fire that melts through defenses.",
    "Will of Fire: A technique that channels the user's inner fire, increasing their strength and resolve.",
    "Flamestorm Spiral: A spiraling vortex of fire that consumes everything in its radius.",
    "Burning Crescence: A crescent-shaped wave of fire that scorches the earth.",
    "Crimson Fang Slash: A fiery slash that leaves a trail of burning embers.",
    "Supernova: A cataclysmic explosion of solar energy, mimicking the death of a star.",
    "Sunlord: A move that summons the power of the sun, radiating intense heat and light.",
    "Wisp: A small flame spirit that guides and empowers the user.",
    "Flare: A bright burst of fire that blinds and burns enemies.",
    "Sunfire: A radiant flame that burns with the intensity of the sun.",
    "Magma Quake: A seismic eruption of magma that devastates the battlefield.",
    "Horizon: A move that summons a wall of fire, cutting off escape routes.",
    "Solarclaw: A claw attack infused with solar energy, leaving searing wounds.",
    "Volcanic Strike: A powerful strike that triggers a volcanic eruption.",
    "Fireheart: A move that ignites the user's heart, increasing their passion and power.",
    "Ashstorm: A storm of burning ash that suffocates and burns enemies.",
    "Crystal Tempest: A storm of crystalline water that freezes and shatters enemies.",
    "Spiritbound Vortex: A whirlpool infused with the spirits of the ocean, dragging enemies into the depths.",
    "Aqua Surge: A surge of water that crashes over enemies with immense force.",
    "Rising Tide Strike: A strike that summons a tidal wave, overwhelming foes.",
    "Ocean Requiem: A mournful song that calms the seas and lulls enemies to sleep.",
    "Plunge: A diving attack that uses the weight of water to crush enemies.",
    "Watergun: A high-pressure jet of water that pierces through defenses.",
    "Hurricane: A massive storm that devastates the battlefield with wind and rain.",
    "Hydro Cannon: A cannonball of water that explodes on impact.",
    "Splash: A playful move that splashes water, distracting enemies.",
    "Bubblebeam: A stream of bubbles that trap and confuse enemies.",
    "Coral Spike: A sharp spike of coral that impales enemies.",
    "Ocean Voice: A soothing voice that calms the seas and heals allies.",
    "Wavepool: A pool of water that rises and falls, damaging enemies caught within.",
    "Stormbound: A move that binds enemies with chains of water and lightning.",
    "Hydrolash: A whip of water that strikes with the force of a tidal wave.",
    "Rift: A tear in the fabric of reality that summons a flood of water.",
    "Hydronova: A burst of water energy that heals allies and damages enemies.",
    "Brine Edge: A blade of saltwater that corrodes and cuts through defenses.",
    "Seafoam Barrage: A barrage of seafoam that blinds and slows enemies.",
    "Crystalwave: A wave of crystalline water that freezes enemies on contact.",
    "Oceans Embrace: A protective embrace of water that shields and heals allies.",
    "Venomdance: A deadly dance that spreads poison with every step.",
    "Phantom Reaver: A ghostly blade that poisons the soul.",
    "Toxic Vortex: A swirling vortex of toxic gas that suffocates enemies.",
    "Shadow Venom: A venom that corrupts the mind and body.",
    "Serpent's Spite: A strike imbued with the venom of a vengeful serpent.",
    "Coil: A constricting move that traps and poisons enemies.",
    "Poison Bite: A bite that injects a deadly toxin.",
    "Venomshock: A shockwave of venom that paralyzes enemies.",
    "Erosion: A corrosive substance that eats away at defenses.",
    "Venom Trap: A trap that releases venom when triggered.",
    "Paralyze: A move that immobilizes enemies with a neurotoxin.",
    "Poison Beak: A peck that delivers a potent poison.",
    "Chemical Burn: A burn caused by toxic chemicals.",
    "Mustard Gas: A cloud of toxic gas that damages and blinds enemies.",
    "Dao of Poison: A philosophy that embraces the art of poisoning.",
    "Purple Lotus: A beautiful but deadly flower that releases toxic pollen.",
    "Miasma: A noxious fog that weakens and poisons enemies.",
    "Corrosive Swipe: A swipe that corrodes armor and flesh.",
    "Fangs of Decay: Fangs that inject a rotting venom.",
    "Putrid: A move that emits a foul stench, weakening enemies.",
    "Corrosive Requiem: A song that spreads decay and destruction.",
    "Plaguestorm: A storm that rains down disease and poison.",
    "Mana Bloom: A flower that drains mana and poisons enemies.",
    "Nature’s Wrath: A powerful strike that channels the fury of nature.",
    "Verdant Slash: A slash that summons vines to entangle enemies.",
    "Ivybind: A move that binds enemies with thorny ivy.",
    "Leaf Tempest: A storm of razor-sharp leaves that cuts through enemies.",
    "Grass Knot: A move that tangles enemies in grass, immobilizing them.",
    "Natures Embrace: A healing move that restores health using the power of nature.",
    "Spore Zone: An area filled with toxic spores that weaken enemies.",
    "Terra Devestation: A catastrophic move that reshapes the battlefield.",
    "Call of the Spirits: A summoning move that calls forth nature spirits to aid in battle.",
    "Mud: A move that covers enemies in mud, slowing them down.",
    "Jungle Gym: A move that creates a jungle-like environment, confusing enemies.",
    "Heal: A restorative move that uses nature's energy to heal wounds.",
    "Jungle Juice: A potion made from jungle plants that restores health and energy.",
    "Petalstrike: A strike that uses flower petals to cut through enemies.",
    "Foliage: A move that creates a dense thicket, providing cover and protection.",
    "Bloomveil: A veil of blooming flowers that shields and heals allies.",
    "Wildflare: A burst of wild energy that ignites the battlefield.",
    "Thornburst: A burst of thorns that damages and poisons enemies.",
    "Budstrike: A strike that uses budding plants to entrap enemies.",
    "Thorns of Ruin: Thorns that drain the life force of those they touch.",
    "Verdescence: A radiant aura of green energy that enhances nature-based moves.",
    "Titan’s Fist: A colossal punch that shakes the earth.",
    "Earthspike Rupture: A move that summons spikes of earth to impale enemies.",
    "Quakebreaker Slam: A slam that creates a seismic shockwave.",
    "Shatterstrike: A strike that shatters the ground, causing debris to fly.",
    "Creeping Death: A move that causes the earth to swallow enemies.",
    "Earth Barrier: A wall of earth that blocks attacks.",
    "Harden: A move that hardens the user's body, increasing defense.",
    "Stone Barricade: A barricade of stone that protects allies.",
    "Earth Spike: A spike of earth that erupts from the ground.",
    "Stomp: A powerful stomp that causes tremors.",
    "New Earth: A move that rejuvenates the battlefield with fertile soil.",
    "Bedrock: A move that creates an unbreakable foundation.",
    "Gravelstrike: A strike that uses gravel to blind and damage enemies.",
    "Tremor: A move that creates small tremors, destabilizing enemies.",
    "Faultline: A move that creates a fissure in the earth, trapping enemies.",
    "Geospike: A spike of earth that erupts with explosive force.",
    "Seismic Crush: A crushing move that uses seismic energy.",
    "Sediment: A move that covers enemies in sediment, slowing them down.",
    "Terraburst: A burst of earth energy that damages and knocks back enemies.",
    "Meteor Impact: A move that summons a meteor to crash into the battlefield.",
    "Torterra: A move that summons a massive turtle-like creature to crush enemies.",
    "Duststorm: A storm of dust that blinds and damages enemies.",
    "Voidflare Rift: A rift that unleashes the power of the Void, consuming all in its path.",
    "Mind Burst: A psychic explosion that overwhelms the minds of enemies.",
    "Timefracture: A move that fractures time, slowing down enemies.",
    "Echoing Frenzy: A psychic wave that drives enemies into a frenzy.",
    "Soulpierce Shot: A shot that pierces the soul, causing immense pain.",
    "Spectral Bolt: A bolt of spectral energy that disrupts the mind.",
    "Astral Coil: A coil of astral energy that binds and weakens enemies.",
    "Dreambreaker: A move that shatters the dreams of enemies, leaving them vulnerable.",
    "Etherwave: A wave of ether energy that disrupts the fabric of reality.",
    "Memory Wipe: A move that erases the memories of enemies, disorienting them.",
    "Enlightenment: A move that grants clarity and focus, enhancing psychic abilities.",
    "Lionheart Lunge: A brave and powerful lunge that strikes fear into enemies.",
    "Arrowstorm: A barrage of arrows that rains down on enemies.",
    "Echo Strike: A strike that echoes with additional force.",
    "Phantom Edge: A blade that strikes with the speed of a phantom.",
    "Bladestorm Spiral: A spinning attack that creates a storm of blades.",
    "Slash: A basic but effective slash attack.",
    "Crunch: A powerful bite that crushes through defenses.",
    "Leer: A menacing glare that lowers the enemy's defenses.",
    "Workout: A move that increases the user's strength and stamina.",
    "Sword Soul: A move that channels the user's soul into their sword, increasing its power.",
    "Aura: A protective aura that enhances the user's abilities.",
    "Headbutt: A forceful headbutt that stuns enemies.",
    "Jab: A quick and precise jab that disrupts enemies.",
    "Frenzy: A wild and uncontrolled attack that strikes multiple times.",
    "Trueform: A move that reveals the user's true form, increasing their power.",
    "Empty: A move that clears the mind, allowing for precise and focused attacks.",
    "Howl: A chilling howl that freezes enemies in fear.",
    "Frostfang Missile: A missile of ice that freezes enemies on impact.",
    "Crystal Tempest: A storm of crystalline ice that cuts through enemies.",
    "Frozen Starlight: A move that freezes enemies with the light of a distant star.",
    "Shatterfang: A bite that freezes and shatters enemies.",
    "Aurora: A beautiful but deadly display of light that freezes enemies.",
    "Ice Heart: A move that freezes the user's heart, increasing their resistance to damage.",
    "Frozen World: A move that freezes the entire battlefield, slowing down enemies.",
    "Icicle: A sharp icicle that impales enemies.",
    "Frostshard: A shard of ice that explodes on impact.",
    "Icevein: A move that freezes the veins of enemies, slowing their movements.",
    "Tundrashard: A shard of ice from the tundra that freezes enemies.",
    "Cryoshard: A shard of ice that explodes into a freezing mist.",
    "Subzero: A move that lowers the temperature to subzero levels, freezing enemies.",
    "Polarveil: A veil of polar energy that shields and freezes enemies.",
    "Icefang Tempest: A storm of icy fangs that pierce and freeze enemies.",
    "Frozen Requiem: A song that freezes the hearts of enemies, leaving them vulnerable.",
    "Stormbreaker: A move that breaks through storms, unleashing lightning.",
    "Thunderstrike: A powerful strike of lightning that electrifies enemies.",
    "Lightning Surge: A surge of lightning that courses through the battlefield.",
    "Arcburst: A burst of electrical energy that shocks and stuns enemies.",
    "Electrify: A move that electrifies the user, increasing their speed and power.",
    "Cloudlash: A whip of lightning that strikes from the clouds.",
    "Thunderpulse: A pulse of thunder that knocks back enemies.",
    "Lightningcry: A cry that summons a storm of lightning.",
    "Blitz: A rapid and powerful strike of lightning.",
    "Skyflare: A brilliant flash of celestial fire ignites the sky, scorching foes with the fury of the heavens.",
    "Sky Sunder: With a mighty strike, the sky itself is torn asunder, unleashing a devastating force from above.",
    "Storm Lord: Harnessing the power of the tempests, the user commands the storm, summoning lightning and thunder to strike down enemies.",
    "Tribulation Lightning: Bolts of divine judgment rain down, punishing those who stand against fate with relentless electrical fury.",
    "Agile: The user moves with unmatched swiftness, evading attacks and striking with graceful precision.",
    "Zephyr: A gentle yet swift current of wind empowers the user, enhancing their speed and agility in battle.",
    "Tornado: A spiraling vortex of wind is conjured, lifting foes into the air before hurling them aside with violent force.",
    "Windshear: A razor-sharp gust of wind cuts through the battlefield, slicing through defenses with precision.",
    "Skybound: The user ascends with the power of the skies, gaining an aerial advantage and striking from above.",
    "Sky Breaker: A thunderous blow that shatters the very air, sending shockwaves through the battlefield.",
    "Airstream: A powerful gust propels the user forward, striking swiftly and overwhelming foes with momentum.",
    "Winglash: The user lashes out with wings or air-forged blades, delivering a cutting strike that whips through the air.",
    "Cut: A swift and precise slash that carves through obstacles and enemies alike.",
    "Aerial Ace: A flawless airborne maneuver that ensures the user's attack lands unerringly, striking with pinpoint accuracy."
]

beast_lore = [
    "A creature of forgotten songs, said to hum melodies that guide lost sailors home.",
    "A guardian of the abyss, ensuring no one disturbs the secrets buried in the ocean’s depths.",
    "Feared by many, it devours memories of those who encounter it, leaving them with only an eerie sense of loss.",
    "Known as the Keeper of Light, it emits pulses of energy that awaken dormant relics scattered across the ocean floor.",
    "A legendary healer, its presence purifies the water and restores life to dying reefs.",
    "The eternal wanderer, said to appear before those on the brink of discovery, pushing them toward untold knowledge.",
    "A master of deception, it lures prey with an inviting glow before releasing a mind-altering mist.",
    "A spectral entity that exists between dimensions, glimpsed only when the fabric of reality weakens.",
    "Known as the Trickster of the Deep, it manipulates shadows and whispers riddles to those who dare to listen.",
    "A collector of lost treasures, it hoards ancient relics and jealously guards them from prying hands.",
    "Said to be the keeper of the Ocean’s Crown, a mythical artifact granting dominion over the seas.",
    "A being of legend, rumored to be the last remnant of a long-forgotten underwater civilization.",
    "A mimic of extraordinary ability, it assumes the presence of anything it encounters, leaving others questioning reality.",
    "The silent observer, it watches the tides of war and peace, only intervening when fate demands.",
    "Capable of glimpsing into the past, it etches the history of the ocean onto coral walls.",
    "Said to have emerged during the first flood, it carries the echoes of an ancient world in its wake.",
    "A being of pure motion, forever shifting and reshaping the currents to maintain balance in the sea.",
    "Revered by sailors, its presence signals an upcoming storm or a long-awaited safe passage.",
    "A harbinger of change, wherever it swims, the waters take on new life—or wither into silence.",
    "A messenger of the unknown, it delivers omens of disaster to those who dare venture too deep.",
    "Thought to be a fragment of something far greater, it seeks to reclaim its missing pieces.",
    "Said to be animated by the souls of lost mariners, it drifts lifelessly until it finds justice for the fallen.",
    "A bringer of harmony, it appears during moments of crisis to unite rivaling factions beneath the waves.",
    "A creature of mischief, known for meddling with the ocean’s flow and confusing navigators.",
    "Legends say it carries the laughter of the sea, bringing joy to those who hear its silent song.",
    "A beacon of hope, its presence signals the return of something long thought lost.",
    "Born from the mist of shipwrecks, it carries the weight of every lost vessel in its silent path.",
    "A force of destruction and rebirth, it reshapes the ocean floor with its volcanic essence.",
    "Said to be the first creature to step between water and air, bridging the worlds above and below.",
    "A harbinger of fire, it thrives where the earth’s core touches the deep, birthing new islands in its wake.",
    "A bringer of wisdom, sought by scholars for its knowledge of tides and time itself.",
    "Considered a living relic, it is believed to hold the secrets of an ancient, sunken empire.",
    "Worshiped by deep-sea dwellers, it is said to be the light that keeps the abyss from consuming all.",
    "A guardian of nature’s balance, its existence ensures the ocean and land remain in harmony.",
    "A legend of the frozen seas, it brings winter wherever it drifts, turning water to ice with its presence.",
    "Feared by all, its touch induces hallucinations, twisting the minds of those who stray too close.",
    "A being without form, it consumes the identity of those it encounters, leaving behind only echoes.",
    "A silent predator, it moves unseen in the depths, leaving only shadows in its wake.",
    "Said to be the key to an ancient machine, its very existence is tied to the rise and fall of lost civilizations.",
    "A master of illusions, it bends the ocean’s darkness to hide what should never be found.",
    "A legendary force of the deep, rumored to have the power to part the sea at will.",
    "A storyteller of the abyss, its presence causes visions of histories long buried beneath the waves.",
    "Feared by sailors, it is said to appear only before the greatest tragedies at sea.",
    "A creature of the in-between, neither alive nor dead, it mimics the voices of those long gone.",
    "A drifting wraith, forever searching for the life it once had but can never reclaim.",
    "Born of fire and ice, it holds the power to freeze and burn with equal fury.",
    "A divine being, said to be the last remnant of an ancient pantheon lost beneath the tides.",
    "A creature of the frozen deep, known for appearing in the coldest waters where even light dares not tread.",
    "Said to be the guardian of the last iceberg, its presence marks the end of an era.",
    "A bringer of chaos, it disrupts balance wherever it swims, turning peaceful waters into raging tempests.",
    "A ghostly being, it drifts between worlds, watching over those who linger too long in the abyss.",
    "Said to be the embodiment of radiant energy, it can breathe life into the darkest corners of the ocean.",
    "A traveler of frozen waters, bringing ice to even the warmest currents.",
    "A beast of eternal winter, it is said to be the reason why the polar seas never thaw.",
    "A silent observer, it watches over the abyss, ensuring no soul is taken before its time.",
    "A creature of twilight, thriving where darkness meets light, forever shifting between the two.",
    "A warrior of the old world, said to be the last of an order sworn to defend the ocean’s secrets.",
    "A keeper of balance, ensuring no force becomes too dominant within the deep.",
    "A godlike being of frozen tides, its awakening is said to mark the return of a forgotten age.",
    "A guardian of the cold abyss, it thrives in places where only the strongest can endure.",
    "A creature of duality, wielding both the power of fire and ice to reshape its surroundings.",
    "A venomous entity of legend, known for bringing ruin to those who seek forbidden knowledge.",
    "A voice in the deep, its song calls to sailors, promising either salvation or doom.",
    "A creature of light, bound by ancient magic, waiting for the day it is freed.",
    "Feared by all, its mere presence warps reality, twisting the ocean into an endless labyrinth.",
    "A ruler of the forgotten, commanding an army of lost souls bound to the depths.",
    "A force of nature, its presence signifies an era of change within the ocean’s domain.",
    "A whisper in the waves, moving unseen through the currents, known only by the trail it leaves behind.",
    "Said to mark the end of civilizations, bringing eternal darkness to the waters it touches.",
    "A counterpart to its dark twin, it revives dying reefs and restores the balance of the deep.",
    "The embodiment of the ocean’s will, existing beyond time, forever watching over its domain.",
    "A titan of the deep, said to be the last remnant of an age when monsters ruled the seas."
]




image00 = pygame.image.load(resource_path('images/bubble.png'))
image00 = pygame.transform.scale(image00, (15, 15))
image01 = pygame.image.load(resource_path('images/bubble.png'))
image01 = pygame.transform.scale(image01, (25, 25))
image02 = pygame.image.load(resource_path('images/bubble.png'))
image02 = pygame.transform.scale(image02, (35, 35))

imagen6 = pygame.image.load(resource_path('images/goldglow.png'))
imagen6 = pygame.transform.scale(imagen6, (100, 100))

imagewhite = pygame.image.load(resource_path('images/blankwhitepage.jpg'))
imagewhitehalo = pygame.image.load(resource_path('images/whiteglowhalo.png'))
imagewhiteground = pygame.image.load(resource_path('images/whitehaloground.png'))
imagewhitecircle = pygame.image.load(resource_path('images/whitehalocircle.png'))

image4 = pygame.image.load(resource_path('images/blackscreen.jpg'))
image4 = pygame.transform.scale(image4, (3920, 1080))
image30 = pygame.image.load(resource_path('images/skipbutton.png'))
image30 = pygame.transform.scale(image30, (90, 50))
image31 = pygame.image.load(resource_path('images/purplerect.png'))
image31 = pygame.transform.scale(image31, (50, 80))
image42 = pygame.image.load(resource_path('images/yellowdiamond.png'))
image42 = pygame.transform.scale(image42, (30, 30))
image52 = pygame.image.load(resource_path('images/knightwalkthrough.png'))
image52 = pygame.transform.scale(image52, (500, 250))
image53 = pygame.image.load(resource_path('images/speechbubble.png'))
image53 = pygame.transform.scale(image53, (500, 230))
image56 = pygame.image.load(resource_path('images/blueglow.png'))
image56 = pygame.transform.scale(image56, (100, 100))

redgloww = pygame.image.load(resource_path('images/redglow2.png'))
redgloww = pygame.transform.scale(redgloww, (100, 100))
#######paimons shop images##############
image58 = pygame.image.load(resource_path('images/paimonshop.webp'))
image58 = pygame.transform.scale(image58, (1550, 870))
image59 = pygame.image.load(resource_path('images/paimonmenushop.png'))
image59 = pygame.transform.scale(image59, (900, 900))
imageBlack = pygame.image.load(resource_path('images/blackscreen.jpg'))
imageBlack = pygame.transform.scale(imageBlack, (765, 700))
imagebackdrop = pygame.image.load(resource_path('images/STASHBACKDROP.jpg'))
imagebackdrop = pygame.transform.scale(imagebackdrop, (765, 700))
image60 = pygame.image.load(resource_path('images/returnarrow.png'))
image60 = pygame.transform.scale(image60, (75, 75))
image61 = pygame.image.load(resource_path('images/whitereturnarrow.png'))
image61 = pygame.transform.scale(image61, (75, 75))
########################################################################################################################
image62 = pygame.image.load(resource_path('images/purplepotion.png'))
image62 = pygame.transform.scale(image62, (50, 50))
image63 = pygame.image.load(resource_path('images/bluepotion.png'))
image63 = pygame.transform.scale(image63, (50, 50))
image64 = pygame.image.load(resource_path('images/greenpotion.png'))
image64 = pygame.transform.scale(image64, (50, 50))
image65 = pygame.image.load(resource_path('images/whitepotion.png'))
image65 = pygame.transform.scale(image65, (50, 50))
image66 = pygame.image.load(resource_path('images/healingpotion.png'))
image66 = pygame.transform.scale(image66, (50, 50))
image67 = pygame.image.load(resource_path('images/apple.png'))
image67 = pygame.transform.scale(image67, (50, 50))
image68 = pygame.image.load(resource_path('images/goldenapple.png'))
image68 = pygame.transform.scale(image68, (50, 50))

image69 = pygame.image.load(resource_path('images/enchantedbook1.png'))
image69 = pygame.transform.scale(image69, (50, 50))
image70 = pygame.image.load(resource_path('images/whiteamulet.png'))
image70 = pygame.transform.scale(image70, (50, 50))
image71 = pygame.image.load(resource_path('images/redamulet.png'))
image71 = pygame.transform.scale(image71, (50, 50))
image72 = pygame.image.load(resource_path('images/purpleamulet.png'))
image72 = pygame.transform.scale(image72, (50, 50))
image73 = pygame.image.load(resource_path('images/underwatercrown.png'))
image73 = pygame.transform.scale(image73, (50, 50))
image74 = pygame.image.load(resource_path('images/mysterybag.png'))
image74 = pygame.transform.scale(image74, (50, 50))
image75 = pygame.image.load(resource_path('images/supermysterybag.png'))
image75 = pygame.transform.scale(image75, (50, 50))

image76 = pygame.image.load(resource_path('images/rustysword.png'))
image76 = pygame.transform.scale(image76, (50, 50))
image77 = pygame.image.load(resource_path('images/bronzesword.png'))
image77 = pygame.transform.scale(image77, (50, 50))
image78 = pygame.image.load(resource_path('images/Ironsword.png'))
image78 = pygame.transform.scale(image78, (50, 50))
image79 = pygame.image.load(resource_path('images/diamondsword.png'))
image79 = pygame.transform.scale(image79, (50, 50))
image80 = pygame.image.load(resource_path('images/simplestaff.png'))
image80 = pygame.transform.scale(image80, (50, 50))
image81 = pygame.image.load(resource_path('images/leatherhelmet.png'))
image81 = pygame.transform.scale(image81, (50, 50))
image82 = pygame.image.load(resource_path('images/leatherchestplate.png'))
image82 = pygame.transform.scale(image82, (50, 50))

imageesneak83 = pygame.image.load(resource_path('images/leatherpants.png'))
imageesneak83 = pygame.transform.scale(imageesneak83, (50, 50))
imageesneak84 = pygame.image.load(resource_path('images/leatherboots.png'))
imageesneak84 = pygame.transform.scale(imageesneak84, (50, 50))
image83 = pygame.image.load(resource_path('images/metalhelmet.png'))
image83 = pygame.transform.scale(image83, (50, 50))
image84 = pygame.image.load(resource_path('images/metalchestplate.png'))
image84 = pygame.transform.scale(image84, (50, 50))
image85 = pygame.image.load(resource_path('images/metalgreeves.png'))
image85 = pygame.transform.scale(image85, (50, 50))
image86 = pygame.image.load(resource_path('images/metalboots.png'))
image86 = pygame.transform.scale(image86, (50, 50))
image87 = pygame.image.load(resource_path('images/coralhelmet.png'))
image87 = pygame.transform.scale(image87, (50, 50))

image88 = pygame.image.load(resource_path('images/coralchestplate.png'))
image88 = pygame.transform.scale(image88, (50, 50))
image89 = pygame.image.load(resource_path('images/coralpants.png'))
image89 = pygame.transform.scale(image89, (50, 50))
image90 = pygame.image.load(resource_path('images/coralshoes.png'))
image90 = pygame.transform.scale(image90, (50, 50))
image91 = pygame.image.load(resource_path('images/expouch.png'))
image91 = pygame.transform.scale(image91, (50, 50))
image92 = pygame.image.load(resource_path('images/largeexppouch.png'))
image92 = pygame.transform.scale(image92, (50, 50))
image93 = pygame.image.load(resource_path('images/timedilator.png'))
image93 = pygame.transform.scale(image93, (50, 50))
########################################################################################################################
image94 = pygame.image.load(resource_path('images/purplepotion.png'))
image94 = pygame.transform.scale(image94, (350, 350))
image95 = pygame.image.load(resource_path('images/enchantedbook1.png'))
image95 = pygame.transform.scale(image95, (350, 350))
image96 = pygame.image.load(resource_path('images/rustysword.png'))
image96 = pygame.transform.scale(image96, (350, 350))
image97 = pygame.image.load(resource_path('images/leatherpants.png'))
image97 = pygame.transform.scale(image97, (350, 350))
image98 = pygame.image.load(resource_path('images/coralchestplate.png'))
image98 = pygame.transform.scale(image98, (350, 350))

image99 = pygame.image.load(resource_path('images/bluepotion.png'))
image99 = pygame.transform.scale(image99, (350, 350))
image100 = pygame.image.load(resource_path('images/whiteamulet.png'))
image100 = pygame.transform.scale(image100, (350, 350))
image101 = pygame.image.load(resource_path('images/bronzesword.png'))
image101 = pygame.transform.scale(image101, (350, 350))
image102 = pygame.image.load(resource_path('images/leatherboots.png'))
image102 = pygame.transform.scale(image102, (350, 350))
image103 = pygame.image.load(resource_path('images/coralpants.png'))
image103 = pygame.transform.scale(image103, (350, 350))

image104 = pygame.image.load(resource_path('images/greenpotion.png'))
image104 = pygame.transform.scale(image104, (350, 350))
image105 = pygame.image.load(resource_path('images/redamulet.png'))
image105 = pygame.transform.scale(image105, (350, 350))
image106 = pygame.image.load(resource_path('images/Ironsword.png'))
image106 = pygame.transform.scale(image106, (350, 350))
image107 = pygame.image.load(resource_path('images/metalhelmet.png'))
image107 = pygame.transform.scale(image107, (350, 350))
image108 = pygame.image.load(resource_path('images/coralshoes.png'))
image108 = pygame.transform.scale(image108, (350, 350))

image109 = pygame.image.load(resource_path('images/whitepotion.png'))
image109 = pygame.transform.scale(image109, (350, 350))
image110 = pygame.image.load(resource_path('images/purpleamulet.png'))
image110 = pygame.transform.scale(image110, (350, 350))
image111 = pygame.image.load(resource_path('images/diamondsword.png'))
image111 = pygame.transform.scale(image111, (350, 350))
image112 = pygame.image.load(resource_path('images/metalchestplate.png'))
image112 = pygame.transform.scale(image112, (350, 350))
image113 = pygame.image.load(resource_path('images/expouch.png'))
image113 = pygame.transform.scale(image113, (350, 350))

image114 = pygame.image.load(resource_path('images/healingpotion.png'))
image114 = pygame.transform.scale(image114, (350, 350))
image115 = pygame.image.load(resource_path('images/underwatercrown.png'))
image115 = pygame.transform.scale(image115, (350, 350))
image116 = pygame.image.load(resource_path('images/simplestaff.png'))
image116 = pygame.transform.scale(image116, (350, 350))
image117 = pygame.image.load(resource_path('images/metalgreeves.png'))
image117 = pygame.transform.scale(image117, (350, 350))
image118 = pygame.image.load(resource_path('images/largeexppouch.png'))
image118 = pygame.transform.scale(image118, (350, 350))

image119 = pygame.image.load(resource_path('images/apple.png'))
image119 = pygame.transform.scale(image119, (350, 350))
image120 = pygame.image.load(resource_path('images/mysterybag.png'))
image120 = pygame.transform.scale(image120, (350, 350))
image121 = pygame.image.load(resource_path('images/leatherhelmet.png'))
image121 = pygame.transform.scale(image121, (350, 350))
image122 = pygame.image.load(resource_path('images/metalboots.png'))
image122 = pygame.transform.scale(image122, (350, 350))
image123 = pygame.image.load(resource_path('images/timedilator.png'))
image123 = pygame.transform.scale(image123, (350, 350))

image124 = pygame.image.load(resource_path('images/goldenapple.png'))
image124 = pygame.transform.scale(image124, (350, 350))
image125 = pygame.image.load(resource_path('images/supermysterybag.png'))
image125 = pygame.transform.scale(image125, (350, 350))
image126 = pygame.image.load(resource_path('images/leatherchestplate.png'))
image126 = pygame.transform.scale(image126, (350, 350))
image127 = pygame.image.load(resource_path('images/coralhelmet.png'))
image127 = pygame.transform.scale(image127, (350, 350))

########################################################################################################################
image128 = pygame.image.load(resource_path('images/stars.png'))
image128 = pygame.transform.scale(image128, ((770, 740)))
image129 = pygame.image.load(resource_path('images/itemframe.png'))
image129 = pygame.transform.scale(image129, ((950, 1150)))
image130 = pygame.image.load(resource_path('images/buybutton.png'))
image130 = pygame.transform.scale(image130, ((300, 300)))
image131 = pygame.image.load(resource_path('images/glowbuybutton.png'))
image131 = pygame.transform.scale(image131, ((300, 300)))
imageBlack2 = pygame.image.load(resource_path('images/blackscreen.jpg'))
imageBlack2 = pygame.transform.scale(imageBlack2, (275, 85))


image132 = pygame.image.load(resource_path('images/mainmap.JPG'))
image132 = pygame.transform.scale(image132, (1550, 870))
image0133 = pygame.image.load(resource_path('images/workmap.jpg'))
image0133 = pygame.transform.scale(image0133, (1550, 870))
image0134 = pygame.image.load(resource_path('images/gamblemap.jpg'))
image0134 = pygame.transform.scale(image0134, (1550, 870))
image0135 = pygame.image.load(resource_path('images/paimonmap.jpg'))
image0135 = pygame.transform.scale(image0135, (1550, 870))
image0136 = pygame.image.load(resource_path('images/castlemap.jpg'))
image0136 = pygame.transform.scale(image0136, (1550, 870))
image0137 = pygame.image.load(resource_path('images/colleseummap.jpg'))
image0137 = pygame.transform.scale(image0137, (1550, 870))
image0138 = pygame.image.load(resource_path('images/adventuremap.jpg'))
image0138 = pygame.transform.scale(image0138, (1550, 870))
image0139 = pygame.image.load(resource_path('images/guildmap.jpg'))
image0139 = pygame.transform.scale(image0139, (1550, 870))
image0140 = pygame.image.load(resource_path('images/stashmap.jpg'))
image0140 = pygame.transform.scale(image0140, (1550, 870))
image0141 = pygame.image.load(resource_path('images/blackmarketmap.jpg'))
image0141 = pygame.transform.scale(image0141, (1550, 870))


image133 = pygame.image.load(resource_path('images/greenglow.png'))
image133 = pygame.transform.scale(image133, (80, 80))
imagee133 = pygame.image.load(resource_path('images/redglow.png'))
imagee133 = pygame.transform.scale(imagee133, (80, 80))
image134 = pygame.image.load(resource_path('images/returnbutton.png'))
image134 = pygame.transform.scale(image134, (125, 125))
image135 = pygame.image.load(resource_path('images/returnbutton2.png'))
image135 = pygame.transform.scale(image135, (125, 125))
image136 = pygame.image.load(resource_path('images/returnbutton2.png'))
image136 = pygame.transform.scale(image136, (250, 250))
########################################################################################################################
image137 = pygame.image.load(resource_path('images/goblin.jpg'))
image137 = pygame.transform.scale(image137, (1550, 870))
image138 = pygame.image.load(resource_path('images/laborchoices.png'))
image138 = pygame.transform.scale(image138, (800, 600))
image139 = pygame.image.load(resource_path('images/redx.png'))
image139 = pygame.transform.scale(image139, (400, 100))
image140 = pygame.image.load(resource_path('images/laborchoiceshover1.png'))
image140 = pygame.transform.scale(image140, (800, 600))
image141 = pygame.image.load(resource_path('images/mininggameworld.jpg'))
image142 = pygame.image.load(resource_path('images/betacharacter.png'))
image142 = pygame.transform.scale(image142, (50, 50))
image143 = pygame.image.load(resource_path('images/lightbluegem.png'))
image144 = pygame.image.load(resource_path('images/pinkgem.png'))
image145 = pygame.image.load(resource_path('images/rubygem.png'))
image146 = pygame.image.load(resource_path('images/heartgem.png'))
image147 = pygame.image.load(resource_path('images/diamondgem.png'))
image148 = pygame.image.load(resource_path('images/purplegem.png'))
image149 = pygame.image.load(resource_path('images/darkbluegem.png'))
image150 = pygame.image.load(resource_path('images/miningworldgame2.jpg'))
image151 = pygame.image.load(resource_path('images/dighole.png'))
image151 = pygame.transform.scale(image151, (60, 60))
image152 = pygame.image.load(resource_path('images/digholereturnarro.png'))
image152 = pygame.transform.scale(image152, (60, 60))
image153 = pygame.image.load(resource_path('images/digholereturnarrow.png'))
image153 = pygame.transform.scale(image153, (60, 60))
image154 = pygame.image.load(resource_path('images/trilobite.png'))
image155 = pygame.image.load(resource_path('images/gems.png'))
image156 = pygame.image.load(resource_path('images/dinosaurbones.png'))
image157 = pygame.image.load(resource_path('images/crown.png'))
image158 = pygame.image.load(resource_path('images/spider.png'))
image159 = pygame.image.load(resource_path('images/egg.png'))
image160 = pygame.image.load(resource_path('images/digchest1.png'))
image161 = pygame.image.load(resource_path('images/digchest2.png'))
image162 = pygame.image.load(resource_path('images/digchest3.png'))
image163 = pygame.image.load(resource_path('images/digchest4.png'))
image164 = pygame.image.load(resource_path('images/invertreturnsign.png'))
image164 = pygame.transform.scale(image164, (60, 60))
image165 = pygame.image.load(resource_path('images/invertreturnsignpurple.png'))
image165 = pygame.transform.scale(image165, (60, 60))
image166 = pygame.image.load(resource_path('images/lava1.png'))
image167 = pygame.image.load(resource_path('images/lava2.png'))
image168 = pygame.image.load(resource_path('images/miningstatsimage1.png'))
image169 = pygame.image.load(resource_path('images/miningstatsimage2.png'))
image170 = pygame.image.load(resource_path('images/digginggameupgradescreen.png'))
image171 = pygame.image.load(resource_path('images/statfilledbox.jpg'))
########################################################################################################################
image172 = pygame.image.load(resource_path('images/casinoimage1.webp'))
image172 = pygame.transform.scale(image172, (1550, 870))
image173 = pygame.image.load(resource_path('images/gamblingchoices.webp'))
image173 = pygame.transform.scale(image173, (800, 800))
image174 = pygame.image.load(resource_path('images/roulette1.jpg'))
image174 = pygame.transform.scale(image174, (1550, 870))
image175 = pygame.image.load(resource_path('images/reddownarrow.png'))
image176 = pygame.image.load(resource_path('images/slotsimage.webp'))
image176 = pygame.transform.scale(image176, (1550, 870))
image177 = pygame.image.load(resource_path('images/slotimage.png'))
image178 = pygame.image.load(resource_path('images/slotimage2.png'))
image179 = pygame.image.load(resource_path('images/slotimage3.png'))
image180 = pygame.image.load(resource_path('images/goldbackground.jpg'))

image181 = pygame.image.load(resource_path('images/slotnum1.jpg'))
image182 = pygame.image.load(resource_path('images/slotnum2.jpg'))
image183 = pygame.image.load(resource_path('images/slotnum3.jpg'))
image184 = pygame.image.load(resource_path('images/slotnum4.jpg'))
image185 = pygame.image.load(resource_path('images/slotnum5.jpg'))
image186 = pygame.image.load(resource_path('images/slotnum6.jpg'))
image187 = pygame.image.load(resource_path('images/slotnum7.jpg'))
image188 = pygame.image.load(resource_path('images/slotnum8.jpg'))
image189 = pygame.image.load(resource_path('images/slotnum9.jpg'))

image190 = pygame.image.load(resource_path('images/slotimage4.png'))

image191 = pygame.image.load(resource_path('images/diceimage.jpg'))
image191 = pygame.transform.scale(image191, (1550, 870))

image192 = pygame.image.load(resource_path('images/dice1.jpg'))
image192 = pygame.transform.scale(image192, (320, 320))
image193 = pygame.image.load(resource_path('images/dice2.jpg'))
image193 = pygame.transform.scale(image193, (320, 320))
image194 = pygame.image.load(resource_path('images/dice3.jpg'))
image194 = pygame.transform.scale(image194, (320, 320))
image195 = pygame.image.load(resource_path('images/dice4.jpg'))
image195 = pygame.transform.scale(image195, (320, 320))
image196 = pygame.image.load(resource_path('images/dice5.jpg'))
image196 = pygame.transform.scale(image196, (320, 320))
image197 = pygame.image.load(resource_path('images/dice6.jpg'))
image197 = pygame.transform.scale(image197, (320, 320))
image198 = pygame.image.load(resource_path('images/dice7.png'))
image198 = pygame.transform.scale(image198, (320, 320))

image199 = pygame.image.load(resource_path('images/bluebakcground.jpg'))

image201 = pygame.transform.scale(image192, (150, 150))
image202 = pygame.transform.scale(image193, (150, 150))
image203 = pygame.transform.scale(image194, (150, 150))
image204 = pygame.transform.scale(image195, (150, 150))
image205 = pygame.transform.scale(image196, (150, 150))
image206 = pygame.transform.scale(image197, (150, 150))

image207 = pygame.image.load(resource_path('images/guildroom.png'))
image207 = pygame.transform.scale(image207, (1550, 870))
image208 = pygame.image.load(resource_path('images/questboard.jpg'))
image208 = pygame.transform.scale(image208, (1550, 870))
image209 = pygame.image.load(resource_path('images/alchemyroom.jpg'))
image209 = pygame.transform.scale(image209, (1550, 870))

image210 = pygame.image.load(resource_path('images/cauldron.png'))
image211 = pygame.image.load(resource_path('images/stopbutton.png'))
image212 = pygame.image.load(resource_path('images/glowstopbutton.png'))
image213 = pygame.image.load(resource_path('images/meterimage.jpg'))
image214 = pygame.image.load(resource_path('images/meterline.png'))

image215 = pygame.image.load(resource_path('images/pot1.png'))
image216 = pygame.image.load(resource_path('images/pot2.png'))
image217 = pygame.image.load(resource_path('images/pot3.png'))
image218 = pygame.image.load(resource_path('images/pot4.png'))
image219 = pygame.image.load(resource_path('images/pot5.png'))

image220 = pygame.image.load(resource_path('images/goldlabel.png'))
image221 = pygame.image.load(resource_path('images/lvllabel.png'))
image222 = pygame.image.load(resource_path('images/gemlabel.png'))

image223 = pygame.image.load(resource_path('images/cauldronstars.png'))
image224 = pygame.image.load(resource_path('images/sunlight.png'))

image225 = pygame.image.load(resource_path('images/chestopened.png'))
image226 = pygame.image.load(resource_path('images/chestclosed.png'))
########################################################################################################################
image227 = pygame.image.load(resource_path('images/bluechip.png'))
image228 = pygame.image.load(resource_path('images/redchip.png'))
image229 = pygame.image.load(resource_path('images/blackchip.png'))
image230 = pygame.image.load(resource_path('images/allchip.png'))
image231 = pygame.image.load(resource_path('images/goldchip.png'))

image232 = pygame.image.load(resource_path('images/pokertable.webp'))
image232 = pygame.transform.scale(image232, (1550, 870))

image233 = pygame.image.load(resource_path('images/outlinechipblue.png'))
image234 = pygame.image.load(resource_path('images/outlinechipred.png'))
image235 = pygame.image.load(resource_path('images/outlinechipblack.png'))
image236 = pygame.image.load(resource_path('images/outlinechipall.png'))
image237 = pygame.image.load(resource_path('images/outlinechipgold.png'))

image238 = pygame.image.load(resource_path('images/hearts.png'))
image239 = pygame.image.load(resource_path('images/diamonds.png'))
image240 = pygame.image.load(resource_path('images/spades.png'))
image241 = pygame.image.load(resource_path('images/clovers.png'))
image242 = pygame.image.load(resource_path('images/facedowncard.png'))

image243 = pygame.image.load(resource_path('images/blackmarketbyron.jpg'))
image243 = pygame.transform.scale(image243, (1550, 870))
image244 = pygame.image.load(resource_path('images/blackmarketloot.webp'))
image244 = pygame.transform.scale(image244, (1550, 870))

image245 = pygame.image.load(resource_path('images/arrowleft.png'))
image246 = pygame.image.load(resource_path('images/arrowright.png'))

image247 = pygame.image.load(resource_path('images/woodchest.png'))
image248 = pygame.image.load(resource_path('images/diamondchest.png'))
image249 = pygame.image.load(resource_path('images/emeraldchest.png'))
image250 = pygame.image.load(resource_path('images/blackdoor.png'))
image251 = pygame.image.load(resource_path('images/redarrowleft.png'))
image252 = pygame.image.load(resource_path('images/redarrowright.png'))

image253 = pygame.image.load(resource_path('images/glowwoodentreasurechest.png'))
image254 = pygame.image.load(resource_path('images/glowdiamondtreasurechest.png'))
image255 = pygame.image.load(resource_path('images/glowemeraldtreasurechest.png'))
image256 = pygame.image.load(resource_path('images/glowblackdoor.png'))

image257 = pygame.image.load(resource_path('images/bat.png'))
image258 = pygame.image.load(resource_path('images/ant.png'))
image259 = pygame.image.load(resource_path('images/snake.png'))
image260 = pygame.image.load(resource_path('images/dino.png'))
image261 = pygame.image.load(resource_path('images/boulder.png'))

image262 = pygame.image.load(resource_path('images/vault.jpg'))
image262 = pygame.transform.scale(image262, (1550, 870))
image263 = pygame.image.load(resource_path('images/seaofstars.webp'))
image263 = pygame.transform.scale(image263, (1550, 870))

image264 = pygame.image.load(resource_path('images/stashchoose.jpg'))
image264 = pygame.transform.scale(image264, (1550, 870))

image266 = pygame.image.load(resource_path('images/stashwindow2.png'))
image267 = pygame.image.load(resource_path('images/stashwindow.png'))
########################################################################################################################
image268 = pygame.image.load(resource_path('images/battleground1.jpg'))
image268 = pygame.transform.scale(image268, (1550, 870))
image269 = pygame.image.load(resource_path('images/battleground2.jpg'))
image269 = pygame.transform.scale(image269, (1550, 870))
image270 = pygame.image.load(resource_path('images/battleground3.jpg'))
image270 = pygame.transform.scale(image270, (1550, 870))
image271 = pygame.image.load(resource_path('images/battleground4.jpg'))
image271 = pygame.transform.scale(image271, (1550, 870))
image272 = pygame.image.load(resource_path('images/battleground5.jpg'))
image272= pygame.transform.scale(image272, (1550, 870))
image273 = pygame.image.load(resource_path('images/battleground6.jpg'))
image273 = pygame.transform.scale(image273, (1550, 870))
image274 = pygame.image.load(resource_path('images/battleground7.jpg'))
image274 = pygame.transform.scale(image274, (1550, 870))

image275 = pygame.image.load(resource_path('images/colleseumstartimage.jpg'))
image275 = pygame.transform.scale(image275, (1550, 870))

image276 = pygame.image.load(resource_path('images/colleseummenu.png'))
#image276 = pygame.transform.scale(image276, (1550, 870))

image277 = pygame.image.load(resource_path('images/colleseummenu1.png'))
#image277 = pygame.transform.scale(image277, (1550, 870))

image278 = pygame.image.load(resource_path('images/colleseummenu2.jpg'))
#image278 = pygame.transform.scale(image278, (1550, 870))

image279 = pygame.image.load(resource_path('images/colleseummenu3.jpg'))
#image279 = pygame.transform.scale(image279, (1550, 870))

image280 = pygame.image.load(resource_path('images/entercolleseum.webp'))
image280 = pygame.transform.scale(image280, (1550, 870))
########################################################################################################################
displaylength = 1920
displaywidth = 1080
halfdisplay = displaylength / 2
DISPLAYSURF = pygame.display.set_mode((1920, 1080))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
font = pygame.font.SysFont(None, 75)
font2 = pygame.font.SysFont("Arial", 60)
font3 = pygame.font.SysFont("Times New Roman", 40)
font4 = pygame.font.SysFont("Comic Sans", 40)
font5 = pygame.font.SysFont("Comic Sans", 20)
font6 = pygame.font.Font(resource_path("fonts/Danger.otf"), 25)
font7 = pygame.font.Font(resource_path("fonts/eroded.ttf"), 20)
font8 = pygame.font.Font(resource_path("fonts/HelpMe.ttf"), 20)
font9 = pygame.font.Font(resource_path("fonts/Overwave.otf"), 20)
font10 = pygame.font.Font(resource_path("fonts/Comfy.otf"), 22)
font11 = pygame.font.Font(resource_path("fonts/anime.otf"), 15)
font12 = pygame.font.Font(resource_path("fonts/oldenFont.otf"), 50)
font13 = pygame.font.Font(resource_path("fonts/SwordsmanFont.TTF"), 20)
font14 = pygame.font.Font(resource_path("fonts/AsianFont.ttf"), 20)
font15 = pygame.font.Font(resource_path("fonts/womenfont.ttf"), 20)
font16 = pygame.font.Font(resource_path("fonts/runefont.otf"), 20)
font17 = pygame.font.Font(resource_path("fonts/dragonfont.ttf"), 20)
font18 = pygame.font.Font(resource_path("fonts/oldenFont.otf"), 70)
font19 = pygame.font.Font(resource_path("fonts/Danger.otf"), 100)
font20 = pygame.font.Font(resource_path("fonts/AsianFont.ttf"), 60)
font21 = pygame.font.SysFont("Comic Sans", 16)
font22 = pygame.font.Font(resource_path("fonts/AsianFont.ttf"), 50)
font23 = pygame.font.Font(resource_path("fonts/oldenFont.otf"), 35)
font24 = pygame.font.Font(resource_path("fonts/AsianFont.ttf"), 40)
font25 = pygame.font.SysFont("Comic Sans", 30)
font26 = pygame.font.Font(resource_path("fonts/AsianFont.ttf"), 30)
font27 = pygame.font.Font(resource_path("fonts/Comfy.otf"), 15)

gameStatus = True
########################################################################################################################
def draw_text(text, font, color, surface, x, y, alpha=255):
    textobj = font.render(text, True, color)  # Render the text
    textobj.set_alpha(alpha)  # Set the alpha for transparency
    textrect = textobj.get_rect()  # Create a rectangle for the text
    textrect.topleft = (x, y)  # Set the position of the text
    surface.blit(textobj, textrect)  # Blit the text surface onto the display surface
########################################################################################################################
def draw_text_center(text, font, color, surface, x, y, alpha=255):
    textobj = font.render(text, True, color)  # Render the text
    textobj.set_alpha(alpha)  # Set the alpha for transparency
    textrect = textobj.get_rect()  # Create a rectangle for the text
    textrect.midtop = (x, y)  # Center the rectangle at the specified position
    surface.blit(textobj, textrect)  # Blit the text surface onto the display surfac
########################################################################################################################
def transition(speed):
    transitionbool = True
    transitioncounter = 1
    while (transitionbool == True):
        transitioncounter = transitioncounter + speed
        image4.set_alpha(transitioncounter)
        DISPLAYSURF.blit(image4, (0, 0))
        pygame.display.update()
        if (transitioncounter >= 240):
            transitionbool = False
            transitioncounter = 1
########################################################################################################################
def save_creature(creature_data, filename="creaturedata.txt"):
    try:
        with open(resource_path(filename), "r")as file:
            data = json.load(file)  # Load existing data
    except (FileNotFoundError, json.JSONDecodeError):
        data = []  # If file doesn't exist or is empty, start with an empty list

    data.append(creature_data)  # Add new creature data

    with open(resource_path(filename), "w") as file:
        json.dump(data, file, indent=4)  # Save updated data
########################################################################################################################
def load_creatures(filename="creaturedata.txt"):
    try:
        with open(resource_path(filename), "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Return empty list if file doesn't exist or is empty

    #creatures = load_creatures()
    #print(creatures)  # Displays the list of saved creatures
########################################################################################################################
def modify_creature(index, new_attributes, filename="creaturedata.txt"):
    try:
        with open(resource_path(filename), "r") as file:
            creatures = json.load(file)  # Load existing creatures
    except (FileNotFoundError, json.JSONDecodeError):
        print("No creatures found.")
        return

    if index < 0 or index >= len(creatures):  # Check if index is valid
        print(f"Invalid index: {index}. No creature modified.")
        return

    creatures[index].update(new_attributes)  # Modify attributes



    with open(resource_path(filename), "w") as file:
        json.dump(creatures, file, indent=4)  # Save changes

    print(f"Creature '{creatures[index][0]}' updated successfully!")
# modify_creature(index, {"health": 120, "attack": 25})  # Updates Dragon's health and attack
########################################################################################################################
def delete_creature_by_index(index, filename="creaturedata.txt"):
    try:
        with open(resource_path(filename), "r") as file:
            creatures = json.load(file)  # Load existing creatures
    except (FileNotFoundError, json.JSONDecodeError):
        print("No creatures found.")
        return

    if index < 0 or index >= len(creatures):  # Check if index is valid
        print(f"Invalid index: {index}. No creature deleted.")
        return

    deleted_creature = creatures.pop(index)  # Remove the creature at the index

    with open(resource_path(filename), "w") as file:
        json.dump(creatures, file, indent=4)  # Save updated list

    print(f"Creature at index {index} ('{deleted_creature.get('name', 'Unknown')}') deleted successfully!")
# delete_creature_by_index(2)  # Deletes the third creature (index 2)
########################################################################################################################
def load_teamcreatures(filename="teamdata.txt"):
    try:
        with open(resource_path(filename), "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Return empty list if file doesn't exist or is empty

    #creatures = load_creatures()
    #print(creatures)  # Displays the list of saved creatures
########################################################################################################################
def modify_teamcreature(index, new_attributes, filename="teamdata.txt"):
    try:
        with open(resource_path(filename), "r") as file:
            creatures = json.load(file)  # Load existing creatures
    except (FileNotFoundError, json.JSONDecodeError):
        print("No creatures found.")
        return

    if index < 0 or index >= len(creatures):  # Check if index is valid
        print(f"Invalid index: {index}. No creature modified.")
        return

    creatures[index].update(new_attributes)  # Modify attributes



    with open(resource_path(filename), "w") as file:
        json.dump(creatures, file, indent=4)  # Save changes

    print(f"Creature updated successfully!")
# modify_creature(index, {"health": 120, "attack": 25})  # Updates Dragon's health and attack
########################################################################################################################
def save_teamcreature(creature_data, filename="teamdata.txt"):
    try:
        with open(resource_path(filename), "r") as file:
            data = json.load(file)  # Load existing data
    except (FileNotFoundError, json.JSONDecodeError):
        data = []  # If file doesn't exist or is empty, start with an empty list

    data.append(creature_data)  # Add new creature data

    with open(resource_path(filename), "w") as file:
        json.dump(data, file, indent=4)  # Save updated data
########################################################################################################################
def empty_item(index, filename="equipeditems.txt"):
    try:
        with open(resource_path(filename), "r") as file:
            items = json.load(file)  # Load existing creatures
    except (FileNotFoundError, json.JSONDecodeError):
        print("No creatures found.")
        return

    if index < 0 or index >= len(items):  # Check if index is valid
        print(f"Invalid index: {index}. No creature modified.")
        return

    items[index].clear()  # Modify attributes



    with open(resource_path(filename), "w") as file:
        json.dump(items, file, indent=4)  # Save changes

    print(f"item cleared!")
########################################################################################################################
def moveprint(movestatus, target = "opponent"):
    movereturn = " "
    if(target == "opponent"):
        if(movestatus == "userdeath"):
            movereturn = "Forbidden moves are not to be taken lightly. The user instantly dies upon use."
        if(movestatus == "fire"):
            movereturn = "Small chance of setting opponent on fire."
        if(movestatus == "fire2"):
            movereturn = "High chance of setting opponent on fire and being a Arsonist."
        if(movestatus == "heal1"):
            movereturn = "A lesser heal. Rejuvenates 25% hp"
        if(movestatus == "heal2"):
            movereturn = "A greater heal. Rejuvenates 50% hp"
        if(movestatus == "poison"):
            movereturn = "Small chance of poisoning the opponent."
        if(movestatus == "poison2"):
            movereturn = "Great chance of poisoning the opponent."
        if(movestatus == "riptide"):
            movereturn = "Small chance of your opponent getting caught in a riptide"
        if(movestatus == "riptide2"):
            movereturn = "Highly likely your opponent getting caught in a riptide"
        if(movestatus == "freeze"):
            movereturn = "Small chance of perma-freezing your opponent"
        if(movestatus == "freeze2"):
            movereturn = "High chance of perma-freezing your opponent"
        if(movestatus == "paralyze"):
            movereturn = "Medium chance of paralyzing your opponent"
        if(movestatus == "paralyze2"):
            movereturn = "High chance of paralyzing your opponent"
        if(movestatus == "bloom"):
            movereturn = "Small chance of infecting your opponent with bloom."
        if(movestatus == "bloom2"):
            movereturn = "High chance of infecting your opponent with bloom."
        if(movestatus == "gravity"):
            movereturn = "Small chance of your opponent getting stuck in a gravity field"
        if(movestatus == "gravity2"):
            movereturn = "High chance of your opponent getting stuck in a gravity field"

        if(movestatus == "accuracy+1"):
            movereturn = "Slightly increases your opponents Accuracy"
        if(movestatus == "accuracy+2"):
            movereturn = "Drastically increases your opponents Accuracy"
        if(movestatus == "accuracy-1"):
            movereturn = "Decreases your opponents Accuracy"
        if(movestatus == "accuracy-2"):
            movereturn = "Drastically decreases your opponents Accuracy"

        if(movestatus == "speed+1"):
            movereturn = "slightly increases your opponents Speed"
        if(movestatus == "speed+2"):
            movereturn = "Sharply increases your opponents Speed"
        if(movestatus == "attack+1"):
            movereturn = "slightly increases your opponents Attack Stat"
        if(movestatus == "attack+2"):
            movereturn = "Sharply increases your foes Attack"
        if(movestatus == "specattack+1"):
            movereturn = "slightly increases your foes Special Attack Stat"
        if(movestatus == "specattack+2"):
            movereturn = "Sharply increases your foes Special Attack"
        if(movestatus == "defense+1"):
            movereturn = "slightly increases your foes Defense Stat"
        if(movestatus == "defense+2"):
            movereturn = "Sharply increases your foes Defense"
        if(movestatus == "speed-1"):
            movereturn = "decreases your rivals Speed Stat"
        if(movestatus == "speed-2"):
            movereturn = "Harshly decreases your rivals Speed"
        if(movestatus == "attack-1"):
            movereturn = "decreases your rivals Attack Stat"
        if(movestatus == "attack-2"):
            movereturn = "Harshly decreases your rivals Attack"
        if(movestatus == "specattack-1"):
            movereturn = "decreases your rivals Special Attack Stat"
        if(movestatus == "specattack-2"):
            movereturn = "Harshly decreases your rivals Special Attack"
        if(movestatus == "defense-1"):
            movereturn = "decreases your rivals defense stat"
        if(movestatus == "defense-2"):
            movereturn = "Harshly decreases your rivals Defense"

    if (target == "self"):
        if (movestatus == "userdeath"):
            movereturn = "Forbidden moves are not to be taken lightly. The user instantly dies upon use."
        if (movestatus == "fire"):
            movereturn = "Small chance of setting yourself on fire."
        if (movestatus == "fire2"):
            movereturn = "High chance of setting yourself on fire dying."
        if (movestatus == "heal1"):
            movereturn = "A lesser heal. Rejuvenates 25% hp"
        if (movestatus == "heal2"):
            movereturn = "A greater heal. Rejuvenates 50% hp"
        if (movestatus == "poison"):
            movereturn = "Small chance of poisoning yourself."
        if (movestatus == "poison2"):
            movereturn = "Great chance of poisoning yourself."
        if (movestatus == "riptide"):
            movereturn = "Small chance of getting yourself caught in a riptide"
        if (movestatus == "riptide2"):
            movereturn = "Highly likely you will get yourself caught in a riptide"
        if (movestatus == "freeze"):
            movereturn = "Small chance of becoming perma-frozen"
        if (movestatus == "freeze2"):
            movereturn = "High chance of becoming perma-frozen"
        if (movestatus == "paralyze"):
            movereturn = "Medium chance of being paralyzed"
        if (movestatus == "paralyze2"):
            movereturn = "High chance of being paralyzed"
        if (movestatus == "bloom"):
            movereturn = "Small chance of getting infected with bloom"
        if (movestatus == "bloom2"):
            movereturn = "High chance of getting infected with bloom"
        if (movestatus == "gravity"):
            movereturn = "Small chance of gettin stuck in a gravity field"
        if (movestatus == "gravity2"):
            movereturn = "High chance of gettin stuck in a gravity field"

        if (movestatus == "accuracy+1"):
            movereturn = "Slightly increases your Accuracy"
        if (movestatus == "accuracy+2"):
            movereturn = "Drastically increases your Accuracy"
        if (movestatus == "accuracy-1"):
            movereturn = "Decreases your Accuracy"
        if (movestatus == "accuracy-2"):
            movereturn = "Drastically decreases your Accuracy"

        if (movestatus == "speed+1"):
            movereturn = "slightly increases your Speed"
        if (movestatus == "speed+2"):
            movereturn = "Sharply increases your Speed"
        if (movestatus == "attack+1"):
            movereturn = "slightly increases your Attack Stat"
        if (movestatus == "attack+2"):
            movereturn = "Sharply increases your Attack"
        if (movestatus == "specattack+1"):
            movereturn = "slightly increases your Special Attack Stat"
        if (movestatus == "specattack+2"):
            movereturn = "Sharply increases your Special Attack"
        if (movestatus == "defense+1"):
            movereturn = "slightly increases your Defense Stat"
        if (movestatus == "defense+2"):
            movereturn = "Sharply increases your Defense"
        if (movestatus == "speed-1"):
            movereturn = "decreases your Speed Stat"
        if (movestatus == "speed-2"):
            movereturn = "Harshly decreases your Speed"
        if (movestatus == "attack-1"):
            movereturn = "decreases your Attack Stat"
        if (movestatus == "attack-2"):
            movereturn = "Harshly decreases your Attack"
        if (movestatus == "specattack-1"):
            movereturn = "decreases your Special Attack Stat"
        if (movestatus == "specattack-2"):
            movereturn = "Harshly decreases your Special Attack"
        if (movestatus == "defense-1"):
            movereturn = "decreases your defense stat"
        if (movestatus == "defense-2"):
            movereturn = "Harshly decreases your creatures Defense"



    if(movereturn == " "):
        print("failed to capture move effect!")
        print(movestatus)
        print("failed to capture move effect!")

    return movereturn
########################################################################################################################
class maingameareas(pygame.sprite.Sprite):
    def __init__(self, inputvalue=""):
        super().__init__()
        self.inputvalue = inputvalue

        if self.inputvalue == "mainscreen":
            self.mainscreen()
########################################################################################################################
    def mainscreen(self):
        global gold
        global gem
        global level
        starx = random.randint(200,1500)
        stary = random.randint(00,1100)
        starfader = 1
        starbool = True
        chestcollected = 0
        randomgold = 0
        randomgem = 0
        random2 = 0
        chestbool = 0
        pygame.mixer.music.load(resource_path("audio/fantasyhomemusic.mp3"))
        pygame.mixer.music.queue(resource_path("audio/fantasyhomemusic2.mp3"))
        pygame.mixer.music.play(-1)
        mainloop = True
        video = cv2.VideoCapture(resource_path("video/underwater.mp4"))

        bubbles = 800
        bubblex = []
        bubbley = []
        bubblechooser = []
        while(bubbles != 0):
            bubblex.append(random.randint(1, 2000))
            bubbley.append((bubbles * 100) + (random.randint(1, 12000)))
            bubblechooser.append(random.randint(0, 2))
            bubbles = bubbles - 1

        while(mainloop):
            with open(resource_path("gamedata.txt"), "r") as file:
                lines = file.readlines()
                goldline = lines[0].strip()
                goldline = goldline[7:]
                gemline = lines[1].strip()
                gemline = gemline[6:]
                level = lines[15].strip()
                level = level[8:]
                level = int(level)
                gem = int(gemline)
                gold = int(goldline)

            startTime = pygame.time.get_ticks()
            rainbowcolor1 = int((math.sin(startTime * 0.002) + 1) * 127.5)
            rainbowcolor2 = int((math.sin(startTime * 0.003 + 2) + 1) * 127.5)
            rainbowcolor3 = int((math.sin(startTime * 0.004 + 2) + 1) * 127.5)

            mouseX, mouseY = pygame.mouse.get_pos()
            mouse_pos = pygame.mouse.get_pos()
            global textFader
            DISPLAYSURF.fill(BLACK)
            image4.set_alpha(textFader)
            DISPLAYSURF.blit(image132, (195, 100))

            paimonrect = pygame.Rect(1300, 420, 270, 130)
            labormarketrect = pygame.Rect(1300, 690, 310, 210)
            gamblingdenrect = pygame.Rect(1400, 555, 150, 130)
            castlerect = pygame.Rect(889, 465, 140, 130)
            colesseumrect = pygame.Rect(889, 630, 140, 130)
            guildrect = pygame.Rect(640, 560, 90, 100)
            stashrect = pygame.Rect(470, 690, 310, 230)
            blackmarketrect = pygame.Rect(250, 588, 160, 140)
            adventurerect = pygame.Rect(690, 130, 180, 270)

            rainbow = (rainbowcolor1,rainbowcolor2,rainbowcolor3)

            draw_text("Paimons Shop", font13, PINPPINK, DISPLAYSURF, 1340, 415)
            draw_text("Labor Market", font13, RED, DISPLAYSURF, 1340, 735)
            draw_text("Gambling Den", font13, LIGHTYELLOW, DISPLAYSURF, 1415, 547)
            draw_text("Guild Hall", font13, SKYBLUE, DISPLAYSURF, 630, 550)
            draw_text("Black Market", font13, PURPLE, DISPLAYSURF, 250, 575)
            draw_text("Stash", font13, PINK, DISPLAYSURF, 570, 685)
            draw_text_center("Colleseum", font13, AQUA, DISPLAYSURF, 960, 620)

            if paimonrect.collidepoint(mouse_pos):
                DISPLAYSURF.blit(image0135, (195, 100))
                draw_text("Paimons Shop", font13, rainbow, DISPLAYSURF, 1340, 415)
            if labormarketrect.collidepoint(mouse_pos):
                DISPLAYSURF.blit(image0133, (195, 100))
                draw_text("Labor Market", font13, rainbow, DISPLAYSURF, 1340, 735)
            if gamblingdenrect.collidepoint(mouse_pos):
                DISPLAYSURF.blit(image0134, (195, 100))
                draw_text("Gambling Den", font13, rainbow, DISPLAYSURF, 1415, 547)
            if castlerect.collidepoint(mouse_pos):
                DISPLAYSURF.blit(image0136, (195, 100))
            if colesseumrect.collidepoint(mouse_pos):
                DISPLAYSURF.blit(image0137, (195, 100))
                draw_text_center("Colleseum", font13, rainbow, DISPLAYSURF, 960, 620)
            if guildrect.collidepoint(mouse_pos):
                DISPLAYSURF.blit(image0139, (195, 100))
                draw_text("Guild Hall", font13, rainbow, DISPLAYSURF, 630, 550)
            if stashrect.collidepoint(mouse_pos):
                DISPLAYSURF.blit(image0140, (195, 100))
                draw_text("Stash", font13, rainbow, DISPLAYSURF, 570, 685)
            if blackmarketrect.collidepoint(mouse_pos):
                DISPLAYSURF.blit(image0141, (195, 100))
                draw_text("Black Market", font13, rainbow, DISPLAYSURF, 250, 575)
            if adventurerect.collidepoint(mouse_pos):
                DISPLAYSURF.blit(image0138, (195, 100))

            ret, frame = video.read()
            if not ret:
                video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue  # Continue to the next loop iteration
            frame = cv2.resize(frame, (1550, 880))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_surface = pygame.surfarray.make_surface(frame)
            frame_surface = pygame.transform.rotate(frame_surface, -90)  # Rotate if necessary
            frame_surface = pygame.transform.flip(frame_surface, True, False)
            frame_surface.set_alpha(70)
            DISPLAYSURF.blit(frame_surface, (190, 100))


            image133.set_alpha(150)
            DISPLAYSURF.blit(image133, (mouseX - 41, mouseY - 37))

            chesttimer = pygame.time.get_ticks()
            chestrect = pygame.Rect(230, 220, 100, 100)


            if((((chestcollected + 600000) - chesttimer) / 1000) >= 0):
                DISPLAYSURF.blit(image226, (230, 220))
                draw_text((str(int(((chestcollected + 600000) - chesttimer) / 1000))), font5, BLACK, DISPLAYSURF, 260, 310)
            if((((chestcollected + 600000) - chesttimer) / 1000) < 0):
                draw_text("Ready!", font5, RED, DISPLAYSURF, 245, 310)
                DISPLAYSURF.blit(image225, (230, 220))
            if(chestbool > 0):
                chestbool = chestbool - 1
                if(random2 == 2):
                    draw_text_center("You received " +str(randomgold) +" gold from the treasure chest!", font5, GOLD, DISPLAYSURF, halfdisplay, 270)
                if(random2 == 1):
                    draw_text_center("You received " +str(randomgem) +" gems from the treasure chest!", font5, PURPLE, DISPLAYSURF, halfdisplay, 270)

            if(starbool):
                starfader = starfader + 1
            if(starbool == False):
                starfader = starfader - 1
            if(starfader == 0):
                starbool = True
                starx = random.randint(200, 1500)
                stary = random.randint(00, 1100)
            if(starfader == 255):
                starbool = False

            image128.set_alpha(starfader)
            DISPLAYSURF.blit(image128, (starx, stary))

            DISPLAYSURF.blit(image220, (360, 130))
            DISPLAYSURF.blit(image221, (655, 125))
            DISPLAYSURF.blit(image222, (1260, 130))
            draw_text_center(str(gold), font5, GOLD, DISPLAYSURF, 507, 152)
            draw_text_center(str(gem), font5, PURPLE, DISPLAYSURF, 1410, 152)
            draw_text_center(str(level), font5, GREY, DISPLAYSURF, 710, 150)
            draw_text_center(str(level), font5, GREY, DISPLAYSURF, 1210, 150)

            # print("x and y = " +str(mouseX) +" " +str(mouseY))

            draw_text_center("Coming Soon", font13, DARKRED, DISPLAYSURF, 960, 460)
            draw_text_center("Coming Soon", font13, DARKRED, DISPLAYSURF, 780, 254)

            mouseX, mouseY = pygame.mouse.get_pos()

            # pygame.draw.rect(DISPLAYSURF, PURPLE, paimonrect, 6)
            # pygame.draw.rect(DISPLAYSURF, BLUE, labormarketrect, 6)
            # pygame.draw.rect(DISPLAYSURF, RED, gamblingdenrect, 6)
            # pygame.draw.rect(DISPLAYSURF, BLACK, castlerect, 6)
            # pygame.draw.rect(DISPLAYSURF, GREEN, colesseumrect, 6)
            # pygame.draw.rect(DISPLAYSURF, WHITE, guildrect, 6)
            # pygame.draw.rect(DISPLAYSURF, YELLOW, stashrect, 6)
            # pygame.draw.rect(DISPLAYSURF, LIGHTBLUE, blackmarketrect, 6)
            # pygame.draw.rect(DISPLAYSURF, GOLD, adventurerect, 6)

            bubblecounter = 799
            while (bubblecounter > 0):
                bubbley[bubblecounter] = bubbley[bubblecounter] - 1
                image00.set_alpha(210)
                image01.set_alpha(210)
                image02.set_alpha(210)
                if(bubblechooser[bubblecounter] == 0):
                    DISPLAYSURF.blit(image00, (bubblex[bubblecounter], bubbley[bubblecounter]))
                elif(bubblechooser[bubblecounter] == 1):
                    DISPLAYSURF.blit(image01, (bubblex[bubblecounter], bubbley[bubblecounter]))
                elif(bubblechooser[bubblecounter] == 2):
                    DISPLAYSURF.blit(image02, (bubblex[bubblecounter], bubbley[bubblecounter]))
                bubblecounter = bubblecounter - 1


            if (textFader < 253):
                textFader = textFader + 2

            draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
            xrect = pygame.Rect(1680, 123, 35, 35)
            if xrect.collidepoint(mouse_pos):
                draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)

            adminrect = pygame.Rect(1680, 940, 50, 50)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_g:
                        if adminrect.collidepoint(mouse_pos):
                            with open(resource_path("gamedata.txt"), "r") as file:
                                lines = file.readlines()
                                gold = 1000000000
                                gem = 100000000
                                lines[0] = f"gold = {1000000000}\n"
                                lines[1] = f"gem = {100000000}\n"
                                lines[15] = f"level = {100}\n"
                            with open(resource_path("gamedata.txt"), "w") as file:
                                file.writelines(lines)

                if event.type == MOUSEBUTTONDOWN:
                    if chestrect.collidepoint(mouse_pos):
                        if ((((chestcollected + 600000) - chesttimer) / 1000) < 0):
                            randomgold = random.randint(0, level * 250)
                            randomgem = random.randint(0, 10 * level)
                            random2 = random.randint(1,2)
                            if(random2 == 2):
                                gold = gold + randomgold
                            if(random2 == 1):
                                gem = gem + randomgem
                            sound_effect = pygame.mixer.Sound(resource_path("audio/nextlevel.mp3"))
                            pygame.mixer.music.set_volume(0.5)
                            sound_effect.play()
                            chestbool = 150
                            chestcollected = chesttimer
                    if paimonrect.collidepoint(mouse_pos):
                        video.release()
                        transition(6)
                        sound_effect = pygame.mixer.Sound(resource_path("audio/dissapearwhoosh.mp3"))
                        sound_effect.play()
                        PaimonShop()
                        pygame.mixer.music.load(resource_path("audio/fantasyhomemusic.mp3"))
                        pygame.mixer.music.queue(resource_path("audio/fantasyhomemusic2.mp3"))
                        pygame.mixer.music.play(-1)
                        video = cv2.VideoCapture(resource_path("video/underwater.mp4"))
                    if labormarketrect.collidepoint(mouse_pos):
                        video.release()
                        transition(6)
                        sound_effect = pygame.mixer.Sound(resource_path("audio/dissapearwhoosh.mp3"))
                        sound_effect.play()
                        labormarket()
                        pygame.mixer.music.load(resource_path("audio/fantasyhomemusic.mp3"))
                        pygame.mixer.music.queue(resource_path("audio/fantasyhomemusic2.mp3"))
                        pygame.mixer.music.play(-1)
                        video = cv2.VideoCapture(resource_path("video/underwater.mp4"))
                    if gamblingdenrect.collidepoint(mouse_pos):
                        video.release()
                        transition(6)
                        sound_effect = pygame.mixer.Sound(resource_path("audio/dissapearwhoosh.mp3"))
                        sound_effect.play()
                        casino()
                        pygame.mixer.music.load(resource_path("audio/fantasyhomemusic.mp3"))
                        pygame.mixer.music.queue(resource_path("audio/fantasyhomemusic2.mp3"))
                        pygame.mixer.music.play(-1)
                        video = cv2.VideoCapture(resource_path("video/underwater.mp4"))
                    if guildrect.collidepoint(mouse_pos):
                        video.release()
                        transition(6)
                        sound_effect = pygame.mixer.Sound(resource_path("audio/dissapearwhoosh.mp3"))
                        sound_effect.play()
                        guild()
                        pygame.mixer.music.load(resource_path("audio/fantasyhomemusic.mp3"))
                        pygame.mixer.music.queue(resource_path("audio/fantasyhomemusic2.mp3"))
                        pygame.mixer.music.play(-1)
                        video = cv2.VideoCapture(resource_path("video/underwater.mp4"))
                    if blackmarketrect.collidepoint(mouse_pos):
                        video.release()
                        transition(6)
                        sound_effect = pygame.mixer.Sound(resource_path("audio/dissapearwhoosh.mp3"))
                        sound_effect.play()
                        blackmarket()
                        pygame.mixer.music.load(resource_path("audio/fantasyhomemusic.mp3"))
                        pygame.mixer.music.queue(resource_path("audio/fantasyhomemusic2.mp3"))
                        pygame.mixer.music.play(-1)
                        video = cv2.VideoCapture(resource_path("video/underwater.mp4"))
                    if stashrect.collidepoint(mouse_pos):
                        video.release()
                        transition(6)
                        sound_effect = pygame.mixer.Sound(resource_path("audio/dissapearwhoosh.mp3"))
                        sound_effect.play()
                        stash()
                        pygame.mixer.music.load(resource_path("audio/fantasyhomemusic.mp3"))
                        pygame.mixer.music.queue(resource_path("audio/fantasyhomemusic2.mp3"))
                        pygame.mixer.music.play(-1)
                        video = cv2.VideoCapture(resource_path("video/underwater.mp4"))
                    if colesseumrect.collidepoint(mouse_pos):
                        video.release()
                        transition(6)
                        sound_effect = pygame.mixer.Sound(resource_path("audio/dissapearwhoosh.mp3"))
                        sound_effect.play()
                        colleseum()
                        pygame.mixer.music.load(resource_path("audio/fantasyhomemusic.mp3"))
                        pygame.mixer.music.queue(resource_path("audio/fantasyhomemusic2.mp3"))
                        pygame.mixer.music.play(-1)
                        video = cv2.VideoCapture(resource_path("video/underwater.mp4"))
                    if xrect.collidepoint(mouse_pos):
                        print("Quit clicked")
                        video.release()
                        pygame.mixer.music.stop()
                        pygame.quit()
                        sys.exit()
            with open(resource_path("gamedata.txt"), "r") as file:
                lines = file.readlines()
                lines[0] = f"gold = {gold}\n"
                lines[1] = f"gem = {gem}\n"
            with open(resource_path("gamedata.txt"), "w") as file:
                file.writelines(lines)
            pygame.display.update()
########################################################################################################################
class PaimonShop(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.menu_activepaimon = True
        self.paimonshop()
########################################################################################################################
    def displayitemscene(self, itemdisplay, gamescene, name, temporary, imagecore, image, attack=0, armor=0, speed=0,
                         hp=0, specialattack=0, luck=0, price=0):
        startTime = pygame.time.get_ticks()
        rainbowcolor1 = int((math.sin(startTime * 0.001) + 1) * 127.5)
        rainbowcolor2 = int((math.sin(startTime * 0.004 + 2) + 1) * 127.5)
        rainbowcolor3 = int((math.sin(startTime * 0.005 + 2) + 1) * 127.5)
        mouse_pos = pygame.mouse.get_pos()
        errorswitch = False
        global gold
        global itemlist
        global itemboughtswitch

        imageBlack.set_alpha(210)
        DISPLAYSURF.blit(imageBlack, (600, 195))
        image128.set_alpha(rainbowcolor1)
        DISPLAYSURF.blit(image128, (570, 155))
        DISPLAYSURF.blit(image129, (540, 10))

        buyrect = pygame.Rect(1360, 640, 300, 300)
        if buyrect.collidepoint(mouse_pos):
            DISPLAYSURF.blit(image131, (1350, 630))
        else:
            DISPLAYSURF.blit(image130, (1350, 630))

        errorimagecounter = 0
        if(errorswitch):
            DISPLAYSURF.blit(image136, (1350, 630))
            if (errorimagecounter < 100):
                errorimagecounter = errorimagecounter + 1
            else:
                errorimagecounter = 0
                itemboughtswitch = False

        imageBlack2.set_alpha(220)
        DISPLAYSURF.blit(imageBlack2, (1385, 550))
        draw_text("Current Gold- ", font11, WHITE, DISPLAYSURF, 1395, 565)
        draw_text(str(gold), font11, GOLD, DISPLAYSURF, 1560, 565)
        draw_text("Item Price- ", font11, WHITE, DISPLAYSURF, 1395, 600)
        draw_text(str(price), font11, GOLD, DISPLAYSURF, 1560, 600)

        draw_text(name, font12, WHITE, DISPLAYSURF, 800, 200)
        DISPLAYSURF.blit(image, (680, 290))
        draw_text(str(attack), font11, WHITE, DISPLAYSURF, 1270, 706)
        draw_text(str(armor), font11, WHITE, DISPLAYSURF, 1270, 731)
        draw_text(str(speed), font11, WHITE, DISPLAYSURF, 1270, 756)
        draw_text(str(hp), font11, WHITE, DISPLAYSURF, 1270, 781)
        draw_text(str(specialattack), font11, WHITE, DISPLAYSURF, 1270, 806)
        draw_text(str(luck), font11, SKYBLUE, DISPLAYSURF, 1270, 831)
        if ((temporary != 0) and (temporary != -1)):
            draw_text("*Temporary Item*", font13,
                      (rainbowcolor2, rainbowcolor3, rainbowcolor1), DISPLAYSURF, 1120, 630)
        elif (temporary == -1):
            draw_text("Consumable Item", font13, (rainbowcolor2, rainbowcolor3, rainbowcolor1), DISPLAYSURF, 1120,
                      630)
        xrect = pygame.Rect(1325, 203, 45, 45)
        draw_text('x', font4, WHITE, DISPLAYSURF, 1330, 195)
        if xrect.collidepoint(mouse_pos):
            draw_text('x', font4, LIGHTBLUE, DISPLAYSURF, 1330, 195)

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if xrect.collidepoint(mouse_pos):
                    print("item display exit clicked")
                    return (0, 7)
                if buyrect.collidepoint(mouse_pos):
                    if (gold >= price):
                        gold = gold - price
                        itemlist.append(name)
                        print("item bought")
                        sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                        itemboughtswitch = True
                        sound_effect.play()
                        item = {
                            "name": name,
                            "imagecore": imagecore,
                            "HP": hp,
                            "armor": armor,
                            "Attack": attack,
                            "specialattack": specialattack,
                            "speed": speed,
                            "luck": luck,
                        }
                        if(temporary == 0):
                            save_creature(item, "itemdata.txt")
                        if (temporary == 1):
                            save_creature(item, "tempitems.txt")
                        return (0, 7)
                    else:
                        sound_effect = pygame.mixer.Sound(resource_path("audio/error.mp3"))
                        errorswitch = True
                        sound_effect.play()
                        pygame.mixer.music.set_volume(0.5)

        return (itemdisplay, gamescene)
    ########################################################################################################################
    def xbutton(self, gamescene):
        global FaderBool
        global Fader
        global textFader
        if (FaderBool):
            Fader = Fader + .5
            if (Fader > 110):
                FaderBool = False
        if (FaderBool == False):
            Fader = Fader - .5
            if (Fader < 10):
                FaderBool = True
        mouse_pos = pygame.mouse.get_pos()
        mouseX, mouseY = pygame.mouse.get_pos()
        DISPLAYSURF.blit(image56, (mouseX - 47, mouseY - 44))
        xrect = pygame.Rect(1680, 123, 35, 35)
        xrect2 = pygame.Rect(130, 100, 120, 80)
        mouseX, mouseY = pygame.mouse.get_pos()
        mouse_pos = pygame.mouse.get_pos()
        image42.set_alpha(Fader)
        DISPLAYSURF.blit(image42, (1655, 917))
        draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
        if xrect.collidepoint(mouse_pos):
            draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
        for event in pygame.event.get():
            mouseX, mouseY = pygame.mouse.get_pos()
            if xrect.collidepoint(mouse_pos):
                if event.type == MOUSEBUTTONDOWN:
                    if xrect.collidepoint(mouse_pos):
                        print("Quit clicked")
                        pygame.mixer.music.stop()
                        pygame.quit()
                        sys.exit()
            else:
                if event.type == MOUSEBUTTONDOWN:
                    if 0 <= mouseX <= 1920 and 150 <= mouseY <= 1080:
                        sound_effect = pygame.mixer.Sound(resource_path("audio/clicknoise.mp3"))
                        sound_effect.play()
                        pygame.mixer.music.set_volume(0.4)
                        pygame.display.update()
                        textFader = 0
                        return (gamescene + 1)
        pygame.display.update()
        return gamescene
    ########################################################################################################################
    def paimonshop(self):
        global FaderBool
        global Fader
        global textFader
        global itemboughtswitch
        startTime = pygame.time.get_ticks()
        self.gamescene = 1
        itemdisplay = 0
        xcounter = 0
        mouse_pos = pygame.mouse.get_pos()
        pygame.mixer.music.load(resource_path("audio/celestialmusic.mp3"))
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        print("Paimons shop initialized")
        global textFader
        global characterName
        global firsttimepaimon

        with open(resource_path("gamedata.txt"), "r") as file:
            lines = file.readlines()
            paimonshopline = lines[11].strip()
            paimonshopline = paimonshopline[18:]

        if(paimonshopline == 'true'):
            self.gamescene = 1
        elif(paimonshopline == 'false'):
            self.gamescene = 10

        while self.menu_activepaimon:
            with open(resource_path("gamedata.txt"), "r") as file:
                lines = file.readlines()
                if len(lines) >= 8:
                    goldline = lines[0].strip()
                    goldline = goldline[7:]
                    gemline = lines[1].strip()
                    gemline = gemline[6:]
                    gold = int(goldline)
                    gem = int(gemline)
            if (self.gamescene == 1):
                firsttimepaimon = False
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image58, (200, 100))
                self.gamescene = self.xbutton(self.gamescene)
                pygame.display.update()
            if (self.gamescene == 2):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image58, (200, 100))
                DISPLAYSURF.blit(image53, (1070, 110))
                draw_text('Hello human,', font5, PINK, DISPLAYSURF, 1255, 150)
                draw_text('My name is Paimon,', font5, PINK, DISPLAYSURF, 1230, 175)
                draw_text('its so nice to meet you!', font5, PINK, DISPLAYSURF, 1210, 200)
                self.gamescene = self.xbutton(self.gamescene)
                pygame.display.update()
            if (self.gamescene == 3):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image58, (200, 100))
                DISPLAYSURF.blit(image53, (1070, 110))
                draw_text('Its been many years', font5, PINK, DISPLAYSURF, 1220, 150)
                draw_text('since ive last interacted', font5, PINK, DISPLAYSURF, 1200, 175)
                draw_text('with a human', font5, PINK, DISPLAYSURF, 1240, 200)
                self.gamescene = self.xbutton(self.gamescene)
                pygame.display.update()
            if (self.gamescene == 4):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image58, (200, 100))
                DISPLAYSURF.blit(image53, (1070, 110))
                draw_text('This is so much fun!', font5, PINK, DISPLAYSURF, 1220, 175)
                draw_text('you must come here often okay?', font5, PINK, DISPLAYSURF, 1175, 200)
                self.gamescene = self.xbutton(self.gamescene)
                pygame.display.update()
            if (self.gamescene == 5):
                with open(resource_path("gamedata.txt"), "r") as file:
                    lines = file.readlines()
                    lines[11] = f"firstpaimonshop = false\n"
                with open(resource_path("gamedata.txt"), "w") as file:
                    file.writelines(lines)  # Write the modified lines back to the file
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image58, (200, 100))
                DISPLAYSURF.blit(image53, (1070, 110))
                draw_text('Ill give special discounts just for you', font5, PINK, DISPLAYSURF, 1140, 175)
                draw_text('*wink*', font5, PINK, DISPLAYSURF, 1280, 200)
                draw_text('g', font15, SKYBLUE, DISPLAYSURF, 1345, 190)
                self.gamescene = self.xbutton(self.gamescene)
                pygame.display.update()
            if (self.gamescene == 6):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image58, (200, 100))
                DISPLAYSURF.blit(image53, (1070, 110))
                draw_text('Come take a look and see all that I have', font5, PINK, DISPLAYSURF, 1130, 175)
                draw_text('for you.', font5, PINK, DISPLAYSURF, 1280, 200)
                self.gamescene = self.xbutton(self.gamescene)
                pygame.display.update()
            if ((self.gamescene == 7)and (itemdisplay == 0)):
                startTime = pygame.time.get_ticks()
                rainbowcolor1 = int((math.sin(startTime * 0.002) + 1) * 127.5)
                rainbowcolor2 = int((math.sin(startTime * 0.003 + 2) + 1) * 127.5)
                rainbowcolor3 = int((math.sin(startTime * 0.004 + 2) + 1) * 127.5)
                rainbow = (rainbowcolor1, rainbowcolor2, rainbowcolor3)
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image58, (200, 100))
                image59.set_alpha(230)
                image4.set_alpha(100)
                DISPLAYSURF.blit(image4, (0, 0))
                DISPLAYSURF.blit(image59, (530, 80))
                DISPLAYSURF.blit(image60, (1430, 130))


                ####return rect#
                returnrect = pygame.Rect(1420, 119, 100, 100)
                ###column 1#####
                hover_rect1 = pygame.Rect(649, 321, 73, 73)
                hover_rect2 = pygame.Rect(649, 419.6, 73, 73)
                hover_rect3 = pygame.Rect(649, 512, 73, 73)
                hover_rect4 = pygame.Rect(649, 604, 73, 73)
                hover_rect5 = pygame.Rect(649, 695.8, 73, 73)
                DISPLAYSURF.blit(image62, (659, 335))
                DISPLAYSURF.blit(image69, (659, 431.6))
                DISPLAYSURF.blit(image76, (659, 525.2))
                DISPLAYSURF.blit(imageesneak83, (659, 618.8))
                DISPLAYSURF.blit(image88, (659, 709.4))

                ###column 2#####
                hover_rect6 = pygame.Rect(747, 321, 73, 73)
                hover_rect7 = pygame.Rect(747, 419.6, 73, 73)
                hover_rect8 = pygame.Rect(747, 512, 73, 73)
                hover_rect9 = pygame.Rect(747, 604, 73, 73)
                hover_rect10 = pygame.Rect(747, 695.8, 73, 73)
                DISPLAYSURF.blit(image63, (757, 335))
                DISPLAYSURF.blit(image70, (757, 431.6))
                DISPLAYSURF.blit(image77, (757, 525.2))
                DISPLAYSURF.blit(imageesneak84, (757, 618.8))
                DISPLAYSURF.blit(image89, (757, 709.4))

                ###column 3#####
                hover_rect11 = pygame.Rect(845, 321, 73, 73)
                hover_rect12 = pygame.Rect(845, 419.6, 73, 73)
                hover_rect13 = pygame.Rect(845, 512, 73, 73)
                hover_rect14 = pygame.Rect(845, 604, 73, 73)
                hover_rect15 = pygame.Rect(845, 695.8, 73, 73)
                DISPLAYSURF.blit(image64, (855, 335))
                DISPLAYSURF.blit(image71, (855, 431.6))
                DISPLAYSURF.blit(image78, (855, 525.2))
                DISPLAYSURF.blit(image83, (855, 618.8))
                DISPLAYSURF.blit(image90, (855, 709.4))

                ###column 4#####
                hover_rect16 = pygame.Rect(943, 321, 73, 73)
                hover_rect17 = pygame.Rect(943, 419.6, 73, 73)
                hover_rect18 = pygame.Rect(943, 512, 73, 73)
                hover_rect19 = pygame.Rect(943, 604, 73, 73)
                hover_rect20 = pygame.Rect(943, 695.8, 73, 73)
                DISPLAYSURF.blit(image65, (953, 335))
                DISPLAYSURF.blit(image72, (953, 431.6))
                DISPLAYSURF.blit(image79, (953, 525.2))
                DISPLAYSURF.blit(image84, (953, 618.8))
                DISPLAYSURF.blit(image91, (953, 711.4))

                ###column 5#####
                hover_rect21 = pygame.Rect(1041, 321, 73, 73)
                hover_rect22 = pygame.Rect(1041, 419.6, 73, 73)
                hover_rect23 = pygame.Rect(1041, 512, 73, 73)
                hover_rect24 = pygame.Rect(1041, 604, 73, 73)
                hover_rect25 = pygame.Rect(1041, 695.8, 73, 73)
                DISPLAYSURF.blit(image66, (1051, 335))
                DISPLAYSURF.blit(image73, (1051, 431.6))
                DISPLAYSURF.blit(image80, (1051, 525.2))
                DISPLAYSURF.blit(image85, (1051, 618.8))
                DISPLAYSURF.blit(image92, (1051, 711.4))

                ###column 6#####
                hover_rect26 = pygame.Rect(1139, 321, 73, 73)
                hover_rect27 = pygame.Rect(1139, 419.6, 73, 73)
                hover_rect28 = pygame.Rect(1139, 512, 73, 73)
                hover_rect29 = pygame.Rect(1139, 604, 73, 73)
                hover_rect30 = pygame.Rect(1139, 695.8, 73, 73)
                DISPLAYSURF.blit(image67, (1149, 335))
                DISPLAYSURF.blit(image74, (1149, 431.6))
                DISPLAYSURF.blit(image81, (1149, 525.2))
                DISPLAYSURF.blit(image86, (1149, 618.8))
                DISPLAYSURF.blit(image93, (1149, 711.4))

                ###column 7#####
                hover_rect31 = pygame.Rect(1237, 321, 73, 73)
                hover_rect32 = pygame.Rect(1237, 419.6, 73, 73)
                hover_rect33 = pygame.Rect(1237, 512, 73, 73)
                hover_rect34 = pygame.Rect(1237, 604, 73, 73)
                DISPLAYSURF.blit(image68, (1247, 335))
                DISPLAYSURF.blit(image75, (1247, 431.6))
                DISPLAYSURF.blit(image82, (1247, 525.2))
                DISPLAYSURF.blit(image87, (1247, 618.8))

                ################
                mouseX, mouseY = pygame.mouse.get_pos()
                mouse_pos = pygame.mouse.get_pos()
                if returnrect.collidepoint(mouse_pos):
                    pygame.draw.rect(DISPLAYSURF, (PINK), returnrect, 8)
                    DISPLAYSURF.blit(image61, (1430, 130))
                if (itemdisplay == 0):
                    ###column 1#####
                    if hover_rect1.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbow), hover_rect1, 6)  # (color, rect, border thickness)
                    if hover_rect2.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbow), hover_rect2, 6)
                    if hover_rect3.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbow), hover_rect3, 6)
                    if hover_rect4.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbow), hover_rect4, 6)
                    if hover_rect5.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbow), hover_rect5, 6)
                    ###column 2#####
                    if hover_rect6.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbow), hover_rect6, 6)
                    if hover_rect7.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbow), hover_rect7, 6)
                    if hover_rect8.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbow), hover_rect8, 6)
                    if hover_rect9.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbow), hover_rect9, 6)
                    if hover_rect10.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbow), hover_rect10, 6)
                    ###column 3#####
                    if hover_rect11.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbow), hover_rect11, 6)
                    if hover_rect12.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbow), hover_rect12, 6)
                    if hover_rect13.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbow), hover_rect13, 6)
                    if hover_rect14.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbow), hover_rect14, 6)
                    if hover_rect15.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbow), hover_rect15, 6)
                    ###column 4#####
                    if hover_rect16.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbow), hover_rect16, 6)
                    if hover_rect17.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbow), hover_rect17, 6)
                    if hover_rect18.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbow), hover_rect18, 6)
                    if hover_rect19.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbow), hover_rect19, 6)
                    if hover_rect20.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbow), hover_rect20, 6)
                    ###column 5#####
                    if hover_rect21.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbow), hover_rect21, 6)
                    if hover_rect22.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbow), hover_rect22, 6)
                    if hover_rect23.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbow), hover_rect23, 6)
                    if hover_rect24.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbow), hover_rect24, 6)
                    if hover_rect25.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbow), hover_rect25, 6)
                    ###column 6#####
                    if hover_rect26.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbow), hover_rect26, 6)
                    if hover_rect27.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbow), hover_rect27, 6)
                    if hover_rect28.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbow), hover_rect28, 6)
                    if hover_rect29.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbow), hover_rect29, 6)
                    if hover_rect30.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbow), hover_rect30, 6)
                    ###column 7#####
                    if hover_rect31.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbow), hover_rect31, 6)
                    if hover_rect32.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbow), hover_rect32, 6)
                    if hover_rect33.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbow), hover_rect33, 6)
                    if hover_rect34.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbow), hover_rect34, 6)
                ################
                if (itemboughtswitch):
                    imageBlack2.set_alpha(220)
                    DISPLAYSURF.blit(imageBlack2, (800, 450))
                    DISPLAYSURF.blit(imageBlack2, (860, 450))

                    draw_text('Item Purchased', font18, GOLD, DISPLAYSURF, 805, 450)
                    if (xcounter < 100):
                        xcounter = xcounter + 1
                    else:
                        xcounter = 0
                        itemboughtswitch = False
                ################
                mouse_pos = pygame.mouse.get_pos()
                returnmenurect = pygame.Rect(200, 40, 140, 190)
                if returnmenurect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image135, (200, 100))
                else:
                    DISPLAYSURF.blit(image134, (200, 100))

                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == MOUSEBUTTONDOWN:
                        sound_effect = pygame.mixer.Sound(resource_path("audio/shopclicksound.mp3"))
                        sound_effect.play()
                        if returnrect.collidepoint(mouse_pos):
                            print("exited paimon shop menu")
                            self.gamescene = 10
                        if returnmenurect.collidepoint(mouse_pos):
                            transition(6)
                            self.menu_activepaimon = False
                            pygame.event.clear()

                        else:
                            if (itemdisplay == 0):
                                if hover_rect1.collidepoint(mouse_pos):
                                    itemdisplay = 1
                                if hover_rect2.collidepoint(mouse_pos):
                                    itemdisplay = 2
                                if hover_rect3.collidepoint(mouse_pos):
                                    itemdisplay = 3
                                if hover_rect4.collidepoint(mouse_pos):
                                    itemdisplay = 4
                                if hover_rect5.collidepoint(mouse_pos):
                                    itemdisplay = 5
                                if hover_rect6.collidepoint(mouse_pos):
                                    itemdisplay = 6
                                if hover_rect7.collidepoint(mouse_pos):
                                    itemdisplay = 7
                                if hover_rect8.collidepoint(mouse_pos):
                                    itemdisplay = 8
                                if hover_rect9.collidepoint(mouse_pos):
                                    itemdisplay = 9
                                if hover_rect10.collidepoint(mouse_pos):
                                    itemdisplay = 10
                                if hover_rect11.collidepoint(mouse_pos):
                                    itemdisplay = 11
                                if hover_rect12.collidepoint(mouse_pos):
                                    itemdisplay = 12
                                if hover_rect13.collidepoint(mouse_pos):
                                    itemdisplay = 13
                                if hover_rect14.collidepoint(mouse_pos):
                                    itemdisplay = 14
                                if hover_rect15.collidepoint(mouse_pos):
                                    itemdisplay = 15
                                if hover_rect16.collidepoint(mouse_pos):
                                    itemdisplay = 16
                                if hover_rect17.collidepoint(mouse_pos):
                                    itemdisplay = 17
                                if hover_rect18.collidepoint(mouse_pos):
                                    itemdisplay = 18
                                if hover_rect19.collidepoint(mouse_pos):
                                    itemdisplay = 19
                                if hover_rect20.collidepoint(mouse_pos):
                                    itemdisplay = 20
                                if hover_rect21.collidepoint(mouse_pos):
                                    itemdisplay = 21
                                if hover_rect22.collidepoint(mouse_pos):
                                    itemdisplay = 22
                                if hover_rect23.collidepoint(mouse_pos):
                                    itemdisplay = 23
                                if hover_rect24.collidepoint(mouse_pos):
                                    itemdisplay = 24
                                if hover_rect25.collidepoint(mouse_pos):
                                    itemdisplay = 25
                                if hover_rect26.collidepoint(mouse_pos):
                                    itemdisplay = 26
                                if hover_rect27.collidepoint(mouse_pos):
                                    itemdisplay = 27
                                if hover_rect28.collidepoint(mouse_pos):
                                    itemdisplay = 28
                                if hover_rect29.collidepoint(mouse_pos):
                                    itemdisplay = 29
                                if hover_rect30.collidepoint(mouse_pos):
                                    itemdisplay = 30
                                if hover_rect31.collidepoint(mouse_pos):
                                    itemdisplay = 31
                                if hover_rect32.collidepoint(mouse_pos):
                                    itemdisplay = 32
                                if hover_rect33.collidepoint(mouse_pos):
                                    itemdisplay = 33
                                if hover_rect34.collidepoint(mouse_pos):
                                    itemdisplay = 34

            if(itemdisplay == 1):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Purple Potion", 1,'images/purplepotion.png', image94, 0, 0, 0, 0, 0, 0, 250)
                draw_text('Increases Attack stat for 10 min', font5, TAN, DISPLAYSURF, 675, 730)

            if(itemdisplay == 2):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Codex", 1,'images/enchantedbook1.png', image95, 0, 0, 0, 0, 0, 0, 20000)
                draw_text('A codex filled with the knowledge of', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('the gods. Use this item to gain ', font5, TAN, DISPLAYSURF, 675, 760)
                draw_text('1-5000 user experience points', font5, TAN, DISPLAYSURF, 675, 790)

            if(itemdisplay == 3):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Rusty Sword", 0,'images/rustysword.png', image96, 2, 0, 2, 0, 0, 0, 250)
                draw_text('A sword with a forgotten story.', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('This sword is the bare minimum', font5, TAN, DISPLAYSURF, 675, 760)
                draw_text('for surviving in this world.', font5, TAN, DISPLAYSURF, 675, 790)

            if(itemdisplay == 4):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Leather Greeves", 0,'images/leatherpants.png', image97, 0, 2, 0, 2, 0, 0, 250)
                draw_text('Can barely be called armor.', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('Made to be cheap and light.', font5, TAN, DISPLAYSURF, 675, 760)

            if(itemdisplay == 5):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Ascendent Chestplate", 0,'images/coralchestplate.png', image98, 1, 40, 0, 30, 0, 5, 125000)
                draw_text('A chestplate crafted from the divine', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('blacksmith of Lucidea. This armor', font5, TAN, DISPLAYSURF, 675, 760)
                draw_text('was crafted within a star.', font5, TAN, DISPLAYSURF, 675, 790)

            if(itemdisplay == 6):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Wind Potion", 1,'images/bluepotion.png', image99, 0, 0, 0, 0, 0, 0, 250)
                draw_text('Increases Speed stat for 10 min', font5, TAN, DISPLAYSURF, 675, 730)

            if(itemdisplay == 7):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Aqua Amulet", 0,'images/whiteamulet.png', image100, 0, 5, 5, 5, 0, 0, 5000)
                draw_text('An amulet inbued with the power of water.', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('Blessed by the goddest of water.', font5, TAN, DISPLAYSURF, 675, 760)
                draw_text('(equipable jewelry slot)', font5, TAN, DISPLAYSURF, 675, 790)

            if(itemdisplay == 8):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Bronze Sword", 0,'images/bronzesword.png', image101, 5, 0, 3, 0, 1, 1, 1000)
                draw_text('A sword forged by an amateur.', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('A sword for beginners, to create', font5, TAN, DISPLAYSURF, 675, 760)
                draw_text('new beginnings.', font5, TAN, DISPLAYSURF, 675, 790)

            if(itemdisplay == 9):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Leather Boots", 0,'images/leatherboots.png', image102, 0, 2, 2, 2, 0, 0, 250)
                draw_text('Can barely be called armor.', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('Made to be cheap and light.', font5, TAN, DISPLAYSURF, 675, 760)

            if(itemdisplay == 10):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Ascendent Greeves", 0,'images/coralpants.png', image103, 0, 30, 10, 10, 0, 5, 100000)
                draw_text('Greeves crafted from the divine', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('blacksmith of Lucidea. This armor', font5, TAN, DISPLAYSURF, 675, 760)
                draw_text('was crafted within a star.', font5, TAN, DISPLAYSURF, 675, 790)

            if (itemdisplay == 11):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Lucky Potion", 1,'images/greenpotion.png', image104,0, 0, 0, 0, 0, 0, 250)
                draw_text('Increases Luck by 10 min', font5, TAN, DISPLAYSURF, 675, 730)

            if (itemdisplay == 12):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Lava Amulet", 0,'images/redamulet.png', image105, 5, 0,0, 5, 5, 0, 5000)
                draw_text('An amulet inbued with the power of Lava.', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('Blessed by the goddest of fire.', font5, TAN, DISPLAYSURF, 675, 760)
                draw_text('(equipable jewelry slot)', font5, TAN, DISPLAYSURF, 675, 790)

            if (itemdisplay == 13):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Silverline Sword", 0,'images/Ironsword.png', image106,10, 0, 5, 0, 10, 0, 3500)
                draw_text('A sword used by all knights of the kingdom', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('A sword worshipped by the light and dreaded', font5, TAN, DISPLAYSURF, 675, 760)
                draw_text('by the dark.', font5, TAN, DISPLAYSURF, 705, 790)

            if (itemdisplay == 14):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Plated Helmet", 0,'images/metalhelmet.png',image107, 0, 10, -5, 5, 0, 0, 5000)
                draw_text('Heavy and reliable', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('this armor is made for war.', font5, TAN, DISPLAYSURF, 675, 760)

            if (itemdisplay == 15):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Ascendent Boots",0,'images/coralshoes.png', image108, 0, 20, 30, 5, 0, 5, 100000)
                draw_text('Boots crafted from the divine', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('blacksmith of Lucidea. This armor', font5, TAN, DISPLAYSURF, 675, 760)
                draw_text('was crafted within a star.', font5, TAN, DISPLAYSURF, 675, 790)

            if (itemdisplay == 16):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Resistence Potion", 1,'images/whitepotion.png', image109,0, 0, 0, 0, 0, 0, 250)
                draw_text('Increases Defense stat for 10 min', font5, TAN, DISPLAYSURF, 675, 730)

            if (itemdisplay == 17):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Amulet of Heaven", 0,'images/purpleamulet.png', image110, 10, 10,10, 10, 10, 10, 1000000)
                draw_text('An amulet of unknown origins,', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('blessed by the heavens.', font5, TAN, DISPLAYSURF, 675, 760)
                draw_text('Increases all elemental resistence by 10%', font5, TAN, DISPLAYSURF, 675, 790)

            if (itemdisplay == 18):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Adamantine Sword", 0,'images/diamondsword.png', image111,25, 5, 5, 0, 0, 0, 25000)
                draw_text('A sword made for heroes.', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('Unlock the way of the sword.', font5, TAN, DISPLAYSURF, 675, 760)
                draw_text(' ', font5, TAN, DISPLAYSURF, 675, 790)

            if (itemdisplay == 19):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Plated Chestplate", 0,'images/metalchestplate.png',image112, 0, 10, -5, 5, 0, 0, 5000)
                draw_text('Heavy and reliable', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('this armor is made for war.', font5, TAN, DISPLAYSURF, 675, 760)

            if (itemdisplay == 20):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Small EXP Pouch",1,'images/expouch.png', image113, 0, 0, 0, 0, 0, 0, 1000)
                draw_text('Used by Beast Tamers for fast results.', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('Increase a Beasts exp by 1-1,000 exp', font5, TAN, DISPLAYSURF, 675, 760)

            if (itemdisplay == 21):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Healing Potion", 1,'images/healingpotion.png', image114, 0, 0, 0, 0, 0, 0, 500)
                draw_text('Heals 25% hp', font5, TAN, DISPLAYSURF, 675, 730)

            if (itemdisplay == 22):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Lost Crown", 0,'images/underwatercrown.png', image115, 0, 3, 0, 0, 25, 10, 50000)
                draw_text('The power of the king.', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('Stand on the corpse of a trillion souls,', font5, TAN, DISPLAYSURF, 675, 760)
                draw_text('and ask them how important honor is?', font5, TAN, DISPLAYSURF, 675, 790)

            if (itemdisplay == 23):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Simple Staff", 0,'images/simplestaff.png', image116, 0, 0, 1, 0, 5, 0, 500)
                draw_text('Tired of using a sword?', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('Become a wizard!', font5, TAN, DISPLAYSURF, 675, 760)
                draw_text('(equipable weapon slot)', font5, TAN, DISPLAYSURF, 675, 790)

            if (itemdisplay == 24):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Plated Greeves", 0,'images/metalgreeves.png', image117, -1, 10, -5, 5, 0, 0, 5000)
                draw_text('Heavy and reliable', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('this armor is made for war.', font5, TAN, DISPLAYSURF, 675, 760)

            if (itemdisplay == 25):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene,"Large EXP Pouch", 1,'images/largeexppouch.png', image118, 0, 0,0, 0, 0, 0, 10000)
                draw_text('Used by wealthy Beast Tamers for fast results.', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('Increase a Beasts exp by 1,000-10,000 exp', font5, TAN, DISPLAYSURF, 675, 760)

            if (itemdisplay == 26):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Apple", 1,'images/apple.png', image119, 0,0, 0, 0, 0, 0, 100)
                draw_text('Apples exist underwater?', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('Heals 25 hp', font5, TAN, DISPLAYSURF, 675, 760)

            if (itemdisplay == 27):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Mystery bag", 1, 'images/mysterybag.png', image120, 0,0, 0, 0, 0, 0, 7500)
                draw_text('obtain an #$*@ item', font5, TAN, DISPLAYSURF, 675, 730)

            if (itemdisplay == 28):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Leather Cap", 0,'images/leatherhelmet.png', image121, 0, 2, 3, 1, 0, 0, 250)
                draw_text('Can barely be called armor.', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('Made to be cheap and light.', font5, TAN, DISPLAYSURF, 675, 760)

            if (itemdisplay == 29):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene,"Plated Boots", 0,'images/metalboots.png', image122, 3, 10,-5, 5, 0, 0, 5000)
                draw_text('Heavy and reliable', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('this armor is made for war.', font5, TAN, DISPLAYSURF, 675, 760)

            if (itemdisplay == 30):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Time Dilator", 1,'images/timedilator.png', image123,0, 0, 0, 0, 0, 0, 5000)
                draw_text('??#?#$???9?????5????9?@?#??', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('Revert a creature back to lvl 1', font5, TAN, DISPLAYSURF, 675, 760)
                draw_text('??#?#$???9?????5????9?@?#??', font5, TAN, DISPLAYSURF, 675, 790)

            if (itemdisplay == 31):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Golden Apple", 1,'images/goldenapple.png', image124, 0, 0, 0, 0, 0, 0, 2222)
                draw_text('whats next, enchanted golden apple?', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('Heals 100 HP', font5, TAN, DISPLAYSURF, 675, 760)

            if (itemdisplay == 32):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Mysterious Dao Bag",1,'images/supermysterybag.png', image125, 1, 2, 3, 4, 5, 6, 125000)
                draw_text('obtain an rare or higher #$*@ item', font5, TAN, DISPLAYSURF, 675, 730)

            if (itemdisplay == 33):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Leather Chestplate",0,'images/leatherchestplate.png', image126, 0, 4, 4, 0, 0, 0, 500)
                draw_text('You are broke arent you?', font5, TAN, DISPLAYSURF, 675, 730)

            if (itemdisplay == 34):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Ascendent Helmet",0,'images/coralhelmet.png', image127, 0, 30, 10, 5, 0, 5, 100000)
                draw_text('A helmet crafted from the divine', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('blacksmith of Lucidea. This armor', font5, TAN, DISPLAYSURF, 675, 760)
                draw_text('was crafted within a star.', font5, TAN, DISPLAYSURF, 675, 790)
            pygame.display.update()
            if (self.gamescene == 10):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image58, (200, 100))

                mouse_pos = pygame.mouse.get_pos()
                returnmenurect = pygame.Rect(200, 40, 140, 190)
                if returnmenurect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image135, (200, 100))
                else:
                    DISPLAYSURF.blit(image134, (200, 100))

                if (FaderBool):
                    Fader = Fader + .5
                    if (Fader > 110):
                        FaderBool = False
                if (FaderBool == False):
                    Fader = Fader - .5
                    if (Fader < 10):
                        FaderBool = True
                mouse_pos = pygame.mouse.get_pos()
                mouseX, mouseY = pygame.mouse.get_pos()
                DISPLAYSURF.blit(image56, (mouseX - 47, mouseY - 44))
                xrect = pygame.Rect(1680, 123, 35, 35)
                xrect2 = pygame.Rect(130, 100, 120, 80)
                mouseX, mouseY = pygame.mouse.get_pos()
                mouse_pos = pygame.mouse.get_pos()
                image42.set_alpha(Fader)
                DISPLAYSURF.blit(image42, (1655, 917))
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                for event in pygame.event.get():
                    mouseX, mouseY = pygame.mouse.get_pos()
                    if xrect.collidepoint(mouse_pos):
                        if event.type == MOUSEBUTTONDOWN:
                            if xrect.collidepoint(mouse_pos):
                                print("Quit clicked")
                                pygame.mixer.music.stop()
                                pygame.quit()
                                sys.exit()
                    else:
                        if event.type == MOUSEBUTTONDOWN:
                            if returnmenurect.collidepoint(mouse_pos):
                                transition(6)
                                self.menu_activepaimon = False
                                pygame.event.clear()
                            if 100 <= mouseX <= 1920 and 150 <= mouseY <= 1080:
                                sound_effect = pygame.mixer.Sound(resource_path("audio/clicknoise.mp3"))
                                sound_effect.play()
                                pygame.mixer.music.set_volume(0.4)
                                pygame.display.update()
                                textFader = 0
                                self.gamescene = self.gamescene + 1

                randomtext = random.randint(1, 8)
                pygame.display.update()
            if (self.gamescene == 11):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image58, (200, 100))
                DISPLAYSURF.blit(image53, (1070, 110))
                mouse_pos = pygame.mouse.get_pos()
                returnmenurect = pygame.Rect(200, 40, 140, 190)
                if returnmenurect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image135, (200, 100))
                else:
                    DISPLAYSURF.blit(image134, (200, 100))


                if (FaderBool):
                    Fader = Fader + .5
                    if (Fader > 110):
                        FaderBool = False
                if (FaderBool == False):
                    Fader = Fader - .5
                    if (Fader < 10):
                        FaderBool = True
                mouse_pos = pygame.mouse.get_pos()
                mouseX, mouseY = pygame.mouse.get_pos()
                DISPLAYSURF.blit(image56, (mouseX - 47, mouseY - 44))
                xrect = pygame.Rect(1680, 123, 35, 35)
                xrect2 = pygame.Rect(130, 100, 120, 80)
                mouseX, mouseY = pygame.mouse.get_pos()
                mouse_pos = pygame.mouse.get_pos()
                image42.set_alpha(Fader)
                DISPLAYSURF.blit(image42, (1655, 917))
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                for event in pygame.event.get():
                    mouseX, mouseY = pygame.mouse.get_pos()
                    if xrect.collidepoint(mouse_pos):
                        if event.type == MOUSEBUTTONDOWN:
                            if xrect.collidepoint(mouse_pos):
                                print("Quit clicked")
                                pygame.mixer.music.stop()
                                pygame.quit()
                                sys.exit()
                    else:
                        if event.type == MOUSEBUTTONDOWN:
                            if returnmenurect.collidepoint(mouse_pos):
                                transition(6)
                                self.menu_activepaimon = False
                                pygame.event.clear()
                            if 100 <= mouseX <= 1920 and 150 <= mouseY <= 1080:
                                sound_effect = pygame.mixer.Sound(resource_path("audio/clicknoise.mp3"))
                                sound_effect.play()
                                pygame.mixer.music.set_volume(0.4)
                                pygame.display.update()
                                textFader = 0
                                self.gamescene = self.gamescene + 1

                if(randomtext == 0):
                    draw_text('Hey cutie your back again I see!', font5, PINK, DISPLAYSURF, 1145, 175)
                elif(randomtext == 1):
                    draw_text('Did you miss me ' +characterName +"?", font5, PINK, DISPLAYSURF, 1235, 175)
                elif(randomtext == 2):
                    draw_text('I missed you so much ' +characterName +"!", font5, PINK, DISPLAYSURF, 1205, 175)
                elif(randomtext == 3):
                    draw_text('Mmm look who it is, my cutest customer.', font5, PINK, DISPLAYSURF, 1135, 175)
                elif(randomtext == 4):
                    draw_text('Ahhh, my future husband has come back !', font5, PINK, DISPLAYSURF, 1135, 175)
                    draw_text('finally!', font5, PINK, DISPLAYSURF, 1270, 200)
                elif(randomtext == 5):
                    draw_text('Welcome back master <3', font5, PINK, DISPLAYSURF, 1170, 175)
                elif(randomtext == 6):
                    draw_text('I got some interesting new items for you', font5, PINK, DISPLAYSURF, 1135, 175)
                    draw_text('sweetie!', font5, PINK, DISPLAYSURF, 1270, 200)
                elif(randomtext == 7):
                    draw_text('How come you havent been coming as much', font5, PINK, DISPLAYSURF, 1135, 175)
                    draw_text('lately? :(', font5, PINK, DISPLAYSURF, 1270, 200)
                pygame.display.update()
            if (self.gamescene == 12):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image58, (200, 100))
                DISPLAYSURF.blit(image53, (1070, 110))
                mouse_pos = pygame.mouse.get_pos()
                returnmenurect = pygame.Rect(200, 40, 140, 190)
                if returnmenurect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image135, (200, 100))
                else:
                    DISPLAYSURF.blit(image134, (200, 100))

                if (FaderBool):
                    Fader = Fader + .5
                    if (Fader > 110):
                        FaderBool = False
                if (FaderBool == False):
                    Fader = Fader - .5
                    if (Fader < 10):
                        FaderBool = True
                mouse_pos = pygame.mouse.get_pos()
                mouseX, mouseY = pygame.mouse.get_pos()
                DISPLAYSURF.blit(image56, (mouseX - 47, mouseY - 44))
                xrect = pygame.Rect(1680, 123, 35, 35)
                xrect2 = pygame.Rect(130, 100, 120, 80)
                mouseX, mouseY = pygame.mouse.get_pos()
                mouse_pos = pygame.mouse.get_pos()
                image42.set_alpha(Fader)
                DISPLAYSURF.blit(image42, (1655, 917))
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                for event in pygame.event.get():
                    mouseX, mouseY = pygame.mouse.get_pos()
                    if xrect.collidepoint(mouse_pos):
                        if event.type == MOUSEBUTTONDOWN:
                            if xrect.collidepoint(mouse_pos):
                                print("Quit clicked")
                                pygame.mixer.music.stop()
                                pygame.quit()
                                sys.exit()
                    else:
                        if event.type == MOUSEBUTTONDOWN:
                            if returnmenurect.collidepoint(mouse_pos):
                                transition(6)
                                self.menu_activepaimon = False
                                pygame.event.clear()
                            if 100 <= mouseX <= 1920 and 150 <= mouseY <= 1080:
                                sound_effect = pygame.mixer.Sound(resource_path("audio/clicknoise.mp3"))
                                sound_effect.play()
                                pygame.mixer.music.set_volume(0.4)
                                pygame.display.update()
                                textFader = 0
                                self.gamescene = self.gamescene + 1
                draw_text('*giggle*', font5, PINK, DISPLAYSURF, 1280, 175)
                draw_text('go take a look around sweetheart', font5, PINK, DISPLAYSURF, 1170, 200)
                pygame.display.update()
            if (self.gamescene == 13):
                self.gamescene = 7
        with open(resource_path("gamedata.txt"), "r") as file:
            lines = file.readlines()
            lines[0] = f"gold = {gold}\n"
            lines[1] = f"gem = {gem}\n"
        with open(resource_path("gamedata.txt"), "w") as file:
            file.writelines(lines)
        return 0
########################################################################################################################
########################################################################################################################
class labormarket(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.goblinmenubool = True
        self.diggingbool = True
        self.labormarketmenu()
########################################################################################################################
    def xbutton(self, gamescene):
        global FaderBool
        global Fader
        global textFader
        if (FaderBool):
            Fader = Fader + .5
            if (Fader > 110):
                FaderBool = False
        if (FaderBool == False):
            Fader = Fader - .5
            if (Fader < 10):
                FaderBool = True
        mouse_pos = pygame.mouse.get_pos()
        mouseX, mouseY = pygame.mouse.get_pos()
        xrect = pygame.Rect(1680, 123, 35, 35)
        xrect2 = pygame.Rect(130, 100, 120, 80)
        mouseX, mouseY = pygame.mouse.get_pos()
        mouse_pos = pygame.mouse.get_pos()
        image42.set_alpha(Fader)
        DISPLAYSURF.blit(image42, (1655, 917))
        draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
        if xrect.collidepoint(mouse_pos):
            draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
        for event in pygame.event.get():
            mouseX, mouseY = pygame.mouse.get_pos()
            if xrect.collidepoint(mouse_pos):
                if event.type == MOUSEBUTTONDOWN:
                    if xrect.collidepoint(mouse_pos):
                        print("Quit clicked")
                        pygame.mixer.music.stop()
                        pygame.quit()
                        sys.exit()
            else:
                if event.type == MOUSEBUTTONDOWN:
                    if 0 <= mouseX <= 1920 and 150 <= mouseY <= 1080:
                        sound_effect = pygame.mixer.Sound(resource_path("audio/clicknoise.mp3"))
                        sound_effect.play()
                        pygame.mixer.music.set_volume(0.4)

                        textFader = 0
                        return (gamescene + 1)
        return gamescene
    ########################################################################################################################
    def labormarketmenu(self):
        global FaderBool
        global Fader
        global textFader
        video = cv2.VideoCapture(resource_path("video/goldglitterbackground.mp4"))
        startTime = pygame.time.get_ticks()
        self.gamescene = 1
        mouse_pos = pygame.mouse.get_pos()
        pygame.mixer.music.load(resource_path("audio/goblindancemusic.mp3"))
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        print("labor market initialized")
        global textFader
        global characterName
        while self.goblinmenubool:
            if (self.gamescene == 1):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image137, (200, 100))
                self.gamescene = self.xbutton(self.gamescene)
                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))
                clickrect = pygame.Rect(0, 300, 1900, 1000)
                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 140, 100)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if clickrect.collidepoint(mouse_pos):
                            self.gamescene = self.gamescene + 1
                        if returnarrowrect.collidepoint(mouse_pos):
                            transition(6)
                            self.goblinmenubool = False
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()

            if (self.gamescene == 2):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image137, (200, 100))
                image4.set_alpha(210)
                DISPLAYSURF.blit(image4, (0, 880))
                draw_text_center('Welcome friend,', font13, RED, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('what brings you here today?', font13, RED, DISPLAYSURF, halfdisplay, 925)
                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))
                clickrect = pygame.Rect(0, 250, 1900, 1000)
                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 120, 70)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if returnarrowrect.collidepoint(mouse_pos):
                            transition(6)
                            self.goblinmenubool = False
                        if clickrect.collidepoint(mouse_pos):
                            self.gamescene = self.gamescene + 1
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()

            if (self.gamescene == 3):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image137, (200, 100))
                image4.set_alpha(210)
                DISPLAYSURF.blit(image4, (0, 880))
                draw_text_center('Are you looking to make some quick gold?', font13, RED, DISPLAYSURF, halfdisplay, 890)
                self.gamescene = self.xbutton(self.gamescene)
                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))
                clickrect = pygame.Rect(0, 250, 1900, 1000)
                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 120, 70)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if clickrect.collidepoint(mouse_pos):
                            self.gamescene = self.gamescene + 1
                        if returnarrowrect.collidepoint(mouse_pos):
                            transition(6)
                            self.goblinmenubool = False
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()

            if (self.gamescene == 4):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image137, (200, 100))
                image4.set_alpha(210)
                DISPLAYSURF.blit(image4, (0, 880))
                draw_text_center('Come, Come, I have a job for you', font13, RED, DISPLAYSURF, halfdisplay, 890)
                self.gamescene = self.xbutton(self.gamescene)
                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))
                clickrect = pygame.Rect(0, 250, 1900, 1000)
                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 120, 70)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if clickrect.collidepoint(mouse_pos):
                            self.gamescene = self.gamescene + 1
                        if returnarrowrect.collidepoint(mouse_pos):
                            transition(6)
                            self.goblinmenubool = False
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()

            if (self.gamescene == 5):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image137, (200, 100))
                imageBlack.set_alpha(210)
                DISPLAYSURF.blit(imageBlack, (620, 160))

                ret, frame = video.read()
                if not ret:
                    video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    continue  # Continue to the next loop iteration
                frame = cv2.resize(frame, (1550, 880))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_surface = pygame.surfarray.make_surface(frame)
                frame_surface = pygame.transform.rotate(frame_surface, -90)  # Rotate if necessary
                frame_surface = pygame.transform.flip(frame_surface, True, False)
                frame_surface.set_alpha(100)
                DISPLAYSURF.blit(frame_surface, (190, 100))

                DISPLAYSURF.blit(image138, (590, 230))
                mininrect = pygame.Rect(725, 390, 370, 80)
                pygame.draw.rect(DISPLAYSURF, WHITE, mininrect, 6)
                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))
                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 120, 70)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                if mininrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image140, (590, 230))
                    pygame.draw.rect(DISPLAYSURF, PURPLE, mininrect, 6)
                DISPLAYSURF.blit(image139, (650, 485))
                DISPLAYSURF.blit(image139, (650, 590))
                DISPLAYSURF.blit(image139, (650, 695))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if mininrect.collidepoint(mouse_pos):
                            print("mining game clicked")
                            self.repeatminigameloop = True
                            self.miningGame()
                        if returnarrowrect.collidepoint(mouse_pos):
                            transition(6)
                            self.goblinmenubool = False
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            video.release()
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()

            mouseX, mouseY = pygame.mouse.get_pos()
            image133.set_alpha(150)
            DISPLAYSURF.blit(image133, (mouseX - 41, mouseY - 37))
            pygame.display.update()
########################################################################################################################
    def miningGame(self):
        while(self.repeatminigameloop):
            self.diggingbool = True
            global miningspeed
            global miningefficiency
            global time
            global luck
            global spawnchance
            global specialefficiency
            startTime = pygame.time.get_ticks()
            scene = 1
            popcounter = 1
            mouse_pos = pygame.mouse.get_pos()
            pygame.mixer.music.load(resource_path("audio/beachmusic.mp3"))
            pygame.mixer.music.queue(resource_path("audio/fantasyhomemusic2.mp3"))
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)
            secondsextra = 0
            x = random.randint(-8100, 600)
            y = -1245
            secondstouch = 0
            looptime = 0
            timer = 0
            looptimeg =0
            timerg = 0
            looptimet =0
            timert = 0
            digs = []
            tempgold = 0
            tempgem = 0
            global gold
            global gem
            xlocation = []
            ylocation = []
            spawncounter = 10000
            tempgold2 = 0
            tempgem2 = 0

            sunlightfader = 1
            sunlightbool = True

            while spawncounter > 0:
                ylocation.append(random.randint(2000, 18500))
                xlocation.append(random.randint(0, 9500))
                spawncounter -= 1

            timecount = True
            begintime = 0
            start_ticks = 0
            while(self.diggingbool):
                with open(resource_path("gamedata.txt"), "r") as file:
                    lines = file.readlines()
                    if len(lines) >= 8:
                        goldline = lines[0].strip()
                        goldline = goldline[7:]
                        gemline = lines[1].strip()
                        gemline = gemline[6:]
                        miningspeedline = lines[5].strip()
                        miningspeedline = miningspeedline[14:]
                        miningefficiencyline = lines[6].strip()
                        miningefficiencyline = miningefficiencyline[19:]
                        timeline = lines[7].strip()
                        timeline = timeline[7:]
                        luckline = lines[8].strip()
                        luckline = luckline[7:]
                        spawnchanceline = lines[9].strip()
                        spawnchanceline = spawnchanceline[14:]
                        specialefficiencyline = lines[10].strip()
                        specialefficiencyline = specialefficiencyline[20:]
                        miningspeed = int(miningspeedline)
                        miningefficiency = int(miningefficiencyline)
                        time = int(timeline)
                        luck = int(luckline)
                        gold = int(goldline)
                        gem = int(gemline)
                        spawnchance = int(spawnchanceline)
                        specialefficiency = int(specialefficiencyline)
                        ######
                        miningspeedtemp = int(miningspeedline)
                        miningefficiencytemp = int(miningefficiencyline)
                        timetemp = int(timeline)
                        lucktemp = int(luckline)
                        spawnchancetemp = int(spawnchanceline)
                        specialefficiencytemp = int(specialefficiencyline)
                        ######
                rainbowcolor1 = int((math.sin(startTime * 0.002) + 1) * 127.5)
                rainbowcolor2 = int((math.sin(startTime * 0.003 + 2) + 1) * 127.5)
                rainbowcolor3 = int((math.sin(startTime * 0.004 + 2) + 1) * 127.5)
                rainbowcol = (rainbowcolor1, rainbowcolor2, rainbowcolor3)
                startTime = pygame.time.get_ticks()
                rainbowcolor2 = int((math.sin(startTime * 0.003 + 2) + 1) * 127.5)
                rainbowcolorr = (rainbowcolor2, 20, 20)
                if(scene == 1):
                    mouse_pos = pygame.mouse.get_pos()
                    DISPLAYSURF.fill(BLACK)
                    DISPLAYSURF.blit(image150, (x, y))

                    if(sunlightbool):
                        sunlightfader = sunlightfader + .2
                    if(sunlightbool == False):
                        sunlightfader = sunlightfader - .2
                    if(sunlightfader <= 80):
                        sunlightbool = True
                    if(sunlightfader >= 255):
                        sunlightbool = False
                    image224.set_alpha(sunlightfader)
                    DISPLAYSURF.blit(image224, (150, 100))

                    DISPLAYSURF.blit(image164, (198, 110))
                    DISPLAYSURF.blit(image168, (1450, 340))
                    draw_text('[Click to Begin]', font2, rainbowcolorr, DISPLAYSURF, 780, 690)
                    xrect = pygame.Rect(1680, 123, 35, 35)
                    beginrect = pygame.Rect(760, 680, 440, 95)
                    returnarrowrect = pygame.Rect(153, 110, 120, 70)
                    statsrect = pygame.Rect(1450, 340, 210, 180)
                    pygame.draw.rect(DISPLAYSURF, (DARKGREEN), statsrect, 6)
                    pygame.draw.rect(DISPLAYSURF, (RED), returnarrowrect, 6)
                    draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                    if statsrect.collidepoint(mouse_pos):
                        DISPLAYSURF.blit(image169, (1450, 340))
                    if xrect.collidepoint(mouse_pos):
                        draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                    if returnarrowrect.collidepoint(mouse_pos):
                        DISPLAYSURF.blit(image165, (198, 110))
                    if beginrect.collidepoint(mouse_pos):
                        draw_text('[Click to Begin]', font2, (rainbowcolor2, rainbowcolor1, rainbowcolor3), DISPLAYSURF, 780, 690)
                        pygame.draw.rect(DISPLAYSURF, (rainbowcolor1, rainbowcolor3, rainbowcolor2), beginrect, 6)

                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if beginrect.collidepoint(mouse_pos):
                                sound_effect = pygame.mixer.Sound(resource_path("audio/yippie.mp3"))
                                sound_effect.play()
                                scene = scene + 1
                            if xrect.collidepoint(mouse_pos):
                                print("Quit clicked")
                                pygame.mixer.music.stop()
                                pygame.quit()
                                sys.exit()
                            if returnarrowrect.collidepoint(mouse_pos):
                                transition(6)
                                self.repeatminigameloop = False
                                self.diggingbool = False
                            if statsrect.collidepoint(mouse_pos):
                                scene = 5

                if(scene == 2):
                    movementbool1 = True
                    movementbool2 = True
                    movementbool3 = True
                    movementbool4 = True

                    if(popcounter <= 5):
                        popcounter = popcounter + 1
                    if(popcounter > 5):
                        popcounter = 0

                    if(tempgold > 0):
                        tempgold2 = tempgold
                    if(tempgem > 0):
                        tempgem2 = tempgem
                    if(y > -1249):
                        y = -1249
                    if(y < -18819):
                        y = -18819
                    if(x > 964):
                        x = 964
                    if(x < -8480):
                        x = -8480
                    if (miningspeedtemp < 5):
                        if(len(digs) > 53):
                            digs.pop(0)
                            digs.pop(1)
                            digs.pop(2)

                    if (5 <= miningspeedtemp < 10):
                        if(len(digs) > 53):
                            digs.pop(0)
                            digs.pop(1)
                            digs.pop(2)

                    if (10 <= miningspeedtemp):
                        if(len(digs) > 53):
                            digs.pop(0)
                            digs.pop(1)
                            digs.pop(2)

                    if(timecount == True):
                        begintime = 45000 + (3000 * time)
                        start_ticks = pygame.time.get_ticks()
                        timecount = False
                    elapsed_time = pygame.time.get_ticks() - start_ticks
                    remaining_time = (begintime - elapsed_time)
                    seconds = (remaining_time // 1000) + secondsextra
                    DISPLAYSURF.fill(BLACK)
                    DISPLAYSURF.blit(image150, (x, y))
                    for element in digs:
                        if (miningspeedtemp < 5):
                            DISPLAYSURF.blit(image151, (element[0] + x, element[1] + y))
                        if (5 <= miningspeedtemp < 10):
                            DISPLAYSURF.blit(image151, (element[0] + x, element[1] + y))
                        if (10 <= miningspeedtemp):
                            DISPLAYSURF.blit(image151, (element[0] + x, element[1] + y))
                    screen_width, screen_height = DISPLAYSURF.get_size()
                    DISPLAYSURF.blit(image142, (screen_width/2, screen_height/2))
                    itemgenerationcounter = (90 + (4 * int(spawnchance)))
                    mouse_pos = pygame.mouse.get_pos()
                    while(itemgenerationcounter > 0):
                        if(itemgenerationcounter % 12 == 1):
                            screen_center = DISPLAYSURF.get_rect().center
                            xlocation[itemgenerationcounter + 6000] = xlocation[itemgenerationcounter + 6000] + random.randint(-10,10)
                            ylocation[itemgenerationcounter + 6000] = ylocation[itemgenerationcounter + 6000] + random.randint(-10,10)

                            DISPLAYSURF.blit(image156, (xlocation[itemgenerationcounter + 5000] + x, ylocation[itemgenerationcounter + 5000] + y + 5000))
                            DISPLAYSURF.blit(image157, (xlocation[itemgenerationcounter + 5500] + x, ylocation[itemgenerationcounter + 5500] + y + 3000))
                            DISPLAYSURF.blit(image158, (xlocation[itemgenerationcounter + 6000] + x, ylocation[itemgenerationcounter + 6000] + y + 1000))
                            DISPLAYSURF.blit(image159, (xlocation[itemgenerationcounter + 6500] + x, ylocation[itemgenerationcounter + 6500] + y + 10000))
                            DISPLAYSURF.blit(image161, (xlocation[itemgenerationcounter + 7000] + x, ylocation[itemgenerationcounter + 7000] + y + 5000))
                            DISPLAYSURF.blit(image162, (xlocation[itemgenerationcounter + 7500] + x, ylocation[itemgenerationcounter + 7500] + y + 7000))
                            DISPLAYSURF.blit(image163, (xlocation[itemgenerationcounter + 8000] + x, ylocation[itemgenerationcounter + 8000] + y + 9000))
                            DISPLAYSURF.blit(image160, (xlocation[itemgenerationcounter + 4500] + x, ylocation[itemgenerationcounter + 4500] + y + 2000))
                            draw_text('5 secs', font5, (0, 0, rainbowcolor3), DISPLAYSURF, xlocation[itemgenerationcounter + 8500] + x, ylocation[itemgenerationcounter + 8500] + y + 6000)
                            draw_text('3 secs', font5, (0, 0, rainbowcolor3), DISPLAYSURF, xlocation[itemgenerationcounter + 8700] + x, ylocation[itemgenerationcounter + 8700] + y + 2000)
                            draw_text('1 secs', font5, (0, 0, rainbowcolor3), DISPLAYSURF, xlocation[itemgenerationcounter + 8900] + x, ylocation[itemgenerationcounter + 8900] + y + 500)

                            gem9rect = pygame.Rect((xlocation[itemgenerationcounter + 5000] + x - 16, ylocation[itemgenerationcounter + 5000] + y - 30 + 5000, 240, 190))
                            gem10rect = pygame.Rect((xlocation[itemgenerationcounter + 5500] + x - 8, ylocation[itemgenerationcounter + 5500] + y - 20 + 3000, 85, 85))
                            gem11rect = pygame.Rect((xlocation[itemgenerationcounter + 6000] + x - 8, ylocation[itemgenerationcounter + 6000] + y - 25 + 1000, 85, 85))
                            gem12rect = pygame.Rect((xlocation[itemgenerationcounter + 6500] + x - 16, ylocation[itemgenerationcounter + 6500] + y - 30 + 10000, 100, 100))
                            gem13rect = pygame.Rect((xlocation[itemgenerationcounter + 7000] + x - 8, ylocation[itemgenerationcounter + 7000] + y - 30 + 5000, 85, 85))
                            gem14rect = pygame.Rect((xlocation[itemgenerationcounter + 7500] + x - 8, ylocation[itemgenerationcounter + 7500] + y - 30 + 7000, 85, 85))
                            gem15rect = pygame.Rect((xlocation[itemgenerationcounter + 8000] + x - 6, ylocation[itemgenerationcounter + 8000] + y - 30 + 9000, 85, 85))
                            gem8rect = pygame.Rect((xlocation[itemgenerationcounter + 4500] + x - 8, ylocation[itemgenerationcounter + 4500] + y - 30 + 2000, 85, 85))
                            text1rect = pygame.Rect((xlocation[itemgenerationcounter + 8500] + x - 6, ylocation[itemgenerationcounter + 8500] + y - 20 + 6000, 100, 55))
                            text2rect = pygame.Rect((xlocation[itemgenerationcounter + 8700] + x - 6, ylocation[itemgenerationcounter + 8700] + y - 20 + 2000, 100, 55))
                            text3rect = pygame.Rect((xlocation[itemgenerationcounter + 8900] + x - 6, ylocation[itemgenerationcounter + 8900] + y - 20 + 500, 100, 55))

                            # pygame.draw.rect(DISPLAYSURF, (WHITE), gem9rect, 5)
                            # pygame.draw.rect(DISPLAYSURF, (RED), gem10rect, 5)
                            # pygame.draw.rect(DISPLAYSURF, (BLUE), gem11rect, 5)
                            # pygame.draw.rect(DISPLAYSURF, (SKYBLUE), gem12rect, 5)
                            # pygame.draw.rect(DISPLAYSURF, (GREEN), gem13rect, 5)
                            # pygame.draw.rect(DISPLAYSURF, (BLACK), gem14rect, 5)
                            # pygame.draw.rect(DISPLAYSURF, (PURPLE), gem15rect, 5)
                            # pygame.draw.rect(DISPLAYSURF, (GOLD), gem8rect, 5)
                            # pygame.draw.rect(DISPLAYSURF, (BLACK), text1rect, 5)
                            # pygame.draw.rect(DISPLAYSURF, (BLACK), text2rect, 5)
                            # pygame.draw.rect(DISPLAYSURF, (BLACK), text3rect, 5)

                            if text1rect.collidepoint((screen_center[0], screen_center[1])):
                                print("time collected!")
                                xlocation[itemgenerationcounter + 8500] = (-20000)
                                ylocation[itemgenerationcounter + 8500] = (-20000)
                                sound_effect = pygame.mixer.Sound(resource_path("audio/scifinoise.mp3"))
                                sound_effect.play()
                                secondstouch = 5
                                secondsextra = secondsextra + 5
                                looptimet = pygame.time.get_ticks() + 2000
                                timert = pygame.time.get_ticks()
                            if text2rect.collidepoint((screen_center[0], screen_center[1])):
                                print("time collected!")
                                xlocation[itemgenerationcounter + 8700] = (-20000)
                                ylocation[itemgenerationcounter + 8700] = (-20000)
                                sound_effect = pygame.mixer.Sound(resource_path("audio/scifinoise.mp3"))
                                sound_effect.play()
                                secondstouch = 3
                                secondsextra = secondsextra + 3
                                looptimet = pygame.time.get_ticks() + 2000
                                timert = pygame.time.get_ticks()
                            if text3rect.collidepoint((screen_center[0], screen_center[1])):
                                print("time collected!")
                                xlocation[itemgenerationcounter + 8900] = (-20000)
                                ylocation[itemgenerationcounter + 8900] = (-20000)
                                sound_effect = pygame.mixer.Sound(resource_path("audio/scifinoise.mp3"))
                                sound_effect.play()
                                secondstouch = 1
                                secondsextra = secondsextra + 1
                                looptimet = pygame.time.get_ticks() + 2000
                                timert = pygame.time.get_ticks()
                            if gem9rect.collidepoint((screen_center[0] + 10, screen_center[1] + 10)):
                                print("dinosaur collected!")
                                xlocation[itemgenerationcounter + 5000] = (-20000)
                                ylocation[itemgenerationcounter + 5000] = (-20000)
                                sound_effect = pygame.mixer.Sound(resource_path("audio/itempickup.mp3"))
                                sound_effect.play()
                                tempgold = int(tempgold + (750 * (1 + (.1 * specialefficiency))))
                                looptime = pygame.time.get_ticks() + 2000
                                timer = pygame.time.get_ticks()
                                goldamount = int((750 * (1 + (.1 * specialefficiency))))
                            if gem10rect.collidepoint((screen_center[0] + 10, screen_center[1] + 10)):
                                print("crown collected!")
                                xlocation[itemgenerationcounter + 5500] = (-20000)
                                ylocation[itemgenerationcounter + 5500] = (-20000)
                                sound_effect = pygame.mixer.Sound(resource_path("audio/itempickup.mp3"))
                                sound_effect.play()
                                tempgold = int(tempgold + (100 * (1 + (.1 * specialefficiency))))
                                looptime = pygame.time.get_ticks() + 2000
                                timer = pygame.time.get_ticks()
                                goldamount = int((100 * (1 + (.1 * specialefficiency))))
                            if gem11rect.collidepoint((screen_center[0] + 10, screen_center[1] + 10)):
                                xlocation[itemgenerationcounter + 6000] = (-20000)
                                ylocation[itemgenerationcounter + 6000] = (-20000)
                                print("spider attacked!")
                                sound_effect = pygame.mixer.Sound(resource_path("audio/spidernoise.mp3"))
                                sound_effect.play()
                                gold = gold + tempgold
                                gem = gem + tempgem
                                tempgold = 0
                                tempgem = 0
                                with open(resource_path("gamedata.txt"), "r") as file:
                                    lines = file.readlines()
                                    lines[0] = f"gold = {gold}\n"
                                    lines[1] = f"gem = {gem}\n"
                                with open(resource_path("gamedata.txt"), "w") as file:
                                    file.writelines(lines)
                                scene = 4
                            if gem12rect.collidepoint((screen_center[0] + 10, screen_center[1] + 10)):
                                print("egg collected!")
                                xlocation[itemgenerationcounter + 6500] = (-20000)
                                ylocation[itemgenerationcounter + 6500] = (-20000)
                                sound_effect = pygame.mixer.Sound(resource_path("audio/swoosh.mp3"))
                                sound_effect.play()
                                tempgold = int(tempgold + (2000 * (1 + (.1 * specialefficiency))))
                                looptime = pygame.time.get_ticks() + 2000
                                timer = pygame.time.get_ticks()
                                goldamount = int((2000 * (1 + (.1 * specialefficiency))))
                            if gem13rect.collidepoint((screen_center[0] + 10, screen_center[1] + 10)):
                                print("Chest collected!")
                                xlocation[itemgenerationcounter + 7000] = (-20000)
                                ylocation[itemgenerationcounter + 7000] = (-20000)
                                sound_effect = pygame.mixer.Sound(resource_path("audio/treasureopen.mp3"))
                                sound_effect.play()
                                goldamount = int(random.randint(int(200 + (10 * luck)), int(500 * (1 + (.1 * specialefficiency)))))
                                tempgold = tempgold + goldamount
                                looptime = pygame.time.get_ticks() + 2000
                                timer = pygame.time.get_ticks()
                            if gem14rect.collidepoint((screen_center[0] + 10, screen_center[1] + 10)):
                                print("Chest collected!")
                                xlocation[itemgenerationcounter + 7500] = (-20000)
                                ylocation[itemgenerationcounter + 7500] = (-20000)
                                sound_effect = pygame.mixer.Sound(resource_path("audio/treasureopen.mp3"))
                                sound_effect.play()
                                goldamount = int(random.randint(int(200 + (10 * luck)), int(700 * (1 + (.1 * specialefficiency)))))
                                tempgold = tempgold + goldamount
                                looptime = pygame.time.get_ticks() + 2000
                                timer = pygame.time.get_ticks()
                            if gem15rect.collidepoint((screen_center[0] + 10, screen_center[1] + 10)):
                                print("Chest collected!")
                                xlocation[itemgenerationcounter + 8000] = (-20000)
                                ylocation[itemgenerationcounter + 8000] = (-20000)
                                sound_effect = pygame.mixer.Sound(resource_path("audio/treasureopen.mp3"))
                                sound_effect.play()
                                goldamount = int(random.randint(int(10 + (30 * luck)), int(1500 * (1 + (.1 * specialefficiency)))))
                                tempgold = tempgold + goldamount
                                looptime = pygame.time.get_ticks() + 2000
                                timer = pygame.time.get_ticks()
                            if gem8rect.collidepoint((screen_center[0] + 10, screen_center[1] + 10)):
                                print("Chest collected!")
                                xlocation[itemgenerationcounter + 4500] = (-20000)
                                ylocation[itemgenerationcounter + 4500] = (-20000)
                                sound_effect = pygame.mixer.Sound(resource_path("audio/treasureopen.mp3"))
                                sound_effect.play()
                                goldamount = int(random.randint(int(30 + (2 * luck)), int(80 * (1 + (.1 * specialefficiency)))))
                                tempgold = tempgold + goldamount
                                looptime = pygame.time.get_ticks() + 2000
                                timer = pygame.time.get_ticks()
                        ###############################
                        DISPLAYSURF.blit(image143, (xlocation[itemgenerationcounter] + x, ylocation[itemgenerationcounter] + y))
                        DISPLAYSURF.blit(image144, (xlocation[itemgenerationcounter + 1000] + x, ylocation[itemgenerationcounter + 1000] + y))
                        DISPLAYSURF.blit(image145, (xlocation[itemgenerationcounter + 2000] + x, ylocation[itemgenerationcounter + 2000] + y + 1000))
                        DISPLAYSURF.blit(image146, (xlocation[itemgenerationcounter + 3000] + x, ylocation[itemgenerationcounter + 3000] + y + 2000))
                        DISPLAYSURF.blit(image147, (xlocation[itemgenerationcounter + 4000] + x, ylocation[itemgenerationcounter + 4000] + y + 5000))

                        DISPLAYSURF.blit(image154, (xlocation[itemgenerationcounter + 2500] + x, ylocation[itemgenerationcounter + 2500] + y + 1000))
                        DISPLAYSURF.blit(image155, (xlocation[itemgenerationcounter + 3500] + x, ylocation[itemgenerationcounter + 3500] + y + 1500))

                        DISPLAYSURF.blit(image166, (xlocation[itemgenerationcounter + 3700] + x, ylocation[itemgenerationcounter + 3700] + y + 4500))
                        DISPLAYSURF.blit(image167, (xlocation[itemgenerationcounter + 3900] + x, ylocation[itemgenerationcounter + 3900] + y + 7500))

                        randomcritter = itemgenerationcounter % 4
                        if (randomcritter == 1):
                            DISPLAYSURF.blit(image257, (xlocation[itemgenerationcounter + 4250] + x, ylocation[itemgenerationcounter + 4250] + y + 3000))
                        if (randomcritter == 2):
                            DISPLAYSURF.blit(image258, (xlocation[itemgenerationcounter + 4250] + x, ylocation[itemgenerationcounter + 4250] + y + 3000))
                        if (randomcritter == 0):
                            DISPLAYSURF.blit(image259, (xlocation[itemgenerationcounter + 4250] + x, ylocation[itemgenerationcounter + 4250] + y + 3000))
                        if (randomcritter == 3):
                            DISPLAYSURF.blit(image260, (xlocation[itemgenerationcounter + 4250] + x, ylocation[itemgenerationcounter + 4250] + y + 3000))

                        batrect = pygame.Rect((xlocation[itemgenerationcounter + 4250] + x - 16, ylocation[itemgenerationcounter + 4250] + y - 30 + 3000, 120, 90))

                        DISPLAYSURF.blit(image261, (xlocation[itemgenerationcounter + 4750] + x, ylocation[itemgenerationcounter + 4750] + y + 1000))
                        boulderect = pygame.Rect((xlocation[itemgenerationcounter + 4750] + x - 16, ylocation[itemgenerationcounter + 4750] + y - 10 + 1000, 210, 150))


                        gem1rect = pygame.Rect((xlocation[itemgenerationcounter] + x - 15, ylocation[itemgenerationcounter] + y - 40, 70, 70))
                        gem2rect = pygame.Rect((xlocation[itemgenerationcounter + 1000] + x - 20, ylocation[itemgenerationcounter + 1000] + y - 35, 65, 65))
                        gem3rect = pygame.Rect((xlocation[itemgenerationcounter + 2000] + x - 20, ylocation[itemgenerationcounter + 2000] + y - 25 + 1000, 65, 65))
                        gem4rect = pygame.Rect((xlocation[itemgenerationcounter + 3000] + x - 20, ylocation[itemgenerationcounter + 3000] + y - 25 + 2000, 65, 65))
                        gem5rect = pygame.Rect((xlocation[itemgenerationcounter + 4000] + x - 20, ylocation[itemgenerationcounter + 4000] + y - 25 + 5000, 65, 65))

                        gem6rect = pygame.Rect((xlocation[itemgenerationcounter + 2500] + x - 20, ylocation[itemgenerationcounter + 2500] + y - 25 + 1000, 65, 60))
                        gem7rect = pygame.Rect((xlocation[itemgenerationcounter + 3500] + x - 20, ylocation[itemgenerationcounter + 3500] + y - 25 + 1500, 65, 65))

                        lava1rect = pygame.Rect((xlocation[itemgenerationcounter + 3700] + x + 80, ylocation[itemgenerationcounter + 3700] + y - 10 + 4500, 210, 200))
                        lava2rect = pygame.Rect((xlocation[itemgenerationcounter + 3900] + x + 10, ylocation[itemgenerationcounter + 3900] + y - 0 + 7500, 280, 410))

                        # pygame.draw.rect(DISPLAYSURF, (WHITE), gem1rect, 5)
                        # pygame.draw.rect(DISPLAYSURF, (RED), gem2rect, 5)
                        # pygame.draw.rect(DISPLAYSURF, (BLUE), gem3rect, 5)
                        # pygame.draw.rect(DISPLAYSURF, (SKYBLUE), gem4rect, 5)
                        # pygame.draw.rect(DISPLAYSURF, (GREEN), gem5rect, 5)
                        # pygame.draw.rect(DISPLAYSURF, (BLACK), gem6rect, 5)
                        # pygame.draw.rect(DISPLAYSURF, (PURPLE), gem7rect, 5)
                        # pygame.draw.rect(DISPLAYSURF, (RED), lava1rect, 5)
                        # pygame.draw.rect(DISPLAYSURF, (RED), lava2rect, 5)
                        screen_center = DISPLAYSURF.get_rect().center
                        speed = .9 + (.20 * miningspeed)

                        batrect2 = pygame.Rect((xlocation[itemgenerationcounter + 4250] + x - 500, ylocation[itemgenerationcounter + 4250] + y - 500 + 3000, 1000, 1000))

                        if boulderect.collidepoint((screen_center[0] + 10, screen_center[1] + 10 + speed)):
                            movementbool1 = False
                        if boulderect.collidepoint((screen_center[0] + 10, screen_center[1] + 10 - speed)):
                            movementbool2 = False
                        if boulderect.collidepoint((screen_center[0] + 10 + speed, screen_center[1] + 10)):
                            movementbool3 = False
                        if boulderect.collidepoint((screen_center[0] + 10 - speed, screen_center[1] + 10)):
                            movementbool4 = False

                        if batrect2.collidepoint((screen_center[0] + 10, screen_center[1] + 10)):
                            if((screen_center[0] + 10) >  xlocation[itemgenerationcounter + 4250] + x):
                                xlocation[itemgenerationcounter + 4250] = xlocation[itemgenerationcounter + 4250] + 1
                            if((screen_center[0] + 10) <  xlocation[itemgenerationcounter + 4250] + x):
                                xlocation[itemgenerationcounter + 4250] = xlocation[itemgenerationcounter + 4250] - 1
                            if ((screen_center[1] + 10) > ylocation[itemgenerationcounter + 4250] + y + 3000):
                                ylocation[itemgenerationcounter + 4250] = ylocation[itemgenerationcounter + 4250] + 1
                            if ((screen_center[1] + 10) < ylocation[itemgenerationcounter + 4250] + y + 3000):
                                ylocation[itemgenerationcounter + 4250] = ylocation[itemgenerationcounter + 4250] - 1

                        if batrect.collidepoint((screen_center[0] + 10, screen_center[1] + 10)):
                            xlocation[itemgenerationcounter + 4250] = (-20000)
                            ylocation[itemgenerationcounter + 4250] = (-20000)
                            print("Bat attacked!")
                            sound_effect = pygame.mixer.Sound(resource_path("audio/critternoise.mp3"))
                            sound_effect.play()
                            gold = gold + tempgold
                            gem = gem + tempgem
                            tempgold = 0
                            tempgem = 0
                            with open(resource_path("gamedata.txt"), "r") as file:
                                lines = file.readlines()
                                lines[0] = f"gold = {gold}\n"
                                lines[1] = f"gem = {gem}\n"
                            with open(resource_path("gamedata.txt"), "w") as file:
                                file.writelines(lines)
                            scene = 4
                        if lava1rect.collidepoint((screen_center[0] + 10, screen_center[1] + 10)):
                            xlocation[itemgenerationcounter + 3700] = (-20000)
                            ylocation[itemgenerationcounter + 3700] = (-20000)
                            print("Jumped into Lava!")
                            sound_effect = pygame.mixer.Sound(resource_path("audio/lavanoise.mp3"))
                            sound_effect.play()
                            gold = gold + tempgold
                            gem = gem + tempgem
                            tempgold = 0
                            tempgem = 0
                            with open(resource_path("gamedata.txt"), "r") as file:
                                lines = file.readlines()
                                lines[0] = f"gold = {gold}\n"
                                lines[1] = f"gem = {gem}\n"
                            with open(resource_path("gamedata.txt"), "w") as file:
                                file.writelines(lines)
                            scene = 4
                        if lava2rect.collidepoint((screen_center[0] + 10, screen_center[1] + 10)):
                            xlocation[itemgenerationcounter + 3900] = (-20000)
                            ylocation[itemgenerationcounter + 3900] = (-20000)
                            print("Jumped into Lava!")
                            sound_effect = pygame.mixer.Sound(resource_path("audio/lavanoise.mp3"))
                            sound_effect.play()
                            gold = gold + tempgold
                            gem = gem + tempgem
                            tempgold = 0
                            tempgem = 0
                            with open(resource_path("gamedata.txt"), "r") as file:
                                lines = file.readlines()
                                lines[0] = f"gold = {gold}\n"
                                lines[1] = f"gem = {gem}\n"
                            with open(resource_path("gamedata.txt"), "w") as file:
                                file.writelines(lines)
                            scene = 4
                        if gem1rect.collidepoint((screen_center[0],screen_center[1])):
                            print("gem collected!")
                            xlocation[itemgenerationcounter] = (-20000)
                            ylocation[itemgenerationcounter] = (-20000)
                            sound_effect = pygame.mixer.Sound(resource_path("audio/nextlevel.mp3"))
                            sound_effect.play()
                            tempgold = int(tempgold + (10 * (1 + (.1 * miningefficiency))))
                            looptime = pygame.time.get_ticks() + 2000
                            timer = pygame.time.get_ticks()
                            goldamount = int((10 * (1 + (.1 * miningefficiency))))
                        if gem2rect.collidepoint((screen_center[0] + 10, screen_center[1] + 10)):
                            print("gem collected!")
                            xlocation[itemgenerationcounter + 1000] = (-20000)
                            ylocation[itemgenerationcounter + 1000] = (-20000)
                            sound_effect = pygame.mixer.Sound(resource_path("audio/nextlevel.mp3"))
                            sound_effect.play()
                            tempgold = int(tempgold + (5 * (1 + (.1 * miningefficiency))))
                            looptime = pygame.time.get_ticks() + 2000
                            timer = pygame.time.get_ticks()
                            goldamount = int((5 * (1 + (.1 * miningefficiency))))
                        if gem3rect.collidepoint((screen_center[0] + 10, screen_center[1] + 10)):
                            print("gem collected!")
                            xlocation[itemgenerationcounter + 2000] = (-20000)
                            ylocation[itemgenerationcounter + 2000] = (-20000)
                            sound_effect = pygame.mixer.Sound(resource_path("audio/nextlevel.mp3"))
                            sound_effect.play()
                            tempgold = int(tempgold + (7 * (1 + (.1 * miningefficiency))))
                            looptime = pygame.time.get_ticks() + 2000
                            timer = pygame.time.get_ticks()
                            goldamount = int((7 * (1 + (.1 * miningefficiency))))
                        if gem4rect.collidepoint((screen_center[0] + 10, screen_center[1] + 10)):
                            print("gem collected!")
                            xlocation[itemgenerationcounter + 3000] = (-20000)
                            ylocation[itemgenerationcounter + 3000] = (-20000)
                            sound_effect = pygame.mixer.Sound(resource_path("audio/nextlevel.mp3"))
                            sound_effect.play()
                            tempgold = int(tempgold + (20 * (1 + (.1 * miningefficiency))))
                            looptime = pygame.time.get_ticks() + 2000
                            timer = pygame.time.get_ticks()
                            goldamount = int((20 * (1 + (.1 * miningefficiency))))
                        if gem5rect.collidepoint((screen_center[0] + 10, screen_center[1] + 10)):
                            print("gem collected!")
                            xlocation[itemgenerationcounter + 4000] = (-20000)
                            ylocation[itemgenerationcounter + 4000] = (-20000)
                            sound_effect = pygame.mixer.Sound(resource_path("audio/nextlevel.mp3"))
                            sound_effect.play()
                            tempgold = int(tempgold + (3 * (1 + (.1 * miningefficiency))))
                            looptime = pygame.time.get_ticks() + 2000
                            timer = pygame.time.get_ticks()
                            goldamount = int((3 * (1 + (.1 * miningefficiency))))
                        if gem6rect.collidepoint((screen_center[0] + 10, screen_center[1] + 10)):
                            print("trilobite collected!")
                            xlocation[itemgenerationcounter + 2500] = (-20000)
                            ylocation[itemgenerationcounter + 2500] = (-20000)
                            sound_effect = pygame.mixer.Sound(resource_path("audio/nextlevel.mp3"))
                            sound_effect.play()
                            tempgold = int(tempgold + (1 * (1 + (.5 * specialefficiency))))
                            looptime = pygame.time.get_ticks() + 2000
                            timer = pygame.time.get_ticks()
                            goldamount = int((1 * (1 + (.5 * specialefficiency))))
                        if gem7rect.collidepoint((screen_center[0] + 10, screen_center[1] + 10)):
                            print("special gem collected!")
                            xlocation[itemgenerationcounter + 3500] = (-20000)
                            ylocation[itemgenerationcounter + 3500] = (-20000)
                            sound_effect = pygame.mixer.Sound(resource_path("audio/nextlevel.mp3"))
                            sound_effect.play()
                            tempgem = int(tempgem + (1 * (1 + (.25 * specialefficiency))))
                            looptimeg = pygame.time.get_ticks() + 2000
                            timerg = pygame.time.get_ticks()
                        itemgenerationcounter = itemgenerationcounter - 1

                    if(looptime > timer):
                        timer = pygame.time.get_ticks()
                        draw_text_center('gained ' +str(goldamount) +' gold!', font5, GOLD, DISPLAYSURF, halfdisplay, screen_height/2 - 240)

                    if(looptimeg > timerg):
                        timerg = pygame.time.get_ticks()
                        draw_text_center('gained a gem!', font5, BLUE, DISPLAYSURF, halfdisplay , screen_height/2 - 210)

                    if(looptimet > timert):
                        timert = pygame.time.get_ticks()
                        draw_text_center('gained ' +str(secondstouch) +' seconds!', font5, (0, 0, rainbowcolor3), DISPLAYSURF, halfdisplay, screen_height/2 - 180)
                    speed = .9 + (.20 * miningspeed)
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_s:
                                if(movementbool1 == True):
                                    y = y - speed
                                    if(popcounter == 3):
                                        digs.append(((-x + screen_width / 2), (-y + screen_height / 2)))
                            elif event.key == pygame.K_w:
                                if(movementbool2 == True):
                                    y = y + speed
                                    if(popcounter == 3):
                                        digs.append(((-x + screen_width / 2), (-y + screen_height / 2)))
                            elif event.key == pygame.K_d:
                                if(movementbool3 == True):
                                    x = x - speed
                                    if(popcounter == 3):
                                        digs.append(((-x + screen_width / 2), (-y + screen_height / 2)))
                            elif event.key == pygame.K_a:
                                if(movementbool4 == True):
                                    x = x + speed
                                    if(popcounter == 3):
                                        digs.append(((-x + screen_width / 2), (-y + screen_height / 2)))
                            elif event.key == pygame.K_UP:
                                if(movementbool2 == True):
                                    y = y + speed
                                    if(popcounter == 3):
                                        digs.append(((-x + screen_width / 2), (-y + screen_height / 2)))
                            elif event.key == pygame.K_DOWN:
                                if(movementbool1 == True):
                                    y = y - speed
                                    if(popcounter == 3):
                                        digs.append(((-x + screen_width / 2), (-y + screen_height / 2)))
                            elif event.key == pygame.K_LEFT:
                                if(movementbool4 == True):
                                    x = x + speed
                                    if(popcounter == 3):
                                        digs.append(((-x + screen_width / 2), (-y + screen_height / 2)))
                            elif event.key == pygame.K_RIGHT:
                                if(movementbool3 == True):
                                    x = x - speed
                                    if(popcounter == 3):
                                        digs.append(((-x + screen_width / 2), (-y + screen_height / 2)))
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if returnarrowrect.collidepoint(mouse_pos):
                                transition(6)
                                self.gamescene == 1
                                self.diggingbool = False
                                tempgem = 0
                                tempgem2 = 0
                                tempgold = 0
                                tempgold2 = 0
                            if xrect.collidepoint(mouse_pos):
                                print("Quit clicked")
                                pygame.mixer.music.stop()
                                pygame.quit()
                                sys.exit()
                    keys = pygame.key.get_pressed()

                    # Check if specific keys are being held down
                    if keys[pygame.K_s]:
                        if (movementbool1 == True):
                            y = y - speed
                            if (popcounter == 3):
                                digs.append(((-x + screen_width / 2), (-y + screen_height / 2)))
                    if keys[pygame.K_w]:
                        if (movementbool2 == True):
                            y = y + speed
                            if (popcounter == 3):
                                digs.append(((-x + screen_width / 2), (-y + screen_height / 2)))
                    if keys[pygame.K_d]:
                        if (movementbool3 == True):
                            x = x - speed
                            if (popcounter == 3):
                                digs.append(((-x + screen_width / 2), (-y + screen_height / 2)))
                    if keys[pygame.K_a]:
                        if (movementbool4 == True):
                            x = x + speed
                            if (popcounter == 3):
                                digs.append(((-x + screen_width / 2), (-y + screen_height / 2)))
                    if keys[pygame.K_UP]:
                        if (movementbool2 == True):
                            y = y + speed
                            if (popcounter == 3):
                                digs.append(((-x + screen_width / 2), (-y + screen_height / 2)))
                    if keys[pygame.K_DOWN]:
                        if (movementbool1 == True):
                            y = y - speed
                            if (popcounter == 3):
                                digs.append(((-x + screen_width / 2), (-y + screen_height / 2)))
                    if keys[pygame.K_LEFT]:
                        if (movementbool4 == True):
                            x = x + speed
                            if (popcounter == 3):
                                digs.append(((-x + screen_width / 2), (-y + screen_height / 2)))
                    if keys[pygame.K_RIGHT]:
                        if (movementbool3 == True):
                            x = x - speed
                            if (popcounter == 3):
                                digs.append(((-x + screen_width / 2), (-y + screen_height / 2)))
                    draw_text_center(str(seconds) +" seconds remaining", font4, rainbowcol, DISPLAYSURF, halfdisplay, screen_height/2 - 400)
                    if seconds <= 0:
                        print("Time's up!")
                        gold = gold + tempgold
                        gem = gem + tempgem
                        tempgold = 0
                        tempgem = 0
                        with open(resource_path("gamedata.txt"), "r") as file:
                            lines = file.readlines()
                            lines[0] = f"gold = {gold}\n"
                            lines[1] = f"gem = {gem}\n"
                        with open(resource_path("gamedata.txt"), "w") as file:
                            file.writelines(lines)
                        scene = 3
                    xrect = pygame.Rect(1680, 123, 35, 35)
                    returnarrowrect = pygame.Rect(150, 110, 120, 70)
                    draw_text('gold collected', font5, BLACK, DISPLAYSURF, 300, 135)
                    draw_text(str(tempgold2), font5, YELLOW, DISPLAYSURF, 445, 135)
                    draw_text('gems collected', font5, PURPLE, DISPLAYSURF, 520, 135)
                    draw_text(str(tempgem2), font5, BLUE, DISPLAYSURF, 665, 135)
                    draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                    DISPLAYSURF.blit(image152, (198, 110))
                    pygame.draw.rect(DISPLAYSURF, (RED), xrect, 6)
                    pygame.draw.rect(DISPLAYSURF, (RED), returnarrowrect, 6)
                    if xrect.collidepoint(mouse_pos):
                        draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                    if returnarrowrect.collidepoint(mouse_pos):
                        DISPLAYSURF.blit(image153, (198, 110))

                if(scene == 3):
                    mouse_pos = pygame.mouse.get_pos()
                    screen_width, screen_height = DISPLAYSURF.get_size()
                    draw_text_center("Times Up", font4, BLACK, DISPLAYSURF, halfdisplay, screen_height/2 - 300)
                    enddayrect = pygame.Rect(screen_width/2 - 80, screen_height/2 - 55, 210, 100)
                    enddayrect2 = pygame.Rect(screen_width/2 - 80, screen_height/2 - 55, 210, 100)
                    pygame.draw.rect(DISPLAYSURF, (BLACK), enddayrect)
                    draw_text("End Day?", font4, (rainbowcolor2,0,0), DISPLAYSURF, screen_width/2 - 60, screen_height/2 - 45)
                    xrect = pygame.Rect(1680, 123, 35, 35)
                    returnarrowrect = pygame.Rect(150, 110, 120, 70)
                    if enddayrect.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (WHITE), enddayrect2, 5)
                    if xrect.collidepoint(mouse_pos):
                        draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                    if returnarrowrect.collidepoint(mouse_pos):
                        DISPLAYSURF.blit(image153, (198, 110))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if enddayrect.collidepoint(mouse_pos):
                                transition(6)
                                sound_effect = pygame.mixer.Sound(resource_path("audio/scifinoise.mp3"))
                                sound_effect.play()
                                self.diggingbool = False
                                tempgold2 = 0
                                tempgold = 0
                                tempgem = 0
                                tempgem2 = 0

                            if returnarrowrect.collidepoint(mouse_pos):
                                transition(6)
                                self.gamescene == 1
                                self.diggingbool = False
                                tempgold = 0
                                tempgold2 = 0
                                tempgem = 0
                                tempgem2 = 0

                            if xrect.collidepoint(mouse_pos):
                                print("Quit clicked")
                                pygame.mixer.music.stop()
                                pygame.quit()
                                sys.exit()

                if(scene == 4):
                    mouse_pos = pygame.mouse.get_pos()
                    screen_width, screen_height = DISPLAYSURF.get_size()
                    draw_text_center("YOU DIED", font19, RED, DISPLAYSURF, halfdisplay, screen_height/2 - 300)
                    enddayrect = pygame.Rect(screen_width/2 - 50, screen_height/2 - 70, 230, 105)
                    enddayrect2 = pygame.Rect(screen_width/2 - 50, screen_height/2 - 70, 230, 105)
                    pygame.draw.rect(DISPLAYSURF, (BLACK), enddayrect)
                    draw_text("Try Again?", font4, PURPLE, DISPLAYSURF, screen_width/2 - 55, screen_height/2 - 35)
                    xrect = pygame.Rect(1680, 123, 35, 35)
                    returnarrowrect = pygame.Rect(150, 110, 120, 70)
                    if enddayrect.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (WHITE), enddayrect2, 5)
                    if xrect.collidepoint(mouse_pos):
                        draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                    if returnarrowrect.collidepoint(mouse_pos):
                        DISPLAYSURF.blit(image153, (198, 110))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if enddayrect.collidepoint(mouse_pos):
                                sound_effect = pygame.mixer.Sound(resource_path("audio/clicknoise.mp3"))
                                sound_effect.play()
                                transition(6)
                                self.diggingbool = False
                                tempgold2 = 0
                                tempgem2 = 0
                            if returnarrowrect.collidepoint(mouse_pos):
                                sound_effect = pygame.mixer.Sound(resource_path("audio/success.mp3"))
                                sound_effect.play()
                                transition(6)
                                self.gamescene == 1
                                self.diggingbool = False
                                tempgold2 = 0
                                tempgem2 = 0
                            if xrect.collidepoint(mouse_pos):
                                print("Quit clicked")
                                pygame.mixer.music.stop()
                                pygame.quit()
                                sys.exit()

                if(scene == 5):
                    startTime = pygame.time.get_ticks()
                    rainbowcolor1 = int((math.sin(startTime * 0.001) + 1) * 127.5)
                    rainbowcolor2 = int((math.sin(startTime * 0.006 + 2) + 1) * 127.5)
                    rainbowcolor3 = int((math.sin(startTime * 0.003 + 2) + 1) * 127.5)
                    color1 = (rainbowcolor1,rainbowcolor3,rainbowcolor2)
                    mouse_pos = pygame.mouse.get_pos()
                    imageBlack.set_alpha(210)
                    DISPLAYSURF.blit(imageBlack, (620, 160))
                    DISPLAYSURF.blit(image170, (380, 105))
                    draw_text('gold-', font5, GOLD, DISPLAYSURF, 300, 135)
                    draw_text(str(gold), font5, YELLOW, DISPLAYSURF, 360, 135)
                    draw_text('gems-', font5, PURPLE, DISPLAYSURF, 520, 135)
                    draw_text(str(gem), font5, BLUE, DISPLAYSURF, 580, 135)

                    draw_text('x', font19, BLACK, DISPLAYSURF, 1685, 105)
                    draw_text('+', font2, GREEN, DISPLAYSURF, 1380, 750)
                    draw_text('+', font2, GREEN, DISPLAYSURF, 1380, 660)
                    draw_text('+', font2, GREEN, DISPLAYSURF, 1380, 570)
                    draw_text('+', font2, GREEN, DISPLAYSURF, 1380, 480)
                    draw_text('+', font2, GREEN, DISPLAYSURF, 1380, 400)
                    draw_text('+', font2, GREEN, DISPLAYSURF, 1380, 310)
                    plusrect1 = pygame.Rect(1365, 755, 65, 60)
                    plusrect2 = pygame.Rect(1365, 665, 65, 60)
                    plusrect3 = pygame.Rect(1365, 575, 65, 60)
                    plusrect4 = pygame.Rect(1365, 485, 65, 60)
                    plusrect5 = pygame.Rect(1365, 405, 65, 60)
                    plusrect6 = pygame.Rect(1365, 315, 65, 60)
                    pygame.draw.rect(DISPLAYSURF, (RED), plusrect1, 5)
                    pygame.draw.rect(DISPLAYSURF, (RED), plusrect2, 5)
                    pygame.draw.rect(DISPLAYSURF, (RED), plusrect3, 5)
                    pygame.draw.rect(DISPLAYSURF, (RED), plusrect4, 5)
                    pygame.draw.rect(DISPLAYSURF, (RED), plusrect5, 5)
                    pygame.draw.rect(DISPLAYSURF, (RED), plusrect6, 5)

                    DISPLAYSURF.blit(image152, (198, 110))
                    xrect = pygame.Rect(1680, 123, 35, 35)
                    returnarrowrect = pygame.Rect(150, 110, 120, 70)

                    if plusrect1.collidepoint(mouse_pos):
                        draw_text((str(10 * specialefficiencytemp)) +' gems', font2, (rainbowcolor2, rainbowcolor1, rainbowcolor3), DISPLAYSURF, 1160, 230)
                        draw_text('+', font2, color1, DISPLAYSURF, 1380, 750)
                    if plusrect2.collidepoint(mouse_pos):
                        draw_text((str(8 * spawnchancetemp)) +' gems', font2, (rainbowcolor2, rainbowcolor1, rainbowcolor3), DISPLAYSURF, 1160, 230)
                        draw_text('+', font2, color1, DISPLAYSURF, 1380, 660)
                    if plusrect3.collidepoint(mouse_pos):
                        draw_text((str(3 * lucktemp)) +' gems', font2, (rainbowcolor2, rainbowcolor1, rainbowcolor3), DISPLAYSURF, 1160, 230)
                        draw_text('+', font2, color1, DISPLAYSURF, 1380, 570)
                    if plusrect4.collidepoint(mouse_pos):
                        draw_text((str(3 * timetemp)) +' gems', font2, (rainbowcolor2, rainbowcolor1, rainbowcolor3), DISPLAYSURF, 1160, 230)
                        draw_text('+', font2, color1, DISPLAYSURF, 1380, 480)
                    if plusrect5.collidepoint(mouse_pos):
                        draw_text((str(5 * miningefficiencytemp)) +' gems', font2, (rainbowcolor2, rainbowcolor1, rainbowcolor3), DISPLAYSURF, 1160, 230)
                        draw_text('+', font2, color1, DISPLAYSURF, 1380, 400)
                    if plusrect6.collidepoint(mouse_pos):
                        draw_text((str(3 * miningspeedtemp)) +' gems', font2, (rainbowcolor2, rainbowcolor1, rainbowcolor3), DISPLAYSURF, 1160, 230)
                        draw_text('+', font2, color1, DISPLAYSURF, 1380, 310)


                    image171.set_alpha(220)
                    while(miningspeedtemp > 0):
                        DISPLAYSURF.blit(image171, (535 + (49.4 * miningspeedtemp), 321))
                        miningspeedtemp = miningspeedtemp - 1
                    while(miningefficiencytemp > 0):
                        DISPLAYSURF.blit(image171, (534 + (49.4 * miningefficiencytemp), 408.5))
                        miningefficiencytemp = miningefficiencytemp - 1
                    while(timetemp > 0):
                        DISPLAYSURF.blit(image171, (532 + (49.4 * timetemp), 493.2))
                        timetemp = timetemp - 1
                    while(lucktemp > 0):
                        DISPLAYSURF.blit(image171, (533 + (49.4 * lucktemp), 578))
                        lucktemp = lucktemp - 1
                    while(spawnchancetemp > 0):
                        DISPLAYSURF.blit(image171, (532 + (49.4 * spawnchancetemp), 665.4))
                        spawnchancetemp = spawnchancetemp - 1
                    while(specialefficiencytemp > 0):
                        DISPLAYSURF.blit(image171, (531 + (49.4 * specialefficiencytemp), 750.5))
                        specialefficiencytemp = specialefficiencytemp - 1

                    if xrect.collidepoint(mouse_pos):
                        draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                    if returnarrowrect.collidepoint(mouse_pos):
                        DISPLAYSURF.blit(image153, (198, 110))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if returnarrowrect.collidepoint(mouse_pos):
                                scene = 1
                            if xrect.collidepoint(mouse_pos):
                                print("Quit clicked")
                                pygame.mixer.music.stop()
                                pygame.quit()
                                sys.exit()
                            if plusrect6.collidepoint(mouse_pos):
                                if(miningspeed != 16):
                                    if(gem >= (3 * miningspeed)):
                                        gem = (gem - (3 * miningspeed))
                                        miningspeed = miningspeed + 1
                                        sound_effect = pygame.mixer.Sound(resource_path("audio/success.mp3"))
                                        sound_effect.play()
                            if plusrect5.collidepoint(mouse_pos):
                                if(miningefficiency != 16):
                                    if(gem >= (5 * miningefficiency)):
                                        gem = gem - ((5 * miningefficiency))
                                        miningefficiency = miningefficiency + 1
                                        sound_effect = pygame.mixer.Sound(resource_path("audio/success.mp3"))
                                        sound_effect.play()
                            if plusrect4.collidepoint(mouse_pos):
                                if(time != 16):
                                    if(gem >= (3 * time)):
                                        gem = gem - ((3 * time))
                                        time = time + 1
                                        sound_effect = pygame.mixer.Sound(resource_path("audio/success.mp3"))
                                        sound_effect.play()
                            if plusrect3.collidepoint(mouse_pos):
                                if(luck != 16):
                                    if(gem >= (3 * luck)):
                                        gem = gem - ((3 * luck))
                                        luck = luck + 1
                                        sound_effect = pygame.mixer.Sound(resource_path("audio/success.mp3"))
                                        sound_effect.play()
                            if plusrect2.collidepoint(mouse_pos):
                                if(spawnchance != 16):
                                    if(gem >= (8 * spawnchance)):
                                        gem = (gem - (8 * spawnchance))
                                        spawnchance = spawnchance + 1
                                        sound_effect = pygame.mixer.Sound(resource_path("audio/success.mp3"))
                                        sound_effect.play()
                            if plusrect1.collidepoint(mouse_pos):
                                if(specialefficiency != 16):
                                    if(gem >= (10 * specialefficiency)):
                                        gem = (gem - (10 * specialefficiency))
                                        specialefficiency = specialefficiency + 1
                                        sound_effect = pygame.mixer.Sound(resource_path("audio/success.mp3"))
                                        sound_effect.play()
                            with open(resource_path("gamedata.txt"), "r") as file:
                                lines = file.readlines()
                                lines[0] = f"gold = {gold}\n"
                                lines[1] = f"gem = {gem}\n"
                                lines[5] = f"miningspeed = {miningspeed}\n"
                                lines[6] = f"miningefficiency = {miningefficiency}\n"
                                lines[7] = f"time = {time}\n"
                                lines[8] = f"luck = {luck}\n"
                                lines[9] = f"spawnchance = {spawnchance}\n"
                                lines[10] = f"specialefficiency = {specialefficiency}\n"
                            with open(resource_path("gamedata.txt"), "w") as file:
                                file.writelines(lines)

                pygame.display.update()
########################################################################################################################

class casino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.casinomenubool = True
        self.casinomenu()
########################################################################################################################
    def yourbroke(self):
        startTime  = pygame.time.get_ticks()
        completeTime = startTime + 600
        sound_effect = pygame.mixer.Sound(resource_path("audio/error.mp3"))
        sound_effect.play()
        while(completeTime > startTime):
            startTime = pygame.time.get_ticks()
            draw_text_center("NOT ENOUGH GOLD", font20, PINK, DISPLAYSURF, halfdisplay, 500)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("stop clicking so damn much")

        return 0
    ########################################################################################################################
    def casinomenu(self):
        global FaderBool
        global Fader
        global textFader
        video = cv2.VideoCapture(resource_path("video/casinobackgroundglow.mp4"))
        startTime = pygame.time.get_ticks()
        self.gamescene = 1
        mouse_pos = pygame.mouse.get_pos()
        pygame.mixer.music.load(resource_path("audio/casinostartmusic.mp3"))
        pygame.mixer.music.queue(resource_path("audio/slotsmusic.mp3"))
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        print("Casino initialized")
        global textFader
        global characterName
        while self.casinomenubool:
            startTime = pygame.time.get_ticks()
            mouseX, mouseY = pygame.mouse.get_pos()
            if (self.gamescene == 1):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image172, (200, 100))
                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))
                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 120, 70)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 0 <= mouseX <= 1920 and 250 <= mouseY <= 1080:
                            sound_effect = pygame.mixer.Sound(resource_path("audio/clicknoise.mp3"))
                            sound_effect.play()
                            self.gamescene = self.gamescene + 1
                        if returnarrowrect.collidepoint(mouse_pos):
                            transition(6)
                            self.casinomenubool = False
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()

            if (self.gamescene == 2):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image172, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                draw_text_center('Hello young master,', font5, GREY, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('welcome back! ', font5, GREY, DISPLAYSURF, halfdisplay, 925)
                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))
                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 120, 70)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if returnarrowrect.collidepoint(mouse_pos):
                            transition(6)
                            self.casinomenubool = False
                        if 0 <= mouseX <= 1920 and 250 <= mouseY <= 1080:
                            sound_effect = pygame.mixer.Sound(resource_path("audio/clicknoise.mp3"))
                            sound_effect.play()
                            self.gamescene = self.gamescene + 1
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()

            if (self.gamescene == 3):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image172, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                draw_text_center('I hope we can fulfill all of your needs,', font5, GREY, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('and more..', font5, GREY, DISPLAYSURF, halfdisplay, 925)
                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))
                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 120, 70)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 0 <= mouseX <= 1920 and 250 <= mouseY <= 1080:
                            sound_effect = pygame.mixer.Sound(resource_path("audio/clicknoise.mp3"))
                            sound_effect.play()
                            self.gamescene = self.gamescene + 1
                        if returnarrowrect.collidepoint(mouse_pos):
                            transition(6)
                            self.casinomenubool = False
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()

            if (self.gamescene == 4):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image172, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                draw_text_center('Please follow me master', font5, GREY, DISPLAYSURF, halfdisplay, 890)
                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))
                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 120, 70)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 0 <= mouseX <= 1920 and 250 <= mouseY <= 1080:
                            sound_effect = pygame.mixer.Sound(resource_path("audio/clicknoise.mp3"))
                            sound_effect.play()
                            self.gamescene = self.gamescene + 1
                        if returnarrowrect.collidepoint(mouse_pos):
                            transition(6)
                            self.casinomenubool = False
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()

            if (self.gamescene == 5):
                rainbowcolor1 = int((math.sin(startTime * 0.002) + 1) * 127.5)
                rainbowcolor2 = int((math.sin(startTime * 0.003 + 2) + 1) * 127.5)
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image172, (200, 100))
                imageBlack.set_alpha(240)
                DISPLAYSURF.blit(imageBlack, (620, 160))

                ret, frame = video.read()
                if not ret:
                    video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    continue  # Continue to the next loop iteration
                frame = cv2.resize(frame, (1550, 880))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_surface = pygame.surfarray.make_surface(frame)
                frame_surface = pygame.transform.rotate(frame_surface, -90)  # Rotate if necessary
                frame_surface = pygame.transform.flip(frame_surface, True, False)
                frame_surface.set_alpha(100)
                DISPLAYSURF.blit(frame_surface, (190, 100))

                DISPLAYSURF.blit(image173, (560, 150))
                rouletterect = pygame.Rect(570, 157, 400, 385)
                dicerect = pygame.Rect(570, 543, 400, 385)
                blackjackrect = pygame.Rect(970, 157, 400, 385)
                slotsrect = pygame.Rect(970, 543, 400, 385)
                pygame.draw.rect(DISPLAYSURF, YELLOW, rouletterect, 6)
                pygame.draw.rect(DISPLAYSURF, YELLOW, dicerect, 6)
                pygame.draw.rect(DISPLAYSURF, YELLOW, blackjackrect, 6)
                pygame.draw.rect(DISPLAYSURF, YELLOW, slotsrect, 6)
                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))
                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 120, 70)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                if rouletterect.collidepoint(mouse_pos):
                    pygame.draw.rect(DISPLAYSURF,(rainbowcolor1,130,130), rouletterect, 11)
                if dicerect.collidepoint(mouse_pos):
                    pygame.draw.rect(DISPLAYSURF,(rainbowcolor1,130,130), dicerect, 11)
                if blackjackrect.collidepoint(mouse_pos):
                    pygame.draw.rect(DISPLAYSURF,(rainbowcolor1,130,130), blackjackrect, 11)
                if slotsrect.collidepoint(mouse_pos):
                    pygame.draw.rect(DISPLAYSURF,(rainbowcolor1,130,130), slotsrect, 11)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if rouletterect.collidepoint(mouse_pos):
                            transition(4)
                            print("Casino Roulette clicked")
                            self.repeatcasinoloop = True
                            self.casinogameplay()
                        if slotsrect.collidepoint(mouse_pos):
                            transition(4)
                            print("Casino Slots clicked")
                            self.repeatslotloop = True
                            self.slots()
                        if dicerect.collidepoint(mouse_pos):
                            transition(4)
                            print("Casino Slots clicked")
                            self.repeatdiceloop = True
                            self.dice()
                        if blackjackrect.collidepoint(mouse_pos):
                            transition(4)
                            print("Casino Blackjack clicked")
                            self.repeatblackjackloop = True
                            self.blackjack()
                        if returnarrowrect.collidepoint(mouse_pos):
                            transition(6)
                            self.casinomenubool = False
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()

            mouseX, mouseY = pygame.mouse.get_pos()
            imagee133.set_alpha(150)
            DISPLAYSURF.blit(imagee133, (mouseX - 40, mouseY - 42))
            pygame.display.update()
########################################################################################################################
    def casinogameplay(self):
        global gem
        global gold
        cap1 = cv2.VideoCapture(resource_path("video/roulettered.mov"))
        cap2 = cv2.VideoCapture(resource_path("video/rouletteblack.mov"))
        itemchoosen = " "
        blackorred = 0
        moneychoosen = 0
        while(self.repeatcasinoloop):
            self.casinogamebool = True
            startTime = pygame.time.get_ticks()
            scene = 1
            won = False
            pygame.mixer.music.load(resource_path("audio/roulettemusic.mp3"))
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)
            while(self.casinogamebool):
                with open(resource_path("gamedata.txt"), "r") as file:
                    lines = file.readlines()
                    if len(lines) >= 8:
                        goldline = lines[0].strip()
                        goldline = goldline[7:]
                        gemline = lines[1].strip()
                        gemline = gemline[6:]
                        gem = int(gemline)
                        gold = int(goldline)
                        ######
                rainbowcolor1 = int((math.sin(startTime * 0.002) + 1) * 127.5)
                rainbowcolor2 = int((math.sin(startTime * 0.003 + 2) + 1) * 127.5)
                rainbowcolor3 = int((math.sin(startTime * 0.004 + 2) + 1) * 127.5)
                rainbowcol = (rainbowcolor1, rainbowcolor2, rainbowcolor3)
                startTime = pygame.time.get_ticks()
                if(scene == 1):
                    mouse_pos = pygame.mouse.get_pos()
                    DISPLAYSURF.fill(BLACK)
                    DISPLAYSURF.blit(image174, (190, 100))
                    image4.set_alpha(100)
                    DISPLAYSURF.blit(image4, (0, 0))
                    DISPLAYSURF.blit(image164, (198, 110))
                    draw_text('gold - ', font5, WHITE, DISPLAYSURF, 375, 135)
                    draw_text(str(gold), font5, YELLOW, DISPLAYSURF, 445, 135)


                    blackorred = random.randint(0,1)
                    xrect = pygame.Rect(1680, 123, 35, 35)
                    returnarrowrect = pygame.Rect(153, 110, 120, 70)

                    blackrect = pygame.Rect(765, 380, 200, 250)
                    redrect = pygame.Rect(965, 380, 200, 250)

                    spend10rect = pygame.Rect(395, 810, 150, 150)
                    spend100rect = pygame.Rect(595, 810, 150, 150)
                    spend1000rect = pygame.Rect(795, 810, 150, 150)
                    spend10000rect = pygame.Rect(985, 810, 150, 150)
                    spend100000rect = pygame.Rect(1185, 810, 150, 150)
                    spend1000000rect = pygame.Rect(1375, 810, 150, 150)

                    beginrect = pygame.Rect(760, 680, 440, 95)

                    pygame.draw.rect(DISPLAYSURF, (BLACK), blackrect)
                    pygame.draw.rect(DISPLAYSURF, (RED), redrect)
                    pygame.draw.rect(DISPLAYSURF, (WHITE), blackrect, 8)
                    pygame.draw.rect(DISPLAYSURF, (WHITE), redrect, 8)

                    pygame.draw.rect(DISPLAYSURF, (BLACK), spend10rect)
                    pygame.draw.rect(DISPLAYSURF, (BLACK), spend100rect)
                    pygame.draw.rect(DISPLAYSURF, (BLACK), spend1000rect)
                    pygame.draw.rect(DISPLAYSURF, (BLACK), spend10000rect)
                    pygame.draw.rect(DISPLAYSURF, (BLACK), spend100000rect)
                    pygame.draw.rect(DISPLAYSURF, (BLACK), spend1000000rect)

                    pygame.draw.rect(DISPLAYSURF, (GOLD), spend10rect, 10)
                    pygame.draw.rect(DISPLAYSURF, (GOLD), spend100rect, 10)
                    pygame.draw.rect(DISPLAYSURF, (GOLD), spend1000rect, 10)
                    pygame.draw.rect(DISPLAYSURF, (GOLD), spend10000rect, 10)
                    pygame.draw.rect(DISPLAYSURF, (GOLD), spend100000rect, 10)
                    pygame.draw.rect(DISPLAYSURF, (GOLD), spend1000000rect, 10)
                    pygame.draw.rect(DISPLAYSURF, (GOLD), returnarrowrect, 6)
                    draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)

                    if blackrect.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcolor2,rainbowcolor1,rainbowcolor3), blackrect, 14)
                    if redrect.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcolor2,rainbowcolor1,rainbowcolor3), redrect, 14)


                    if spend10rect.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), spend10rect, 12)
                    if spend100rect.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), spend100rect, 12)
                    if spend1000rect.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), spend1000rect, 12)
                    if spend10000rect.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), spend10000rect, 12)
                    if spend100000rect.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), spend100000rect, 12)
                    if spend1000000rect.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), spend1000000rect, 12)
                    if returnarrowrect.collidepoint(mouse_pos):
                        DISPLAYSURF.blit(image165, (198, 110))
                    if xrect.collidepoint(mouse_pos):
                        draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                    if((itemchoosen != ' ') and (moneychoosen != 0)):
                        pygame.draw.rect(DISPLAYSURF, BLACK, beginrect)
                        draw_text(' Click to Spin! ', font2, GOLD, DISPLAYSURF, 785, 690)
                        if beginrect.collidepoint(mouse_pos):
                            draw_text(' Click to Spin! ', font2, (rainbowcolor2, rainbowcolor1, rainbowcolor3), DISPLAYSURF, 785, 690)
                            pygame.draw.rect(DISPLAYSURF, (rainbowcolor1, rainbowcolor3, rainbowcolor2), beginrect, 10)

                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if ((itemchoosen != ' ') and (moneychoosen != 0) and (gold >= moneychoosen)):
                                if beginrect.collidepoint(mouse_pos):
                                    cap1 = cv2.VideoCapture(resource_path("video/roulettered.mov"))
                                    cap2 = cv2.VideoCapture(resource_path("video/rouletteblack.mov"))
                                    scene = scene + 1
                            if blackrect.collidepoint(mouse_pos):
                                itemchoosen = 'black'
                            if redrect.collidepoint(mouse_pos):
                                itemchoosen = 'red'
                            if (spend10rect.collidepoint(mouse_pos) & (gold >= 10)):
                                moneychoosen = 10
                            if (spend10rect.collidepoint(mouse_pos) & (gold < 10)):
                                self.yourbroke()
                            if (spend100rect.collidepoint(mouse_pos) & (gold >= 100)):
                                moneychoosen = 100
                            if (spend100rect.collidepoint(mouse_pos) & (gold < 100)):
                                self.yourbroke()
                            if (spend1000rect.collidepoint(mouse_pos) & (gold >= 1000)):
                                moneychoosen = 1000
                            if (spend1000rect.collidepoint(mouse_pos) & (gold < 1000)):
                                self.yourbroke()
                            if (spend10000rect.collidepoint(mouse_pos) & (gold >= 10000)):
                                moneychoosen = 10000
                            if (spend10000rect.collidepoint(mouse_pos) & (gold < 10000)):
                                self.yourbroke()
                            if (spend100000rect.collidepoint(mouse_pos) & (gold >= 100000)):
                                moneychoosen = 100000
                            if (spend100000rect.collidepoint(mouse_pos) & (gold < 100000)):
                                self.yourbroke()
                            if (spend1000000rect.collidepoint(mouse_pos) & (gold >= 1000000)):
                                moneychoosen = 1000000
                            if (spend1000000rect.collidepoint(mouse_pos) & (gold < 1000000)):
                                self.yourbroke()
                            if xrect.collidepoint(mouse_pos):
                                print("Quit clicked")
                                pygame.mixer.music.stop()
                                pygame.quit()
                                sys.exit()
                            if returnarrowrect.collidepoint(mouse_pos):
                                transition(6)
                                self.repeatcasinoloop = False
                                self.casinogamebool = False

                    if(itemchoosen == 'black'):
                        pygame.draw.rect(DISPLAYSURF, ((rainbowcolor2,rainbowcolor1,rainbowcolor3)), blackrect, 12)
                    if (itemchoosen == 'red'):
                        pygame.draw.rect(DISPLAYSURF, ((rainbowcolor2,rainbowcolor1,rainbowcolor3)), redrect, 12)

                    if(moneychoosen == 10):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), spend10rect, 10)
                    if(moneychoosen == 100):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), spend100rect, 10)
                    if(moneychoosen == 1000):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), spend1000rect, 10)
                    if(moneychoosen == 10000):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), spend10000rect, 10)
                    if(moneychoosen == 100000):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), spend100000rect, 10)
                    if(moneychoosen == 1000000):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), spend1000000rect, 10)

                    draw_text('10', font3, GREY, DISPLAYSURF,445, 860)
                    draw_text('100', font3, GREY, DISPLAYSURF,635, 860)
                    draw_text('1000', font3, GREY, DISPLAYSURF,825, 860)
                    draw_text('10000', font3, GREY, DISPLAYSURF,1007, 860)
                    draw_text('100000', font3, GREY, DISPLAYSURF,1198, 860)
                    draw_text('1000000', font3, GREY, DISPLAYSURF,1384, 860)

                    image175.set_alpha(rainbowcolor1)
                    if(moneychoosen == 0):
                        DISPLAYSURF.blit(image175, (410, 670))
                        DISPLAYSURF.blit(image175, (610, 670))
                        DISPLAYSURF.blit(image175, (800, 670))
                        DISPLAYSURF.blit(image175, (1000, 670))
                        DISPLAYSURF.blit(image175, (1195, 670))
                        DISPLAYSURF.blit(image175, (1395, 670))
                    image175.set_alpha(rainbowcolor2)
                    if(itemchoosen == ' '):
                        DISPLAYSURF.blit(image175, (820, 240))
                        DISPLAYSURF.blit(image175, (1020, 240))

                    pygame.display.update()
                if(scene == 2):
                    sound_effect = pygame.mixer.Sound(resource_path("audio/roulettespinsound.mp3"))
                    sound_effect.play()
                    if(blackorred == 0):
                        if (itemchoosen == 'red'):
                            gold = gold + moneychoosen
                            won = True
                        else:
                            won = False
                            gold = gold - moneychoosen
                        fps = int(cap1.get(cv2.CAP_PROP_FPS))
                        clock = pygame.time.Clock()
                        while cap1.isOpened():
                            ret, frame = cap1.read()
                            if not ret:
                                break
                            frame = cv2.resize(frame, (1600, 873))
                            frame = cv2.flip(frame, 1)
                            frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
                            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                            frame = pygame.surfarray.make_surface(frame).convert()
                            DISPLAYSURF.blit(frame, (163, 100))
                            pygame.display.flip()
                            clock.tick(fps)
                        cap1.release()

                    if(blackorred == 1):
                        if (itemchoosen == 'black'):
                            gold = gold + moneychoosen
                            won = True
                        else:
                            won = False
                            gold = gold - moneychoosen
                        fps = int(cap2.get(cv2.CAP_PROP_FPS))
                        clock = pygame.time.Clock()
                        while cap2.isOpened():
                            ret, frame = cap2.read()
                            if not ret:
                                break
                            frame = cv2.resize(frame, (1600, 873))
                            frame = cv2.flip(frame, 1)
                            frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
                            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                            frame = pygame.surfarray.make_surface(frame).convert()
                            DISPLAYSURF.blit(frame, (164, 100))
                            pygame.display.flip()
                            clock.tick(fps)
                        cap2.release()
                    scene = scene + 1
                    pygame.display.update()
                if(scene == 3):
                    draw_text('gold - ', font5, WHITE, DISPLAYSURF, 375, 135)
                    draw_text(str(gold), font5, YELLOW, DISPLAYSURF, 445, 135)
                    if(won):
                        draw_text('Congrats, You won ' +str(moneychoosen) +" gold", font3, (rainbowcolor1, rainbowcolor1, 0), DISPLAYSURF, 695, 220)
                    else:
                        draw_text('You lost ' +str(moneychoosen) +" gold", font2, (rainbowcolor1, 0 ,rainbowcolor1), DISPLAYSURF, 725, 220)

                    pygame.display.flip()
                    mouse_pos = pygame.mouse.get_pos()
                    for event in pygame.event.get():
                        with open(resource_path("gamedata.txt"), "r") as file:
                            lines = file.readlines()
                            lines[0] = f"gold = {gold}\n"
                        with open(resource_path("gamedata.txt"), "w") as file:
                            file.writelines(lines)
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            scene = 1
                    pygame.display.update()
########################################################################################################################
    def slots(self):
        global gem
        global gold
        moneychoosen = 0
        while(self.repeatslotloop):
            self.casinogamebool = True
            startTime = pygame.time.get_ticks()
            scene = 1
            pygame.mixer.music.load(resource_path("audio/slotsmusic.mp3"))
            pygame.mixer.music.queue(resource_path("audio/slotsmusic2.mp3"))
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)
            while(self.casinogamebool):
                with open(resource_path("gamedata.txt"), "r") as file:
                    lines = file.readlines()
                    if len(lines) >= 8:
                        goldline = lines[0].strip()
                        goldline = goldline[7:]
                        gemline = lines[1].strip()
                        gemline = gemline[6:]
                        gem = int(gemline)
                        gold = int(goldline)
                        ######
                rainbowcolor1 = int((math.sin(startTime * 0.002) + 1) * 127.5)
                rainbowcolor2 = int((math.sin(startTime * 0.003 + 2) + 1) * 127.5)
                rainbowcolor3 = int((math.sin(startTime * 0.004 + 2) + 1) * 127.5)
                rainbowcol = (rainbowcolor1, rainbowcolor2, rainbowcolor3)
                startTime = pygame.time.get_ticks()
                mouseX, mouseY = pygame.mouse.get_pos()
                randomnumber1 = random.randint(1,9)
                randomnumber2 = random.randint(1,9)
                randomnumber3 = random.randint(1,9)
                if(scene == 1):
                    mouse_pos = pygame.mouse.get_pos()
                    DISPLAYSURF.fill(BLACK)
                    DISPLAYSURF.blit(image176, (190, 100))
                    mouse_pos = pygame.mouse.get_pos()
                    draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                    DISPLAYSURF.blit(image164, (198, 110))
                    xrect = pygame.Rect(1680, 123, 35, 35)
                    returnarrowrect = pygame.Rect(153, 110, 120, 70)
                    if xrect.collidepoint(mouse_pos):
                        draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                    if returnarrowrect.collidepoint(mouse_pos):
                        DISPLAYSURF.blit(image165, (198, 110))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if returnarrowrect.collidepoint(mouse_pos):
                                transition(6)
                                self.casinogamebool = False
                                self.repeatslotloop = False
                            if 0 <= mouseX <= 1920 and 250 <= mouseY <= 1080:
                                sound_effect = pygame.mixer.Sound(resource_path("audio/clicknoise.mp3"))
                                sound_effect.play()
                                scene = scene + 1
                            if xrect.collidepoint(mouse_pos):
                                print("Quit clicked")
                                pygame.mixer.music.stop()
                                pygame.quit()
                                sys.exit()
                    pygame.display.update()
                if (scene == 2):
                    DISPLAYSURF.fill(BLACK)
                    DISPLAYSURF.blit(image176, (190, 100))
                    DISPLAYSURF.blit(image53, (1070, 110))
                    draw_text('Are you ready to lose', font5, PINK, DISPLAYSURF, 1220, 175)
                    draw_text('again?', font5, PINK, DISPLAYSURF, 1290, 200)
                    mouse_pos = pygame.mouse.get_pos()
                    draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                    DISPLAYSURF.blit(image164, (198, 110))
                    xrect = pygame.Rect(1680, 123, 35, 35)
                    returnarrowrect = pygame.Rect(153, 110, 120, 70)
                    if xrect.collidepoint(mouse_pos):
                        draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                    if returnarrowrect.collidepoint(mouse_pos):
                        DISPLAYSURF.blit(image165, (198, 110))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if returnarrowrect.collidepoint(mouse_pos):
                                self.repeatslotloop = False
                            if 0 <= mouseX <= 1920 and 250 <= mouseY <= 1080:
                                sound_effect = pygame.mixer.Sound(resource_path("audio/clicknoise.mp3"))
                                sound_effect.play()
                                scene = scene + 1
                            if xrect.collidepoint(mouse_pos):
                                print("Quit clicked")
                                pygame.mixer.music.stop()
                                pygame.quit()
                                sys.exit()
                    pygame.display.update()
                if (scene == 3):
                    mouse_pos = pygame.mouse.get_pos()
                    DISPLAYSURF.fill(BLACK)
                    DISPLAYSURF.blit(image176, (190, 100))
                    image180.set_alpha(100)
                    DISPLAYSURF.blit(image180, (0, 0))
                    draw_text('gold - ', font5, WHITE, DISPLAYSURF, 375, 135)
                    draw_text(str(gold), font5, YELLOW, DISPLAYSURF, 445, 135)
                    mouse_pos = pygame.mouse.get_pos()
                    draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                    DISPLAYSURF.blit(image164, (198, 110))
                    xrect = pygame.Rect(1680, 123, 35, 35)
                    returnarrowrect = pygame.Rect(153, 110, 120, 70)

                    spend1rect = pygame.Rect(395, 810, 150, 150)
                    spend10rect = pygame.Rect(595, 810, 150, 150)
                    spend100rect = pygame.Rect(795, 810, 150, 150)
                    spend1000rect = pygame.Rect(985, 810, 150, 150)
                    spend10000rect = pygame.Rect(1185, 810, 150, 150)
                    spend100000rect = pygame.Rect(1375, 810, 150, 150)
                    beginrect = pygame.Rect(760, 680, 440, 95)

                    pygame.draw.rect(DISPLAYSURF, (BLACK), spend1rect)
                    pygame.draw.rect(DISPLAYSURF, (BLACK), spend10rect)
                    pygame.draw.rect(DISPLAYSURF, (BLACK), spend100rect)
                    pygame.draw.rect(DISPLAYSURF, (BLACK), spend1000rect)
                    pygame.draw.rect(DISPLAYSURF, (BLACK), spend10000rect)
                    pygame.draw.rect(DISPLAYSURF, (BLACK), spend100000rect)

                    pygame.draw.rect(DISPLAYSURF, (GOLD), spend1rect, 10)
                    pygame.draw.rect(DISPLAYSURF, (GOLD), spend10rect, 10)
                    pygame.draw.rect(DISPLAYSURF, (GOLD), spend100rect, 10)
                    pygame.draw.rect(DISPLAYSURF, (GOLD), spend1000rect, 10)
                    pygame.draw.rect(DISPLAYSURF, (GOLD), spend10000rect, 10)
                    pygame.draw.rect(DISPLAYSURF, (GOLD), spend100000rect, 10)
                    pygame.draw.rect(DISPLAYSURF, (GOLD), returnarrowrect, 6)

                    if spend1rect.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), spend1rect, 12)
                    if spend10rect.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), spend10rect, 12)
                    if spend100rect.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), spend100rect, 12)
                    if spend1000rect.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), spend1000rect, 12)
                    if spend10000rect.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), spend10000rect, 12)
                    if spend100000rect.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), spend100000rect, 12)

                    if (moneychoosen != 0):
                        pygame.draw.rect(DISPLAYSURF, BLACK, beginrect)
                        draw_text(' Click to Spin! ', font2, GOLD, DISPLAYSURF, 785, 690)
                        if beginrect.collidepoint(mouse_pos):
                            draw_text(' Click to Spin! ', font2, (rainbowcolor2, rainbowcolor1, rainbowcolor3),DISPLAYSURF, 785, 690)
                            pygame.draw.rect(DISPLAYSURF, (rainbowcolor1, rainbowcolor3, rainbowcolor2), beginrect, 10)

                    if (moneychoosen == 1):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), spend1rect, 10)
                    if (moneychoosen == 10):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), spend10rect, 10)
                    if (moneychoosen == 100):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), spend100rect, 10)
                    if (moneychoosen == 1000):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), spend1000rect, 10)
                    if (moneychoosen == 10000):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), spend10000rect, 10)
                    if (moneychoosen == 100000):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), spend100000rect, 10)

                    if xrect.collidepoint(mouse_pos):
                        draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                    if returnarrowrect.collidepoint(mouse_pos):
                        DISPLAYSURF.blit(image165, (198, 110))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if returnarrowrect.collidepoint(mouse_pos):
                                transition(6)
                                self.casinogamebool = False
                                self.repeatslotloop = False
                            if xrect.collidepoint(mouse_pos):
                                print("Quit clicked")
                                pygame.mixer.music.stop()
                                pygame.quit()
                                sys.exit()
                            if (spend1rect.collidepoint(mouse_pos) & (gold >= 1)):
                                moneychoosen = 1
                            if (spend1rect.collidepoint(mouse_pos) & (gold < 1)):
                                self.yourbroke()
                            if (spend10rect.collidepoint(mouse_pos) & (gold >= 10)):
                                moneychoosen = 10
                            if (spend10rect.collidepoint(mouse_pos) & (gold < 10)):
                                self.yourbroke()
                            if (spend100rect.collidepoint(mouse_pos) & (gold >= 100)):
                                moneychoosen = 100
                            if (spend100rect.collidepoint(mouse_pos) & (gold < 100)):
                                self.yourbroke()
                            if (spend1000rect.collidepoint(mouse_pos) & (gold >= 1000)):
                                moneychoosen = 1000
                            if (spend1000rect.collidepoint(mouse_pos) & (gold < 1000)):
                                self.yourbroke()
                            if (spend10000rect.collidepoint(mouse_pos) & (gold >= 10000)):
                                moneychoosen = 10000
                            if (spend10000rect.collidepoint(mouse_pos) & (gold < 10000)):
                                self.yourbroke()
                            if (spend100000rect.collidepoint(mouse_pos) & (gold >= 100000)):
                                moneychoosen = 100000
                            if (spend100000rect.collidepoint(mouse_pos) & (gold < 100000)):
                                self.yourbroke()
                            if (moneychoosen != 0 & (beginrect.collidepoint(mouse_pos)) & (gold >= moneychoosen)):
                                scene = scene + 1

                    draw_text('1', font3, GREY, DISPLAYSURF, 455, 860)
                    draw_text('10', font3, GREY, DISPLAYSURF, 645, 860)
                    draw_text('100', font3, GREY, DISPLAYSURF, 833, 860)
                    draw_text('1000', font3, GREY, DISPLAYSURF, 1015, 860)
                    draw_text('10000', font3, GREY, DISPLAYSURF, 1206, 860)
                    draw_text('100000', font3, GREY, DISPLAYSURF, 1391, 860)
                    pygame.display.update()
                if (scene == 4):
                    mouse_pos = pygame.mouse.get_pos()
                    DISPLAYSURF.blit(image176, (190, 100))
                    image180.set_alpha(100)
                    DISPLAYSURF.blit(image180, (0, 0))
                    DISPLAYSURF.blit(image177, (360, 60))
                    mouse_pos = pygame.mouse.get_pos()
                    draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                    DISPLAYSURF.blit(image164, (198, 110))
                    draw_text('gold - ', font5, WHITE, DISPLAYSURF, 375, 135)
                    draw_text(str(gold), font5, YELLOW, DISPLAYSURF, 445, 135)
                    xrect = pygame.Rect(1680, 123, 35, 35)
                    returnarrowrect = pygame.Rect(153, 110, 120, 70)
                    slotrect = pygame.Rect(1354, 245, 135, 525)
                    pygame.draw.rect(DISPLAYSURF, (rainbowcol), slotrect, 10)
                    if slotrect.collidepoint(mouse_pos):
                        DISPLAYSURF.blit(image179, (360, 60))
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), slotrect, 10)
                    if xrect.collidepoint(mouse_pos):
                        draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                    if returnarrowrect.collidepoint(mouse_pos):
                        DISPLAYSURF.blit(image165, (198, 110))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if returnarrowrect.collidepoint(mouse_pos):
                                scene = 1
                            if xrect.collidepoint(mouse_pos):
                                print("Quit clicked")
                                pygame.mixer.music.stop()
                                pygame.quit()
                                sys.exit()
                            if slotrect.collidepoint(mouse_pos):
                                if(gold >= moneychoosen):
                                    gold = gold - moneychoosen
                                    scene = scene + 1
                    pygame.display.update()
                if (scene == 5):
                    time1 = pygame.time.get_ticks()
                    loop = True
                    DISPLAYSURF.blit(image176, (190, 100))
                    image180.set_alpha(100)
                    DISPLAYSURF.blit(image180, (0, 0))
                    DISPLAYSURF.blit(image178, (360, 60))
                    draw_text('gold - ', font5, WHITE, DISPLAYSURF, 375, 135)
                    draw_text(str(gold), font5, YELLOW, DISPLAYSURF, 445, 135)
                    sound_effect = pygame.mixer.Sound(resource_path("audio/spin.mp3"))
                    sound_effect.play()
                    while(loop):
                        randomnumber1 = random.randint(1, 9)
                        randomnumber2 = random.randint(1, 9)
                        randomnumber3 = random.randint(1, 9)
                        randomnumber4 = random.randint(1, 4)
                        randomnumber5 = random.randint(1, 4)
                        randomnumber6 = random.randint(1, 4)
                        time2 = pygame.time.get_ticks()
                        mouse_pos = pygame.mouse.get_pos()
                        draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                        DISPLAYSURF.blit(image164, (198, 110))
                        xrect = pygame.Rect(1680, 123, 35, 35)
                        returnarrowrect = pygame.Rect(153, 110, 120, 70)
                        if xrect.collidepoint(mouse_pos):
                            draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                        if returnarrowrect.collidepoint(mouse_pos):
                            DISPLAYSURF.blit(image165, (198, 110))
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if returnarrowrect.collidepoint(mouse_pos):
                                    scene = 1
                                if xrect.collidepoint(mouse_pos):
                                    print("Quit clicked")
                                    pygame.mixer.music.stop()
                                    pygame.quit()
                                    sys.exit()

                        if((time1 + 300) < time2) and (time1 + 3000 > time2):
                            if(randomnumber4 == 1):
                                if(randomnumber1 == 1):
                                    DISPLAYSURF.blit(image181, (603, 551))
                                if (randomnumber1 == 2):
                                    DISPLAYSURF.blit(image182, (603, 551))
                                if (randomnumber1 == 3):
                                    DISPLAYSURF.blit(image183, (603, 551))
                                if (randomnumber1 == 4):
                                    DISPLAYSURF.blit(image184, (603, 551))
                                if (randomnumber1 == 5):
                                    DISPLAYSURF.blit(image185, (603, 551))
                                if (randomnumber1 == 6):
                                    DISPLAYSURF.blit(image186, (603, 551))
                                if (randomnumber1 == 7):
                                    DISPLAYSURF.blit(image187, (603, 551))
                                if (randomnumber1 == 8):
                                    DISPLAYSURF.blit(image188, (603, 551))
                                if (randomnumber1 == 9):
                                    DISPLAYSURF.blit(image189, (603, 551))
                            if (randomnumber5 == 1):
                                if(randomnumber2 == 1):
                                    DISPLAYSURF.blit(image181, (853, 551))
                                if (randomnumber2 == 2):
                                    DISPLAYSURF.blit(image182, (853, 551))
                                if (randomnumber2 == 3):
                                    DISPLAYSURF.blit(image183, (853, 551))
                                if (randomnumber2 == 4):
                                    DISPLAYSURF.blit(image184, (853, 551))
                                if (randomnumber2 == 5):
                                    DISPLAYSURF.blit(image185, (853, 551))
                                if (randomnumber2 == 6):
                                    DISPLAYSURF.blit(image186, (853, 551))
                                if (randomnumber2 == 7):
                                    DISPLAYSURF.blit(image187, (853, 551))
                                if (randomnumber2 == 8):
                                    DISPLAYSURF.blit(image188, (853, 551))
                                if (randomnumber2 == 9):
                                    DISPLAYSURF.blit(image189, (853, 551))

                            if (randomnumber6 == 1):
                                if (randomnumber3 == 1):
                                    DISPLAYSURF.blit(image181, (1103, 551))
                                if (randomnumber3 == 2):
                                    DISPLAYSURF.blit(image182, (1103, 551))
                                if (randomnumber3 == 3):
                                    DISPLAYSURF.blit(image183, (1103, 551))
                                if (randomnumber3 == 4):
                                    DISPLAYSURF.blit(image184, (1103, 551))
                                if (randomnumber3 == 5):
                                    DISPLAYSURF.blit(image185, (1103, 551))
                                if (randomnumber3 == 6):
                                    DISPLAYSURF.blit(image186, (1103, 551))
                                if (randomnumber3 == 7):
                                    DISPLAYSURF.blit(image187, (1103, 551))
                                if (randomnumber3 == 8):
                                    DISPLAYSURF.blit(image188, (1103, 551))
                                if (randomnumber3 == 9):
                                    DISPLAYSURF.blit(image189, (1103, 551))

                        if(time1 + 3000 < time2):
                            DISPLAYSURF.blit(image190, (360, 60))
                            if(randomnumber1 == 1):
                                DISPLAYSURF.blit(image181, (603, 551))
                            if (randomnumber1 == 2):
                                DISPLAYSURF.blit(image182, (603, 551))
                            if (randomnumber1 == 3):
                                DISPLAYSURF.blit(image183, (603, 551))
                            if (randomnumber1 == 4):
                                DISPLAYSURF.blit(image184, (603, 551))
                            if (randomnumber1 == 5):
                                DISPLAYSURF.blit(image185, (603, 551))
                            if (randomnumber1 == 6):
                                DISPLAYSURF.blit(image186, (603, 551))
                            if (randomnumber1 == 7):
                                DISPLAYSURF.blit(image187, (603, 551))
                            if (randomnumber1 == 8):
                                DISPLAYSURF.blit(image188, (603, 551))
                            if (randomnumber1 == 9):
                                DISPLAYSURF.blit(image189, (603, 551))

                            if(randomnumber2 == 1):
                                DISPLAYSURF.blit(image181, (853, 551))
                            if (randomnumber2 == 2):
                                DISPLAYSURF.blit(image182, (853, 551))
                            if (randomnumber2 == 3):
                                DISPLAYSURF.blit(image183, (853, 551))
                            if (randomnumber2 == 4):
                                DISPLAYSURF.blit(image184, (853, 551))
                            if (randomnumber2 == 5):
                                DISPLAYSURF.blit(image185, (853, 551))
                            if (randomnumber2 == 6):
                                DISPLAYSURF.blit(image186, (853, 551))
                            if (randomnumber2 == 7):
                                DISPLAYSURF.blit(image187, (853, 551))
                            if (randomnumber2 == 8):
                                DISPLAYSURF.blit(image188, (853, 551))
                            if (randomnumber2 == 9):
                                DISPLAYSURF.blit(image189, (853, 551))

                            if (randomnumber3 == 1):
                                DISPLAYSURF.blit(image181, (1103, 551))
                            if (randomnumber3 == 2):
                                DISPLAYSURF.blit(image182, (1103, 551))
                            if (randomnumber3 == 3):
                                DISPLAYSURF.blit(image183, (1103, 551))
                            if (randomnumber3 == 4):
                                DISPLAYSURF.blit(image184, (1103, 551))
                            if (randomnumber3 == 5):
                                DISPLAYSURF.blit(image185, (1103, 551))
                            if (randomnumber3 == 6):
                                DISPLAYSURF.blit(image186, (1103, 551))
                            if (randomnumber3 == 7):
                                DISPLAYSURF.blit(image187, (1103, 551))
                            if (randomnumber3 == 8):
                                DISPLAYSURF.blit(image188, (1103, 551))
                            if (randomnumber3 == 9):
                                DISPLAYSURF.blit(image189, (1103, 551))

                            screen_width, screen_height = DISPLAYSURF.get_size()
                            if((randomnumber1 == 7) and (randomnumber2 == 7) and (randomnumber3 == 7)):
                                sound_effect = pygame.mixer.Sound(resource_path("audio/slotwin1.mp3"))
                                sound_effect.play()
                                gold = gold + (moneychoosen * 1000)
                                draw_text('gained ' + str(moneychoosen * 1000) + ' gold!', font3, GOLD, DISPLAYSURF, screen_width / 2 - 155, screen_height / 2 - 45)
                            else:
                                if((randomnumber1 == randomnumber2) and (randomnumber1 == randomnumber3) and (randomnumber2 == randomnumber3)):
                                    sound_effect = pygame.mixer.Sound(resource_path("audio/slotwin2.mp3"))
                                    sound_effect.play()
                                    gold = gold + (moneychoosen * 80)
                                    draw_text('gained ' + str(moneychoosen * 80) + ' gold!', font3, GOLD, DISPLAYSURF, screen_width / 2 - 155, screen_height / 2 - 45)

                                else:
                                    if(randomnumber1 == randomnumber2):
                                        sound_effect = pygame.mixer.Sound(resource_path("audio/minislotwin.mp3"))
                                        sound_effect.play()
                                        gold = gold + (moneychoosen * 1)
                                        draw_text('You won ' + str(moneychoosen * 1) + ' gold!', font3, GOLD, DISPLAYSURF, screen_width / 2 - 155, screen_height / 2 - 45)

                                    if(randomnumber3 == randomnumber2):
                                        sound_effect = pygame.mixer.Sound(resource_path("audio/minislotwin.mp3"))
                                        sound_effect.play()
                                        gold = gold + (moneychoosen * 1)
                                        draw_text('You won ' + str(moneychoosen * 1) + ' gold!', font3, GOLD, DISPLAYSURF, screen_width / 2 - 155, screen_height / 2 - 45)

                                    if(randomnumber3 == randomnumber1):
                                        sound_effect = pygame.mixer.Sound(resource_path("audio/minislotwin.mp3"))
                                        sound_effect.play()
                                        gold = gold + (moneychoosen * 1)
                                        draw_text('You won ' + str(moneychoosen * 1) + ' gold!', font3, GOLD, DISPLAYSURF, screen_width / 2 - 155, screen_height / 2 - 45)

                            loop = False
                            with open(resource_path("gamedata.txt"), "r") as file:
                                lines = file.readlines()
                                lines[0] = f"gold = {gold}\n"
                                lines[1] = f"gem = {gem}\n"
                            with open(resource_path("gamedata.txt"), "w") as file:
                                file.writelines(lines)
                            scene = scene + 1
                        pygame.display.update()
                    pygame.display.update()

                if (scene == 6):
                    mouse_pos = pygame.mouse.get_pos()
                    draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                    DISPLAYSURF.blit(image164, (198, 110))
                    xrect = pygame.Rect(1680, 123, 35, 35)
                    returnarrowrect = pygame.Rect(153, 110, 120, 70)
                    if xrect.collidepoint(mouse_pos):
                        draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                    if returnarrowrect.collidepoint(mouse_pos):
                        DISPLAYSURF.blit(image165, (198, 110))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if returnarrowrect.collidepoint(mouse_pos):
                                scene = 1
                            if xrect.collidepoint(mouse_pos):
                                print("Quit clicked")
                                pygame.mixer.music.stop()
                                pygame.quit()
                                sys.exit()
                            if 0 <= mouseX <= 1920 and 250 <= mouseY <= 1080:
                                sound_effect = pygame.mixer.Sound(resource_path("audio/clicknoise.mp3"))
                                sound_effect.play()
                                scene = 4

                    pygame.display.update()
########################################################################################################################
    def dice(self):
        global gem
        global gold
        dicechoosen = 0
        moneychoosen = 0
        while(self.repeatdiceloop):
            self.casinogamebool = True
            startTime = pygame.time.get_ticks()
            scene = -1
            pygame.mixer.music.load(resource_path("audio/dicemusic.mp3"))
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)
            while(self.casinogamebool):
                with open(resource_path("gamedata.txt"), "r") as file:
                    lines = file.readlines()
                    if len(lines) >= 8:
                        goldline = lines[0].strip()
                        goldline = goldline[7:]
                        gemline = lines[1].strip()
                        gemline = gemline[6:]
                        gem = int(gemline)
                        gold = int(goldline)
                        ######
                rainbowcolor1 = int((math.sin(startTime * 0.002) + 1) * 127.5)
                rainbowcolor2 = int((math.sin(startTime * 0.003 + 2) + 1) * 127.5)
                rainbowcolor3 = int((math.sin(startTime * 0.004 + 2) + 1) * 127.5)
                rainbowcol = (rainbowcolor1, rainbowcolor2, rainbowcolor3)
                startTime = pygame.time.get_ticks()
                mouseX, mouseY = pygame.mouse.get_pos()
                randomnumber1 = random.randint(1,9)
                randomnumber2 = random.randint(1,9)
                randomnumber3 = random.randint(1,9)
                if (scene == -1):
                    mouse_pos = pygame.mouse.get_pos()
                    DISPLAYSURF.blit(image191, (190, 100))
                    mouse_pos = pygame.mouse.get_pos()
                    draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                    DISPLAYSURF.blit(image164, (198, 110))
                    draw_text('gold - ', font5, WHITE, DISPLAYSURF, 375, 135)
                    draw_text(str(gold), font5, YELLOW, DISPLAYSURF, 445, 135)
                    xrect = pygame.Rect(1680, 123, 35, 35)
                    returnarrowrect = pygame.Rect(153, 110, 120, 70)
                    if xrect.collidepoint(mouse_pos):
                        draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                    if returnarrowrect.collidepoint(mouse_pos):
                        DISPLAYSURF.blit(image165, (198, 110))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if returnarrowrect.collidepoint(mouse_pos):
                                transition(6)
                                self.casinogamebool = False
                                self.repeatdiceloop = False
                            if xrect.collidepoint(mouse_pos):
                                print("Quit clicked")
                                pygame.mixer.music.stop()
                                pygame.quit()
                                sys.exit()
                            if 0 <= mouseX <= 1920 and 250 <= mouseY <= 1080:
                                scene = scene + 1
                    pygame.display.update()
                if(scene == 0):
                    mouse_pos = pygame.mouse.get_pos()
                    DISPLAYSURF.fill(BLACK)
                    DISPLAYSURF.blit(image191, (190, 100))
                    image199.set_alpha(150)
                    DISPLAYSURF.blit(image199, (0, 0))
                    draw_text('gold - ', font5, WHITE, DISPLAYSURF, 375, 135)
                    draw_text(str(gold), font5, YELLOW, DISPLAYSURF, 445, 135)
                    mouse_pos = pygame.mouse.get_pos()
                    draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                    DISPLAYSURF.blit(image164, (198, 110))
                    xrect = pygame.Rect(1680, 123, 35, 35)
                    returnarrowrect = pygame.Rect(153, 110, 120, 70)


                    dice1 = pygame.Rect(395, 600, 150, 150)
                    dice2 = pygame.Rect(595, 600, 150, 150)
                    dice3 = pygame.Rect(795, 600, 150, 150)
                    dice4 = pygame.Rect(985, 600, 150, 150)
                    dice5 = pygame.Rect(1185, 600, 150, 150)
                    dice6 = pygame.Rect(1375, 600, 150, 150)
                    DISPLAYSURF.blit(image201, (395, 600))
                    DISPLAYSURF.blit(image202, (595, 600))
                    DISPLAYSURF.blit(image203, (795, 600))
                    DISPLAYSURF.blit(image204, (985, 600))
                    DISPLAYSURF.blit(image205, (1185, 600))
                    DISPLAYSURF.blit(image206, (1375, 600))


                    spend10rect = pygame.Rect(395, 810, 150, 150)
                    spend100rect = pygame.Rect(595, 810, 150, 150)
                    spend1000rect = pygame.Rect(795, 810, 150, 150)
                    spend10000rect = pygame.Rect(985, 810, 150, 150)
                    spend100000rect = pygame.Rect(1185, 810, 150, 150)
                    spend1000000rect = pygame.Rect(1375, 810, 150, 150)
                    beginrect = pygame.Rect(760, 480, 440, 95)

                    pygame.draw.rect(DISPLAYSURF, (YELLOW), dice1, 10)
                    pygame.draw.rect(DISPLAYSURF, (YELLOW), dice2, 10)
                    pygame.draw.rect(DISPLAYSURF, (YELLOW), dice3, 10)
                    pygame.draw.rect(DISPLAYSURF, (YELLOW), dice4, 10)
                    pygame.draw.rect(DISPLAYSURF, (YELLOW), dice5, 10)
                    pygame.draw.rect(DISPLAYSURF, (YELLOW), dice6, 10)

                    pygame.draw.rect(DISPLAYSURF, (BLACK), spend10rect)
                    pygame.draw.rect(DISPLAYSURF, (BLACK), spend100rect)
                    pygame.draw.rect(DISPLAYSURF, (BLACK), spend1000rect)
                    pygame.draw.rect(DISPLAYSURF, (BLACK), spend10000rect)
                    pygame.draw.rect(DISPLAYSURF, (BLACK), spend100000rect)
                    pygame.draw.rect(DISPLAYSURF, (BLACK), spend1000000rect)

                    pygame.draw.rect(DISPLAYSURF, (RED), spend10rect, 10)
                    pygame.draw.rect(DISPLAYSURF, (RED), spend100rect, 10)
                    pygame.draw.rect(DISPLAYSURF, (RED), spend1000rect, 10)
                    pygame.draw.rect(DISPLAYSURF, (RED), spend10000rect, 10)
                    pygame.draw.rect(DISPLAYSURF, (RED), spend100000rect, 10)
                    pygame.draw.rect(DISPLAYSURF, (RED), spend1000000rect, 10)
                    pygame.draw.rect(DISPLAYSURF, (RED), returnarrowrect, 6)

                    if dice1.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcolor3,rainbowcolor2,rainbowcolor3), dice1, 12)
                    if dice2.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcolor3,rainbowcolor2,rainbowcolor3), dice2, 12)
                    if dice3.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcolor3,rainbowcolor2,rainbowcolor3), dice3, 12)
                    if dice4.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcolor3,rainbowcolor2,rainbowcolor3), dice4, 12)
                    if dice5.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcolor3,rainbowcolor2,rainbowcolor3), dice5, 12)
                    if dice6.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcolor3,rainbowcolor2,rainbowcolor3), dice6, 12)

                    if spend10rect.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), spend10rect, 12)
                    if spend100rect.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), spend100rect, 12)
                    if spend1000rect.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), spend1000rect, 12)
                    if spend10000rect.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), spend10000rect, 12)
                    if spend100000rect.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), spend100000rect, 12)
                    if spend1000000rect.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), spend1000000rect, 12)

                    if ((moneychoosen != 0) and (dicechoosen != 0)):
                        pygame.draw.rect(DISPLAYSURF, BLACK, beginrect)
                        draw_text(' Click to Roll! ', font2, (105, 36, 166), DISPLAYSURF, 785, 490)
                        if beginrect.collidepoint(mouse_pos):
                            draw_text(' Click to Roll! ', font2, (rainbowcolor2, rainbowcolor1, rainbowcolor3),DISPLAYSURF, 785, 490)
                            pygame.draw.rect(DISPLAYSURF, (rainbowcolor1, rainbowcolor3, rainbowcolor2), beginrect, 10)

                    if (dicechoosen == 1):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcolor3,rainbowcolor2,rainbowcolor3), dice1, 10)
                    if (dicechoosen == 2):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcolor3,rainbowcolor2,rainbowcolor3), dice2, 10)
                    if (dicechoosen == 3):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcolor3,rainbowcolor2,rainbowcolor3), dice3, 10)
                    if (dicechoosen == 4):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcolor3,rainbowcolor2,rainbowcolor3), dice4, 10)
                    if (dicechoosen == 5):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcolor3,rainbowcolor2,rainbowcolor3), dice5, 10)
                    if (dicechoosen == 6):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcolor3,rainbowcolor2,rainbowcolor3), dice6, 10)

                    if (moneychoosen == 10):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), spend10rect, 10)
                    if (moneychoosen == 100):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), spend100rect, 10)
                    if (moneychoosen == 1000):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), spend1000rect, 10)
                    if (moneychoosen == 10000):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), spend10000rect, 10)
                    if (moneychoosen == 100000):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), spend100000rect, 10)
                    if (moneychoosen == 1000000):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), spend1000000rect, 10)

                    if xrect.collidepoint(mouse_pos):
                        draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                    if returnarrowrect.collidepoint(mouse_pos):
                        DISPLAYSURF.blit(image165, (198, 110))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if returnarrowrect.collidepoint(mouse_pos):
                                transition(6)
                                self.casinogamebool = False
                                self.repeatdiceloop = False
                            if xrect.collidepoint(mouse_pos):
                                print("Quit clicked")
                                pygame.mixer.music.stop()
                                pygame.quit()
                                sys.exit()

                            if (dice1.collidepoint(mouse_pos)):
                                dicechoosen = 1
                            if (dice2.collidepoint(mouse_pos)):
                                dicechoosen = 2
                            if (dice3.collidepoint(mouse_pos)):
                                dicechoosen = 3
                            if (dice4.collidepoint(mouse_pos)):
                                dicechoosen = 4
                            if (dice5.collidepoint(mouse_pos)):
                                dicechoosen = 5
                            if (dice6.collidepoint(mouse_pos)):
                                dicechoosen = 6

                            if (spend10rect.collidepoint(mouse_pos) & (gold >= 10)):
                                moneychoosen = 10
                            if (spend10rect.collidepoint(mouse_pos) & (gold < 10)):
                                self.yourbroke()
                            if (spend100rect.collidepoint(mouse_pos) & (gold >= 100)):
                                moneychoosen = 100
                            if (spend100rect.collidepoint(mouse_pos) & (gold < 100)):
                                self.yourbroke()
                            if (spend1000rect.collidepoint(mouse_pos) & (gold >= 1000)):
                                moneychoosen = 1000
                            if (spend1000rect.collidepoint(mouse_pos) & (gold < 1000)):
                                self.yourbroke()
                            if (spend10000rect.collidepoint(mouse_pos) & (gold >= 10000)):
                                moneychoosen = 10000
                            if (spend10000rect.collidepoint(mouse_pos) & (gold < 10000)):
                                self.yourbroke()
                            if (spend100000rect.collidepoint(mouse_pos) & (gold >= 100000)):
                                moneychoosen = 100000
                            if (spend100000rect.collidepoint(mouse_pos) & (gold < 100000)):
                                self.yourbroke()
                            if (spend1000000rect.collidepoint(mouse_pos) & (gold >= 1000000)):
                                moneychoosen = 1000000
                            if (spend1000000rect.collidepoint(mouse_pos) & (gold < 1000000)):
                                self.yourbroke()
                            if (moneychoosen != 0) and (beginrect.collidepoint(mouse_pos) and (gold >= moneychoosen)):
                                scene = scene + 1

                    draw_text('10', font3, GREY, DISPLAYSURF, 450, 860)
                    draw_text('100', font3, GREY, DISPLAYSURF, 635, 860)
                    draw_text('1000', font3, GREY, DISPLAYSURF, 827, 860)
                    draw_text('10000', font3, GREY, DISPLAYSURF, 1010, 860)
                    draw_text('100000', font3, GREY, DISPLAYSURF, 1197, 860)
                    draw_text('1000000', font3, GREY, DISPLAYSURF, 1380, 860)
                    pygame.display.update()
                if (scene == 1):
                    mouse_pos = pygame.mouse.get_pos()
                    DISPLAYSURF.blit(image191, (190, 100))
                    image199.set_alpha(150)
                    DISPLAYSURF.blit(image199, (0, 0))
                    DISPLAYSURF.blit(image197, (800, 325))
                    mouse_pos = pygame.mouse.get_pos()
                    draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                    DISPLAYSURF.blit(image164, (198, 110))
                    draw_text('gold - ', font5, WHITE, DISPLAYSURF, 375, 135)
                    draw_text(str(gold), font5, YELLOW, DISPLAYSURF, 445, 135)
                    xrect = pygame.Rect(1680, 123, 35, 35)
                    returnarrowrect = pygame.Rect(153, 110, 120, 70)
                    dicerect = pygame.Rect(800, 325, 320, 320)
                    pygame.draw.rect(DISPLAYSURF, (rainbowcol), dicerect, 10)
                    if dicerect.collidepoint(mouse_pos):
                        DISPLAYSURF.blit(image198, (800, 325))
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), dicerect, 10)
                    if xrect.collidepoint(mouse_pos):
                        draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                    if returnarrowrect.collidepoint(mouse_pos):
                        DISPLAYSURF.blit(image165, (198, 110))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if returnarrowrect.collidepoint(mouse_pos):
                                scene = -1
                            if xrect.collidepoint(mouse_pos):
                                print("Quit clicked")
                                pygame.mixer.music.stop()
                                pygame.quit()
                                sys.exit()
                            if dicerect.collidepoint(mouse_pos):
                                if(gold >= moneychoosen):
                                    gold = gold - moneychoosen
                                    scene = scene + 1
                    pygame.display.update()
                if (scene == 2):
                    DISPLAYSURF.blit(image191, (190, 100))
                    image199.set_alpha(150)
                    DISPLAYSURF.blit(image199, (0, 0))
                    draw_text('gold - ', font5, WHITE, DISPLAYSURF, 375, 135)
                    draw_text(str(gold), font5, YELLOW, DISPLAYSURF, 445, 135)
                    sound_effect = pygame.mixer.Sound(resource_path("audio/dicerollsound.mp3"))
                    sound_effect.play()
                    randomnumber1 = random.randint(1, 6)
                    mouse_pos = pygame.mouse.get_pos()
                    draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                    DISPLAYSURF.blit(image164, (198, 110))
                    xrect = pygame.Rect(1680, 123, 35, 35)
                    returnarrowrect = pygame.Rect(153, 110, 120, 70)
                    if xrect.collidepoint(mouse_pos):
                        draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                    if returnarrowrect.collidepoint(mouse_pos):
                        DISPLAYSURF.blit(image165, (198, 110))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if returnarrowrect.collidepoint(mouse_pos):
                                scene = -1
                            if xrect.collidepoint(mouse_pos):
                                print("Quit clicked")
                                pygame.mixer.music.stop()
                                pygame.quit()
                                sys.exit()

                    dicevideo = cv2.VideoCapture(resource_path("video/dicerolling.mov"))
                    fps = int(dicevideo.get(cv2.CAP_PROP_FPS))
                    clock = pygame.time.Clock()
                    while dicevideo.isOpened():
                        ret, frame = dicevideo.read()
                        if not ret:
                            break
                        frame = cv2.resize(frame, (1570, 870))
                        frame = cv2.flip(frame, 1)
                        frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
                        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        frame = pygame.surfarray.make_surface(frame).convert()
                        DISPLAYSURF.blit(frame, (179, 100))
                        draw_text('gold - ', font5, WHITE, DISPLAYSURF, 375, 135)
                        draw_text(str(gold), font5, YELLOW, DISPLAYSURF, 445, 135)
                        pygame.display.flip()
                        clock.tick(fps)
                    dicevideo.release()

                    if (randomnumber1 == 1):
                        DISPLAYSURF.blit(image192, (800, 325))
                    if (randomnumber1 == 2):
                        DISPLAYSURF.blit(image193, (800, 325))
                    if (randomnumber1 == 3):
                        DISPLAYSURF.blit(image194, (800, 325))
                    if (randomnumber1 == 4):
                        DISPLAYSURF.blit(image195, (800, 325))
                    if (randomnumber1 == 5):
                        DISPLAYSURF.blit(image196, (800, 325))
                    if (randomnumber1 == 6):
                        DISPLAYSURF.blit(image197, (800, 325))

                    screen_width, screen_height = DISPLAYSURF.get_size()
                    if(int(randomnumber1) == int(dicechoosen)):
                        sound_effect = pygame.mixer.Sound(resource_path("audio/minislotwin.mp3"))
                        sound_effect.play()
                        gold = gold + (moneychoosen * 6)
                        draw_text('You won ' + str(moneychoosen * 6) + ' gold!', font2, GOLD, DISPLAYSURF, screen_width / 2 - 215, screen_height / 2 - 345)
                    else:
                        draw_text('You lost, try again.', font2, PURPLE, DISPLAYSURF, screen_width / 2 - 215, screen_height / 2 - 345)
                    print("dice random = " +str(randomnumber1))
                    print("dice choosen = " +str(dicechoosen))

                    with open(resource_path("gamedata.txt"), "r") as file:
                        lines = file.readlines()
                        lines[0] = f"gold = {gold}\n"
                        lines[1] = f"gem = {gem}\n"
                    with open(resource_path("gamedata.txt"), "w") as file:
                        file.writelines(lines)
                    scene = scene + 1
                    pygame.display.update()


                if (scene == 3):
                    mouse_pos = pygame.mouse.get_pos()
                    draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                    DISPLAYSURF.blit(image164, (198, 110))
                    xrect = pygame.Rect(1680, 123, 35, 35)
                    returnarrowrect = pygame.Rect(153, 110, 120, 70)
                    if xrect.collidepoint(mouse_pos):
                        draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                    if returnarrowrect.collidepoint(mouse_pos):
                        DISPLAYSURF.blit(image165, (198, 110))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if returnarrowrect.collidepoint(mouse_pos):
                                scene = -1
                            if xrect.collidepoint(mouse_pos):
                                print("Quit clicked")
                                pygame.mixer.music.stop()
                                pygame.quit()
                                sys.exit()
                            if 0 <= mouseX <= 1920 and 250 <= mouseY <= 1080:
                                sound_effect = pygame.mixer.Sound(resource_path("audio/clicknoise.mp3"))
                                sound_effect.play()
                                scene = 1
                    pygame.display.update()
########################################################################################################################
    def blackjack(self):
        global gem
        global gold
        card1 = 0
        card2 = 0
        card3 = 0
        card4 = 0
        card5 = 0
        card6 = 0
        card7 = 0
        card8 = 0
        card9 = 0
        card10 = 0
        card11 = 0
        card12 = 0
        card1y = -100
        card2y = -100
        card3y = -100
        card4y = -100
        timer = 0
        standswitch = False
        moneychoosen = 0
        standcounter = 0
        while(self.repeatblackjackloop):
            self.casinogamebool = True
            startTime = pygame.time.get_ticks()
            scene = -1
            pygame.mixer.music.load(resource_path("audio/blackjack1.mp3"))
            pygame.mixer.music.play(-1)
            while(self.casinogamebool):
                with open(resource_path("gamedata.txt"), "r") as file:
                    lines = file.readlines()
                    if len(lines) >= 8:
                        goldline = lines[0].strip()
                        goldline = goldline[7:]
                        gemline = lines[1].strip()
                        gemline = gemline[6:]
                        gem = int(gemline)
                        gold = int(goldline)
                        ######
                rainbowcolor1 = int((math.sin(startTime * 0.002) + 1) * 127.5)
                rainbowcolor2 = int((math.sin(startTime * 0.003 + 2) + 1) * 127.5)
                rainbowcolor3 = int((math.sin(startTime * 0.004 + 2) + 1) * 127.5)
                rainbowcol = (rainbowcolor1, rainbowcolor2, rainbowcolor3)
                startTime = pygame.time.get_ticks()
                mouseX, mouseY = pygame.mouse.get_pos()
                card1num = card1 % 13
                card2num = card2 % 13
                card3num = card3 % 13
                card4num = card4 % 13
                card5num = card5 % 13
                card6num = card6 % 13
                card7num = card7 % 13
                card8num = card8 % 13
                card9num = card9 % 13
                card10num = card10 % 13
                card11num = card11 % 13
                card12num = card12 % 13

                card1suite = card1 % 4
                card2suite = card2 % 4
                card3suite = card3 % 4
                card4suite = card4 % 4
                card5suite = card5 % 4
                card6suite = card6 % 4
                card7suite = card7 % 4
                card8suite = card8 % 4
                card9suite = card9 % 4
                card10suite = card10 % 4
                card11suite = card11 % 4
                card12suite = card12 % 4

                CARDVALUE1 = card1num + 1
                CARDVALUE2 = card2num + 1
                CARDVALUE3 = card3num + 1
                CARDVALUE4 = card4num + 1
                CARDVALUE5 = card5num + 1
                CARDVALUE6 = card6num + 1
                CARDVALUE7 = card7num + 1
                CARDVALUE8 = card8num + 1
                CARDVALUE9 = card9num + 1
                CARDVALUE10 = card10num + 1
                CARDVALUE11 = card11num + 1
                CARDVALUE12 = card12num + 1

                if((CARDVALUE1 > 9) and (CARDVALUE1 != 13)):
                    CARDVALUE1 = 10
                if((CARDVALUE2 > 9) and (CARDVALUE2 != 13)):
                    CARDVALUE2 = 10
                if((CARDVALUE3 > 9) and (CARDVALUE3 != 13)):
                    CARDVALUE3 = 10
                if((CARDVALUE4 > 9) and (CARDVALUE4 != 13)):
                    CARDVALUE4 = 10
                if((CARDVALUE5 > 9) and (CARDVALUE5 != 13)):
                    CARDVALUE5 = 10
                if((CARDVALUE6 > 9) and (CARDVALUE6 != 13)):
                    CARDVALUE6 = 10
                if((CARDVALUE7 > 9) and (CARDVALUE7 != 13)):
                    CARDVALUE7 = 10
                if((CARDVALUE8 > 9) and (CARDVALUE8 != 13)):
                    CARDVALUE8 = 10
                if((CARDVALUE9 > 9) and (CARDVALUE9 != 13)):
                    CARDVALUE9 = 10
                if((CARDVALUE10 > 9) and (CARDVALUE10 != 13)):
                    CARDVALUE10 = 10
                if((CARDVALUE11 > 9) and (CARDVALUE11 != 13)):
                    CARDVALUE11 = 10
                if((CARDVALUE12 > 9) and (CARDVALUE12 != 13)):
                    CARDVALUE12 = 10

                if(CARDVALUE1 == 13):
                    CARDVALUE1 = 11
                if(CARDVALUE2 == 13):
                    CARDVALUE2 = 11
                if(CARDVALUE3 == 13):
                    CARDVALUE3 = 11
                if(CARDVALUE4 == 13):
                    CARDVALUE4 = 11
                if(CARDVALUE5 == 13):
                    CARDVALUE5 = 11
                if(CARDVALUE6 == 13):
                    CARDVALUE6 = 11
                if(CARDVALUE7 == 13):
                    CARDVALUE7 = 11
                if(CARDVALUE8 == 13):
                    CARDVALUE8 = 11
                if(CARDVALUE9 == 13):
                    CARDVALUE9 = 11
                if(CARDVALUE10 == 13):
                    CARDVALUE10 = 11
                if(CARDVALUE11 == 13):
                    CARDVALUE11 = 11
                if(CARDVALUE12 == 13):
                    CARDVALUE12 = 11

                if (card1num <= 9):
                    card1numm = str(card1num + 1)
                if (card2num <= 9):
                    card2numm = str(card2num + 1)
                if (card3num <= 9):
                    card3numm = str(card3num + 1)
                if (card4num <= 9):
                    card4numm = str(card4num + 1)
                if (card5num <= 9):
                    card5numm = str(card5num + 1)
                if (card6num <= 9):
                    card6numm = str(card6num + 1)
                if (card7num <= 9):
                    card7numm = str(card7num + 1)
                if (card8num <= 9):
                    card8numm = str(card8num + 1)
                if (card9num <= 9):
                    card9numm = str(card9num + 1)
                if (card10num <= 9):
                    card10numm = str(card10num + 1)
                if (card11num <= 9):
                    card11numm = str(card11num + 1)
                if (card12num <= 9):
                    card12numm = str(card12num + 1)
                if (card1num == 12):
                    card1numm = 'A'
                if (card2num == 12):
                    card2numm = 'A'
                if (card3num == 12):
                    card3numm = 'A'
                if (card4num == 12):
                    card4numm = 'A'
                if (card5num == 12):
                    card5numm = 'A'
                if (card6num == 12):
                    card6numm = 'A'
                if (card7num == 12):
                    card7numm = 'A'
                if (card8num == 12):
                    card8numm = 'A'
                if (card9num == 12):
                    card9numm = 'A'
                if (card10num == 12):
                    card10numm = 'A'
                if (card11num == 12):
                    card11numm = 'A'
                if (card12num == 12):
                    card12numm = 'A'

                if (card1num == 11):
                    card1numm = 'Q'
                if (card2num == 11):
                    card2numm = 'Q'
                if (card3num == 11):
                    card3numm = 'Q'
                if (card4num == 11):
                    card4numm = 'Q'
                if (card5num == 11):
                    card5numm = 'Q'
                if (card6num == 11):
                    card6numm = 'Q'
                if (card7num == 11):
                    card7numm = 'Q'
                if (card8num == 11):
                    card8numm = 'Q'
                if (card9num == 11):
                    card9numm = 'Q'
                if (card10num == 11):
                    card10numm = 'Q'
                if (card11num == 11):
                    card11numm = 'Q'
                if (card12num == 11):
                    card12numm = 'Q'


                if (card1num == 10):
                    card1numm = 'K'
                if (card2num == 10):
                    card2numm = 'K'
                if (card3num == 10):
                    card3numm = 'K'
                if (card4num == 10):
                    card4numm = 'K'
                if (card5num == 10):
                    card5numm = 'K'
                if (card6num == 10):
                    card6numm = 'K'
                if (card7num == 10):
                    card7numm = 'K'
                if (card8num == 10):
                    card8numm = 'K'
                if (card9num == 10):
                    card9numm = 'K'
                if (card10num == 10):
                    card10numm = 'K'
                if (card11num == 10):
                    card11numm = 'K'
                if (card12num == 10):
                    card12numm = 'K'

                if (card1num == 9):
                    card1numm = 'J'
                if (card2num == 9):
                    card2numm = 'J'
                if (card3num == 9):
                    card3numm = 'J'
                if (card4num == 9):
                    card4numm = 'J'
                if (card5num == 9):
                    card5numm = 'J'
                if (card6num == 9):
                    card6numm = 'J'
                if (card7num == 9):
                    card7numm = 'J'
                if (card8num == 9):
                    card8numm = 'J'
                if (card9num == 9):
                    card9numm = 'J'
                if (card10num == 9):
                    card10numm = 'J'
                if (card11num == 9):
                    card11numm = 'J'
                if (card12num == 9):
                    card12numm = 'J'
                if (scene == -1):
                    DISPLAYSURF.blit(image232, (190, 100))
                    mouse_pos = pygame.mouse.get_pos()
                    draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                    DISPLAYSURF.blit(image164, (198, 110))
                    draw_text('gold - ', font5, WHITE, DISPLAYSURF, 375, 135)
                    draw_text(str(gold), font5, YELLOW, DISPLAYSURF, 445, 135)
                    xrect = pygame.Rect(1680, 123, 35, 35)
                    returnarrowrect = pygame.Rect(153, 110, 120, 70)
                    if xrect.collidepoint(mouse_pos):
                        draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                    if returnarrowrect.collidepoint(mouse_pos):
                        DISPLAYSURF.blit(image165, (198, 110))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if returnarrowrect.collidepoint(mouse_pos):
                                transition(6)
                                self.casinogamebool = False
                                self.repeatblackjackloop = False
                            if xrect.collidepoint(mouse_pos):
                                print("Quit clicked")
                                pygame.mixer.music.stop()
                                pygame.quit()
                                sys.exit()
                            if 0 <= mouseX <= 1920 and 250 <= mouseY <= 1080:
                                scene = scene + 1
                    pygame.display.update()
                if(scene == 0):
                    mouseX, mouseY = pygame.mouse.get_pos()
                    DISPLAYSURF.fill(BLACK)
                    DISPLAYSURF.blit(image232, (190, 100))
                    image4.set_alpha(70)
                    DISPLAYSURF.blit(image4, (0, 0))
                    draw_text('gold - ', font5, WHITE, DISPLAYSURF, 375, 135)
                    draw_text(str(gold), font5, YELLOW, DISPLAYSURF, 445, 135)
                    mouse_pos = pygame.mouse.get_pos()
                    draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                    DISPLAYSURF.blit(image164, (198, 110))
                    xrect = pygame.Rect(1680, 123, 35, 35)
                    returnarrowrect = pygame.Rect(153, 110, 120, 70)
                    draw_text('Current Bet - ' +str(moneychoosen), font3, YELLOW, DISPLAYSURF, 1240, 210)

                    # print("x and y = " +str(mouseX) +" " +str(mouseY))

                    DISPLAYSURF.blit(image227, (395, 810))
                    DISPLAYSURF.blit(image228, (595, 810))
                    DISPLAYSURF.blit(image229, (795, 810))
                    DISPLAYSURF.blit(image230, (985, 810))
                    DISPLAYSURF.blit(image231, (1185, 810))


                    spend100rect = pygame.Rect(395, 810, 150, 150)
                    spend1000rect = pygame.Rect(595, 810, 150, 150)
                    spend10000rect = pygame.Rect(795, 810, 150, 150)
                    spend100000rect = pygame.Rect(985, 810, 150, 150)
                    spendallrect = pygame.Rect(1185, 810, 150, 150)
                    clearect = pygame.Rect(1385, 810, 150, 150)

                    beginrect = pygame.Rect(760, 480, 440, 95)

                    pygame.draw.rect(DISPLAYSURF, (BLACK), clearect)
                    pygame.draw.rect(DISPLAYSURF, (PINK), clearect, 7)

                    pygame.draw.rect(DISPLAYSURF, (RED), returnarrowrect, 6)

                    if spend100rect.collidepoint(mouse_pos):
                        DISPLAYSURF.blit(image233, (388, 803))
                    if spend1000rect.collidepoint(mouse_pos):
                        DISPLAYSURF.blit(image234, (588, 803))
                    if spend10000rect.collidepoint(mouse_pos):
                        DISPLAYSURF.blit(image235, (793, 810))
                    if spend100000rect.collidepoint(mouse_pos):
                        DISPLAYSURF.blit(image236, (978, 803))
                    if spendallrect.collidepoint(mouse_pos):
                        DISPLAYSURF.blit(image237, (1184, 803))
                    if clearect.collidepoint(mouse_pos):
                        pygame.draw.rect(DISPLAYSURF, (rainbowcol), clearect, 10)

                    if ((moneychoosen != 0)):
                        pygame.draw.rect(DISPLAYSURF, BLACK, beginrect)
                        draw_text(' Click to Play! ', font2, (105, 36, 166), DISPLAYSURF, 785, 490)
                        if beginrect.collidepoint(mouse_pos):
                            draw_text(' Click to Play! ', font2, (rainbowcolor2, rainbowcolor1, rainbowcolor3),DISPLAYSURF, 785, 490)
                            pygame.draw.rect(DISPLAYSURF, (rainbowcolor1, rainbowcolor3, rainbowcolor2), beginrect, 10)

                    if xrect.collidepoint(mouse_pos):
                        draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                    if returnarrowrect.collidepoint(mouse_pos):
                        DISPLAYSURF.blit(image165, (198, 110))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if returnarrowrect.collidepoint(mouse_pos):
                                transition(6)
                                self.casinogamebool = False
                                self.repeatblackjackloop = False
                            if xrect.collidepoint(mouse_pos):
                                print("Quit clicked")
                                pygame.mixer.music.stop()
                                pygame.quit()
                                sys.exit()
                            if (spend100rect.collidepoint(mouse_pos) & (gold < (moneychoosen + 100))):
                                self.yourbroke()
                            if (spend100rect.collidepoint(mouse_pos) & (gold >= (moneychoosen + 100))):
                                moneychoosen = moneychoosen + 100
                            if (spend1000rect.collidepoint(mouse_pos) & (gold < (moneychoosen + 1000))):
                                self.yourbroke()
                            if (spend1000rect.collidepoint(mouse_pos) & (gold >= (moneychoosen + 1000))):
                                moneychoosen = moneychoosen + 1000
                            if (spend10000rect.collidepoint(mouse_pos) & (gold < (moneychoosen + 10000))):
                                self.yourbroke()
                            if (spend10000rect.collidepoint(mouse_pos) & (gold >= (moneychoosen + 10000))):
                                moneychoosen = moneychoosen + 10000
                            if (spend100000rect.collidepoint(mouse_pos) & (gold < (moneychoosen + 100000))):
                                self.yourbroke()
                            if (spend100000rect.collidepoint(mouse_pos) & (gold >= (moneychoosen + 100000))):
                                moneychoosen = moneychoosen + 100000
                            if (spendallrect.collidepoint(mouse_pos)):
                                moneychoosen = gold
                            if (clearect.collidepoint(mouse_pos)):
                                moneychoosen = 0
                            if (moneychoosen != 0) & (beginrect.collidepoint(mouse_pos)) & (gold >= moneychoosen):
                                card1 = random.randint(1,52)
                                card2 = random.randint(1,52)
                                card3 = random.randint(1,52)
                                card4 = random.randint(1,52)
                                card5 = random.randint(1,52)
                                card6 = random.randint(1,52)
                                card7 = random.randint(1,52)
                                card8 = random.randint(1,52)
                                card9 = random.randint(1,52)
                                card10 = random.randint(1,52)
                                card11 = random.randint(1,52)
                                card12 = random.randint(1,52)

                                card1y = -100
                                card2y = -100
                                card3y = -400
                                card4y = -400
                                gold = gold - moneychoosen
                                scene = scene + 1
                                timer = 125
                    draw_text('100', font3, RED, DISPLAYSURF, 435, 755)
                    draw_text('1000', font3, RED, DISPLAYSURF, 625, 755)
                    draw_text('10000', font3, RED, DISPLAYSURF, 817, 755)
                    draw_text('100000', font3, RED, DISPLAYSURF, 1005, 755)
                    draw_text('All In', font3, RED, DISPLAYSURF, 1210, 755)
                    draw_text('Clear', font3, WHITE, DISPLAYSURF, 1405, 865)

                    pygame.display.update()

                if (scene == 1):
                    mouseX, mouseY = pygame.mouse.get_pos()
                    DISPLAYSURF.blit(image232, (190, 100))
                    image4.set_alpha(70)
                    DISPLAYSURF.blit(image4, (0, 0))
                    mouse_pos = pygame.mouse.get_pos()
                    draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                    DISPLAYSURF.blit(image164, (198, 110))
                    draw_text('gold - ', font5, WHITE, DISPLAYSURF, 375, 135)
                    draw_text(str(gold), font5, YELLOW, DISPLAYSURF, 445, 135)
                    draw_text('Current Bet - ' +str(moneychoosen), font3, YELLOW, DISPLAYSURF, 1240, 210)
                    # print("x and y = " +str(mouseX) +" " +str(mouseY))

                    if(card1y <= 630):
                        card1y = card1y + 10
                        card2y = card2y + 10
                    if(card3y <= 135):
                        card3y = card3y + 10
                        card4y = card4y + 10

                    DISPLAYSURF.blit(image242, (780, card3y))
                    DISPLAYSURF.blit(image242, (980, card4y))
                    if (timer != 0):
                        timer = timer - 1
                        DISPLAYSURF.blit(image242, (780, card1y))
                        DISPLAYSURF.blit(image242, (980, card2y))

                    if (timer == 0):

                        if (card1suite == 0):
                            DISPLAYSURF.blit(image238, (780, card1y))
                        if (card1suite == 1):
                            DISPLAYSURF.blit(image239, (780, card1y))
                        if (card1suite == 2):
                            DISPLAYSURF.blit(image240, (780, card1y))
                        if (card1suite == 3):
                            DISPLAYSURF.blit(image241, (780, card1y))
                        if (card2suite == 0):
                            DISPLAYSURF.blit(image238, (980, card2y))
                        if (card2suite == 1):
                            DISPLAYSURF.blit(image239, (980, card2y))
                        if (card2suite == 2):
                            DISPLAYSURF.blit(image240, (980, card2y))
                        if (card2suite == 3):
                            DISPLAYSURF.blit(image241, (980, card2y))
                        if (card4suite == 0):
                            DISPLAYSURF.blit(image238, (980, card4y))
                        if (card4suite == 1):
                            DISPLAYSURF.blit(image239, (980, card4y))
                        if (card4suite == 2):
                            DISPLAYSURF.blit(image240, (980, card4y))
                        if (card4suite == 3):
                            DISPLAYSURF.blit(image241, (980, card4y))
                        '''if (card3suite == 0):
                            DISPLAYSURF.blit(image238, (780, card3y))
                        if (card3suite == 1):
                            DISPLAYSURF.blit(image239, (780, card3y))
                        if (card3suite == 2):
                            DISPLAYSURF.blit(image240, (780, card3y))
                        if (card3suite == 3):
                            DISPLAYSURF.blit(image241, (780, card3y))
                        if (card4suite == 0):
                            DISPLAYSURF.blit(image238, (980, card4y))
                        if (card4suite == 1):
                            DISPLAYSURF.blit(image239, (980, card4y))
                        if (card4suite == 2):
                            DISPLAYSURF.blit(image240, (980, card4y))
                        if (card4suite == 3):
                            DISPLAYSURF.blit(image241, (980, card4y))'''
                        draw_text(card1numm, font5, BLACK, DISPLAYSURF, 783, 635)
                        draw_text(card2numm, font5, BLACK, DISPLAYSURF, 983, 635)
                        draw_text(card4numm, font5, BLACK, DISPLAYSURF, 990, 144)

                        draw_text(card1numm, font5, BLACK, DISPLAYSURF, 915, 812)
                        draw_text(card2numm, font5, BLACK, DISPLAYSURF, 1115, 812)
                        draw_text(card4numm, font5, BLACK, DISPLAYSURF, 1122, 305)

                        if(standswitch):
                            if (card3suite == 0):
                                DISPLAYSURF.blit(image238, (780, card3y))
                            if (card3suite == 1):
                                DISPLAYSURF.blit(image239, (780, card3y))
                            if (card3suite == 2):
                                DISPLAYSURF.blit(image240, (780, card3y))
                            if (card3suite == 3):
                                DISPLAYSURF.blit(image241, (780, card3y))
                            draw_text(card3numm, font5, BLACK, DISPLAYSURF, 800, 144)
                            draw_text(card3numm, font5, BLACK, DISPLAYSURF, 910, 310)
                            if (CARDVALUE3 + CARDVALUE4 >= 17):
                                if(CARDVALUE3 + CARDVALUE4 == 21):
                                    sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                    sound_effect.play()
                                    scene = 98
                                elif (CARDVALUE3 + CARDVALUE4 > 21):
                                    sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                    sound_effect.play()
                                    scene = 99
                                elif(CARDVALUE1 + CARDVALUE2 >= 17):
                                    if (CARDVALUE3 + CARDVALUE4 < CARDVALUE1 + CARDVALUE2):
                                        sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                        sound_effect.play()
                                        scene = 99
                                    if (CARDVALUE3 + CARDVALUE4 >= CARDVALUE1 + CARDVALUE2):
                                        sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                        sound_effect.play()
                                        scene = 98
                            if (CARDVALUE3 + CARDVALUE4 < 17):
                                if (card8suite == 0):
                                    DISPLAYSURF.blit(image238, (1180, 140))
                                if (card8suite == 1):
                                    DISPLAYSURF.blit(image239, (1180, 140))
                                if (card8suite == 2):
                                    DISPLAYSURF.blit(image240, (1180, 140))
                                if (card8suite == 3):
                                    DISPLAYSURF.blit(image241, (1180, 140))
                                draw_text(card8numm, font5, BLACK, DISPLAYSURF, 1183, 144)
                                draw_text(card8numm, font5, BLACK, DISPLAYSURF, 1315, 305)
                                if (CARDVALUE3 + CARDVALUE4 + CARDVALUE8 >= 17):
                                    dealerhand = CARDVALUE3 + CARDVALUE4 + CARDVALUE8
                                    playerhand = CARDVALUE1 + CARDVALUE2
                                    if (dealerhand == 21):
                                        sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                        sound_effect.play()
                                        scene = 98
                                    if (dealerhand > 21):
                                        sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                        sound_effect.play()
                                        scene = 99
                                    if(dealerhand != 21 and dealerhand < 21):
                                        if(dealerhand >= playerhand):
                                            sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                            sound_effect.play()
                                            scene = 98
                                        if(dealerhand < playerhand):
                                            sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                            sound_effect.play()
                                            scene = 99
                                else:
                                    if (card9suite == 0):
                                        DISPLAYSURF.blit(image238, (1380, 140))
                                    if (card9suite == 1):
                                        DISPLAYSURF.blit(image239, (1380, 140))
                                    if (card9suite == 2):
                                        DISPLAYSURF.blit(image240, (1380, 140))
                                    if (card9suite == 3):
                                        DISPLAYSURF.blit(image241, (1380, 140))
                                    draw_text(card9numm, font5, BLACK, DISPLAYSURF, 1383, 144)
                                    draw_text(card9numm, font5, BLACK, DISPLAYSURF, 1515, 305)
                                    if (CARDVALUE3 + CARDVALUE4 + CARDVALUE8 + CARDVALUE9 >= 17):
                                        dealerhand = CARDVALUE3 + CARDVALUE4 + CARDVALUE8 + CARDVALUE9
                                        playerhand = CARDVALUE1 + CARDVALUE2
                                        if(dealerhand == 21):
                                            sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                            sound_effect.play()
                                            scene = 98
                                        if(dealerhand > 21):
                                            sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                            sound_effect.play()
                                            scene = 99
                                        if (dealerhand != 21 and dealerhand < 21):
                                            if (dealerhand >= playerhand):
                                                sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                                sound_effect.play()
                                                scene = 98
                                            if (dealerhand < playerhand):
                                                sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                                sound_effect.play()
                                                scene = 99
                                    else:
                                        if (card10suite == 0):
                                            DISPLAYSURF.blit(image238, (580, 140))
                                        if (card10suite == 1):
                                            DISPLAYSURF.blit(image239, (580, 140))
                                        if (card10suite == 2):
                                            DISPLAYSURF.blit(image240, (580, 140))
                                        if (card10suite == 3):
                                            DISPLAYSURF.blit(image241, (580, 140))
                                        draw_text(card10numm, font5, BLACK, DISPLAYSURF, 583, 144)
                                        draw_text(card10numm, font5, BLACK, DISPLAYSURF, 715, 305)
                                        if (CARDVALUE3 + CARDVALUE4 + CARDVALUE8 + CARDVALUE9 + CARDVALUE10 >= 17):
                                            dealerhand = CARDVALUE3 + CARDVALUE4 + CARDVALUE8 + CARDVALUE9 + CARDVALUE10
                                            playerhand = CARDVALUE1 + CARDVALUE2
                                            if (dealerhand == 21):
                                                sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                                sound_effect.play()
                                                scene = 98
                                            if (dealerhand > 21):
                                                sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                                sound_effect.play()
                                                scene = 99
                                            if (dealerhand != 21 and dealerhand < 21):
                                                if (dealerhand >= playerhand):
                                                    sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                                    sound_effect.play()
                                                    scene = 98
                                                if (dealerhand < playerhand):
                                                    sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                                    sound_effect.play()
                                                    scene = 99
                                        else:
                                            if (card11suite == 0):
                                                DISPLAYSURF.blit(image238, (380, 140))
                                            if (card11suite == 1):
                                                DISPLAYSURF.blit(image239, (380, 140))
                                            if (card11suite == 2):
                                                DISPLAYSURF.blit(image240, (380, 140))
                                            if (card11suite == 3):
                                                DISPLAYSURF.blit(image241, (380, 140))
                                            draw_text(card11numm, font5, BLACK, DISPLAYSURF, 383, 144)
                                            draw_text(card11numm, font5, BLACK, DISPLAYSURF, 515, 305)
                                            if (CARDVALUE3 + CARDVALUE4 + CARDVALUE8 + CARDVALUE9 + CARDVALUE10 + CARDVALUE11 >= 17):
                                                dealerhand = CARDVALUE3 + CARDVALUE4 + CARDVALUE8 + CARDVALUE9 + CARDVALUE10 + CARDVALUE11
                                                playerhand = CARDVALUE1 + CARDVALUE2
                                                if (dealerhand == 21):
                                                    sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                                    sound_effect.play()
                                                    scene = 98
                                                if (dealerhand > 21):
                                                    sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                                    sound_effect.play()
                                                    scene = 99
                                                if (dealerhand != 21 and dealerhand < 21):
                                                    if (dealerhand >= playerhand):
                                                        sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                                        sound_effect.play()
                                                        scene = 98
                                                    if (dealerhand < playerhand):
                                                        sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                                        sound_effect.play()
                                                        scene = 99
                                            else:
                                                if (dealerhand >= playerhand):
                                                    sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                                    sound_effect.play()
                                                    scene = 98
                                                if (dealerhand < playerhand):
                                                    sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                                    sound_effect.play()
                                                    scene = 99

                        if(CARDVALUE1 + CARDVALUE2 > 21):
                            sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                            sound_effect.play()
                            scene = 100

                    hitbox = pygame.Rect(782, 900, 160, 35)
                    standbox = pygame.Rect(982, 900, 160, 35)
                    pygame.draw.rect(DISPLAYSURF, BLACK, hitbox)
                    pygame.draw.rect(DISPLAYSURF, BLACK, standbox)
                    pygame.draw.rect(DISPLAYSURF, RED, hitbox, 6)
                    pygame.draw.rect(DISPLAYSURF, SKYBLUE, standbox, 6)

                    draw_text('Hit', font5, WHITE, DISPLAYSURF, 845, 902)
                    draw_text('Stand ', font5, WHITE, DISPLAYSURF, 1032, 902)
                    if hitbox.collidepoint(mouse_pos):
                        draw_text('Hit', font5, RED, DISPLAYSURF, 845, 902)
                    if standbox.collidepoint(mouse_pos):
                        draw_text('Stand ', font5, BLUE, DISPLAYSURF, 1032, 902)
                    xrect = pygame.Rect(1680, 123, 35, 35)
                    returnarrowrect = pygame.Rect(153, 110, 120, 70)

                    if xrect.collidepoint(mouse_pos):
                        draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                    if returnarrowrect.collidepoint(mouse_pos):
                        DISPLAYSURF.blit(image165, (198, 110))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if returnarrowrect.collidepoint(mouse_pos):
                                standswitch = True
                                scene = -1
                            if xrect.collidepoint(mouse_pos):
                                print("Quit clicked")
                                pygame.mixer.music.stop()
                                pygame.quit()
                                sys.exit()
                            if (card1y >= 630):
                                if hitbox.collidepoint(mouse_pos):
                                    card5y = -100
                                    card6y = -100
                                    card7y = -100
                                    card8y = -100
                                    timer = 125
                                    scene = scene + 1
                                if standbox.collidepoint(mouse_pos):
                                    standswitch = True
                    pygame.display.update()
                if (scene == 2):
                    mouseX, mouseY = pygame.mouse.get_pos()
                    DISPLAYSURF.blit(image232, (190, 100))
                    image4.set_alpha(70)
                    DISPLAYSURF.blit(image4, (0, 0))
                    mouse_pos = pygame.mouse.get_pos()
                    draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                    DISPLAYSURF.blit(image164, (198, 110))
                    draw_text('gold - ', font5, WHITE, DISPLAYSURF, 375, 135)
                    draw_text(str(gold), font5, YELLOW, DISPLAYSURF, 445, 135)
                    draw_text('Current Bet - ' + str(moneychoosen), font3, YELLOW, DISPLAYSURF, 1240, 210)
                    # print("x and y = " + str(mouseX) + " " + str(mouseY))

                    if (card5y <= 630):
                        card5y = card5y + 10

                    if (card1suite == 0):
                        DISPLAYSURF.blit(image238, (780, card1y))
                    if (card1suite == 1):
                        DISPLAYSURF.blit(image239, (780, card1y))
                    if (card1suite == 2):
                        DISPLAYSURF.blit(image240, (780, card1y))
                    if (card1suite == 3):
                        DISPLAYSURF.blit(image241, (780, card1y))
                    if (card2suite == 0):
                        DISPLAYSURF.blit(image238, (980, card2y))
                    if (card2suite == 1):
                        DISPLAYSURF.blit(image239, (980, card2y))
                    if (card2suite == 2):
                        DISPLAYSURF.blit(image240, (980, card2y))
                    if (card2suite == 3):
                        DISPLAYSURF.blit(image241, (980, card2y))
                    if (card4suite == 0):
                        DISPLAYSURF.blit(image238, (980, card4y))
                    if (card4suite == 1):
                        DISPLAYSURF.blit(image239, (980, card4y))
                    if (card4suite == 2):
                        DISPLAYSURF.blit(image240, (980, card4y))
                    if (card4suite == 3):
                        DISPLAYSURF.blit(image241, (980, card4y))
                    '''if (card3suite == 0):
                        DISPLAYSURF.blit(image238, (780, card3y))
                    if (card3suite == 1):
                        DISPLAYSURF.blit(image239, (780, card3y))
                    if (card3suite == 2):
                        DISPLAYSURF.blit(image240, (780, card3y))
                    if (card3suite == 3):
                        DISPLAYSURF.blit(image241, (780, card3y))
                    if (card4suite == 0):
                        DISPLAYSURF.blit(image238, (980, card4y))
                    if (card4suite == 1):
                        DISPLAYSURF.blit(image239, (980, card4y))
                    if (card4suite == 2):
                        DISPLAYSURF.blit(image240, (980, card4y))
                    if (card4suite == 3):
                        DISPLAYSURF.blit(image241, (980, card4y))'''
                    draw_text(card1numm, font5, BLACK, DISPLAYSURF, 783, 635)
                    draw_text(card2numm, font5, BLACK, DISPLAYSURF, 983, 635)
                    draw_text(card4numm, font5, BLACK, DISPLAYSURF, 990, 144)

                    draw_text(card1numm, font5, BLACK, DISPLAYSURF, 915, 812)
                    draw_text(card2numm, font5, BLACK, DISPLAYSURF, 1115, 812)
                    draw_text(card4numm, font5, BLACK, DISPLAYSURF, 1122, 305)

                    DISPLAYSURF.blit(image242, (780, card3y))
                    if (timer != 0):
                        timer = timer - 1
                        DISPLAYSURF.blit(image242, (1180, card5y))

                    if (timer == 0):
                        if (card5suite == 0):
                            DISPLAYSURF.blit(image238, (1180, card5y))
                        if (card5suite == 1):
                            DISPLAYSURF.blit(image239, (1180, card5y))
                        if (card5suite == 2):
                            DISPLAYSURF.blit(image240, (1180, card5y))
                        if (card5suite == 3):
                            DISPLAYSURF.blit(image241, (1180, card5y))

                        draw_text(card5numm, font5, BLACK, DISPLAYSURF, 1183, 635)
                        draw_text(card5numm, font5, BLACK, DISPLAYSURF, 1315, 812)

                        if(standswitch):
                            if (card3suite == 0):
                                DISPLAYSURF.blit(image238, (780, card3y))
                            if (card3suite == 1):
                                DISPLAYSURF.blit(image239, (780, card3y))
                            if (card3suite == 2):
                                DISPLAYSURF.blit(image240, (780, card3y))
                            if (card3suite == 3):
                                DISPLAYSURF.blit(image241, (780, card3y))
                            draw_text(card3numm, font5, BLACK, DISPLAYSURF, 800, 144)
                            draw_text(card3numm, font5, BLACK, DISPLAYSURF, 910, 310)
                            if (CARDVALUE3 + CARDVALUE4 >= 17):
                                if(CARDVALUE3 + CARDVALUE4 == 21):
                                    sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                    sound_effect.play()
                                    scene = 98
                                elif (CARDVALUE3 + CARDVALUE4 > 21):
                                    sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                    sound_effect.play()
                                    scene = 99
                                elif(CARDVALUE1 + CARDVALUE2 >= 17):
                                    if (CARDVALUE3 + CARDVALUE4 < CARDVALUE1 + CARDVALUE2+ CARDVALUE5):
                                        sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                        sound_effect.play()
                                        scene = 99
                                    if (CARDVALUE3 + CARDVALUE4 >= CARDVALUE1 + CARDVALUE2 + CARDVALUE5):
                                        sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                        sound_effect.play()
                                        scene = 98
                            if (CARDVALUE3 + CARDVALUE4 < 17):
                                if (card8suite == 0):
                                    DISPLAYSURF.blit(image238, (1180, 140))
                                if (card8suite == 1):
                                    DISPLAYSURF.blit(image239, (1180, 140))
                                if (card8suite == 2):
                                    DISPLAYSURF.blit(image240, (1180, 140))
                                if (card8suite == 3):
                                    DISPLAYSURF.blit(image241, (1180, 140))
                                draw_text(card8numm, font5, BLACK, DISPLAYSURF, 1183, 144)
                                draw_text(card8numm, font5, BLACK, DISPLAYSURF, 1315, 305)
                                if (CARDVALUE3 + CARDVALUE4 + CARDVALUE8 >= 17):
                                    dealerhand = CARDVALUE3 + CARDVALUE4 + CARDVALUE8
                                    playerhand = CARDVALUE1 + CARDVALUE2 + CARDVALUE5
                                    if (dealerhand == 21):
                                        sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                        sound_effect.play()
                                        scene = 98
                                    if (dealerhand > 21):
                                        sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                        sound_effect.play()
                                        scene = 99
                                    if(dealerhand != 21 and dealerhand < 21):
                                        if(dealerhand >= playerhand):
                                            sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                            sound_effect.play()
                                            scene = 98
                                        if(dealerhand < playerhand):
                                            sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                            sound_effect.play()
                                            scene = 99
                                else:
                                    if (card9suite == 0):
                                        DISPLAYSURF.blit(image238, (1380, 140))
                                    if (card9suite == 1):
                                        DISPLAYSURF.blit(image239, (1380, 140))
                                    if (card9suite == 2):
                                        DISPLAYSURF.blit(image240, (1380, 140))
                                    if (card9suite == 3):
                                        DISPLAYSURF.blit(image241, (1380, 140))
                                    draw_text(card9numm, font5, BLACK, DISPLAYSURF, 1383, 144)
                                    draw_text(card9numm, font5, BLACK, DISPLAYSURF, 1515, 305)
                                    if (CARDVALUE3 + CARDVALUE4 + CARDVALUE8 + CARDVALUE9 >= 17):
                                        dealerhand = CARDVALUE3 + CARDVALUE4 + CARDVALUE8 + CARDVALUE9
                                        playerhand = CARDVALUE1 + CARDVALUE2 + CARDVALUE5
                                        if(dealerhand == 21):
                                            sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                            sound_effect.play()
                                            scene = 98
                                        if(dealerhand > 21):
                                            sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                            sound_effect.play()
                                            scene = 99
                                        if (dealerhand != 21 and dealerhand < 21):
                                            if (dealerhand >= playerhand):
                                                sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                                sound_effect.play()
                                                scene = 98
                                            if (dealerhand < playerhand):
                                                sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                                sound_effect.play()
                                                scene = 99
                                    else:
                                        if (card10suite == 0):
                                            DISPLAYSURF.blit(image238, (1380, 140))
                                        if (card10suite == 1):
                                            DISPLAYSURF.blit(image239, (1380, 140))
                                        if (card10suite == 2):
                                            DISPLAYSURF.blit(image240, (1380, 140))
                                        if (card10suite == 3):
                                            DISPLAYSURF.blit(image241, (1380, 140))
                                        draw_text(card10numm, font5, BLACK, DISPLAYSURF, 1383, 144)
                                        draw_text(card10numm, font5, BLACK, DISPLAYSURF, 1515, 305)
                                        if (CARDVALUE3 + CARDVALUE4 + CARDVALUE8 + CARDVALUE9 + CARDVALUE10 >= 17):
                                            dealerhand = CARDVALUE3 + CARDVALUE4 + CARDVALUE8 + CARDVALUE9 + CARDVALUE10
                                            playerhand = CARDVALUE1 + CARDVALUE2 + CARDVALUE5
                                            if (dealerhand == 21):
                                                sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                                sound_effect.play()
                                                scene = 98
                                            if (dealerhand > 21):
                                                sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                                sound_effect.play()
                                                scene = 99
                                            if (dealerhand != 21 and dealerhand < 21):
                                                if (dealerhand >= playerhand):
                                                    sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                                    sound_effect.play()
                                                    scene = 98
                                                if (dealerhand < playerhand):
                                                    sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                                    sound_effect.play()
                                                    scene = 99
                                        else:
                                            if (card11suite == 0):
                                                DISPLAYSURF.blit(image238, (1380, 140))
                                            if (card11suite == 1):
                                                DISPLAYSURF.blit(image239, (1380, 140))
                                            if (card11suite == 2):
                                                DISPLAYSURF.blit(image240, (1380, 140))
                                            if (card11suite == 3):
                                                DISPLAYSURF.blit(image241, (1380, 140))
                                            draw_text(card11numm, font5, BLACK, DISPLAYSURF, 1383, 144)
                                            draw_text(card11numm, font5, BLACK, DISPLAYSURF, 1515, 305)
                                            if (CARDVALUE3 + CARDVALUE4 + CARDVALUE8 + CARDVALUE9 + CARDVALUE10 + CARDVALUE11 >= 17):
                                                dealerhand = CARDVALUE3 + CARDVALUE4 + CARDVALUE8 + CARDVALUE9 + CARDVALUE10 + CARDVALUE11
                                                playerhand = CARDVALUE1 + CARDVALUE2 + CARDVALUE5
                                                if (dealerhand == 21):
                                                    sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                                    sound_effect.play()
                                                    scene = 98
                                                if (dealerhand > 21):
                                                    sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                                    sound_effect.play()
                                                    scene = 99
                                                if (dealerhand != 21 and dealerhand < 21):
                                                    if (dealerhand >= playerhand):
                                                        sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                                        sound_effect.play()
                                                        scene = 98
                                                    if (dealerhand < playerhand):
                                                        sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                                        sound_effect.play()
                                                        scene = 99
                                            else:
                                                if (dealerhand >= playerhand):
                                                    sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                                    sound_effect.play()
                                                    scene = 98
                                                if (dealerhand < playerhand):
                                                    sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                                    sound_effect.play()
                                                    scene = 99

                            elif(CARDVALUE3 + CARDVALUE4 == 21):
                                sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                sound_effect.play()
                                scene = 98
                            elif (CARDVALUE3 + CARDVALUE4 > 21):
                                sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                sound_effect.play()
                                scene = 99
                            else:
                                if (CARDVALUE3 + CARDVALUE4 < CARDVALUE1 + CARDVALUE2 + CARDVALUE5):
                                    sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                    sound_effect.play()
                                    scene = 99
                                if (CARDVALUE3 + CARDVALUE4 >= CARDVALUE1 + CARDVALUE2 + CARDVALUE5):
                                    sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                    sound_effect.play()
                                    scene = 98

                        if((CARDVALUE1 + CARDVALUE2 + CARDVALUE5) > 21):
                            sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                            sound_effect.play()
                            scene = 100

                    hitbox = pygame.Rect(782, 900, 160, 35)
                    standbox = pygame.Rect(982, 900, 160, 35)
                    pygame.draw.rect(DISPLAYSURF, BLACK, hitbox)
                    pygame.draw.rect(DISPLAYSURF, BLACK, standbox)
                    pygame.draw.rect(DISPLAYSURF, RED, hitbox, 6)
                    pygame.draw.rect(DISPLAYSURF, SKYBLUE, standbox, 6)

                    draw_text('Hit', font5, WHITE, DISPLAYSURF, 845, 902)
                    draw_text('Stand ', font5, WHITE, DISPLAYSURF, 1032, 902)
                    if hitbox.collidepoint(mouse_pos):
                        draw_text('Hit', font5, RED, DISPLAYSURF, 845, 902)
                    if standbox.collidepoint(mouse_pos):
                        draw_text('Stand ', font5, BLUE, DISPLAYSURF, 1032, 902)

                    xrect = pygame.Rect(1680, 123, 35, 35)
                    returnarrowrect = pygame.Rect(153, 110, 120, 70)

                    if xrect.collidepoint(mouse_pos):
                        draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                    if returnarrowrect.collidepoint(mouse_pos):
                        DISPLAYSURF.blit(image165, (198, 110))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if returnarrowrect.collidepoint(mouse_pos):
                                standswitch = True
                                scene = -1
                            if xrect.collidepoint(mouse_pos):
                                print("Quit clicked")
                                pygame.mixer.music.stop()
                                pygame.quit()
                                sys.exit()
                            if (card5y >= 630):
                                if hitbox.collidepoint(mouse_pos):
                                    draw_text('Hit', font5, RED, DISPLAYSURF, 845, 902)
                                    card6y = -100
                                    card7y = -100
                                    card8y = -100
                                    timer = 125
                                    scene = scene + 1
                                if standbox.collidepoint(mouse_pos):
                                    draw_text('Stand ', font5, BLUE, DISPLAYSURF, 1032, 902)
                                    standswitch = True
                    pygame.display.update()
                if (scene == 3):
                    mouseX, mouseY = pygame.mouse.get_pos()
                    DISPLAYSURF.blit(image232, (190, 100))
                    image4.set_alpha(70)
                    DISPLAYSURF.blit(image4, (0, 0))
                    mouse_pos = pygame.mouse.get_pos()
                    draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                    DISPLAYSURF.blit(image164, (198, 110))
                    draw_text('gold - ', font5, WHITE, DISPLAYSURF, 375, 135)
                    draw_text(str(gold), font5, YELLOW, DISPLAYSURF, 445, 135)
                    draw_text('Current Bet - ' + str(moneychoosen), font3, YELLOW, DISPLAYSURF, 1240, 210)
                    # print("x and y = " + str(mouseX) + " " + str(mouseY))

                    if (card6y <= 630):
                        card6y = card6y + 10

                    if (card1suite == 0):
                        DISPLAYSURF.blit(image238, (780, card1y))
                    if (card1suite == 1):
                        DISPLAYSURF.blit(image239, (780, card1y))
                    if (card1suite == 2):
                        DISPLAYSURF.blit(image240, (780, card1y))
                    if (card1suite == 3):
                        DISPLAYSURF.blit(image241, (780, card1y))
                    if (card2suite == 0):
                        DISPLAYSURF.blit(image238, (980, card2y))
                    if (card2suite == 1):
                        DISPLAYSURF.blit(image239, (980, card2y))
                    if (card2suite == 2):
                        DISPLAYSURF.blit(image240, (980, card2y))
                    if (card2suite == 3):
                        DISPLAYSURF.blit(image241, (980, card2y))
                    if (card4suite == 0):
                        DISPLAYSURF.blit(image238, (980, card4y))
                    if (card4suite == 1):
                        DISPLAYSURF.blit(image239, (980, card4y))
                    if (card4suite == 2):
                        DISPLAYSURF.blit(image240, (980, card4y))
                    if (card4suite == 3):
                        DISPLAYSURF.blit(image241, (980, card4y))
                    '''if (card3suite == 0):
                        DISPLAYSURF.blit(image238, (780, card3y))
                    if (card3suite == 1):
                        DISPLAYSURF.blit(image239, (780, card3y))
                    if (card3suite == 2):
                        DISPLAYSURF.blit(image240, (780, card3y))
                    if (card3suite == 3):
                        DISPLAYSURF.blit(image241, (780, card3y))
                    if (card4suite == 0):
                        DISPLAYSURF.blit(image238, (980, card4y))
                    if (card4suite == 1):
                        DISPLAYSURF.blit(image239, (980, card4y))
                    if (card4suite == 2):
                        DISPLAYSURF.blit(image240, (980, card4y))
                    if (card4suite == 3):
                        DISPLAYSURF.blit(image241, (980, card4y))'''
                    if (card5suite == 0):
                        DISPLAYSURF.blit(image238, (1180, card5y))
                    if (card5suite == 1):
                        DISPLAYSURF.blit(image239, (1180, card5y))
                    if (card5suite == 2):
                        DISPLAYSURF.blit(image240, (1180, card5y))
                    if (card5suite == 3):
                        DISPLAYSURF.blit(image241, (1180, card5y))
                    draw_text(card1numm, font5, BLACK, DISPLAYSURF, 915, 812)
                    draw_text(card2numm, font5, BLACK, DISPLAYSURF, 1115, 812)
                    draw_text(card1numm, font5, BLACK, DISPLAYSURF, 783, 635)
                    draw_text(card2numm, font5, BLACK, DISPLAYSURF, 983, 635)
                    draw_text(card5numm, font5, BLACK, DISPLAYSURF, 1183, 635)
                    draw_text(card5numm, font5, BLACK, DISPLAYSURF, 1315, 812)

                    draw_text(card4numm, font5, BLACK, DISPLAYSURF, 990, 144)
                    draw_text(card4numm, font5, BLACK, DISPLAYSURF, 1122, 305)

                    DISPLAYSURF.blit(image242, (780, card3y))
                    if (timer != 0):
                        timer = timer - 1
                        DISPLAYSURF.blit(image242, (1380, card6y))

                    if (timer == 0):
                        if (card6suite == 0):
                            DISPLAYSURF.blit(image238, (1380, card6y))
                        if (card6suite == 1):
                            DISPLAYSURF.blit(image239, (1380, card6y))
                        if (card6suite == 2):
                            DISPLAYSURF.blit(image240, (1380, card6y))
                        if (card6suite == 3):
                            DISPLAYSURF.blit(image241, (1380, card6y))

                        draw_text(card6numm, font5, BLACK, DISPLAYSURF, 1383, 635)

                        #draw_text(card3numm, font5, BLACK, DISPLAYSURF, 783, 131)
                        #draw_text(card4numm, font5, BLACK, DISPLAYSURF, 983, 131)

                        draw_text(card6numm, font5, BLACK, DISPLAYSURF, 1515, 812)

                        #draw_text(card3numm, font5, BLACK, DISPLAYSURF, 918, 315)
                        #draw_text(card4numm, font5, BLACK, DISPLAYSURF, 1118, 315)

                        if(standswitch):
                            if (card3suite == 0):
                                DISPLAYSURF.blit(image238, (780, card3y))
                            if (card3suite == 1):
                                DISPLAYSURF.blit(image239, (780, card3y))
                            if (card3suite == 2):
                                DISPLAYSURF.blit(image240, (780, card3y))
                            if (card3suite == 3):
                                DISPLAYSURF.blit(image241, (780, card3y))
                            draw_text(card3numm, font5, BLACK, DISPLAYSURF, 800, 144)
                            draw_text(card3numm, font5, BLACK, DISPLAYSURF, 910, 310)
                            if (CARDVALUE3 + CARDVALUE4 >= 17):
                                if(CARDVALUE3 + CARDVALUE4 == 21):
                                    sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                    sound_effect.play()
                                    scene = 98
                                elif (CARDVALUE3 + CARDVALUE4 > 21):
                                    sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                    sound_effect.play()
                                    scene = 99
                                elif(CARDVALUE1 + CARDVALUE2 >= 17):
                                    if (CARDVALUE3 + CARDVALUE4 < CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6):
                                        sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                        sound_effect.play()
                                        scene = 99
                                    if (CARDVALUE3 + CARDVALUE4 >= CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6):
                                        sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                        sound_effect.play()
                                        scene = 98
                            if (CARDVALUE3 + CARDVALUE4 < 17):
                                if (card8suite == 0):
                                    DISPLAYSURF.blit(image238, (1180, 140))
                                if (card8suite == 1):
                                    DISPLAYSURF.blit(image239, (1180, 140))
                                if (card8suite == 2):
                                    DISPLAYSURF.blit(image240, (1180, 140))
                                if (card8suite == 3):
                                    DISPLAYSURF.blit(image241, (1180, 140))
                                draw_text(card8numm, font5, BLACK, DISPLAYSURF, 1183, 144)
                                draw_text(card8numm, font5, BLACK, DISPLAYSURF, 1315, 305)
                                if (CARDVALUE3 + CARDVALUE4 + CARDVALUE8 >= 17):
                                    dealerhand = CARDVALUE3 + CARDVALUE4 + CARDVALUE8
                                    playerhand = CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6
                                    if (dealerhand == 21):
                                        sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                        sound_effect.play()
                                        scene = 98
                                    if (dealerhand > 21):
                                        sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                        sound_effect.play()
                                        scene = 99
                                    if(dealerhand != 21 and dealerhand < 21):
                                        if(dealerhand >= playerhand):
                                            sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                            sound_effect.play()
                                            scene = 98
                                        if(dealerhand < playerhand):
                                            sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                            sound_effect.play()
                                            scene = 99
                                else:
                                    if (card9suite == 0):
                                        DISPLAYSURF.blit(image238, (1380, 140))
                                    if (card9suite == 1):
                                        DISPLAYSURF.blit(image239, (1380, 140))
                                    if (card9suite == 2):
                                        DISPLAYSURF.blit(image240, (1380, 140))
                                    if (card9suite == 3):
                                        DISPLAYSURF.blit(image241, (1380, 140))
                                    draw_text(card9numm, font5, BLACK, DISPLAYSURF, 1383, 144)
                                    draw_text(card9numm, font5, BLACK, DISPLAYSURF, 1515, 305)
                                    if (CARDVALUE3 + CARDVALUE4 + CARDVALUE8 + CARDVALUE9 >= 17):
                                        dealerhand = CARDVALUE3 + CARDVALUE4 + CARDVALUE8 + CARDVALUE9
                                        playerhand = CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6
                                        if(dealerhand == 21):
                                            sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                            sound_effect.play()
                                            scene = 98
                                        if(dealerhand > 21):
                                            sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                            sound_effect.play()
                                            scene = 99
                                        if (dealerhand != 21 and dealerhand < 21):
                                            if (dealerhand >= playerhand):
                                                sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                                sound_effect.play()
                                                scene = 98
                                            if (dealerhand < playerhand):
                                                sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                                sound_effect.play()
                                                scene = 99
                                    else:
                                        if (card10suite == 0):
                                            DISPLAYSURF.blit(image238, (1380, 140))
                                        if (card10suite == 1):
                                            DISPLAYSURF.blit(image239, (1380, 140))
                                        if (card10suite == 2):
                                            DISPLAYSURF.blit(image240, (1380, 140))
                                        if (card10suite == 3):
                                            DISPLAYSURF.blit(image241, (1380, 140))
                                        draw_text(card10numm, font5, BLACK, DISPLAYSURF, 1383, 144)
                                        draw_text(card10numm, font5, BLACK, DISPLAYSURF, 1515, 305)
                                        if (CARDVALUE3 + CARDVALUE4 + CARDVALUE8 + CARDVALUE9 + CARDVALUE10 >= 17):
                                            dealerhand = CARDVALUE3 + CARDVALUE4 + CARDVALUE8 + CARDVALUE9 + CARDVALUE10
                                            playerhand = CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6
                                            if (dealerhand == 21):
                                                sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                                sound_effect.play()
                                                scene = 98
                                            if (dealerhand > 21):
                                                sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                                sound_effect.play()
                                                scene = 99
                                            if (dealerhand != 21 and dealerhand < 21):
                                                if (dealerhand >= playerhand):
                                                    sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                                    sound_effect.play()
                                                    scene = 98
                                                if (dealerhand < playerhand):
                                                    sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                                    sound_effect.play()
                                                    scene = 99
                                        else:
                                            if (card11suite == 0):
                                                DISPLAYSURF.blit(image238, (1380, 140))
                                            if (card11suite == 1):
                                                DISPLAYSURF.blit(image239, (1380, 140))
                                            if (card11suite == 2):
                                                DISPLAYSURF.blit(image240, (1380, 140))
                                            if (card11suite == 3):
                                                DISPLAYSURF.blit(image241, (1380, 140))
                                            draw_text(card11numm, font5, BLACK, DISPLAYSURF, 1383, 144)
                                            draw_text(card11numm, font5, BLACK, DISPLAYSURF, 1515, 305)
                                            if (CARDVALUE3 + CARDVALUE4 + CARDVALUE8 + CARDVALUE9 + CARDVALUE10 + CARDVALUE11 >= 17):
                                                dealerhand = CARDVALUE3 + CARDVALUE4 + CARDVALUE8 + CARDVALUE9 + CARDVALUE10 + CARDVALUE11
                                                playerhand = CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6
                                                if (dealerhand == 21):
                                                    sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                                    sound_effect.play()
                                                    scene = 98
                                                if (dealerhand > 21):
                                                    sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                                    sound_effect.play()
                                                    scene = 99
                                                if (dealerhand != 21 and dealerhand < 21):
                                                    if (dealerhand >= playerhand):
                                                        sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                                        sound_effect.play()
                                                        scene = 98
                                                    if (dealerhand < playerhand):
                                                        sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                                        sound_effect.play()
                                                        scene = 99
                                            else:
                                                if (dealerhand >= playerhand):
                                                    sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                                    sound_effect.play()
                                                    scene = 98
                                                if (dealerhand < playerhand):
                                                    sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                                    sound_effect.play()
                                                    scene = 99

                            elif(CARDVALUE3 + CARDVALUE4 == 21):
                                sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                sound_effect.play()
                                scene = 98
                            elif (CARDVALUE3 + CARDVALUE4 > 21):
                                sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                sound_effect.play()
                                scene = 99
                            else:
                                if (CARDVALUE3 + CARDVALUE4 < CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6):
                                    sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                    sound_effect.play()
                                    scene = 99
                                if (CARDVALUE3 + CARDVALUE4 >= CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6):
                                    sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                    sound_effect.play()
                                    scene = 98

                        if((CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6) > 21):
                            sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                            sound_effect.play()
                            scene = 100

                    hitbox = pygame.Rect(782, 900, 160, 35)
                    standbox = pygame.Rect(982, 900, 160, 35)
                    pygame.draw.rect(DISPLAYSURF, BLACK, hitbox)
                    pygame.draw.rect(DISPLAYSURF, BLACK, standbox)
                    pygame.draw.rect(DISPLAYSURF, RED, hitbox, 6)
                    pygame.draw.rect(DISPLAYSURF, SKYBLUE, standbox, 6)

                    draw_text('Hit', font5, WHITE, DISPLAYSURF, 845, 902)
                    draw_text('Stand ', font5, WHITE, DISPLAYSURF, 1032, 902)
                    if hitbox.collidepoint(mouse_pos):
                        draw_text('Hit', font5, RED, DISPLAYSURF, 845, 902)
                    if standbox.collidepoint(mouse_pos):
                        draw_text('Stand ', font5, BLUE, DISPLAYSURF, 1032, 902)

                    xrect = pygame.Rect(1680, 123, 35, 35)
                    returnarrowrect = pygame.Rect(153, 110, 120, 70)

                    if xrect.collidepoint(mouse_pos):
                        draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                    if returnarrowrect.collidepoint(mouse_pos):
                        DISPLAYSURF.blit(image165, (198, 110))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if returnarrowrect.collidepoint(mouse_pos):
                                standswitch = True
                                scene = -1
                            if xrect.collidepoint(mouse_pos):
                                print("Quit clicked")
                                pygame.mixer.music.stop()
                                pygame.quit()
                                sys.exit()
                            if (card6y >= 630):
                                if hitbox.collidepoint(mouse_pos):
                                    draw_text('Hit', font5, RED, DISPLAYSURF, 845, 902)
                                    card7y = -100
                                    card8y = -100
                                    timer = 125
                                    scene = scene + 1
                                if standbox.collidepoint(mouse_pos):
                                    draw_text('Stand ', font5, BLUE, DISPLAYSURF, 1032, 902)
                                    standswitch = True
                    pygame.display.update()
                if (scene == 4):
                    mouseX, mouseY = pygame.mouse.get_pos()
                    DISPLAYSURF.blit(image232, (190, 100))
                    image4.set_alpha(70)
                    DISPLAYSURF.blit(image4, (0, 0))
                    mouse_pos = pygame.mouse.get_pos()
                    draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                    DISPLAYSURF.blit(image164, (198, 110))
                    draw_text('gold - ', font5, WHITE, DISPLAYSURF, 375, 135)
                    draw_text(str(gold), font5, YELLOW, DISPLAYSURF, 445, 135)
                    draw_text('Current Bet - ' + str(moneychoosen), font3, YELLOW, DISPLAYSURF, 1240, 210)
                    # print("x and y = " + str(mouseX) + " " + str(mouseY))

                    if (card7y <= 630):
                        card7y = card7y + 10

                    if (card1suite == 0):
                        DISPLAYSURF.blit(image238, (780, card1y))
                    if (card1suite == 1):
                        DISPLAYSURF.blit(image239, (780, card1y))
                    if (card1suite == 2):
                        DISPLAYSURF.blit(image240, (780, card1y))
                    if (card1suite == 3):
                        DISPLAYSURF.blit(image241, (780, card1y))
                    if (card2suite == 0):
                        DISPLAYSURF.blit(image238, (980, card2y))
                    if (card2suite == 1):
                        DISPLAYSURF.blit(image239, (980, card2y))
                    if (card2suite == 2):
                        DISPLAYSURF.blit(image240, (980, card2y))
                    if (card2suite == 3):
                        DISPLAYSURF.blit(image241, (980, card2y))
                    if (card4suite == 0):
                        DISPLAYSURF.blit(image238, (980, card4y))
                    if (card4suite == 1):
                        DISPLAYSURF.blit(image239, (980, card4y))
                    if (card4suite == 2):
                        DISPLAYSURF.blit(image240, (980, card4y))
                    if (card4suite == 3):
                        DISPLAYSURF.blit(image241, (980, card4y))
                    '''if (card3suite == 0):
                        DISPLAYSURF.blit(image238, (780, card3y))
                    if (card3suite == 1):
                        DISPLAYSURF.blit(image239, (780, card3y))
                    if (card3suite == 2):
                        DISPLAYSURF.blit(image240, (780, card3y))
                    if (card3suite == 3):
                        DISPLAYSURF.blit(image241, (780, card3y))
                    if (card4suite == 0):
                        DISPLAYSURF.blit(image238, (980, card4y))
                    if (card4suite == 1):
                        DISPLAYSURF.blit(image239, (980, card4y))
                    if (card4suite == 2):
                        DISPLAYSURF.blit(image240, (980, card4y))
                    if (card4suite == 3):
                        DISPLAYSURF.blit(image241, (980, card4y))'''
                    if (card5suite == 0):
                        DISPLAYSURF.blit(image238, (1180, card5y))
                    if (card5suite == 1):
                        DISPLAYSURF.blit(image239, (1180, card5y))
                    if (card5suite == 2):
                        DISPLAYSURF.blit(image240, (1180, card5y))
                    if (card5suite == 3):
                        DISPLAYSURF.blit(image241, (1180, card5y))
                    if (card6suite == 0):
                        DISPLAYSURF.blit(image238, (1380, card6y))
                    if (card6suite == 1):
                        DISPLAYSURF.blit(image239, (1380, card6y))
                    if (card6suite == 2):
                        DISPLAYSURF.blit(image240, (1380, card6y))
                    if (card6suite == 3):
                        DISPLAYSURF.blit(image241, (1380, card6y))
                    draw_text(card1numm, font5, BLACK, DISPLAYSURF, 915, 812)
                    draw_text(card2numm, font5, BLACK, DISPLAYSURF, 1115, 812)
                    draw_text(card1numm, font5, BLACK, DISPLAYSURF, 783, 635)
                    draw_text(card2numm, font5, BLACK, DISPLAYSURF, 983, 635)
                    draw_text(card5numm, font5, BLACK, DISPLAYSURF, 1183, 635)
                    draw_text(card5numm, font5, BLACK, DISPLAYSURF, 1315, 812)
                    draw_text(card6numm, font5, BLACK, DISPLAYSURF, 1383, 635)
                    draw_text(card6numm, font5, BLACK, DISPLAYSURF, 1515, 812)
                    draw_text(card4numm, font5, BLACK, DISPLAYSURF, 990, 144)
                    draw_text(card4numm, font5, BLACK, DISPLAYSURF, 1122, 305)

                    DISPLAYSURF.blit(image242, (780, card3y))
                    if (timer != 0):
                        timer = timer - 1
                        DISPLAYSURF.blit(image242, (580, card7y))

                    if (timer == 0):
                        if (card7suite == 0):
                            DISPLAYSURF.blit(image238, (580, card7y))
                        if (card7suite == 1):
                            DISPLAYSURF.blit(image239, (580, card7y))
                        if (card7suite == 2):
                            DISPLAYSURF.blit(image240, (580, card7y))
                        if (card7suite == 3):
                            DISPLAYSURF.blit(image241, (580, card7y))

                        draw_text(card7numm, font5, BLACK, DISPLAYSURF, 583, 635)

                        #draw_text(card3numm, font5, BLACK, DISPLAYSURF, 783, 131)
                        #draw_text(card4numm, font5, BLACK, DISPLAYSURF, 983, 131)

                        draw_text(card6numm, font5, BLACK, DISPLAYSURF, 715, 812)

                        #draw_text(card3numm, font5, BLACK, DISPLAYSURF, 918, 315)
                        #draw_text(card4numm, font5, BLACK, DISPLAYSURF, 1118, 315)
                        if(standswitch):
                            if (card3suite == 0):
                                DISPLAYSURF.blit(image238, (780, card3y))
                            if (card3suite == 1):
                                DISPLAYSURF.blit(image239, (780, card3y))
                            if (card3suite == 2):
                                DISPLAYSURF.blit(image240, (780, card3y))
                            if (card3suite == 3):
                                DISPLAYSURF.blit(image241, (780, card3y))
                            draw_text(card3numm, font5, BLACK, DISPLAYSURF, 800, 144)
                            draw_text(card3numm, font5, BLACK, DISPLAYSURF, 910, 310)
                            if (CARDVALUE3 + CARDVALUE4 >= 17):
                                if(CARDVALUE3 + CARDVALUE4 == 21):
                                    sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                    sound_effect.play()
                                    scene = 98
                                elif (CARDVALUE3 + CARDVALUE4 > 21):
                                    sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                    sound_effect.play()
                                    scene = 99
                                elif(CARDVALUE1 + CARDVALUE2 >= 17):
                                    if (CARDVALUE3 + CARDVALUE4 < CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6 + CARDVALUE7):
                                        sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                        sound_effect.play()
                                        scene = 99
                                    if (CARDVALUE3 + CARDVALUE4 >= CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6 + CARDVALUE7):
                                        sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                        sound_effect.play()
                                        scene = 98
                            if (CARDVALUE3 + CARDVALUE4 < 17):
                                if (card8suite == 0):
                                    DISPLAYSURF.blit(image238, (1180, 140))
                                if (card8suite == 1):
                                    DISPLAYSURF.blit(image239, (1180, 140))
                                if (card8suite == 2):
                                    DISPLAYSURF.blit(image240, (1180, 140))
                                if (card8suite == 3):
                                    DISPLAYSURF.blit(image241, (1180, 140))
                                draw_text(card8numm, font5, BLACK, DISPLAYSURF, 1183, 144)
                                draw_text(card8numm, font5, BLACK, DISPLAYSURF, 1315, 305)
                                if (CARDVALUE3 + CARDVALUE4 + CARDVALUE8 >= 17):
                                    dealerhand = CARDVALUE3 + CARDVALUE4 + CARDVALUE8
                                    playerhand = CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6 + CARDVALUE7
                                    if (dealerhand == 21):
                                        sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                        sound_effect.play()
                                        scene = 98
                                    if (dealerhand > 21):
                                        sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                        sound_effect.play()
                                        scene = 99
                                    if(dealerhand != 21 and dealerhand < 21):
                                        if(dealerhand >= playerhand):
                                            sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                            sound_effect.play()
                                            scene = 98
                                        if(dealerhand < playerhand):
                                            sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                            sound_effect.play()
                                            scene = 99
                                else:
                                    if (card9suite == 0):
                                        DISPLAYSURF.blit(image238, (1380, 140))
                                    if (card9suite == 1):
                                        DISPLAYSURF.blit(image239, (1380, 140))
                                    if (card9suite == 2):
                                        DISPLAYSURF.blit(image240, (1380, 140))
                                    if (card9suite == 3):
                                        DISPLAYSURF.blit(image241, (1380, 140))
                                    draw_text(card9numm, font5, BLACK, DISPLAYSURF, 1383, 144)
                                    draw_text(card9numm, font5, BLACK, DISPLAYSURF, 1515, 305)
                                    if (CARDVALUE3 + CARDVALUE4 + CARDVALUE8 + CARDVALUE9 >= 17):
                                        dealerhand = CARDVALUE3 + CARDVALUE4 + CARDVALUE8 + CARDVALUE9
                                        playerhand = CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6 + CARDVALUE7
                                        if(dealerhand == 21):
                                            sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                            sound_effect.play()
                                            scene = 98
                                        if(dealerhand > 21):
                                            sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                            sound_effect.play()
                                            scene = 99
                                        if (dealerhand != 21 and dealerhand < 21):
                                            if (dealerhand >= playerhand):
                                                sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                                sound_effect.play()
                                                scene = 98
                                            if (dealerhand < playerhand):
                                                sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                                sound_effect.play()
                                                scene = 99
                                    else:
                                        if (card10suite == 0):
                                            DISPLAYSURF.blit(image238, (1380, 140))
                                        if (card10suite == 1):
                                            DISPLAYSURF.blit(image239, (1380, 140))
                                        if (card10suite == 2):
                                            DISPLAYSURF.blit(image240, (1380, 140))
                                        if (card10suite == 3):
                                            DISPLAYSURF.blit(image241, (1380, 140))
                                        draw_text(card10numm, font5, BLACK, DISPLAYSURF, 1383, 144)
                                        draw_text(card10numm, font5, BLACK, DISPLAYSURF, 1515, 305)
                                        if (CARDVALUE3 + CARDVALUE4 + CARDVALUE8 + CARDVALUE9 + CARDVALUE10 >= 17):
                                            dealerhand = CARDVALUE3 + CARDVALUE4 + CARDVALUE8 + CARDVALUE9 + CARDVALUE10
                                            playerhand = CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6 + CARDVALUE7
                                            if (dealerhand == 21):
                                                sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                                sound_effect.play()
                                                scene = 98
                                            if (dealerhand > 21):
                                                sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                                sound_effect.play()
                                                scene = 99
                                            if (dealerhand != 21 and dealerhand < 21):
                                                if (dealerhand >= playerhand):
                                                    sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                                    sound_effect.play()
                                                    scene = 98
                                                if (dealerhand < playerhand):
                                                    sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                                    sound_effect.play()
                                                    scene = 99
                                        else:
                                            if (card11suite == 0):
                                                DISPLAYSURF.blit(image238, (1380, 140))
                                            if (card11suite == 1):
                                                DISPLAYSURF.blit(image239, (1380, 140))
                                            if (card11suite == 2):
                                                DISPLAYSURF.blit(image240, (1380, 140))
                                            if (card11suite == 3):
                                                DISPLAYSURF.blit(image241, (1380, 140))
                                            draw_text(card11numm, font5, BLACK, DISPLAYSURF, 1383, 144)
                                            draw_text(card11numm, font5, BLACK, DISPLAYSURF, 1515, 305)
                                            if (CARDVALUE3 + CARDVALUE4 + CARDVALUE8 + CARDVALUE9 + CARDVALUE10 + CARDVALUE11 >= 17):
                                                dealerhand = CARDVALUE3 + CARDVALUE4 + CARDVALUE8 + CARDVALUE9 + CARDVALUE10 + CARDVALUE11
                                                playerhand = CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6 + CARDVALUE7
                                                if (dealerhand == 21):
                                                    sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                                    sound_effect.play()
                                                    scene = 98
                                                if (dealerhand > 21):
                                                    sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                                    sound_effect.play()
                                                    scene = 99
                                                if (dealerhand != 21 and dealerhand < 21):
                                                    if (dealerhand >= playerhand):
                                                        sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                                        sound_effect.play()
                                                        scene = 98
                                                    if (dealerhand < playerhand):
                                                        sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                                        sound_effect.play()
                                                        scene = 99
                                            else:
                                                if (dealerhand >= playerhand):
                                                    sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                                    sound_effect.play()
                                                    scene = 98
                                                if (dealerhand < playerhand):
                                                    sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                                    sound_effect.play()
                                                    scene = 99

                            elif(CARDVALUE3 + CARDVALUE4 == 21):
                                sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                sound_effect.play()
                                scene = 98
                            elif (CARDVALUE3 + CARDVALUE4 > 21):
                                sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                sound_effect.play()
                                scene = 99
                            else:
                                if (CARDVALUE3 + CARDVALUE4 < CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6 + CARDVALUE7):
                                    sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                    sound_effect.play()
                                    scene = 99
                                if (CARDVALUE3 + CARDVALUE4 >= CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6 + CARDVALUE7):
                                    sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                    sound_effect.play()
                                    scene = 98

                        if((CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6 + CARDVALUE7) > 21):
                            sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                            sound_effect.play()
                            scene = 100

                    hitbox = pygame.Rect(782, 900, 160, 35)
                    standbox = pygame.Rect(982, 900, 160, 35)
                    pygame.draw.rect(DISPLAYSURF, BLACK, hitbox)
                    pygame.draw.rect(DISPLAYSURF, BLACK, standbox)
                    pygame.draw.rect(DISPLAYSURF, RED, hitbox, 6)
                    pygame.draw.rect(DISPLAYSURF, SKYBLUE, standbox, 6)

                    draw_text('Reveal ', font5, WHITE, DISPLAYSURF, 1032, 902)
                    if standbox.collidepoint(mouse_pos):
                        draw_text('Reveal ', font5, BLUE, DISPLAYSURF, 1032, 902)

                    xrect = pygame.Rect(1680, 123, 35, 35)
                    returnarrowrect = pygame.Rect(153, 110, 120, 70)

                    draw_text('Hit', font5, WHITE, DISPLAYSURF, 845, 902)
                    draw_text('Stand ', font5, WHITE, DISPLAYSURF, 1032, 902)
                    if hitbox.collidepoint(mouse_pos):
                        draw_text('Hit', font5, RED, DISPLAYSURF, 845, 902)
                    if standbox.collidepoint(mouse_pos):
                        draw_text('Stand ', font5, BLUE, DISPLAYSURF, 1032, 902)

                    xrect = pygame.Rect(1680, 123, 35, 35)
                    returnarrowrect = pygame.Rect(153, 110, 120, 70)

                    if xrect.collidepoint(mouse_pos):
                        draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                    if returnarrowrect.collidepoint(mouse_pos):
                        DISPLAYSURF.blit(image165, (198, 110))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if returnarrowrect.collidepoint(mouse_pos):
                                standswitch = True
                                scene = -1
                            if xrect.collidepoint(mouse_pos):
                                print("Quit clicked")
                                pygame.mixer.music.stop()
                                pygame.quit()
                                sys.exit()
                            if (card7y >= 630):
                                if hitbox.collidepoint(mouse_pos):
                                    draw_text('Hit', font5, RED, DISPLAYSURF, 845, 902)
                                    card8y = -100
                                    timer = 125
                                    scene = scene + 1
                                if standbox.collidepoint(mouse_pos):
                                    draw_text('Stand ', font5, BLUE, DISPLAYSURF, 1032, 902)
                                    standswitch = True
                    pygame.display.update()
                if (scene == 5):
                    mouseX, mouseY = pygame.mouse.get_pos()
                    DISPLAYSURF.blit(image232, (190, 100))
                    image4.set_alpha(70)
                    DISPLAYSURF.blit(image4, (0, 0))
                    mouse_pos = pygame.mouse.get_pos()
                    draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                    DISPLAYSURF.blit(image164, (198, 110))
                    draw_text('gold - ', font5, WHITE, DISPLAYSURF, 375, 135)
                    draw_text(str(gold), font5, YELLOW, DISPLAYSURF, 445, 135)
                    draw_text('Current Bet - ' + str(moneychoosen), font3, YELLOW, DISPLAYSURF, 1240, 210)
                    # print("x and y = " + str(mouseX) + " " + str(mouseY))

                    if (card8y <= 630):
                        card8y = card8y + 10

                    if (card1suite == 0):
                        DISPLAYSURF.blit(image238, (780, card1y))
                    if (card1suite == 1):
                        DISPLAYSURF.blit(image239, (780, card1y))
                    if (card1suite == 2):
                        DISPLAYSURF.blit(image240, (780, card1y))
                    if (card1suite == 3):
                        DISPLAYSURF.blit(image241, (780, card1y))
                    if (card2suite == 0):
                        DISPLAYSURF.blit(image238, (980, card2y))
                    if (card2suite == 1):
                        DISPLAYSURF.blit(image239, (980, card2y))
                    if (card2suite == 2):
                        DISPLAYSURF.blit(image240, (980, card2y))
                    if (card2suite == 3):
                        DISPLAYSURF.blit(image241, (980, card2y))
                    if (card4suite == 0):
                        DISPLAYSURF.blit(image238, (980, card4y))
                    if (card4suite == 1):
                        DISPLAYSURF.blit(image239, (980, card4y))
                    if (card4suite == 2):
                        DISPLAYSURF.blit(image240, (980, card4y))
                    if (card4suite == 3):
                        DISPLAYSURF.blit(image241, (980, card4y))
                    '''if (card3suite == 0):
                        DISPLAYSURF.blit(image238, (780, card3y))
                    if (card3suite == 1):
                        DISPLAYSURF.blit(image239, (780, card3y))
                    if (card3suite == 2):
                        DISPLAYSURF.blit(image240, (780, card3y))
                    if (card3suite == 3):
                        DISPLAYSURF.blit(image241, (780, card3y))
                    if (card4suite == 0):
                        DISPLAYSURF.blit(image238, (980, card4y))
                    if (card4suite == 1):
                        DISPLAYSURF.blit(image239, (980, card4y))
                    if (card4suite == 2):
                        DISPLAYSURF.blit(image240, (980, card4y))
                    if (card4suite == 3):
                        DISPLAYSURF.blit(image241, (980, card4y))'''
                    if (card5suite == 0):
                        DISPLAYSURF.blit(image238, (1180, card5y))
                    if (card5suite == 1):
                        DISPLAYSURF.blit(image239, (1180, card5y))
                    if (card5suite == 2):
                        DISPLAYSURF.blit(image240, (1180, card5y))
                    if (card5suite == 3):
                        DISPLAYSURF.blit(image241, (1180, card5y))
                    if (card6suite == 0):
                        DISPLAYSURF.blit(image238, (1380, card6y))
                    if (card6suite == 1):
                        DISPLAYSURF.blit(image239, (1380, card6y))
                    if (card6suite == 2):
                        DISPLAYSURF.blit(image240, (1380, card6y))
                    if (card6suite == 3):
                        DISPLAYSURF.blit(image241, (1380, card6y))
                    if (card7suite == 0):
                        DISPLAYSURF.blit(image238, (580, card7y))
                    if (card7suite == 1):
                        DISPLAYSURF.blit(image239, (580, card7y))
                    if (card7suite == 2):
                        DISPLAYSURF.blit(image240, (580, card7y))
                    if (card7suite == 3):
                        DISPLAYSURF.blit(image241, (580, card7y))
                    draw_text(card1numm, font5, BLACK, DISPLAYSURF, 915, 812)
                    draw_text(card2numm, font5, BLACK, DISPLAYSURF, 1115, 812)
                    draw_text(card1numm, font5, BLACK, DISPLAYSURF, 783, 635)
                    draw_text(card2numm, font5, BLACK, DISPLAYSURF, 983, 635)
                    draw_text(card5numm, font5, BLACK, DISPLAYSURF, 1183, 635)
                    draw_text(card5numm, font5, BLACK, DISPLAYSURF, 1315, 812)
                    draw_text(card6numm, font5, BLACK, DISPLAYSURF, 1383, 635)
                    draw_text(card6numm, font5, BLACK, DISPLAYSURF, 1515, 812)
                    draw_text(card7numm, font5, BLACK, DISPLAYSURF, 583, 635)
                    draw_text(card7numm, font5, BLACK, DISPLAYSURF, 715, 812)
                    draw_text(card4numm, font5, BLACK, DISPLAYSURF, 990, 144)
                    draw_text(card4numm, font5, BLACK, DISPLAYSURF, 1122, 305)

                    DISPLAYSURF.blit(image242, (780, card3y))
                    if (timer != 0):
                        timer = timer - 1
                        DISPLAYSURF.blit(image242, (380, card8y))

                    if (timer == 0):
                        if (card8suite == 0):
                            DISPLAYSURF.blit(image238, (380, card8y))
                        if (card8suite == 1):
                            DISPLAYSURF.blit(image239, (380, card8y))
                        if (card8suite == 2):
                            DISPLAYSURF.blit(image240, (380, card8y))
                        if (card8suite == 3):
                            DISPLAYSURF.blit(image241, (380, card8y))

                        draw_text(card8numm, font5, BLACK, DISPLAYSURF, 383, 635)

                        #draw_text(card3numm, font5, BLACK, DISPLAYSURF, 783, 131)
                        #draw_text(card4numm, font5, BLACK, DISPLAYSURF, 983, 131)

                        draw_text(card8numm, font5, BLACK, DISPLAYSURF, 515, 812)

                        #draw_text(card3numm, font5, BLACK, DISPLAYSURF, 918, 315)
                        #draw_text(card4numm, font5, BLACK, DISPLAYSURF, 1118, 315)

                        if(standswitch):
                            if (card3suite == 0):
                                DISPLAYSURF.blit(image238, (780, card3y))
                            if (card3suite == 1):
                                DISPLAYSURF.blit(image239, (780, card3y))
                            if (card3suite == 2):
                                DISPLAYSURF.blit(image240, (780, card3y))
                            if (card3suite == 3):
                                DISPLAYSURF.blit(image241, (780, card3y))
                            draw_text(card3numm, font5, BLACK, DISPLAYSURF, 800, 144)
                            draw_text(card3numm, font5, BLACK, DISPLAYSURF, 910, 310)
                            if (CARDVALUE3 + CARDVALUE4 >= 17):
                                if(CARDVALUE3 + CARDVALUE4 == 21):
                                    sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                    sound_effect.play()
                                    scene = 98
                                elif (CARDVALUE3 + CARDVALUE4 > 21):
                                    sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                    sound_effect.play()
                                    scene = 99
                                elif(CARDVALUE1 + CARDVALUE2 >= 17):
                                    if (CARDVALUE3 + CARDVALUE4 < CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6 + CARDVALUE7 + CARDVALUE8):
                                        sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                        sound_effect.play()
                                        scene = 99
                                    if (CARDVALUE3 + CARDVALUE4 >= CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6 + CARDVALUE7 + CARDVALUE8):
                                        sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                        sound_effect.play()
                                        scene = 98
                            if (CARDVALUE3 + CARDVALUE4 < 17):
                                if (card8suite == 0):
                                    DISPLAYSURF.blit(image238, (1180, 140))
                                if (card8suite == 1):
                                    DISPLAYSURF.blit(image239, (1180, 140))
                                if (card8suite == 2):
                                    DISPLAYSURF.blit(image240, (1180, 140))
                                if (card8suite == 3):
                                    DISPLAYSURF.blit(image241, (1180, 140))
                                draw_text(card8numm, font5, BLACK, DISPLAYSURF, 1183, 144)
                                draw_text(card8numm, font5, BLACK, DISPLAYSURF, 1315, 305)
                                if (CARDVALUE3 + CARDVALUE4 + CARDVALUE8 >= 17):
                                    dealerhand = CARDVALUE3 + CARDVALUE4 + CARDVALUE8
                                    playerhand = CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6 + CARDVALUE7 + CARDVALUE8
                                    if (dealerhand == 21):
                                        sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                        sound_effect.play()
                                        scene = 98
                                    if (dealerhand > 21):
                                        sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                        sound_effect.play()
                                        scene = 99
                                    if(dealerhand != 21 and dealerhand < 21):
                                        if(dealerhand >= playerhand):
                                            sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                            sound_effect.play()
                                            scene = 98
                                        if(dealerhand < playerhand):
                                            sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                            sound_effect.play()
                                            scene = 99
                                else:
                                    if (card9suite == 0):
                                        DISPLAYSURF.blit(image238, (1380, 140))
                                    if (card9suite == 1):
                                        DISPLAYSURF.blit(image239, (1380, 140))
                                    if (card9suite == 2):
                                        DISPLAYSURF.blit(image240, (1380, 140))
                                    if (card9suite == 3):
                                        DISPLAYSURF.blit(image241, (1380, 140))
                                    draw_text(card9numm, font5, BLACK, DISPLAYSURF, 1383, 144)
                                    draw_text(card9numm, font5, BLACK, DISPLAYSURF, 1515, 305)
                                    if (CARDVALUE3 + CARDVALUE4 + CARDVALUE8 + CARDVALUE9 >= 17):
                                        dealerhand = CARDVALUE3 + CARDVALUE4 + CARDVALUE8 + CARDVALUE9
                                        playerhand = CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6 + CARDVALUE7 + CARDVALUE8
                                        if(dealerhand == 21):
                                            sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                            sound_effect.play()
                                            scene = 98
                                        if(dealerhand > 21):
                                            sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                            sound_effect.play()
                                            scene = 99
                                        if (dealerhand != 21 and dealerhand < 21):
                                            if (dealerhand >= playerhand):
                                                sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                                sound_effect.play()
                                                scene = 98
                                            if (dealerhand < playerhand):
                                                sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                                sound_effect.play()
                                                scene = 99
                                    else:
                                        if (card10suite == 0):
                                            DISPLAYSURF.blit(image238, (1380, 140))
                                        if (card10suite == 1):
                                            DISPLAYSURF.blit(image239, (1380, 140))
                                        if (card10suite == 2):
                                            DISPLAYSURF.blit(image240, (1380, 140))
                                        if (card10suite == 3):
                                            DISPLAYSURF.blit(image241, (1380, 140))
                                        draw_text(card10numm, font5, BLACK, DISPLAYSURF, 1383, 144)
                                        draw_text(card10numm, font5, BLACK, DISPLAYSURF, 1515, 305)
                                        if (CARDVALUE3 + CARDVALUE4 + CARDVALUE8 + CARDVALUE9 + CARDVALUE10 >= 17):
                                            dealerhand = CARDVALUE3 + CARDVALUE4 + CARDVALUE8 + CARDVALUE9 + CARDVALUE10
                                            playerhand = CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6 + CARDVALUE7 + CARDVALUE8
                                            if (dealerhand == 21):
                                                sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                                sound_effect.play()
                                                scene = 98
                                            if (dealerhand > 21):
                                                sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                                sound_effect.play()
                                                scene = 99
                                            if (dealerhand != 21 and dealerhand < 21):
                                                if (dealerhand >= playerhand):
                                                    sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                                    sound_effect.play()
                                                    scene = 98
                                                if (dealerhand < playerhand):
                                                    sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                                    sound_effect.play()
                                                    scene = 99
                                            if(dealerhand < 17):
                                                if (card11suite == 0):
                                                    DISPLAYSURF.blit(image238, (1380, 140))
                                                if (card11suite == 1):
                                                    DISPLAYSURF.blit(image239, (1380, 140))
                                                if (card11suite == 2):
                                                    DISPLAYSURF.blit(image240, (1380, 140))
                                                if (card11suite == 3):
                                                    DISPLAYSURF.blit(image241, (1380, 140))
                                                draw_text(card11numm, font5, BLACK, DISPLAYSURF, 1383, 144)
                                                draw_text(card11numm, font5, BLACK, DISPLAYSURF, 1515, 305)
                                                if (CARDVALUE3 + CARDVALUE4 + CARDVALUE8 + CARDVALUE9 + CARDVALUE10 + CARDVALUE11 >= 17):
                                                    dealerhand = CARDVALUE3 + CARDVALUE4 + CARDVALUE8 + CARDVALUE9 + CARDVALUE10 + CARDVALUE11
                                                    playerhand = CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6 + CARDVALUE7 + CARDVALUE8
                                                    if (dealerhand == 21):
                                                        sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                                        sound_effect.play()
                                                        scene = 98
                                                    if (dealerhand > 21):
                                                        sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                                        sound_effect.play()
                                                        scene = 99
                                                    if (dealerhand != 21 and dealerhand < 21):
                                                        if (dealerhand >= playerhand):
                                                            sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                                            sound_effect.play()
                                                            scene = 98
                                                        if (dealerhand < playerhand):
                                                            sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                                            sound_effect.play()
                                                            scene = 99
                                                else:
                                                    if (dealerhand >= playerhand):
                                                        sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                                        sound_effect.play()
                                                        scene = 98
                                                    if (dealerhand < playerhand):
                                                        sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                                        sound_effect.play()
                                                        scene = 99

                            elif(CARDVALUE3 + CARDVALUE4 == 21):
                                sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                sound_effect.play()
                                scene = 98
                            elif (CARDVALUE3 + CARDVALUE4 > 21):
                                sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                sound_effect.play()
                                scene = 99
                            else:
                                if (CARDVALUE3 + CARDVALUE4 < CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6 + CARDVALUE7 + CARDVALUE8):
                                    sound_effect = pygame.mixer.Sound(resource_path("audio/blackjackwin.mp3"))
                                    sound_effect.play()
                                    scene = 99
                                if (CARDVALUE3 + CARDVALUE4 >= CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6 + CARDVALUE7 + CARDVALUE8):
                                    sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                                    sound_effect.play()
                                    scene = 98

                        if((CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6 + CARDVALUE7 + CARDVALUE8) > 21):
                            sound_effect = pygame.mixer.Sound(resource_path("audio/coinsound.mp3"))
                            sound_effect.play()
                            scene = 100

                    standbox = pygame.Rect(880, 900, 160, 35)
                    pygame.draw.rect(DISPLAYSURF, BLACK, standbox)
                    pygame.draw.rect(DISPLAYSURF, SKYBLUE, standbox, 6)

                    draw_text('Reveal ', font5, WHITE, DISPLAYSURF, 930, 902)
                    if standbox.collidepoint(mouse_pos):
                        draw_text('Reveal ', font5, GREEN, DISPLAYSURF, 930, 902)

                    xrect = pygame.Rect(1680, 123, 35, 35)
                    returnarrowrect = pygame.Rect(153, 110, 120, 70)

                    if xrect.collidepoint(mouse_pos):
                        draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                    if returnarrowrect.collidepoint(mouse_pos):
                        DISPLAYSURF.blit(image165, (198, 110))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if returnarrowrect.collidepoint(mouse_pos):
                                standswitch = False
                                scene = -1

                            if xrect.collidepoint(mouse_pos):
                                print("Quit clicked")
                                pygame.mixer.music.stop()
                                pygame.quit()
                                sys.exit()
                            if (card8y >= 630):
                                if standbox.collidepoint(mouse_pos):
                                    draw_text('Stand ', font5, BLUE, DISPLAYSURF, 1032, 902)
                                    standswitch = True
                    pygame.display.update()
                if (scene == 100):
                    mouseX, mouseY = pygame.mouse.get_pos()
                    mouse_pos = pygame.mouse.get_pos()
                    draw_text('BUSTED', font2, RED, DISPLAYSURF, 830, 425)
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if 0 <= mouseX <= 1920 and 150 <= mouseY <= 1080:
                                with open(resource_path("gamedata.txt"), "r") as file:
                                    lines = file.readlines()
                                    gold = gold - moneychoosen
                                    lines[0] = f"gold = {gold}\n"
                                with open(resource_path("gamedata.txt"), "w") as file:
                                    file.writelines(lines)
                                standswitch = False
                                scene = 0
                    pygame.display.update()
                if (scene == 98):
                    mouseX, mouseY = pygame.mouse.get_pos()
                    mouse_pos = pygame.mouse.get_pos()
                    draw_text('DEALER WINS', font2, RED, DISPLAYSURF, 760, 425)
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if 0 <= mouseX <= 1920 and 150 <= mouseY <= 1080:
                                with open(resource_path("gamedata.txt"), "r") as file:
                                    lines = file.readlines()
                                    gold = gold - moneychoosen
                                    lines[0] = f"gold = {gold}\n"
                                with open(resource_path("gamedata.txt"), "w") as file:
                                    file.writelines(lines)
                                standswitch = False
                                scene = 0
                    pygame.display.update()
                if (scene == 99):
                    mouseX, mouseY = pygame.mouse.get_pos()
                    mouse_pos = pygame.mouse.get_pos()
                    draw_text('YOU WIN!', font2, GREEN, DISPLAYSURF, 820, 425)
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if 0 <= mouseX <= 1920 and 150 <= mouseY <= 1080:
                                with open(resource_path("gamedata.txt"), "r") as file:
                                    lines = file.readlines()
                                    gold = gold + moneychoosen
                                    lines[0] = f"gold = {gold}\n"
                                with open(resource_path("gamedata.txt"), "w") as file:
                                    file.writelines(lines)
                                standswitch = False
                                scene = 0
                    pygame.display.update()
########################################################################################################################
class guild(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.guildbool1 = True
        self.guildbool2 = True
        self.guildroom()
########################################################################################################################
    def guildroom(self):
        global FaderBool
        global Fader
        global textFader
        video = cv2.VideoCapture(resource_path("video/glowparticlevideo.mp4"))

        startTime = pygame.time.get_ticks()
        self.gamescene = 1
        x = 390
        y = 600
        alchemylevelupbool = False
        boolleftorright = True
        mouse_pos = pygame.mouse.get_pos()
        pygame.mixer.music.load(resource_path("audio/bardmusic.mp3"))
        pygame.mixer.music.queue(resource_path("audio/bardmusic2.mp3"))
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        print("Guild initialized")
        global textFader
        global characterName
        global alchemyexp
        global alchemylevel
        global gold
        global gem
        global guildtutorial
        staropacity = 1
        starbool = True
        imagechoosen = image215
        potionimage = 1
        streak = 0
        with open(resource_path("gamedata.txt"), "r") as file:
            lines = file.readlines()
            guildtutorial = lines[14].strip()
            guildtutorial = guildtutorial[16:]
        if (guildtutorial == 'true'):
            self.gamescene = 1
        elif (guildtutorial == 'false'):
            self.gamescene = 11
        while self.guildbool1:
            with open(resource_path("gamedata.txt"), "r") as file:
                lines = file.readlines()
                goldline = lines[0].strip()
                goldline = goldline[7:]
                gemline = lines[1].strip()
                gemline = gemline[6:]
                gold = int(goldline)
                gem = int(gemline)
                alchemyexp = lines[12].strip()
                alchemyexp = alchemyexp[13:]
                alchemylevel = lines[13].strip()
                alchemylevel = alchemylevel[15:]
                alchemyexp = int(alchemyexp)
                alchemylevel = int(alchemylevel)
                guildtutorial = lines[14].strip()
                guildtutorial = guildtutorial[16:]

            if(staropacity >= 255):
                starbool = False
            if(staropacity <= 0):
                starbool = True
            if(starbool):
                staropacity = staropacity + 1
            if(starbool == False):
                staropacity = staropacity - 1

            startTime = pygame.time.get_ticks()
            mouseX, mouseY = pygame.mouse.get_pos()


            if (self.gamescene == 1):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image207, (197, 100))
                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))
                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 120, 70)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 0 <= mouseX <= 1920 and 250 <= mouseY <= 1080:
                            sound_effect = pygame.mixer.Sound(resource_path("audio/clicknoise.mp3"))
                            sound_effect.play()
                            self.gamescene = self.gamescene + 1
                        if returnarrowrect.collidepoint(mouse_pos):
                            transition(6)
                            self.guildbool1 = False
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()

            if (self.gamescene == 2):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image207, (197, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 870))
                draw_text_center('Well well well, if it isnt the new rookie in town.', font5, GREY, DISPLAYSURF, halfdisplay, 880)
                draw_text_center('Ive been waiting for you to show up. Its tough', font5, GREY, DISPLAYSURF, halfdisplay, 910)
                draw_text_center('for us humanoids to survive down here.', font5, GREY, DISPLAYSURF, halfdisplay, 940)
                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))
                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 120, 70)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if returnarrowrect.collidepoint(mouse_pos):
                            transition(6)
                            self.guildbool1 = False
                        if 0 <= mouseX <= 1920 and 250 <= mouseY <= 1080:
                            sound_effect = pygame.mixer.Sound(resource_path("audio/clicknoise.mp3"))
                            sound_effect.play()
                            self.gamescene = self.gamescene + 1
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()

            if (self.gamescene == 3):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image207, (197, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 870))
                draw_text_center('What was your name again...', font5, GREY, DISPLAYSURF, halfdisplay, 880)
                draw_text_center('Johnathon.. Bartholomule.. Ahmad...', font5, GREY, DISPLAYSURF, halfdisplay, 910)
                draw_text_center('Oh thats right, its ' +characterName , font5, GREY, DISPLAYSURF, halfdisplay, 940)
                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))
                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 120, 70)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 0 <= mouseX <= 1920 and 250 <= mouseY <= 1080:
                            sound_effect = pygame.mixer.Sound(resource_path("audio/clicknoise.mp3"))
                            sound_effect.play()
                            self.gamescene = self.gamescene + 1
                        if returnarrowrect.collidepoint(mouse_pos):
                            transition(6)
                            self.guildbool1 = False
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()

            if (self.gamescene == 4):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image207, (197, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 870))
                draw_text_center('Its a pleasure to meet you my name is Coal. ', font5, GREY, DISPLAYSURF, halfdisplay, 880)
                draw_text_center('Im the one and only Leader of the Adventurers Guild,', font5, GREY, DISPLAYSURF, halfdisplay, 910)
                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))
                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 120, 70)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 0 <= mouseX <= 1920 and 250 <= mouseY <= 1080:
                            sound_effect = pygame.mixer.Sound(resource_path("audio/clicknoise.mp3"))
                            sound_effect.play()
                            self.gamescene = self.gamescene + 1
                        if returnarrowrect.collidepoint(mouse_pos):
                            transition(6)
                            self.guildbool1 = False

                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()

            if (self.gamescene == 5):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image207, (197, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 870))
                draw_text_center('We adventurers need a place to stick together and the guild provides just that.', font5, GREY, DISPLAYSURF, halfdisplay, 880)
                draw_text_center('You can accept quests here and you can also work on a profession.', font5, GREY, DISPLAYSURF, halfdisplay, 910)
                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))
                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 120, 70)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 0 <= mouseX <= 1920 and 250 <= mouseY <= 1080:
                            sound_effect = pygame.mixer.Sound(resource_path("audio/clicknoise.mp3"))
                            sound_effect.play()
                            self.gamescene = self.gamescene + 1
                        if returnarrowrect.collidepoint(mouse_pos):
                            transition(6)
                            self.guildbool1 = False

                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()

            if (self.gamescene == 6):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image207, (197, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 870))
                draw_text_center('If you are lucky you might even find a beatiful lady ', font5, GREY, DISPLAYSURF, halfdisplay, 880)
                draw_text_center('to accompany you as well HahUhahahaAhaAaaaa', font5, GREY, DISPLAYSURF, halfdisplay, 910)
                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))
                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 120, 70)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 0 <= mouseX <= 1920 and 250 <= mouseY <= 1080:
                            sound_effect = pygame.mixer.Sound(resource_path("audio/clicknoise.mp3"))
                            sound_effect.play()
                            self.gamescene = self.gamescene + 1
                        if returnarrowrect.collidepoint(mouse_pos):
                            transition(6)
                            self.guildbool1 = False

                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()

            if (self.gamescene == 7):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image207, (197, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 870))
                draw_text_center('Whatever you need, the adventurers guild can provide it.We work as one cohesive family', font5, GREY, DISPLAYSURF, halfdisplay, 880)
                draw_text_center('always watching each others backs, never leaving a guild member behind.', font5, GREY, DISPLAYSURF, halfdisplay, 910)
                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))
                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 120, 70)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 0 <= mouseX <= 1920 and 250 <= mouseY <= 1080:
                            sound_effect = pygame.mixer.Sound(resource_path("audio/clicknoise.mp3"))
                            sound_effect.play()
                            self.gamescene = self.gamescene + 1
                        if returnarrowrect.collidepoint(mouse_pos):
                            transition(6)
                            self.guildbool1 = False

                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()

            if (self.gamescene == 8):
                rainbowcolor1 = int((math.sin(startTime * 0.002) + 1) * 127.5)
                rainbowcolor2 = int((math.sin(startTime * 0.003 + 2) + 1) * 127.5)
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image207, (197, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 870))
                draw_text_center('Say, ' +characterName, font5, GREY, DISPLAYSURF, halfdisplay, 880)
                draw_text_center('would you like to join?', font5, GREY, DISPLAYSURF, halfdisplay, 910)
                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))
                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 120, 70)
                norect = pygame.Rect(980, 157, 300, 300)
                yesrect = pygame.Rect(660, 157, 300, 300)
                pygame.draw.rect(DISPLAYSURF, GREEN, yesrect)
                pygame.draw.rect(DISPLAYSURF, RED, norect)
                draw_text('No', font2, BLACK, DISPLAYSURF, 1070, 227)
                draw_text('Yes', font2, BLACK, DISPLAYSURF, 750, 227)
                if yesrect.collidepoint(mouse_pos):
                    pygame.draw.rect(DISPLAYSURF,(rainbowcolor1,130,130), yesrect, 11)
                if norect.collidepoint(mouse_pos):
                    pygame.draw.rect(DISPLAYSURF,(rainbowcolor1,130,130), norect, 11)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if yesrect.collidepoint(mouse_pos):
                            sound_effect = pygame.mixer.Sound(resource_path("audio/clicknoise.mp3"))
                            sound_effect.play()

                            with open(resource_path("gamedata.txt"), "r") as file:
                                lines = file.readlines()
                                lines[14] = f"guildtutorial = false\n"
                            with open(resource_path("gamedata.txt"), "w") as file:
                                file.writelines(lines)  # Write the modified lines back to the file



                            self.gamescene = self.gamescene + 1
                            print("guild join initiated")
                        if norect.collidepoint(mouse_pos):
                            sound_effect = pygame.mixer.Sound(resource_path("audio/clicknoise.mp3"))
                            sound_effect.play()
                            transition(6)
                            self.guildbool1 = False
                            print("guild join rejected")

                        if returnarrowrect.collidepoint(mouse_pos):
                            transition(6)
                            self.guildbool1 = False
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()

            if (self.gamescene == 9):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image207, (197, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 870))
                draw_text_center('HAHAHHAHAHAAHAHAA, THATS WONDERFUL. WELCOME LITTLE BROTHER TO THE GUILD,', font5, GREY, DISPLAYSURF, halfdisplay, 880)
                draw_text_center('COME COME LET ME SHOW YOU WHAT WE HAVE TO OFFER!', font5, GREY, DISPLAYSURF, halfdisplay, 910)
                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))
                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 120, 70)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 0 <= mouseX <= 1920 and 250 <= mouseY <= 1080:
                            sound_effect = pygame.mixer.Sound(resource_path("audio/clicknoise.mp3"))
                            sound_effect.play()
                            self.gamescene = self.gamescene + 1
                        if returnarrowrect.collidepoint(mouse_pos):
                            transition(6)
                            self.guildbool1 = False
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()

            if (self.gamescene == 10):
                rainbowcolor1 = int((math.sin(startTime * 0.002) + 1) * 127.5)
                rainbowcolor2 = int((math.sin(startTime * 0.003 + 2) + 1) * 127.5)
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image207, (197, 100))
                imageBlack.set_alpha(120)
                DISPLAYSURF.blit(imageBlack, (620, 160))
                questsrect = pygame.Rect(860, 210, 290, 120)
                professionrect = pygame.Rect(810, 440, 370, 120)
                draw_text_center('Quests', font2, BLACK, DISPLAYSURF,halfdisplay, 260)
                draw_text_center('Professions', font2, BLACK, DISPLAYSURF, halfdisplay, 490)
                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))
                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 120, 70)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                if questsrect.collidepoint(mouse_pos):
                    pygame.draw.rect(DISPLAYSURF,(rainbowcolor1, 130, 130), questsrect, 11)
                if professionrect.collidepoint(mouse_pos):
                    pygame.draw.rect(DISPLAYSURF,(rainbowcolor1, 130, 130), professionrect, 11)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if questsrect.collidepoint(mouse_pos):
                            print("quests clicked")
                            self.gamescene = 30
                        if professionrect.collidepoint(mouse_pos):
                            print("profession clicked")
                            if(guildtutorial == "false"):
                                self.gamescene = 54
                            elif (guildtutorial == "true"):
                                self.gamescene = 50
                        if returnarrowrect.collidepoint(mouse_pos):
                            transition(6)
                            self.guildbool1 = False
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()

            if (self.gamescene == 100):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image207, (197, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 870))
                draw_text_center('Farewell young adventurer,', font5, GREY, DISPLAYSURF, halfdisplay, 880)
                draw_text_center('May lady luck be in love with you.', font5, GREY, DISPLAYSURF, halfdisplay, 910)
                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))
                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 120, 70)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 0 <= mouseX <= 1920 and 250 <= mouseY <= 1080:
                            sound_effect = pygame.mixer.Sound(resource_path("audio/clicknoise.mp3"))
                            sound_effect.play()
                            transition(6)
                            self.guildbool1 = False
                        if returnarrowrect.collidepoint(mouse_pos):
                            transition(6)
                            self.guildbool1 = False
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()

            if (self.gamescene == 11):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image207, (197, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 870))
                draw_text_center('Welcome back brother to the guild.', font5, GREY, DISPLAYSURF, halfdisplay, 880)
                draw_text_center('What can we do for you today?', font5, GREY, DISPLAYSURF, halfdisplay, 910)
                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))
                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 120, 70)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 0 <= mouseX <= 1920 and 250 <= mouseY <= 1080:
                            sound_effect = pygame.mixer.Sound(resource_path("audio/clicknoise.mp3"))
                            sound_effect.play()
                            self.gamescene = 10
                        if returnarrowrect.collidepoint(mouse_pos):
                            transition(6)
                            self.guildbool1 = False
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()

            if (self.gamescene == 50):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image209, (197, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 870))
                draw_text_center('Welcome to the alchemy room, where magic happens.', font5, GREY, DISPLAYSURF, halfdisplay, 880)
                draw_text_center('Here you can work for the guild and earn some gold.', font5, GREY, DISPLAYSURF, halfdisplay, 910)
                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))
                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 120, 70)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 0 <= mouseX <= 1920 and 250 <= mouseY <= 1080:
                            sound_effect = pygame.mixer.Sound(resource_path("audio/clicknoise.mp3"))
                            sound_effect.play()
                            self.gamescene = self.gamescene + 1
                        if returnarrowrect.collidepoint(mouse_pos):
                            transition(6)
                            self.guildbool1 = False
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()

            if (self.gamescene == 51):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image209, (197, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 870))
                draw_text_center('We only have one profession now, but we will have more in the future.', font5, GREY, DISPLAYSURF, halfdisplay, 880)
                draw_text_center('Its not at all because the game developer is lazy...', font5, GREY, DISPLAYSURF, halfdisplay, 910)
                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))
                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 120, 70)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 0 <= mouseX <= 1920 and 250 <= mouseY <= 1080:
                            sound_effect = pygame.mixer.Sound(resource_path("audio/clicknoise.mp3"))
                            sound_effect.play()
                            self.gamescene = self.gamescene + 1
                        if returnarrowrect.collidepoint(mouse_pos):
                            transition(6)
                            self.guildbool1 = False
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()

            if (self.gamescene == 52):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image209, (197, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 870))
                draw_text_center('Oh, i forgot to mention brother, the more you practice your skills,', font5, GREY, DISPLAYSURF, halfdisplay, 880)
                draw_text_center('the more you will level up, giving you more gold.', font5, GREY, DISPLAYSURF, halfdisplay, 910)
                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))
                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 120, 70)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 0 <= mouseX <= 1920 and 250 <= mouseY <= 1080:
                            sound_effect = pygame.mixer.Sound(resource_path("audio/clicknoise.mp3"))
                            sound_effect.play()
                            self.gamescene = self.gamescene + 1
                        if returnarrowrect.collidepoint(mouse_pos):
                            transition(6)
                            self.guildbool1 = False
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()

            if (self.gamescene == 53):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image209, (197, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 870))
                draw_text_center('Ill leave you to it now, try not to destroy the continent', font5, GREY, DISPLAYSURF, halfdisplay, 880)
                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))
                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 120, 70)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 0 <= mouseX <= 1920 and 250 <= mouseY <= 1080:
                            sound_effect = pygame.mixer.Sound(resource_path("audio/clicknoise.mp3"))
                            sound_effect.play()
                            self.gamescene = self.gamescene + 1
                        if returnarrowrect.collidepoint(mouse_pos):
                            transition(6)
                            self.guildbool1 = False
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()

            if (self.gamescene == 54):
                guildguide = "false"
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image209, (197, 100))
                image4.set_alpha(150)
                DISPLAYSURF.blit(image4, (0, 0))
                image223.set_alpha(staropacity)

                ret, frame = video.read()
                if not ret:
                    video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    continue  # Continue to the next loop iteration
                frame = cv2.resize(frame, (1550, 880))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_surface = pygame.surfarray.make_surface(frame)
                frame_surface = pygame.transform.rotate(frame_surface, -90)  # Rotate if necessary
                frame_surface = pygame.transform.flip(frame_surface, True, False)
                frame_surface.set_alpha(100)
                DISPLAYSURF.blit(frame_surface, (190, 100))

                DISPLAYSURF.blit(image223, (455, 100))
                DISPLAYSURF.blit(image210, (755, 330))
                DISPLAYSURF.blit(image213, (500, 200))


                draw_text('gold - ', font5, WHITE, DISPLAYSURF, 475, 135)
                draw_text(str(gold), font5, YELLOW, DISPLAYSURF, 545, 135)
                draw_text('gems - ', font5, WHITE, DISPLAYSURF, 675, 135)
                draw_text(str(gem), font5, PURPLE, DISPLAYSURF, 755, 135)
                draw_text('alchemy level - ', font5, WHITE, DISPLAYSURF, 875, 135)
                draw_text(str(alchemylevel), font5, GREEN, DISPLAYSURF, 1025, 135)
                draw_text('Exp needed - ', font5, WHITE, DISPLAYSURF, 1145, 135)
                draw_text(str((alchemylevel * 100) - alchemyexp), font5, DARKGREEN, DISPLAYSURF, 1275, 135)
                draw_text('Current Streak- ', font3, WHITE, DISPLAYSURF, 275, 400)
                draw_text(str(streak), font3, PINK, DISPLAYSURF, 540, 400)

                draw_text('Click to Begin', font2, GREY, DISPLAYSURF, 770, 895)
                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))
                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 120, 70)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 0 <= mouseX <= 1920 and 250 <= mouseY <= 1080:
                            sound_effect = pygame.mixer.Sound(resource_path("audio/clicknoise.mp3"))
                            pygame.mixer.music.load(resource_path("audio/alchemy2.mp3"))
                            pygame.mixer.music.play(-1)
                            pygame.mixer.music.queue(resource_path("audio/alchemy3.mp3"))
                            pygame.mixer.music.queue(resource_path("audio/alchemy1.mp3"))
                            pygame.mixer.music.set_volume(0.5)
                            self.gamescene = self.gamescene + 1
                        if returnarrowrect.collidepoint(mouse_pos):
                            transition(6)
                            video.release()
                            self.guildbool1 = False
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            video.release()
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()

            if (self.gamescene == 55):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image209, (197, 100))
                image4.set_alpha(150)
                DISPLAYSURF.blit(image4, (0, 0))
                image223.set_alpha(staropacity)

                ret, frame = video.read()
                if not ret:
                    video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    continue  # Continue to the next loop iteration
                frame = cv2.resize(frame, (1550, 880))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_surface = pygame.surfarray.make_surface(frame)
                frame_surface = pygame.transform.rotate(frame_surface, -90)  # Rotate if necessary
                frame_surface = pygame.transform.flip(frame_surface, True, False)
                frame_surface.set_alpha(100)
                DISPLAYSURF.blit(frame_surface, (190, 100))

                DISPLAYSURF.blit(image223, (455, 100))
                DISPLAYSURF.blit(image210, (755, 330))
                DISPLAYSURF.blit(image211, (880, 780))
                DISPLAYSURF.blit(image213, (500, 200))
                DISPLAYSURF.blit(image214, (x, 120))
                draw_text('gold - ', font5, WHITE, DISPLAYSURF, 475, 135)
                draw_text(str(gold), font5, YELLOW, DISPLAYSURF, 545, 135)
                draw_text('gems - ', font5, WHITE, DISPLAYSURF, 675, 135)
                draw_text(str(gem), font5, PURPLE, DISPLAYSURF, 755, 135)
                draw_text('alchemy level - ', font5, WHITE, DISPLAYSURF, 875, 135)
                draw_text(str(alchemylevel), font5, GREEN, DISPLAYSURF, 1025, 135)
                draw_text('Exp needed - ', font5, WHITE, DISPLAYSURF, 1145, 135)
                draw_text(str((alchemylevel * 100) - alchemyexp), font5, DARKGREEN, DISPLAYSURF, 1275, 135)
                draw_text('Current Streak- ', font3, WHITE, DISPLAYSURF, 275, 400)
                draw_text(str(streak), font3, PINK, DISPLAYSURF, 540, 400)
                if(x <= 450):
                    boolleftorright = True
                if(x >= 1430):
                    boolleftorright = False
                if(boolleftorright):
                    x = x + 10 + (streak * 2)
                if(boolleftorright != True):
                    x = x - 10 - (streak * 2)
                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))
                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 120, 70)
                stoprect = pygame.Rect(880, 780, 160, 160)
                if stoprect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image212, (876, 776))
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if stoprect.collidepoint(mouse_pos):
                            randompotionvalue = random.randint(1, 4)
                            self.gamescene = self.gamescene + 1
                        if returnarrowrect.collidepoint(mouse_pos):
                            transition(6)
                            video.release()
                            self.guildbool1 = False
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            video.release()
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()
                pygame.display.update()
            if (self.gamescene == 56):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image209, (197, 100))
                image4.set_alpha(150)
                DISPLAYSURF.blit(image4, (0, 0))
                image223.set_alpha(staropacity)

                ret, frame = video.read()
                if not ret:
                    video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    continue  # Continue to the next loop iteration
                frame = cv2.resize(frame, (1550, 880))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_surface = pygame.surfarray.make_surface(frame)
                frame_surface = pygame.transform.rotate(frame_surface, -90)  # Rotate if necessary
                frame_surface = pygame.transform.flip(frame_surface, True, False)
                frame_surface.set_alpha(100)
                DISPLAYSURF.blit(frame_surface, (190, 100))

                DISPLAYSURF.blit(image223, (455, 100))
                DISPLAYSURF.blit(image210, (755, 330))
                DISPLAYSURF.blit(image211, (880, 780))
                DISPLAYSURF.blit(image213, (500, 200))
                DISPLAYSURF.blit(image214, (x, 120))
                DISPLAYSURF.blit(image164, (198, 110))
                alchemyhitrect = pygame.Rect(828, 50, 112, 200)
                superalchemyhitrect = pygame.Rect(940, 50, 65, 200)
                alchemyhitrect2 = pygame.Rect(1005, 50, 120, 200)
                streakrect = pygame.Rect(828, 50, 297, 200)
                DISPLAYSURF.blit(image56, (mouseX - 47, mouseY - 44))

                if alchemyhitrect.collidepoint(x + 47, 150):
                    sound_effect = pygame.mixer.Sound(resource_path("audio/potioncreation.mp3"))
                    sound_effect.play()
                    streak = streak + 1
                    alchemyexp = alchemyexp + 1 + streak
                    gold = int(gold + (randompotionvalue * (alchemylevel + (streak / 4))))
                    if(alchemyexp >= (alchemylevel * 100)):
                        alchemyexp = 0
                        alchemylevel = alchemylevel + 1
                        alchemylevelupbool = True
                if alchemyhitrect2.collidepoint(x + 47, 150):
                    sound_effect = pygame.mixer.Sound(resource_path("audio/potioncreation.mp3"))
                    sound_effect.play()
                    streak = streak + 1
                    alchemyexp = alchemyexp + 1 + streak
                    gold = int(gold + (randompotionvalue * (alchemylevel + (streak / 4))))
                    if(alchemyexp >= (alchemylevel * 100)):
                        alchemyexp = 0
                        alchemylevel = alchemylevel + 1
                        alchemylevelupbool = True
                if superalchemyhitrect.collidepoint(x + 47, 150):
                    sound_effect = pygame.mixer.Sound(resource_path("audio/potioncreation.mp3"))
                    sound_effect.play()
                    streak = streak + 1
                    alchemyexp = alchemyexp + 5 + streak
                    gold = int(gold + (randompotionvalue * (alchemylevel + (streak / 2))))
                    if (alchemyexp >= (alchemylevel * 100)):
                        alchemyexp = 0
                        alchemylevel = alchemylevel + 1
                        alchemylevelupbool = True
                if(streakrect.collidepoint(x + 47, 150)):
                    print("streak increased")
                else:
                    print("streak lost")
                    streak = 0
                    sound_effect = pygame.mixer.Sound(resource_path("audio/messedupalchemy.mp3"))
                    sound_effect.play()

                with open(resource_path("gamedata.txt"), "r") as file:
                    lines = file.readlines()
                    lines[0] = f"gold = {gold}\n"
                    lines[1] = f"gem = {gem}\n"
                    lines[12] = f"alchemyexp = {alchemyexp}\n"
                    lines[13] = f"alchemylevel = {alchemylevel}\n"
                    lines[14] = f"guildtutorial = false\n"
                with open(resource_path("gamedata.txt"), "w") as file:
                    file.writelines(lines)
                potionimage = random.randint(1, 5)
                self.gamescene = self.gamescene + 1
                DISPLAYSURF.blit(image56, (mouseX - 47, mouseY - 44))
                pygame.display.update()
            if (self.gamescene == 57):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image209, (197, 100))
                image4.set_alpha(150)
                DISPLAYSURF.blit(image4, (0, 0))
                image223.set_alpha(staropacity)

                ret, frame = video.read()
                if not ret:
                    video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    continue  # Continue to the next loop iteration
                frame = cv2.resize(frame, (1550, 880))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_surface = pygame.surfarray.make_surface(frame)
                frame_surface = pygame.transform.rotate(frame_surface, -90)  # Rotate if necessary
                frame_surface = pygame.transform.flip(frame_surface, True, False)
                frame_surface.set_alpha(100)
                DISPLAYSURF.blit(frame_surface, (190, 100))

                DISPLAYSURF.blit(image223, (455, 100))
                DISPLAYSURF.blit(image210, (755, 330))
                DISPLAYSURF.blit(image211, (880, 780))
                DISPLAYSURF.blit(image213, (500, 200))
                DISPLAYSURF.blit(image214, (x, 120))
                mouse_pos = pygame.mouse.get_pos()
                draw_text('gold - ', font5, WHITE, DISPLAYSURF, 475, 135)
                draw_text(str(gold), font5, YELLOW, DISPLAYSURF, 545, 135)
                draw_text('gems - ', font5, WHITE, DISPLAYSURF, 675, 135)
                draw_text(str(gem), font5, PURPLE, DISPLAYSURF, 755, 135)
                draw_text('alchemy level - ', font5, WHITE, DISPLAYSURF, 875, 135)
                draw_text(str(alchemylevel), font5, GREEN, DISPLAYSURF, 1025, 135)
                draw_text('Exp needed - ', font5, WHITE, DISPLAYSURF, 1145, 135)
                draw_text(str((alchemylevel * 100) - alchemyexp), font5, DARKGREEN, DISPLAYSURF, 1275, 135)
                draw_text('Current Streak- ', font3, WHITE, DISPLAYSURF, 275, 400)
                draw_text(str(streak), font3, PINK, DISPLAYSURF, 540, 400)

                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))
                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 120, 70)
                alchemyhitrect = pygame.Rect(828, 50, 112, 200)
                superalchemyhitrect = pygame.Rect(940, 50, 65, 200)
                alchemyhitrect2 = pygame.Rect(1005, 50, 120, 200)

                if(potionimage == 1):
                    imagechoosen = image215
                if(potionimage == 2):
                    imagechoosen = image216
                if(potionimage == 3):
                    imagechoosen = image217
                if(potionimage == 4):
                    imagechoosen = image218
                if(potionimage == 5):
                    imagechoosen = image219

                if(alchemylevelupbool):
                    draw_text('You leveled up!', font3, LIGHTBLUE, DISPLAYSURF, 820, 355)
                if alchemyhitrect.collidepoint(x + 47, 150):
                    draw_text('Crafted a Potion!', font3, RED, DISPLAYSURF, 815, 275)
                    draw_text('Gained ' +str(int(randompotionvalue * (alchemylevel + (streak / 4)))) +" gold", font3, GOLD, DISPLAYSURF, 825, 315)
                    DISPLAYSURF.blit(imagechoosen, (1320, 490))
                if alchemyhitrect2.collidepoint(x + 47, 150):
                    draw_text_center('Crafted a Potion!', font3, RED, DISPLAYSURF, halfdisplay, 275)
                    draw_text_center('Gained ' +str(int(randompotionvalue * (alchemylevel + (streak / 4)))) +" gold", font3, GOLD, DISPLAYSURF, halfdisplay, 315)
                    DISPLAYSURF.blit(imagechoosen, (1320, 490))
                if superalchemyhitrect.collidepoint(x + 47, 150):
                    draw_text_center('Crafted a Super Potion!', font3, RED, DISPLAYSURF, halfdisplay, 275)
                    draw_text_center('Gained ' +str(int(randompotionvalue * (alchemylevel + (streak / 2)))) +" gold", font3, GOLD, DISPLAYSURF, halfdisplay, 315)
                    DISPLAYSURF.blit(imagechoosen, (1320, 490))

                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 0 <= mouseX <= 1920 and 250 <= mouseY <= 1080:
                            sound_effect = pygame.mixer.Sound(resource_path("audio/clicknoise.mp3"))
                            sound_effect.play()
                            randomnum = random.randint(1,2)
                            if(randomnum == 1):
                                x = 390
                            if(randomnum == 2):
                                x = 1460
                            alchemylevelupbool = False
                            self.gamescene = self.gamescene - 2
                        if returnarrowrect.collidepoint(mouse_pos):
                            transition(6)
                            video.release()
                            self.guildbool1 = False
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            video.release()
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()
                DISPLAYSURF.blit(image56, (mouseX - 47, mouseY - 44))
                pygame.display.update()
            if (self.gamescene == 30):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image208, (197, 100))
                image128.set_alpha(staropacity)
                DISPLAYSURF.blit(image128, (150, 150))
                DISPLAYSURF.blit(image128, (1000, 150))

                ret, frame = video.read()
                if not ret:
                    video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    continue  # Continue to the next loop iteration
                frame = cv2.resize(frame, (1550, 880))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_surface = pygame.surfarray.make_surface(frame)
                frame_surface = pygame.transform.rotate(frame_surface, -90)  # Rotate if necessary
                frame_surface = pygame.transform.flip(frame_surface, True, False)
                frame_surface.set_alpha(100)
                DISPLAYSURF.blit(frame_surface, (190, 100))


                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))
                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 120, 70)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 0 <= mouseX <= 1920 and 250 <= mouseY <= 1080:
                            sound_effect = pygame.mixer.Sound(resource_path("audio/clicknoise.mp3"))
                            sound_effect.play()
                            self.gamescene = self.gamescene
                        if returnarrowrect.collidepoint(mouse_pos):
                            transition(6)
                            video.release()
                            self.guildbool1 = False
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            video.release()
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()
                DISPLAYSURF.blit(image56, (mouseX - 47, mouseY - 44))
                pygame.display.update()

            mouseX, mouseY = pygame.mouse.get_pos()
            image56.set_alpha(200)
            DISPLAYSURF.blit(image56, (mouseX - 47, mouseY - 44))
            if(self.gamescene != 57):
                pygame.display.update()
########################################################################################################################
class blackmarket(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.menu_activeblackmarket = True
        self.blackmarket()
########################################################################################################################
    def xbutton(self, gamescene):
        global FaderBool
        global Fader
        global textFader
        global level
        if (FaderBool):
            Fader = Fader + .5
            if (Fader > 110):
                FaderBool = False
        if (FaderBool == False):
            Fader = Fader - .5
            if (Fader < 10):
                FaderBool = True
        mouse_pos = pygame.mouse.get_pos()
        mouseX, mouseY = pygame.mouse.get_pos()
        DISPLAYSURF.blit(image56, (mouseX - 47, mouseY - 44))
        xrect = pygame.Rect(1680, 123, 35, 35)
        xrect2 = pygame.Rect(130, 100, 120, 80)
        mouseX, mouseY = pygame.mouse.get_pos()
        mouse_pos = pygame.mouse.get_pos()
        image42.set_alpha(Fader)
        DISPLAYSURF.blit(image42, (1655, 917))
        draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
        if xrect.collidepoint(mouse_pos):
            draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
        for event in pygame.event.get():
            mouseX, mouseY = pygame.mouse.get_pos()
            if xrect.collidepoint(mouse_pos):
                if event.type == MOUSEBUTTONDOWN:
                    if xrect.collidepoint(mouse_pos):
                        print("Quit clicked")
                        pygame.mixer.music.stop()
                        pygame.quit()
                        sys.exit()
            else:
                if event.type == MOUSEBUTTONDOWN:
                    if 0 <= mouseX <= 1920 and 150 <= mouseY <= 1080:
                        sound_effect = pygame.mixer.Sound(resource_path("audio/clicknoise.mp3"))
                        sound_effect.play()
                        pygame.mixer.music.set_volume(0.4)
                        pygame.display.update()
                        textFader = 0
                        return (gamescene + 1)
        pygame.display.update()
        return gamescene
    ########################################################################################################################
    def blackmarket(self):
        global FaderBool
        global Fader
        global textFader
        global gold
        global gem
        music1 = False
        video3 = cv2.VideoCapture(resource_path("video/starglitter2.mp4"))
        video = cv2.VideoCapture(resource_path("video/starglitter.mp4"))
        video2 = cv2.VideoCapture(resource_path("video/unboxingcreature.mp4"))
        global beasts
        randombeast = 0
        randomhp = 1
        randomdefense = 1
        randomstrength = 1
        randomspecattack = 1
        randomspeed = 1
        lootcratespeed = 5
        opacitynum = 1
        opacitybool = True
        self.gamescene = 1
        itemdisplay = 0
        xcounter = 0
        mouse_pos = pygame.mouse.get_pos()
        pygame.mixer.music.load(resource_path("audio/battletheme.mp3"))
        pygame.mixer.music.queue(resource_path("audio/etherealmusic.mp3"))
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        print("blackmarket shop initialized")
        global textFader
        global characterName
        global firsttimeblackmarket

        with open(resource_path("gamedata.txt"), "r") as file:
            lines = file.readlines()
            blackmarketshopline = lines[22].strip()
            blackmarketshopline = blackmarketshopline[19:]
            level = lines[15].strip()
            level = level[8:]
            level = int(level)
        if(blackmarketshopline == 'true'):
            self.gamescene = 1
        elif(blackmarketshopline == 'false'):
            self.gamescene = 10

        while self.menu_activeblackmarket:

            start = pygame.time.get_ticks()

            if(opacitybool == True):
                opacitynum = opacitynum + 5
                if(opacitynum >= 245):
                    opacitybool = False
            if(opacitybool == False):
                opacitynum = opacitynum - 5
                if(opacitynum <= 6):
                    opacitybool = True

            with open(resource_path("gamedata.txt"), "r") as file:
                lines = file.readlines()
                if len(lines) >= 8:
                    goldline = lines[0].strip()
                    goldline = goldline[7:]
                    gemline = lines[1].strip()
                    gemline = gemline[6:]
                    gold = int(goldline)
                    gem = int(gemline)
            if (self.gamescene == 1):
                firsttimeblackmarket = False
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image243, (195, 100))
                self.gamescene = self.xbutton(self.gamescene)
                pygame.display.update()
            if (self.gamescene == 2):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image243, (195, 100))
                DISPLAYSURF.blit(image53, (1050, 150))
                draw_text_center('Hehehe, welcome welcome human. Your quite', font21, DARKGREEN, DISPLAYSURF, 1300, 200)
                draw_text_center('handsome arent you. You can call me Byron,', font21, DARKGREEN, DISPLAYSURF, 1300, 225)
                draw_text_center('im the owner of this humble establishment.', font21, DARKGREEN, DISPLAYSURF, 1300, 250)
                draw_text_center('Come let me show you the merchandise.', font21, DARKGREEN, DISPLAYSURF, 1300, 275)

                self.gamescene = self.xbutton(self.gamescene)
                pygame.display.update()
            if (self.gamescene == 3):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image243, (195, 100))
                DISPLAYSURF.blit(image53, (1050, 150))

                draw_text_center('Your not collaborating with the royal guards', font21, DARKGREEN, DISPLAYSURF, 1300, 200)
                draw_text_center('are you? Those bastards have been on my ass', font21, DARKGREEN, DISPLAYSURF, 1300, 225)
                draw_text_center('for a while. Not that it matters much anyways,', font21, DARKGREEN, DISPLAYSURF, 1300, 250)
                draw_text_center('ill just take care of you like the rest', font21, DARKGREEN, DISPLAYSURF, 1300, 275)
                self.gamescene = self.xbutton(self.gamescene)
                pygame.display.update()
            if (self.gamescene == 4):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image243, (195, 100))
                DISPLAYSURF.blit(image53, (1050, 150))

                draw_text_center('Im just kidding, dont be so tense handsome.', font21, DARKGREEN, DISPLAYSURF, 1300, 200)
                draw_text_center(' I dont bite, much...', font21, DARKGREEN, DISPLAYSURF, 1300, 225)
                self.gamescene = self.xbutton(self.gamescene)
                pygame.display.update()
            if (self.gamescene == 5):
                with open(resource_path("gamedata.txt"), "r") as file:
                    lines = file.readlines()
                    lines[22] = f"firstblackmarket = false\n"
                with open(resource_path("gamedata.txt"), "w") as file:
                    file.writelines(lines)  # Write the modified lines back to the file
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image243, (195, 100))
                DISPLAYSURF.blit(image53, (1050, 150))

                draw_text_center('Now tell, are you here to purchase some', font21, DARKGREEN, DISPLAYSURF, 1300, 200)
                draw_text_center('creatures or are you here for me? *wink*', font21, DARKGREEN, DISPLAYSURF, 1300, 225)
                draw_text_center('p', font15, SKYBLUE, DISPLAYSURF, 1300, 250)
                self.gamescene = self.xbutton(self.gamescene)
                pygame.display.update()
            if (self.gamescene == 6):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image243, (195, 100))
                DISPLAYSURF.blit(image53, (1050, 150))

                draw_text_center('hehe,', font21, DARKGREEN, DISPLAYSURF, 1300, 200)
                draw_text_center('Follow me ill show you our merchandise.', font21, DARKGREEN, DISPLAYSURF, 1300, 225)

                self.gamescene = self.xbutton(self.gamescene)
                pygame.display.update()
                music1 = True
            if (self.gamescene == 7):
                if(music1):
                    pygame.mixer.music.load(resource_path("audio/angels.mp3"))
                    pygame.mixer.music.play(-1)
                    music1 = False
                startTime = pygame.time.get_ticks()
                rainbowcolor1 = int((math.sin(startTime * 0.002) + 1) * 127.5)
                rainbowcolor2 = int((math.sin(startTime * 0.003 + 2) + 1) * 127.5)
                rainbowcolor3 = int((math.sin(startTime * 0.004 + 2) + 1) * 127.5)
                rainbow = (rainbowcolor1, rainbowcolor2, rainbowcolor3)
                DISPLAYSURF.fill(BLACK)
                image244.set_alpha(255)
                DISPLAYSURF.blit(image244, (195, 100))
                image4.set_alpha(150)
                DISPLAYSURF.blit(image4, (0, 0))

                ret, frame = video.read()
                if not ret:
                    video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    continue  # Continue to the next loop iteration
                frame = cv2.resize(frame, (1550, 880))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_surface = pygame.surfarray.make_surface(frame)
                frame_surface = pygame.transform.rotate(frame_surface, -90)  # Rotate if necessary
                frame_surface = pygame.transform.flip(frame_surface, True, False)
                frame_surface.set_alpha(100)
                DISPLAYSURF.blit(frame_surface, (190, 100))

                DISPLAYSURF.blit(image245, (320, 580))
                DISPLAYSURF.blit(image246, (1360, 580))
                Fontbig = pygame.font.SysFont("Overwave.otf", 90)

                draw_text('gold-', font5, GOLD, DISPLAYSURF, 355, 135)
                draw_text(str(gold), font5, YELLOW, DISPLAYSURF, 410, 135)
                draw_text('gems-', font5, PURPLE, DISPLAYSURF, 520, 135)
                draw_text(str(gem), font5, BLUE, DISPLAYSURF, 580, 135)


                leftclickrect = pygame.Rect(320, 560, 250, 200)
                rightclickrect = pygame.Rect(1355, 560, 250, 200)
                buyrect = pygame.Rect(805, 765, 310, 135)
                xrect = pygame.Rect(1680, 123, 35, 35)

                mouseX, mouseY = pygame.mouse.get_pos()
                # print("x and y = " + str(mouseX) + " " + str(mouseY))
                mouseX, mouseY = pygame.mouse.get_pos()

                mouse_pos = pygame.mouse.get_pos()
                returnmenurect = pygame.Rect(200, 40, 140, 190)

                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)

                if leftclickrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image251, (305, 565))
                if rightclickrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image252, (1345, 565))
                if buyrect.collidepoint(mouse_pos):
                    pygame.draw.rect(DISPLAYSURF, (BLUE), buyrect, 9)

                if returnmenurect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image135, (200, 100))
                else:
                    DISPLAYSURF.blit(image134, (200, 100))

                Bigswordfont= pygame.font.Font(resource_path("fonts/SwordsmanFont.TTF"), 50)

                if (itemdisplay == 0):
                    draw_text('1000 Gold', font11, YELLOW, DISPLAYSURF, 1430, 260)
                    draw_text_center('Wooden Treasure Chest', Bigswordfont, WHITE, DISPLAYSURF, halfdisplay, 175)
                    draw_text_center('Wooden Treasure Chest', Bigswordfont, (255, 197, 46), DISPLAYSURF, halfdisplay, 175, opacitynum)
                    draw_text_center('Beginner chest for new adventurers to gain their first companion', font5, GREY, DISPLAYSURF, halfdisplay, 920)

                    image253.set_alpha(opacitynum)
                    DISPLAYSURF.blit(image253, (786, 440))
                    DISPLAYSURF.blit(image247, (800, 450))

                    if (gold < 1000):
                        draw_text_center('Invalid', Fontbig, DARKRED, DISPLAYSURF, halfdisplay, 797)
                        draw_text_center('Invalid', Fontbig, BLACK, DISPLAYSURF, halfdisplay, 797, int(opacitynum/2))

                    if (gold >= 1000):
                        draw_text_center('Purchase', Fontbig, GREEN, DISPLAYSURF, halfdisplay, 797)
                        draw_text_center('Purchase', Fontbig, BLACK, DISPLAYSURF, halfdisplay, 797, int(opacitynum/2))

                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == MOUSEBUTTONDOWN:
                            sound_effect = pygame.mixer.Sound(resource_path("audio/shopclicksound.mp3"))
                            sound_effect.play()
                            if xrect.collidepoint(mouse_pos):
                                print("Quit clicked")
                                pygame.mixer.music.stop()
                                pygame.quit()
                                sys.exit()
                            if returnmenurect.collidepoint(mouse_pos):
                                self.gamescene = 10
                                pygame.event.clear()
                            if leftclickrect.collidepoint(mouse_pos):
                                itemdisplay = itemdisplay - 1
                                if (itemdisplay == -1):
                                    itemdisplay = 3
                            if rightclickrect.collidepoint(mouse_pos):
                                itemdisplay = itemdisplay + 1
                                if (itemdisplay == 4):
                                    itemdisplay = 0
                            if buyrect.collidepoint(mouse_pos):
                                if (gold >= 1000):
                                    gold = gold - 1000
                                    sound_effect = pygame.mixer.Sound(resource_path("audio/ingamepurchase.mp3"))
                                    sound_effect.play()
                                    with open(resource_path("gamedata.txt"), "r") as file:
                                        lines = file.readlines()
                                        lines[0] = f"gold = {gold}\n"
                                    with open(resource_path("gamedata.txt"), "w") as file:
                                        file.writelines(lines)
                                    transition(1)
                                    sound_effect = pygame.mixer.Sound(resource_path("audio/treasureopen.mp3"))
                                    sound_effect.play()
                                    sound_effect = pygame.mixer.Sound(resource_path("audio/lootcratechestsound.mp3"))
                                    sound_effect.play()
                                    self.gamescene = 17


                if(itemdisplay == 1):
                    draw_text('10,000 Gold', font11, YELLOW, DISPLAYSURF, 1430, 260)
                    draw_text_center('Diamond Treasure Chest', Bigswordfont, WHITE, DISPLAYSURF, halfdisplay, 175)
                    draw_text_center('Diamond Treasure Chest', Bigswordfont, (204, 255, 255), DISPLAYSURF, halfdisplay, 175,opacitynum)
                    draw_text_center('A chest worthy of nobility. Only the best of the best can afford diamond.', font5, GREY, DISPLAYSURF, halfdisplay, 920)

                    image254.set_alpha(opacitynum)
                    DISPLAYSURF.blit(image254, (810, 450))
                    DISPLAYSURF.blit(image248, (810, 450))

                    if (gold < 10000):
                        draw_text_center('Invalid', Fontbig, DARKRED, DISPLAYSURF, halfdisplay, 797)
                        draw_text_center('Invalid', Fontbig, BLACK, DISPLAYSURF, halfdisplay, 797, int(opacitynum/2))

                    if (gold >= 10000):
                        draw_text_center('Purchase', Fontbig, GREEN, DISPLAYSURF, halfdisplay, 797)
                        draw_text_center('Purchase', Fontbig, BLACK, DISPLAYSURF, halfdisplay, 797, int(opacitynum/2))

                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == MOUSEBUTTONDOWN:
                            sound_effect = pygame.mixer.Sound(resource_path("audio/shopclicksound.mp3"))
                            sound_effect.play()
                            if xrect.collidepoint(mouse_pos):
                                print("Quit clicked")
                                pygame.mixer.music.stop()
                                pygame.quit()
                                sys.exit()
                            if returnmenurect.collidepoint(mouse_pos):
                                self.gamescene = 10
                                pygame.event.clear()
                            if leftclickrect.collidepoint(mouse_pos):
                                itemdisplay = itemdisplay - 1
                                if (itemdisplay == -1):
                                    itemdisplay = 3
                            if rightclickrect.collidepoint(mouse_pos):
                                itemdisplay = itemdisplay + 1
                                if (itemdisplay == 4):
                                    itemdisplay = 0
                            if buyrect.collidepoint(mouse_pos):
                                if (gold >= 10000):
                                    gold = gold - 10000
                                    sound_effect = pygame.mixer.Sound(resource_path("audio/ingamepurchase.mp3"))
                                    sound_effect.play()
                                    with open(resource_path("gamedata.txt"), "r") as file:
                                        lines = file.readlines()
                                        lines[0] = f"gold = {gold}\n"
                                    with open(resource_path("gamedata.txt"), "w") as file:
                                        file.writelines(lines)
                                    transition(1)
                                    sound_effect = pygame.mixer.Sound(resource_path("audio/lootcratechestsound.mp3"))
                                    sound_effect.play()
                                    self.gamescene = 16

                if(itemdisplay == 2):
                    draw_text('100,000 Gold', font11, YELLOW, DISPLAYSURF, 1430, 260)
                    draw_text_center('Emerald Treasure Chest', Bigswordfont, BLACK, DISPLAYSURF, halfdisplay, 175)
                    draw_text_center('Emerald Treasure Chest', Bigswordfont, (102, 255, 180), DISPLAYSURF, halfdisplay, 175,opacitynum)
                    draw_text_center('Emerald Chests are the pinnacle of treasure and host the greatest beasts in the universe. Through chance, ', font5, GREY, DISPLAYSURF, halfdisplay, 920)
                    draw_text_center('the current King of Lucidea gained a legendary beast through an emerald chest solidifying his claim to the throne.', font5, GREY, DISPLAYSURF, halfdisplay, 940)

                    image255.set_alpha(opacitynum)
                    DISPLAYSURF.blit(image255, (790, 450))
                    DISPLAYSURF.blit(image249, (810, 450))

                    if (gold < 100000):
                        draw_text_center('Invalid', Fontbig, DARKRED, DISPLAYSURF, halfdisplay, 797)
                        draw_text_center('Invalid', Fontbig, BLACK, DISPLAYSURF, halfdisplay, 797, int(opacitynum/2))

                    if (gold >= 100000):
                        draw_text_center('Purchase', Fontbig, GREEN, DISPLAYSURF, halfdisplay, 797)
                        draw_text_center('Purchase', Fontbig, BLACK, DISPLAYSURF, halfdisplay, 797, int(opacitynum/2))

                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == MOUSEBUTTONDOWN:
                            sound_effect = pygame.mixer.Sound(resource_path("audio/shopclicksound.mp3"))
                            sound_effect.play()
                            if xrect.collidepoint(mouse_pos):
                                print("Quit clicked")
                                pygame.mixer.music.stop()
                                pygame.quit()
                                sys.exit()
                            if returnmenurect.collidepoint(mouse_pos):
                                self.gamescene = 10
                                pygame.event.clear()
                            if leftclickrect.collidepoint(mouse_pos):
                                itemdisplay = itemdisplay - 1
                                if (itemdisplay == -1):
                                    itemdisplay = 3
                            if rightclickrect.collidepoint(mouse_pos):
                                itemdisplay = itemdisplay + 1
                                if (itemdisplay == 4):
                                    itemdisplay = 0
                            if buyrect.collidepoint(mouse_pos):
                                if (gold >= 100000):
                                    gold = gold - 100000
                                    sound_effect = pygame.mixer.Sound(resource_path("audio/ingamepurchase.mp3"))
                                    sound_effect.play()
                                    with open(resource_path("gamedata.txt"), "r") as file:
                                        lines = file.readlines()
                                        lines[0] = f"gold = {gold}\n"
                                    with open(resource_path("gamedata.txt"), "w") as file:
                                        file.writelines(lines)

                                    transition(1)
                                    sound_effect = pygame.mixer.Sound(resource_path("audio/treasureopen.mp3"))
                                    sound_effect.play()
                                    sound_effect = pygame.mixer.Sound(resource_path("audio/lootcratechestsound.mp3"))
                                    sound_effect.play()
                                    self.gamescene = 15

                if(itemdisplay == 3):
                    draw_text('200 Gems', font11, rainbow, DISPLAYSURF, 1430, 260)
                    draw_text_center('Cosmic Door', Bigswordfont, BLACK, DISPLAYSURF, halfdisplay, 175)
                    draw_text_center('Cosmic Door', Bigswordfont, (rainbowcolor2, rainbowcolor1, rainbowcolor3), DISPLAYSURF, halfdisplay, 175,opacitynum)
                    draw_text_center('Within Cosmic doors reside creatures sealed through time. What you ressurect will be unknown, will you take the risk?', font5, GREY, DISPLAYSURF, halfdisplay, 920)

                    image256.set_alpha(opacitynum)
                    DISPLAYSURF.blit(image256, (700, 310))
                    DISPLAYSURF.blit(image250, (700, 310))

                    if (gem < 100):
                        draw_text_center('Invalid', Fontbig, DARKRED, DISPLAYSURF, halfdisplay, 797)
                        draw_text_center('Invalid', Fontbig, BLACK, DISPLAYSURF, halfdisplay, 797, int(opacitynum/2))

                    if (gem >= 100):
                        if(level < 10):
                            draw_text_center('lvl 5 Req', Fontbig, BLUE, DISPLAYSURF, halfdisplay, 797)
                            draw_text_center('lvl 5 Req', Fontbig, RED, DISPLAYSURF, halfdisplay, 797, int(opacitynum / 2))
                        else:
                            draw_text_center('Purchase', Fontbig, SKYBLUE, DISPLAYSURF, halfdisplay, 797)
                            draw_text_center('Purchase', Fontbig, BLACK, DISPLAYSURF, halfdisplay, 797, int(opacitynum/2))

                    for event in pygame.event.get():
                        if event.type == QUIT:
                            video.release()
                            video2.release()
                            video3.release()
                            pygame.quit()
                            sys.exit()
                        elif event.type == MOUSEBUTTONDOWN:
                            sound_effect = pygame.mixer.Sound(resource_path("audio/shopclicksound.mp3"))
                            sound_effect.play()
                            if xrect.collidepoint(mouse_pos):
                                print("Quit clicked")
                                video.release()
                                video2.release()
                                video3.release()
                                pygame.mixer.music.stop()
                                pygame.quit()
                                sys.exit()
                            if returnmenurect.collidepoint(mouse_pos):
                                self.gamescene = 10
                                pygame.event.clear()
                            if leftclickrect.collidepoint(mouse_pos):
                                itemdisplay = itemdisplay - 1
                                if (itemdisplay == -1):
                                    itemdisplay = 3
                            if rightclickrect.collidepoint(mouse_pos):
                                itemdisplay = itemdisplay + 1
                                if (itemdisplay == 4):
                                    itemdisplay = 0
                            if buyrect.collidepoint(mouse_pos):
                                if (gem >= 200 and level >= 5):
                                    gem = gem - 200
                                    sound_effect = pygame.mixer.Sound(resource_path("audio/ingamepurchase.mp3"))
                                    sound_effect.play()
                                    with open(resource_path("gamedata.txt"), "r") as file:
                                        lines = file.readlines()
                                        lines[1] = f"gem = {gem}\n"
                                    with open(resource_path("gamedata.txt"), "w") as file:
                                        file.writelines(lines)

                                    transition(1)
                                    sound_effect = pygame.mixer.Sound(resource_path("audio/treasureopen.mp3"))
                                    sound_effect.play()
                                    sound_effect = pygame.mixer.Sound(resource_path("audio/scaryhowlverb.mp3"))
                                    sound_effect.play()
                                    self.gamescene = 14

                pygame.display.update()

            if (self.gamescene == 10):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image243, (195, 100))

                mouse_pos = pygame.mouse.get_pos()
                returnmenurect = pygame.Rect(200, 40, 140, 190)
                if returnmenurect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image135, (200, 100))
                else:
                    DISPLAYSURF.blit(image134, (200, 100))

                if (FaderBool):
                    Fader = Fader + .5
                    if (Fader > 110):
                        FaderBool = False
                if (FaderBool == False):
                    Fader = Fader - .5
                    if (Fader < 10):
                        FaderBool = True
                mouse_pos = pygame.mouse.get_pos()
                mouseX, mouseY = pygame.mouse.get_pos()
                DISPLAYSURF.blit(image56, (mouseX - 47, mouseY - 44))
                xrect = pygame.Rect(1680, 123, 35, 35)
                xrect2 = pygame.Rect(130, 100, 120, 80)
                mouseX, mouseY = pygame.mouse.get_pos()
                mouse_pos = pygame.mouse.get_pos()
                image42.set_alpha(Fader)
                DISPLAYSURF.blit(image42, (1655, 917))
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                for event in pygame.event.get():
                    mouseX, mouseY = pygame.mouse.get_pos()
                    if xrect.collidepoint(mouse_pos):
                        if event.type == MOUSEBUTTONDOWN:
                            if xrect.collidepoint(mouse_pos):
                                print("Quit clicked")
                                pygame.mixer.music.stop()
                                pygame.quit()
                                sys.exit()
                    else:
                        if event.type == MOUSEBUTTONDOWN:
                            if returnmenurect.collidepoint(mouse_pos):
                                transition(6)
                                self.menu_activeblackmarket = False
                                pygame.event.clear()
                            if 100 <= mouseX <= 1920 and 150 <= mouseY <= 1080:
                                sound_effect = pygame.mixer.Sound(resource_path("audio/clicknoise.mp3"))
                                sound_effect.play()
                                pygame.mixer.music.set_volume(0.4)
                                pygame.display.update()
                                textFader = 0
                                self.gamescene = self.gamescene + 1

                randomtext = random.randint(0, 7)
                pygame.display.update()
            if (self.gamescene == 11):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image243, (195, 100))
                DISPLAYSURF.blit(image53, (1050, 150))

                mouse_pos = pygame.mouse.get_pos()
                returnmenurect = pygame.Rect(200, 40, 140, 190)
                if returnmenurect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image135, (200, 100))
                else:
                    DISPLAYSURF.blit(image134, (200, 100))


                if (FaderBool):
                    Fader = Fader + .5
                    if (Fader > 110):
                        FaderBool = False
                if (FaderBool == False):
                    Fader = Fader - .5
                    if (Fader < 10):
                        FaderBool = True
                mouse_pos = pygame.mouse.get_pos()
                mouseX, mouseY = pygame.mouse.get_pos()
                DISPLAYSURF.blit(image56, (mouseX - 47, mouseY - 44))
                xrect = pygame.Rect(1680, 123, 35, 35)
                xrect2 = pygame.Rect(130, 100, 120, 80)
                mouseX, mouseY = pygame.mouse.get_pos()
                mouse_pos = pygame.mouse.get_pos()
                image42.set_alpha(Fader)
                DISPLAYSURF.blit(image42, (1655, 917))
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                for event in pygame.event.get():
                    mouseX, mouseY = pygame.mouse.get_pos()
                    if xrect.collidepoint(mouse_pos):
                        if event.type == MOUSEBUTTONDOWN:
                            if xrect.collidepoint(mouse_pos):
                                print("Quit clicked")
                                pygame.mixer.music.stop()
                                pygame.quit()
                                sys.exit()
                    else:
                        if event.type == MOUSEBUTTONDOWN:
                            if returnmenurect.collidepoint(mouse_pos):
                                transition(6)
                                self.menu_activeblackmarket = False
                                pygame.event.clear()
                            if 100 <= mouseX <= 1920 and 150 <= mouseY <= 1080:
                                sound_effect = pygame.mixer.Sound(resource_path("audio/clicknoise.mp3"))
                                sound_effect.play()
                                pygame.mixer.music.set_volume(0.4)
                                pygame.display.update()
                                textFader = 0
                                self.gamescene = self.gamescene + 1

                if(randomtext == 0):
                    draw_text_center('Hey cutie your back again I see!', font21, DARKGREEN, DISPLAYSURF, 1300, 200)
                elif(randomtext == 1):
                    draw_text_center('Awwww did you miss me that much? You are' +characterName +"?", font21, DARKGREEN, DISPLAYSURF, 1300, 200)
                    draw_text_center('back already '+str(characterName), font21, DARKGREEN, DISPLAYSURF, 1300, 225)
                elif(randomtext == 2):
                    draw_text_center('My richest customer is back again!', font21, DARKGREEN, DISPLAYSURF, 1300, 200)
                    draw_text_center(' please be gentle with me '+str(characterName) +"!", font21, DARKGREEN, DISPLAYSURF, 1300, 225)

                elif(randomtext == 3):
                    draw_text_center('Well well well, look who it is,', font21, DARKGREEN, DISPLAYSURF, 1300, 200)
                    draw_text_center('my cutest customer.', font21, DARKGREEN, DISPLAYSURF, 1300, 225)

                elif(randomtext == 4):
                    draw_text_center('Where have you been? You havent visited', font21, DARKGREEN, DISPLAYSURF, 1300, 200)
                    draw_text_center('in so long! Humphh', font21, DARKGREEN, DISPLAYSURF, 1300, 225)
                elif(randomtext == 5):
                    draw_text_center('hufph, Im not in a good mood, the siren', font21, DARKGREEN, DISPLAYSURF, 1300, 200)
                    draw_text_center('slave shipment escaped earlier...', font21, DARKGREEN, DISPLAYSURF, 1300, 225)

                elif(randomtext == 6):
                    draw_text_center('I got some interesting new mechandise just', font21, DARKGREEN, DISPLAYSURF, 1300, 200)
                    draw_text_center('for you sweetheart!', font21, DARKGREEN, DISPLAYSURF, 1300, 225)
                elif(randomtext == 7):
                    draw_text_center('Should I open a brothel, im sure you', font21, DARKGREEN, DISPLAYSURF, 1300, 200)
                    draw_text_center('would be my biggest customer..', font21, DARKGREEN, DISPLAYSURF, 1300, 225)
                    draw_text_center('or would you like to work there?', font21, DARKGREEN, DISPLAYSURF, 1300, 250)

                pygame.display.update()
            if (self.gamescene == 12):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image243, (195, 100))
                DISPLAYSURF.blit(image53, (1050, 150))
                mouse_pos = pygame.mouse.get_pos()
                returnmenurect = pygame.Rect(200, 40, 140, 190)
                if returnmenurect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image135, (200, 100))
                else:
                    DISPLAYSURF.blit(image134, (200, 100))

                if (FaderBool):
                    Fader = Fader + .5
                    if (Fader > 110):
                        FaderBool = False
                if (FaderBool == False):
                    Fader = Fader - .5
                    if (Fader < 10):
                        FaderBool = True
                mouse_pos = pygame.mouse.get_pos()
                mouseX, mouseY = pygame.mouse.get_pos()
                DISPLAYSURF.blit(image56, (mouseX - 47, mouseY - 44))
                xrect = pygame.Rect(1680, 123, 35, 35)
                xrect2 = pygame.Rect(130, 100, 120, 80)
                mouseX, mouseY = pygame.mouse.get_pos()
                mouse_pos = pygame.mouse.get_pos()
                image42.set_alpha(Fader)
                DISPLAYSURF.blit(image42, (1655, 917))
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                for event in pygame.event.get():
                    mouseX, mouseY = pygame.mouse.get_pos()
                    if xrect.collidepoint(mouse_pos):
                        if event.type == MOUSEBUTTONDOWN:
                            if xrect.collidepoint(mouse_pos):
                                print("Quit clicked")
                                pygame.mixer.music.stop()
                                pygame.quit()
                                sys.exit()
                    else:
                        if event.type == MOUSEBUTTONDOWN:
                            if returnmenurect.collidepoint(mouse_pos):
                                transition(6)
                                self.menu_activeblackmarket = False
                                pygame.event.clear()
                            if 100 <= mouseX <= 1920 and 150 <= mouseY <= 1080:
                                sound_effect = pygame.mixer.Sound(resource_path("audio/clicknoise.mp3"))
                                sound_effect.play()
                                pygame.mixer.music.set_volume(0.4)
                                pygame.display.update()
                                textFader = 0
                                self.gamescene = self.gamescene + 1
                draw_text_center('what are you waiting for darling,', font21, DARKGREEN, DISPLAYSURF, 1300, 200)
                draw_text_center('go on and take a look around', font21, DARKGREEN, DISPLAYSURF, 1300, 225)
                music1 = True
                pygame.display.update()
            if (self.gamescene == 13):
                self.gamescene = 7


            if (self.gamescene == 14):
                currentTime = pygame.time.get_ticks()
                startTime = pygame.time.get_ticks()
                i = 0
                while (lootcratespeed != 20):

                    ret, frame = video2.read()
                    if not ret:
                        video2.set(cv2.CAP_PROP_POS_FRAMES, 0)
                        continue  # Continue to the next loop iteration
                    frame = cv2.resize(frame, (1550, 880))
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame_surface = pygame.surfarray.make_surface(frame)
                    frame_surface = pygame.transform.rotate(frame_surface, -90)  # Rotate if necessary
                    frame_surface = pygame.transform.flip(frame_surface, True, False)
                    frame_surface.set_alpha(100)
                    DISPLAYSURF.blit(frame_surface, (190, 100))

                    currentTime = pygame.time.get_ticks()
                    calculatedTime = currentTime - startTime

                    if (calculatedTime < 4000):
                        lootcratespeed = 1
                    elif (calculatedTime < 6000):
                        lootcratespeed = 2
                    elif (calculatedTime < 8000):
                        lootcratespeed = 4
                    elif (calculatedTime < 9000):
                        lootcratespeed = 6
                    elif (calculatedTime < 10000):
                        lootcratespeed = 8
                    elif (calculatedTime < 13000):
                        lootcratespeed = 12
                    elif (calculatedTime < 17000):
                        lootcratespeed = 20

                    i = i + 1
                    if(i == 1):
                        randombeast = random.randint(0, 75)
                    if(i == lootcratespeed):
                        i = 0
                    if(lootcratespeed == 20):
                        transition(10)
                        sound_effect = pygame.mixer.Sound(resource_path("audio/beastsummon.mp3"))
                        sound_effect.play()

                    copy_beast = beasts[randombeast].copy()
                    copy_beast.fill((0, 0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                    DISPLAYSURF.blit(copy_beast, (700, 380))

                    randomhp = random.randint(0,4)
                    randomdefense = random.randint(0, 4)
                    randomstrength = random.randint(0, 4)
                    randomspecattack = random.randint(0, 4)
                    randomspeed = random.randint(0, 4)
                    pygame.display.update()

                    xrect = pygame.Rect(1680, 123, 35, 35)
                    mouse_pos = pygame.mouse.get_pos()
                    draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                    if xrect.collidepoint(mouse_pos):
                        draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                    for event in pygame.event.get():
                        mouseX, mouseY = pygame.mouse.get_pos()
                        if xrect.collidepoint(mouse_pos):
                            if event.type == MOUSEBUTTONDOWN:
                                if xrect.collidepoint(mouse_pos):
                                    print("Quit clicked")
                                    video2.release()
                                    video.release()
                                    video3.release()
                                    pygame.mixer.music.stop()
                                    pygame.quit()
                                    sys.exit()

                ret, frame = video3.read()
                if not ret:
                    video3.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    continue  # Continue to the next loop iteration
                frame = cv2.resize(frame, (1550, 880))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_surface = pygame.surfarray.make_surface(frame)
                frame_surface = pygame.transform.rotate(frame_surface, -90)  # Rotate if necessary
                frame_surface = pygame.transform.flip(frame_surface, True, False)
                frame_surface.set_alpha(100)
                DISPLAYSURF.blit(frame_surface, (190, 100))

                imagewhitehalo.set_alpha(120)
                imagewhiteground.set_alpha(200)
                imagewhitecircle.set_alpha(160)

                DISPLAYSURF.blit(imagewhitehalo, (500, 170))
                DISPLAYSURF.blit(imagewhiteground, (630, 500))
                DISPLAYSURF.blit(imagewhitecircle, (500, 170))

                DISPLAYSURF.blit(beasts[randombeast], (700, 380))

                Beastlevel = beastattributes[randombeast][0]
                basehp = beastattributes[randombeast][1] + randomhp
                basedefense = beastattributes[randombeast][2] + randomdefense
                basestrength = beastattributes[randombeast][3] + randomstrength
                basespecattack = beastattributes[randombeast][4] + randomspecattack
                basespeed = beastattributes[randombeast][5] + randomspeed
                tier = beastattributes[randombeast][6]
                name = beastattributes[randombeast][7]
                beastimage = beastattributes[randombeast][8]
                beasttype = beastattributes[randombeast][13]
                experience = 0

                move1 = " "
                move2 = " "
                move3 = " "
                move4 = " "

                draw_text('Moveset', font20, GOLD, DISPLAYSURF, 220, 300)
                draw_text('------------', font20, GOLD, DISPLAYSURF, 220, 340)

                if(beastattributes[randombeast][9] != 'empty'):
                    move1 = moves[int(beastattributes[randombeast][9])][0]
                    draw_text(move1, font22, WHITE, DISPLAYSURF, 220, 400)
                if(beastattributes[randombeast][10] != 'empty'):
                    move2 = moves[int(beastattributes[randombeast][10])][0]
                    draw_text(move2, font22, WHITE, DISPLAYSURF, 220, 500)
                if(beastattributes[randombeast][11] != 'empty'):
                    move3 = moves[int(beastattributes[randombeast][11])][0]
                    draw_text(move3, font22, WHITE, DISPLAYSURF, 220, 600)
                if(beastattributes[randombeast][12] != 'empty'):
                    move4 = moves[int(beastattributes[randombeast][12])][0]
                    draw_text(move4, font22, WHITE, DISPLAYSURF, 220, 700)


                draw_text('Lvl- ' +str(Beastlevel), font20, WHITE, DISPLAYSURF, 1375, 300)
                draw_text('Hp- ' +str(int((basehp + (basehp * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 400)
                draw_text('Def- ' +str(int((basedefense + (basedefense * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 500)
                draw_text('Str- ' +str(int((basestrength + (basestrength * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 600)
                draw_text('Sp. Att- ' +str(int((basespecattack + (basespecattack * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 700)
                draw_text('Speed- ' +str(int((basespeed + (basespeed * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 800)
                draw_text_center(str(beastattributes[randombeast][7]), font20, YELLOW, DISPLAYSURF, halfdisplay, 150)

                xrect = pygame.Rect(1680, 123, 35, 35)
                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)

                pygame.display.update()
                for event in pygame.event.get():
                    mouseX, mouseY = pygame.mouse.get_pos()
                    if event.type == MOUSEBUTTONDOWN:
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            video.release()
                            video2.release()
                            video3.release()
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()
                        elif(mouseY > 300):
                            print("end lootcrate initialized")
                            creature = {
                                "name": name,
                                "lvl": Beastlevel,
                                "hp": basehp,
                                "defense": basedefense,
                                "strength": basestrength,
                                "special attack": basespecattack,
                                "speed": basespeed,
                                "tier": tier,
                                "beastimage": beastimage,
                                "move1": move1,
                                "move2": move2,
                                "move3": move3,
                                "move4": move4,
                                "type": beasttype,
                                "experience": experience,
                            }
                            save_creature(creature)
                            lootcratespeed = 1
                            self.gamescene = 7

            if (self.gamescene == 15):
                currentTime = pygame.time.get_ticks()
                startTime = pygame.time.get_ticks()
                i = 0
                while (lootcratespeed != 20):

                    ret, frame = video2.read()
                    if not ret:
                        video2.set(cv2.CAP_PROP_POS_FRAMES, 0)
                        continue  # Continue to the next loop iteration
                    frame = cv2.resize(frame, (1550, 880))
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame_surface = pygame.surfarray.make_surface(frame)
                    frame_surface = pygame.transform.rotate(frame_surface, -90)  # Rotate if necessary
                    frame_surface = pygame.transform.flip(frame_surface, True, False)
                    frame_surface.set_alpha(100)
                    DISPLAYSURF.blit(frame_surface, (190, 100))

                    currentTime = pygame.time.get_ticks()
                    calculatedTime = currentTime - startTime

                    if (calculatedTime < 4000):
                        lootcratespeed = 1
                    elif (calculatedTime < 5000):
                        lootcratespeed = 2
                    elif (calculatedTime < 7000):
                        lootcratespeed = 4
                    elif (calculatedTime < 9000):
                        lootcratespeed = 6
                    elif (calculatedTime < 10000):
                        lootcratespeed = 8
                    elif (calculatedTime < 12000):
                        lootcratespeed = 12
                    elif (calculatedTime < 15000):
                        lootcratespeed = 20

                    i = i + 1
                    if(i == 1):
                        randombeast = random.randint(0, 75)
                    if(i == lootcratespeed):
                        i = 0
                    if(lootcratespeed == 20):
                        transition(10)
                        sound_effect = pygame.mixer.Sound(resource_path("audio/beastsummon2.wav"))
                        sound_effect.play()

                    copy_beast = beasts[randombeast].copy()
                    copy_beast.fill((0, 0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                    DISPLAYSURF.blit(copy_beast, (700, 380))

                    randomhp = random.randint(0,4)
                    randomdefense = random.randint(0, 4)
                    randomstrength = random.randint(0, 4)
                    randomspecattack = random.randint(0, 4)
                    randomspeed = random.randint(0, 4)
                    pygame.display.update()

                    xrect = pygame.Rect(1680, 123, 35, 35)
                    mouse_pos = pygame.mouse.get_pos()
                    draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                    if xrect.collidepoint(mouse_pos):
                        draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                    for event in pygame.event.get():
                        mouseX, mouseY = pygame.mouse.get_pos()
                        if xrect.collidepoint(mouse_pos):
                            if event.type == MOUSEBUTTONDOWN:
                                if xrect.collidepoint(mouse_pos):
                                    print("Quit clicked")
                                    video.release()
                                    video2.release()
                                    video3.release()
                                    pygame.mixer.music.stop()
                                    pygame.quit()
                                    sys.exit()

                ret, frame = video3.read()
                if not ret:
                    video3.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    continue  # Continue to the next loop iteration
                frame = cv2.resize(frame, (1550, 880))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_surface = pygame.surfarray.make_surface(frame)
                frame_surface = pygame.transform.rotate(frame_surface, -90)  # Rotate if necessary
                frame_surface = pygame.transform.flip(frame_surface, True, False)
                frame_surface.set_alpha(100)
                DISPLAYSURF.blit(frame_surface, (190, 100))

                imagewhitehalo.set_alpha(120)
                imagewhiteground.set_alpha(200)
                imagewhitecircle.set_alpha(160)

                DISPLAYSURF.blit(imagewhitehalo, (500, 170))
                DISPLAYSURF.blit(imagewhiteground, (630, 500))
                DISPLAYSURF.blit(imagewhitecircle, (500, 170))

                DISPLAYSURF.blit(beasts[randombeast], (700, 380))

                Beastlevel = beastattributes[randombeast][0]
                basehp = beastattributes[randombeast][1] + randomhp
                basedefense = beastattributes[randombeast][2] + randomdefense
                basestrength = beastattributes[randombeast][3] + randomstrength
                basespecattack = beastattributes[randombeast][4] + randomspecattack
                basespeed = beastattributes[randombeast][5] + randomspeed
                tier = beastattributes[randombeast][6]
                name = beastattributes[randombeast][7]
                beastimage = beastattributes[randombeast][8]
                beasttype = beastattributes[randombeast][13]
                experience = 0

                move1 = " "
                move2 = " "
                move3 = " "
                move4 = " "

                draw_text('Moveset', font20, GOLD, DISPLAYSURF, 220, 300)
                draw_text('------------', font20, GOLD, DISPLAYSURF, 220, 340)

                if(beastattributes[randombeast][9] != 'empty'):
                    move1 = moves[int(beastattributes[randombeast][9])][0]
                    draw_text(move1, font22, WHITE, DISPLAYSURF, 220, 400)
                if(beastattributes[randombeast][10] != 'empty'):
                    move2 = moves[int(beastattributes[randombeast][10])][0]
                    draw_text(move2, font22, WHITE, DISPLAYSURF, 220, 500)
                if(beastattributes[randombeast][11] != 'empty'):
                    move3 = moves[int(beastattributes[randombeast][11])][0]
                    draw_text(move3, font22, WHITE, DISPLAYSURF, 220, 600)
                if(beastattributes[randombeast][12] != 'empty'):
                    move4 = moves[int(beastattributes[randombeast][12])][0]
                    draw_text(move4, font22, WHITE, DISPLAYSURF, 220, 700)


                draw_text('Lvl- ' +str(Beastlevel), font20, WHITE, DISPLAYSURF, 1375, 300)
                draw_text('Hp- ' +str(int((basehp + (basehp * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 400)
                draw_text('Def- ' +str(int((basedefense + (basedefense * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 500)
                draw_text('Str- ' +str(int((basestrength + (basestrength * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 600)
                draw_text('Sp. Att- ' +str(int((basespecattack + (basespecattack * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 700)
                draw_text('Speed- ' +str(int((basespeed + (basespeed * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 800)
                draw_text_center(str(beastattributes[randombeast][7]), font20, YELLOW, DISPLAYSURF, halfdisplay, 150)

                xrect = pygame.Rect(1680, 123, 35, 35)
                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)

                pygame.display.update()
                for event in pygame.event.get():
                    mouseX, mouseY = pygame.mouse.get_pos()
                    if event.type == MOUSEBUTTONDOWN:
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            video.release()
                            video2.release()
                            video3.release()
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()
                        elif(mouseY > 300):
                            print("end lootcrate initialized")
                            creature = {
                                "name": name,
                                "lvl": Beastlevel,
                                "hp": basehp,
                                "defense": basedefense,
                                "strength": basestrength,
                                "special attack": basespecattack,
                                "speed": basespeed,
                                "tier": tier,
                                "beastimage": beastimage,
                                "move1": move1,
                                "move2": move2,
                                "move3": move3,
                                "move4": move4,
                                "type": beasttype,
                                "experience": experience,
                            }
                            save_creature(creature)
                            lootcratespeed = 1
                            self.gamescene = 7

            if (self.gamescene == 16):
                currentTime = pygame.time.get_ticks()
                startTime = pygame.time.get_ticks()
                i = 0
                while (lootcratespeed != 20):

                    ret, frame = video2.read()
                    if not ret:
                        video2.set(cv2.CAP_PROP_POS_FRAMES, 0)
                        continue  # Continue to the next loop iteration
                    frame = cv2.resize(frame, (1550, 880))
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame_surface = pygame.surfarray.make_surface(frame)
                    frame_surface = pygame.transform.rotate(frame_surface, -90)  # Rotate if necessary
                    frame_surface = pygame.transform.flip(frame_surface, True, False)
                    frame_surface.set_alpha(100)
                    DISPLAYSURF.blit(frame_surface, (190, 100))

                    currentTime = pygame.time.get_ticks()
                    calculatedTime = currentTime - startTime

                    if (calculatedTime < 4000):
                        lootcratespeed = 1
                    elif (calculatedTime < 5000):
                        lootcratespeed = 2
                    elif (calculatedTime < 7000):
                        lootcratespeed = 4
                    elif (calculatedTime < 9000):
                        lootcratespeed = 6
                    elif (calculatedTime < 10000):
                        lootcratespeed = 8
                    elif (calculatedTime < 12000):
                        lootcratespeed = 12
                    elif (calculatedTime < 15000):
                        lootcratespeed = 20

                    i = i + 1
                    if(i == 1):
                        randombeast = random.randint(0, 50)
                    if(i == lootcratespeed):
                        i = 0
                    if(lootcratespeed == 20):
                        transition(10)
                        sound_effect = pygame.mixer.Sound(resource_path("audio/beastsummon2.wav"))
                        sound_effect.play()

                    copy_beast = beasts[randombeast].copy()
                    copy_beast.fill((0, 0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                    DISPLAYSURF.blit(copy_beast, (700, 380))

                    randomhp = random.randint(0,4)
                    randomdefense = random.randint(0, 4)
                    randomstrength = random.randint(0, 4)
                    randomspecattack = random.randint(0, 4)
                    randomspeed = random.randint(0, 4)
                    pygame.display.update()

                    xrect = pygame.Rect(1680, 123, 35, 35)
                    mouse_pos = pygame.mouse.get_pos()
                    draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                    if xrect.collidepoint(mouse_pos):
                        draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                    for event in pygame.event.get():
                        mouseX, mouseY = pygame.mouse.get_pos()
                        if xrect.collidepoint(mouse_pos):
                            if event.type == MOUSEBUTTONDOWN:
                                if xrect.collidepoint(mouse_pos):
                                    print("Quit clicked")
                                    video.release()
                                    video2.release()
                                    video3.release()
                                    pygame.mixer.music.stop()
                                    pygame.quit()
                                    sys.exit()


                ret, frame = video.read()
                if not ret:
                    video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    continue  # Continue to the next loop iteration
                frame = cv2.resize(frame, (1550, 880))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_surface = pygame.surfarray.make_surface(frame)
                frame_surface = pygame.transform.rotate(frame_surface, -90)  # Rotate if necessary
                frame_surface = pygame.transform.flip(frame_surface, True, False)
                frame_surface.set_alpha(100)
                DISPLAYSURF.blit(frame_surface, (190, 100))

                imagewhitehalo.set_alpha(120)
                imagewhiteground.set_alpha(200)
                imagewhitecircle.set_alpha(160)

                DISPLAYSURF.blit(imagewhitehalo, (500, 170))
                DISPLAYSURF.blit(imagewhiteground, (630, 500))
                DISPLAYSURF.blit(imagewhitecircle, (500, 170))

                DISPLAYSURF.blit(beasts[randombeast], (700, 380))

                Beastlevel = beastattributes[randombeast][0]
                basehp = beastattributes[randombeast][1] + randomhp
                basedefense = beastattributes[randombeast][2] + randomdefense
                basestrength = beastattributes[randombeast][3] + randomstrength
                basespecattack = beastattributes[randombeast][4] + randomspecattack
                basespeed = beastattributes[randombeast][5] + randomspeed
                tier = beastattributes[randombeast][6]
                name = beastattributes[randombeast][7]
                beastimage = beastattributes[randombeast][8]
                beasttype = beastattributes[randombeast][13]
                experience = 0

                move1 = " "
                move2 = " "
                move3 = " "
                move4 = " "

                draw_text('Moveset', font20, GOLD, DISPLAYSURF, 220, 300)
                draw_text('------------', font20, GOLD, DISPLAYSURF, 220, 340)

                if(beastattributes[randombeast][9] != 'empty'):
                    move1 = moves[int(beastattributes[randombeast][9])][0]
                    draw_text(move1, font22, WHITE, DISPLAYSURF, 220, 400)
                if(beastattributes[randombeast][10] != 'empty'):
                    move2 = moves[int(beastattributes[randombeast][10])][0]
                    draw_text(move2, font22, WHITE, DISPLAYSURF, 220, 500)
                if(beastattributes[randombeast][11] != 'empty'):
                    move3 = moves[int(beastattributes[randombeast][11])][0]
                    draw_text(move3, font22, WHITE, DISPLAYSURF, 220, 600)
                if(beastattributes[randombeast][12] != 'empty'):
                    move4 = moves[int(beastattributes[randombeast][12])][0]
                    draw_text(move4, font22, WHITE, DISPLAYSURF, 220, 700)


                draw_text('Lvl- ' +str(Beastlevel), font20, WHITE, DISPLAYSURF, 1375, 300)
                draw_text('Hp- ' +str(int((basehp + (basehp * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 400)
                draw_text('Def- ' +str(int((basedefense + (basedefense * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 500)
                draw_text('Str- ' +str(int((basestrength + (basestrength * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 600)
                draw_text('Sp. Att- ' +str(int((basespecattack + (basespecattack * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 700)
                draw_text('Speed- ' +str(int((basespeed + (basespeed * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 800)
                draw_text_center(str(beastattributes[randombeast][7]), font20, YELLOW, DISPLAYSURF, halfdisplay, 150)

                xrect = pygame.Rect(1680, 123, 35, 35)
                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)

                pygame.display.update()
                for event in pygame.event.get():
                    mouseX, mouseY = pygame.mouse.get_pos()
                    if event.type == MOUSEBUTTONDOWN:
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            video.release()
                            video2.release()
                            video3.release()
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()
                        elif(mouseY > 300):
                            print("end lootcrate initialized")
                            creature = {
                                "name": name,
                                "lvl": Beastlevel,
                                "hp": basehp,
                                "defense": basedefense,
                                "strength": basestrength,
                                "special attack": basespecattack,
                                "speed": basespeed,
                                "tier": tier,
                                "beastimage": beastimage,
                                "move1": move1,
                                "move2": move2,
                                "move3": move3,
                                "move4": move4,
                                "type": beasttype,
                                "experience": experience,
                            }
                            save_creature(creature)
                            lootcratespeed = 1
                            self.gamescene = 7

            if (self.gamescene == 17):
                currentTime = pygame.time.get_ticks()
                startTime = pygame.time.get_ticks()
                i = 0
                while (lootcratespeed != 20):

                    ret, frame = video2.read()
                    if not ret:
                        video2.set(cv2.CAP_PROP_POS_FRAMES, 0)
                        continue  # Continue to the next loop iteration
                    frame = cv2.resize(frame, (1550, 880))
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame_surface = pygame.surfarray.make_surface(frame)
                    frame_surface = pygame.transform.rotate(frame_surface, -90)  # Rotate if necessary
                    frame_surface = pygame.transform.flip(frame_surface, True, False)
                    frame_surface.set_alpha(100)
                    DISPLAYSURF.blit(frame_surface, (190, 100))

                    currentTime = pygame.time.get_ticks()
                    calculatedTime = currentTime - startTime

                    if (calculatedTime < 4000):
                        lootcratespeed = 1
                    elif (calculatedTime < 5000):
                        lootcratespeed = 2
                    elif (calculatedTime < 7000):
                        lootcratespeed = 4
                    elif (calculatedTime < 9000):
                        lootcratespeed = 6
                    elif (calculatedTime < 10000):
                        lootcratespeed = 8
                    elif (calculatedTime < 12000):
                        lootcratespeed = 12
                    elif (calculatedTime < 15000):
                        lootcratespeed = 20

                    i = i + 1
                    if(i == 1):
                        randombeast = random.randint(0, 25)
                    if(i == lootcratespeed):
                        i = 0
                    if(lootcratespeed == 20):
                        transition(10)
                        sound_effect = pygame.mixer.Sound(resource_path("audio/beastsummon2.wav"))
                        sound_effect.play()

                    copy_beast = beasts[randombeast].copy()
                    copy_beast.fill((0, 0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                    DISPLAYSURF.blit(copy_beast, (700, 380))

                    randomhp = random.randint(0,4)
                    randomdefense = random.randint(0, 4)
                    randomstrength = random.randint(0, 4)
                    randomspecattack = random.randint(0, 4)
                    randomspeed = random.randint(0, 4)

                    pygame.display.update()

                    xrect = pygame.Rect(1680, 123, 35, 35)
                    mouse_pos = pygame.mouse.get_pos()
                    draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                    if xrect.collidepoint(mouse_pos):
                        draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                    for event in pygame.event.get():
                        mouseX, mouseY = pygame.mouse.get_pos()
                        if xrect.collidepoint(mouse_pos):
                            if event.type == MOUSEBUTTONDOWN:
                                if xrect.collidepoint(mouse_pos):
                                    print("Quit clicked")
                                    video2.release()
                                    video.release()
                                    video3.release()
                                    pygame.mixer.music.stop()
                                    pygame.quit()
                                    sys.exit()


                ret, frame = video.read()
                if not ret:
                    video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    continue  # Continue to the next loop iteration
                frame = cv2.resize(frame, (1550, 880))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_surface = pygame.surfarray.make_surface(frame)
                frame_surface = pygame.transform.rotate(frame_surface, -90)  # Rotate if necessary
                frame_surface = pygame.transform.flip(frame_surface, True, False)
                frame_surface.set_alpha(100)
                DISPLAYSURF.blit(frame_surface, (190, 100))

                imagewhitehalo.set_alpha(120)
                imagewhiteground.set_alpha(200)
                imagewhitecircle.set_alpha(160)

                DISPLAYSURF.blit(imagewhitehalo, (500, 170))
                DISPLAYSURF.blit(imagewhiteground, (630, 500))
                DISPLAYSURF.blit(imagewhitecircle, (500, 170))


                DISPLAYSURF.blit(beasts[randombeast], (700, 380))

                Beastlevel = beastattributes[randombeast][0]
                basehp = beastattributes[randombeast][1] + randomhp
                basedefense = beastattributes[randombeast][2] + randomdefense
                basestrength = beastattributes[randombeast][3] + randomstrength
                basespecattack = beastattributes[randombeast][4] + randomspecattack
                basespeed = beastattributes[randombeast][5] + randomspeed
                tier = beastattributes[randombeast][6]
                name = beastattributes[randombeast][7]
                beastimage = beastattributes[randombeast][8]
                beasttype = beastattributes[randombeast][13]
                experience = 0


                move1 = " "
                move2 = " "
                move3 = " "
                move4 = " "

                draw_text('Moveset', font20, GOLD, DISPLAYSURF, 220, 300)
                draw_text('------------', font20, GOLD, DISPLAYSURF, 220, 340)

                if(beastattributes[randombeast][9] != 'empty'):
                    move1 = moves[int(beastattributes[randombeast][9])][0]
                    draw_text(move1, font22, WHITE, DISPLAYSURF, 220, 400)
                if(beastattributes[randombeast][10] != 'empty'):
                    move2 = moves[int(beastattributes[randombeast][10])][0]
                    draw_text(move2, font22, WHITE, DISPLAYSURF, 220, 500)
                if(beastattributes[randombeast][11] != 'empty'):
                    move3 = moves[int(beastattributes[randombeast][11])][0]
                    draw_text(move3, font22, WHITE, DISPLAYSURF, 220, 600)
                if(beastattributes[randombeast][12] != 'empty'):
                    move4 = moves[int(beastattributes[randombeast][12])][0]
                    draw_text(move4, font22, WHITE, DISPLAYSURF, 220, 700)

                draw_text('Lvl- ' +str(Beastlevel), font20, WHITE, DISPLAYSURF, 1375, 300)
                draw_text('Hp- ' +str(int((basehp + (basehp * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 400)
                draw_text('Def- ' +str(int((basedefense + (basedefense * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 500)
                draw_text('Str- ' +str(int((basestrength + (basestrength * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 600)
                draw_text('Sp. Att- ' +str(int((basespecattack + (basespecattack * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 700)
                draw_text('Speed- ' +str(int((basespeed + (basespeed * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 800)
                draw_text_center(str(beastattributes[randombeast][7]), font20, YELLOW, DISPLAYSURF, halfdisplay, 150)

                xrect = pygame.Rect(1680, 123, 35, 35)
                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)

                pygame.display.update()
                for event in pygame.event.get():
                    mouseX, mouseY = pygame.mouse.get_pos()
                    if event.type == MOUSEBUTTONDOWN:
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            video.release()
                            video2.release()
                            video3.release()
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()
                        elif(mouseY > 300):
                            print("end lootcrate initialized")
                            creature = {
                                "name": name,
                                "lvl": Beastlevel,
                                "hp": basehp,
                                "defense": basedefense,
                                "strength": basestrength,
                                "special attack": basespecattack,
                                "speed": basespeed,
                                "tier": tier,
                                "beastimage": beastimage,
                                "move1": move1,
                                "move2": move2,
                                "move3": move3,
                                "move4": move4,
                                "type": beasttype,
                                "experience": experience,
                            }
                            save_creature(creature)
                            lootcratespeed = 1
                            self.gamescene = 7


        with open(resource_path("gamedata.txt"), "r") as file:
            lines = file.readlines()
            lines[0] = f"gold = {gold}\n"
            lines[1] = f"gem = {gem}\n"
        with open(resource_path("gamedata.txt"), "w") as file:
            file.writelines(lines)
        return 0
########################################################################################################################
class stash(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.stashloop = True
        self.stashvault()
########################################################################################################################
    def stashvault(self):
        global FaderBool
        global Fader
        global textFader
        video = cv2.VideoCapture(resource_path("video/underwater.mp4"))
        video2 = cv2.VideoCapture(resource_path("video/vaultenter.mov"))
        opacityvalue = 1
        opacitybool = True
        startTime = pygame.time.get_ticks()
        self.gamescene = 1
        mouse_pos = pygame.mouse.get_pos()
        pygame.mixer.music.load(resource_path("audio/stashambient1.mp3"))
        pygame.mixer.music.queue(resource_path("audio/stashambient2.mp3"))
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        sound_effect = pygame.mixer.Sound(resource_path("audio/landofangels.mp3"))
        sound_effect.play()
        pygame.mixer.music.set_volume(0.4)
        print("Stash initialized")
        global textFader
        global characterName
        global gold
        global gem

        creaturename = []
        creaturelvl = []
        creaturehp = []
        creaturedefense = []
        creaturestrength = []
        creaturespecattack = []
        creaturespeed = []
        creaturestrength = []
        creaturespecattack = []
        creaturespeed = []
        creaturetier = []
        creatureimage = []
        creaturemove1 = []
        creaturemove2 = []
        creaturemove3 = []
        creaturemove4 = []
        creaturetype = []
        creatureexp = []
        clickedrect = -1
        creaturepage = 1
        itempage = 1

        creatures = load_creatures("creaturedata.txt")

        for creature in creatures:
            attributes = list(creature.values())
            creaturename.append(attributes[0])
            creaturelvl.append(attributes[1])
            creaturehp.append(attributes[2])
            creaturedefense.append(attributes[3])
            creaturestrength.append(attributes[4])
            creaturespecattack.append(attributes[5])
            creaturespeed.append(attributes[6])
            creaturetier.append(attributes[7])
            creatureimage.append(attributes[8])
            creaturemove1.append(attributes[9])
            creaturemove2.append(attributes[10])
            creaturemove3.append(attributes[11])
            creaturemove4.append(attributes[12])
            creaturetype.append(attributes[13])
            creatureexp.append(attributes[14])


#################################################
        itemname = []
        itemimagecore = []
        regularimage = []
        itemHP = []
        itemarmor = []
        itemAttack = []
        itemspecialattack = []
        itemspeed = []
        itemluck = []

        items = load_creatures("itemdata.txt")

        for item in items:
            attributes = list(item.values())
            itemname.append(attributes[0])
            regularimage.append(attributes[1])
            tempimage = pygame.image.load(resource_path(attributes[1]))
            tempimage = pygame.transform.scale(tempimage, (60, 60))
            itemimagecore.append(tempimage)
            itemHP.append(attributes[2])
            itemarmor.append(attributes[3])
            itemAttack.append(attributes[4])
            itemspecialattack.append(attributes[5])
            itemspeed.append(attributes[6])
            itemluck.append(attributes[7])

        equipmentimages = [[], [], [], [], [], [], []]
        equipeditems = load_teamcreatures("equipeditems.txt")
        if (len(equipeditems) >= 1 and equipeditems[0] != {}):
            attributes = list(equipeditems[0].values())
            tempimg = pygame.image.load(resource_path(attributes[1]))
            tempimg = pygame.transform.scale(tempimg, (60, 60))
            equipmentimages[0] = tempimg
        if (len(equipeditems) >= 2 and equipeditems[1] != {}):
            attributes = list(equipeditems[1].values())
            tempimg = pygame.image.load(resource_path(attributes[1]))
            tempimg = pygame.transform.scale(tempimg, (60, 60))
            equipmentimages[1] = tempimg
        if (len(equipeditems) >= 3 and equipeditems[2] != {}):
            attributes = list(equipeditems[2].values())
            tempimg = pygame.image.load(resource_path(attributes[1]))
            tempimg = pygame.transform.scale(tempimg, (60, 60))
            equipmentimages[2] = tempimg
        if (len(equipeditems) >= 4 and equipeditems[3] != {}):
            attributes = list(equipeditems[3].values())
            tempimg = pygame.image.load(resource_path(attributes[1]))
            tempimg = pygame.transform.scale(tempimg, (60, 60))
            equipmentimages[3] = tempimg
        if (len(equipeditems) >= 5 and equipeditems[4] != {}):
            attributes = list(equipeditems[4].values())
            tempimg = pygame.image.load(resource_path(attributes[1]))
            tempimg = pygame.transform.scale(tempimg, (60, 60))
            equipmentimages[4] = tempimg
        if (len(equipeditems) >= 6 and equipeditems[5] != {}):
            attributes = list(equipeditems[5].values())
            tempimg = pygame.image.load(resource_path(attributes[1]))
            tempimg = pygame.transform.scale(tempimg, (60, 60))
            equipmentimages[5] = tempimg
        if (len(equipeditems) >= 7 and equipeditems[6] != {}):

            attributes = list(equipeditems[6].values())
            tempimg = pygame.image.load(resource_path(attributes[1]))
            tempimg = pygame.transform.scale(tempimg, (60, 60))
            equipmentimages[6] = tempimg
########################################################################################################################
        while self.stashloop:
            rainbowcolor1 = int((math.sin(startTime * 0.002) + 1) * 127.5)
            rainbowcolor2 = int((math.sin(startTime * 0.003 + 2) + 1) * 127.5)
            rainbowcolor3 = int((math.sin(startTime * 0.005 + 2) + 1) * 127.5)
            rainbow = (rainbowcolor1, rainbowcolor2, rainbowcolor3)
            with open(resource_path("gamedata.txt"), "r") as file:
                lines = file.readlines()
                goldline = lines[0].strip()
                goldline = goldline[7:]
                gemline = lines[1].strip()
                gemline = gemline[6:]
                gold = int(goldline)
                gem = int(gemline)

            startTime = pygame.time.get_ticks()
            mouseX, mouseY = pygame.mouse.get_pos()
            DISPLAYSURF.blit(image56, (mouseX - 47, mouseY - 44))

            if(opacitybool == True):
                opacityvalue = opacityvalue + 1
            if(opacitybool == False):
                opacityvalue = opacityvalue - 1
            if(opacityvalue >= 250):
                opacitybool = False
            if (opacityvalue <= 5):
                opacitybool = True

            if (self.gamescene == 1):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image262, (197, 100))

                ret, frame = video.read()
                if not ret:
                    video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    continue  # Continue to the next loop iteration
                frame = cv2.resize(frame, (1550, 880))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_surface = pygame.surfarray.make_surface(frame)
                frame_surface = pygame.transform.rotate(frame_surface, -90)  # Rotate if necessary
                frame_surface = pygame.transform.flip(frame_surface, True, False)
                frame_surface.set_alpha(70)
                DISPLAYSURF.blit(frame_surface, (190, 100))

                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))
                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 120, 70)
                draw_text_center('Click to Enter Vault', font18, WHITE, DISPLAYSURF, halfdisplay, 300)
                draw_text_center('Click to Enter Vault', font18, AQUA, DISPLAYSURF, halfdisplay, 300, opacityvalue)

                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 0 <= mouseX <= 1920 and 250 <= mouseY <= 1080:
                            sound_effect = pygame.mixer.Sound(resource_path("audio/vaultopen.mp3"))
                            sound_effect.play()
                            sound_effect = pygame.mixer.Sound(resource_path("audio/stashtransitionnoise.mp3"))
                            sound_effect.play()
                            fps = int(video2.get(cv2.CAP_PROP_FPS))
                            clock = pygame.time.Clock()
                            while video2.isOpened():
                                ret, frame = video2.read()
                                if not ret:
                                    break
                                frame = cv2.resize(frame, (1650, 940))
                                frame = cv2.flip(frame, 1)
                                frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
                                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                                frame = pygame.surfarray.make_surface(frame).convert()
                                DISPLAYSURF.blit(frame, (140, 50))
                                pygame.display.flip()  # Update the display
                                clock.tick(fps)
                            video2.release()
                            transition(6)
                            pygame.mixer.stop()
                            pygame.mixer.music.load(resource_path("audio/galacticvoyage.mp3"))
                            pygame.mixer.music.queue(resource_path("audio/celestialdream.mp3"))
                            pygame.mixer.music.play(-1)
                            self.gamescene = self.gamescene + 1
                        if returnarrowrect.collidepoint(mouse_pos):
                            video.release()
                            transition(6)
                            self.stashloop = False
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            video.release()
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()
                pygame.display.update()
            if (self.gamescene == 2):
                DISPLAYSURF.fill(BLACK)
                mouse_pos = pygame.mouse.get_pos()
                mouseX, mouseY = pygame.mouse.get_pos()
                #print("x and y = " + str(mouseX) + " " + str(mouseY))

                image264.set_alpha(150)
                DISPLAYSURF.blit(image264, (197, 100))

                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))

                ret, frame = video.read()
                if not ret:
                    video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    continue  # Continue to the next loop iteration
                frame = cv2.resize(frame, (1550, 880))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_surface = pygame.surfarray.make_surface(frame)
                frame_surface = pygame.transform.rotate(frame_surface, -90)  # Rotate if necessary
                frame_surface = pygame.transform.flip(frame_surface, True, False)
                frame_surface.set_alpha(70)
                DISPLAYSURF.blit(frame_surface, (190, 100))

                DISPLAYSURF.blit(image267, (490, 190))

                draw_text_center('Armory', font23, RED, DISPLAYSURF, 885, 222)
                draw_text_center('Beasts', font23, PURPLE, DISPLAYSURF, 1043, 222)
                draw_text_center('Equipment', font23, AQUA, DISPLAYSURF, 580, 310)
                draw_text_center('Page ' + str(itempage), font23, EMERALD, DISPLAYSURF, halfdisplay + 5, 875)

                DISPLAYSURF.blit(image133, (mouseX - 41, mouseY - 37))

                rects = []
                i = 0
                amountitems = len(itemimagecore)
                while (i != amountitems):

                    ii = (i + (itempage - 1) * 36)
                    size = len(itemimagecore) - 1

                    if (i >= 0 and i <= 5):
                        if (size >= ii):
                            DISPLAYSURF.blit(itemimagecore[ii], (699 + (94 * i), 288))
                            rect = pygame.Rect(695 + (94 * i), 282, 73, 71)
                            rects.append(rect)
                    if (i >= 6 and i <= 11):
                        if (size >= ii):
                            DISPLAYSURF.blit(itemimagecore[ii], (699 + (94 * (i - 6)), 379))
                            rect = pygame.Rect(695 + (94 * (i - 6)), 373, 73, 71)
                            rects.append(rect)
                    if (i >= 12 and i <= 17):
                        if (size >= ii):
                            DISPLAYSURF.blit(itemimagecore[ii], (699 + (94 * (i - 12)), 465))
                            rect = pygame.Rect(695 + (94 * (i - 12)), 460, 73, 71)
                            rects.append(rect)
                    if (i >= 18 and i <= 23):
                        if (size >= ii):
                            DISPLAYSURF.blit(itemimagecore[ii], (699 + (94 * (i - 18)), 555))
                            rect = pygame.Rect(695 + (94 * (i - 18)), 549, 73, 71)
                            rects.append(rect)
                    if (i >= 24 and i <= 29):
                        if (size >= ii):
                            DISPLAYSURF.blit(itemimagecore[ii], (699 + (94 * (i - 24)), 642))
                            rect = pygame.Rect(695 + (94 * (i - 24)), 636, 73, 71)
                            rects.append(rect)
                    if (i >= 30 and i <= 35):
                        if (size >= ii):
                            DISPLAYSURF.blit(itemimagecore[ii], (699 + (94 * (i - 30)), 731))
                            rect = pygame.Rect(695 + (94 * (i - 30)), 726, 73, 71)
                            rects.append(rect)

                    i = i + 1

                showbool = True
                x = 0
                helmetrect = pygame.Rect(576, 354, 107, 80)
                chestplaterect = pygame.Rect(576, 450, 108, 80)
                pantsrect = pygame.Rect(575, 546, 107, 80)
                bootsrect = pygame.Rect(574, 644, 107, 80)

                jewelry1rect = pygame.Rect(501, 364, 63, 55)
                jewelry2rect = pygame.Rect(501, 443,  63, 53)

                weaponrect = pygame.Rect(490, 510, 79, 107)

                pygame.draw.ellipse(DISPLAYSURF, PINPPINK, helmetrect, 6)
                pygame.draw.ellipse(DISPLAYSURF, PINPPINK, chestplaterect, 6)
                pygame.draw.ellipse(DISPLAYSURF, PINPPINK, pantsrect, 6)
                pygame.draw.ellipse(DISPLAYSURF, PINPPINK, bootsrect, 6)

                pygame.draw.rect(DISPLAYSURF, LIME, jewelry1rect, 4, )
                pygame.draw.rect(DISPLAYSURF, LIME, jewelry2rect, 4, )

                pygame.draw.rect(DISPLAYSURF, SLEEPPURPLE, weaponrect, 6)

                for rect in rects:
                    pygame.draw.rect(DISPLAYSURF, PINK, rect, 6, 10)
                    if rect.collidepoint(mouse_pos):
                        showbool = False
                        xx = x + ((itempage - 1) * 36)
                        pygame.draw.rect(DISPLAYSURF, GOLD, rect, 6, 10)
                        draw_text(str(itemname[xx]), font24, LIGHTGREEN, DISPLAYSURF, 1270, 365)
                        draw_text_center("stats", font24, BLUE, DISPLAYSURF, 290, 365)
                        draw_text('Hp- ' +str(itemHP[xx]), font24, SKYBLUE, DISPLAYSURF, 230, 425)
                        draw_text("Armor- " +str(itemarmor[xx]), font24, SKYBLUE, DISPLAYSURF, 230, 465)
                        draw_text("Attack- " +str(itemAttack[xx]), font24, SKYBLUE, DISPLAYSURF, 230, 505)
                        draw_text("Spec Att- " +str(itemspecialattack[xx]), font24, SKYBLUE, DISPLAYSURF, 230, 545)
                        draw_text("Speed- " +str(itemspeed[xx]), font24, SKYBLUE, DISPLAYSURF, 230, 585)
                        draw_text("luck- " +str(itemluck[xx]), font24, SKYBLUE, DISPLAYSURF, 230, 625)
                        draw_text_center("Lore", font5, SLEEPPURPLE, DISPLAYSURF, halfdisplay + 5, 940)
                        draw_text_center("Rarity- ", font24, CLOUD, DISPLAYSURF, 1368, 440)
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                clickedrect = x + ((itempage - 1) * 36)

                    x = x + 1
                if (clickedrect != -1):
                    if (clickedrect > ((itempage - 1) * 36) - 1) and (clickedrect <= ((itempage * 36) - 1)):
                        pygame.draw.rect(DISPLAYSURF, AQUA, rects[clickedrect - ((itempage - 1) * 36)], 6, 10)

                if (showbool == True):
                    if helmetrect.collidepoint(mouse_pos):
                        equipeditems = load_teamcreatures("equipeditems.txt")
                        if (len(equipeditems) >= 1 and equipeditems[0] != {}):
                            attributes = list(equipeditems[0].values())
                            draw_text(str(attributes[0]), font24, LIGHTGREEN, DISPLAYSURF, 1270, 365)
                            draw_text_center("stats", font24, BLUE, DISPLAYSURF, 290, 365)
                            draw_text('Hp- ' +str(attributes[2]), font24, SKYBLUE, DISPLAYSURF, 230, 425)
                            draw_text("Armor- " +str(attributes[3]), font24, SKYBLUE, DISPLAYSURF, 230, 465)
                            draw_text("Attack- " +str(attributes[4]), font24, SKYBLUE, DISPLAYSURF, 230, 505)
                            draw_text("Spec Att- " +str(attributes[5]), font24, SKYBLUE, DISPLAYSURF, 230, 545)
                            draw_text("Speed- " +str(attributes[6]), font24, SKYBLUE, DISPLAYSURF, 230, 585)
                            draw_text("luck- " +str(attributes[7]), font24, SKYBLUE, DISPLAYSURF, 260, 625)
                            draw_text_center("Lore", font5, SLEEPPURPLE, DISPLAYSURF, halfdisplay + 5, 940)
                            draw_text_center("Rarity- ", font24, CLOUD, DISPLAYSURF, 1368, 440)
                    elif chestplaterect.collidepoint(mouse_pos):
                        equipeditems = load_teamcreatures("equipeditems.txt")
                        if (len(equipeditems) >= 2 and equipeditems[1] != {}):
                            attributes = list(equipeditems[1].values())
                            draw_text(str(attributes[0]), font24, LIGHTGREEN, DISPLAYSURF, 1270, 365)
                            draw_text_center("stats", font24, BLUE, DISPLAYSURF, 290, 365)
                            draw_text('Hp- ' +str(attributes[2]), font24, SKYBLUE, DISPLAYSURF, 230, 425)
                            draw_text("Armor- " +str(attributes[3]), font24, SKYBLUE, DISPLAYSURF, 230, 465)
                            draw_text("Attack- " +str(attributes[4]), font24, SKYBLUE, DISPLAYSURF, 230, 505)
                            draw_text("Spec Att- " +str(attributes[5]), font24, SKYBLUE, DISPLAYSURF, 230, 545)
                            draw_text("Speed- " +str(attributes[6]), font24, SKYBLUE, DISPLAYSURF, 230, 585)
                            draw_text("luck- " +str(attributes[7]), font24, SKYBLUE, DISPLAYSURF, 260, 625)
                            draw_text_center("Lore", font5, SLEEPPURPLE, DISPLAYSURF, halfdisplay + 5, 940)
                            draw_text_center("Rarity- ", font24, CLOUD, DISPLAYSURF, 1368, 440)
                    elif pantsrect.collidepoint(mouse_pos):
                        equipeditems = load_teamcreatures("equipeditems.txt")
                        if (len(equipeditems) >= 3 and equipeditems[2] != {}):
                            attributes = list(equipeditems[2].values())
                            draw_text(str(attributes[0]), font24, LIGHTGREEN, DISPLAYSURF, 1270, 365)
                            draw_text_center("stats", font24, BLUE, DISPLAYSURF, 290, 365)
                            draw_text('Hp- ' +str(attributes[2]), font24, SKYBLUE, DISPLAYSURF, 230, 425)
                            draw_text("Armor- " +str(attributes[3]), font24, SKYBLUE, DISPLAYSURF, 230, 465)
                            draw_text("Attack- " +str(attributes[4]), font24, SKYBLUE, DISPLAYSURF, 230, 505)
                            draw_text("Spec Att- " +str(attributes[5]), font24, SKYBLUE, DISPLAYSURF, 230, 545)
                            draw_text("Speed- " +str(attributes[6]), font24, SKYBLUE, DISPLAYSURF, 230, 585)
                            draw_text("luck- " +str(attributes[7]), font24, SKYBLUE, DISPLAYSURF, 260, 625)
                            draw_text_center("Lore", font5, SLEEPPURPLE, DISPLAYSURF, halfdisplay + 5, 940)
                            draw_text_center("Rarity- ", font24, CLOUD, DISPLAYSURF, 1368, 440)
                    elif bootsrect.collidepoint(mouse_pos):
                        equipeditems = load_teamcreatures("equipeditems.txt")
                        if (len(equipeditems) >= 4 and equipeditems[3] != {}):
                            attributes = list(equipeditems[3].values())
                            draw_text(str(attributes[0]), font24, LIGHTGREEN, DISPLAYSURF, 1270, 365)
                            draw_text_center("stats", font24, BLUE, DISPLAYSURF, 290, 365)
                            draw_text('Hp- ' +str(attributes[2]), font24, SKYBLUE, DISPLAYSURF, 230, 425)
                            draw_text("Armor- " +str(attributes[3]), font24, SKYBLUE, DISPLAYSURF, 230, 465)
                            draw_text("Attack- " +str(attributes[4]), font24, SKYBLUE, DISPLAYSURF, 230, 505)
                            draw_text("Spec Att- " +str(attributes[5]), font24, SKYBLUE, DISPLAYSURF, 230, 545)
                            draw_text("Speed- " +str(attributes[6]), font24, SKYBLUE, DISPLAYSURF, 230, 585)
                            draw_text("luck- " +str(attributes[7]), font24, SKYBLUE, DISPLAYSURF, 260, 625)
                            draw_text_center("Lore", font5, SLEEPPURPLE, DISPLAYSURF, halfdisplay + 5, 940)
                            draw_text_center("Rarity- ", font24, CLOUD, DISPLAYSURF, 1368, 440)
                    elif jewelry1rect.collidepoint(mouse_pos):
                        equipeditems = load_teamcreatures("equipeditems.txt")
                        if (len(equipeditems) >= 5 and equipeditems[4] != {}):
                            attributes = list(equipeditems[4].values())
                            draw_text(str(attributes[0]), font24, LIGHTGREEN, DISPLAYSURF, 1270, 365)
                            draw_text_center("stats", font24, BLUE, DISPLAYSURF, 290, 365)
                            draw_text('Hp- ' +str(attributes[2]), font24, SKYBLUE, DISPLAYSURF, 230, 425)
                            draw_text("Armor- " +str(attributes[3]), font24, SKYBLUE, DISPLAYSURF, 230, 465)
                            draw_text("Attack- " +str(attributes[4]), font24, SKYBLUE, DISPLAYSURF, 230, 505)
                            draw_text("Spec Att- " +str(attributes[5]), font24, SKYBLUE, DISPLAYSURF, 230, 545)
                            draw_text("Speed- " +str(attributes[6]), font24, SKYBLUE, DISPLAYSURF, 230, 585)
                            draw_text("luck- " +str(attributes[7]), font24, SKYBLUE, DISPLAYSURF, 260, 625)
                            draw_text_center("Lore", font5, SLEEPPURPLE, DISPLAYSURF, halfdisplay + 5, 940)
                            draw_text_center("Rarity- ", font24, CLOUD, DISPLAYSURF, 1368, 440)
                    elif jewelry2rect.collidepoint(mouse_pos):
                        equipeditems = load_teamcreatures("equipeditems.txt")
                        if (len(equipeditems) >= 6 and equipeditems[5] != {}):
                            attributes = list(equipeditems[5].values())
                            draw_text(str(attributes[0]), font24, LIGHTGREEN, DISPLAYSURF, 1270, 365)
                            draw_text_center("stats", font24, BLUE, DISPLAYSURF, 290, 365)
                            draw_text('Hp- ' +str(attributes[2]), font24, SKYBLUE, DISPLAYSURF, 230, 425)
                            draw_text("Armor- " +str(attributes[3]), font24, SKYBLUE, DISPLAYSURF, 230, 465)
                            draw_text("Attack- " +str(attributes[4]), font24, SKYBLUE, DISPLAYSURF, 230, 505)
                            draw_text("Spec Att- " +str(attributes[5]), font24, SKYBLUE, DISPLAYSURF, 230, 545)
                            draw_text("Speed- " +str(attributes[6]), font24, SKYBLUE, DISPLAYSURF, 230, 585)
                            draw_text("luck- " +str(attributes[7]), font24, SKYBLUE, DISPLAYSURF, 260, 625)
                            draw_text_center("Lore", font5, SLEEPPURPLE, DISPLAYSURF, halfdisplay + 5, 940)
                            draw_text_center("Rarity- ", font24, CLOUD, DISPLAYSURF, 1368, 440)
                    elif weaponrect.collidepoint(mouse_pos):
                        equipeditems = load_teamcreatures("equipeditems.txt")
                        if (len(equipeditems) >= 7 and equipeditems[6] != {}):
                            attributes = list(equipeditems[6].values())
                            draw_text(str(attributes[0]), font24, LIGHTGREEN, DISPLAYSURF, 1270, 365)
                            draw_text_center("stats", font24, BLUE, DISPLAYSURF, 290, 365)
                            draw_text('Hp- ' + str(attributes[2]), font24, SKYBLUE, DISPLAYSURF, 230, 425)
                            draw_text("Armor- " + str(attributes[3]), font24, SKYBLUE, DISPLAYSURF, 230, 465)
                            draw_text("Attack- " + str(attributes[4]), font24, SKYBLUE, DISPLAYSURF, 230, 505)
                            draw_text("Spec Att- " + str(attributes[5]), font24, SKYBLUE, DISPLAYSURF, 230, 545)
                            draw_text("Speed- " + str(attributes[6]), font24, SKYBLUE, DISPLAYSURF, 230, 585)
                            draw_text("luck- " + str(attributes[7]), font24, SKYBLUE, DISPLAYSURF, 260, 625)
                            draw_text_center("Lore", font5, SLEEPPURPLE, DISPLAYSURF, halfdisplay + 5, 940)
                            draw_text_center("Rarity- ", font24, CLOUD, DISPLAYSURF, 1368, 440)
                    elif (clickedrect != -1):
                        if (clickedrect > ((itempage - 1) * 36) - 1) and (clickedrect <= ((itempage * 36) - 1)):
                            pygame.draw.rect(DISPLAYSURF, AQUA, rects[clickedrect - ((itempage - 1) * 36)], 6, 10)
                            draw_text(str(itemname[clickedrect]), font24, LIGHTGREEN, DISPLAYSURF, 1270, 365)
                            draw_text_center("stats", font24, BLUE, DISPLAYSURF, 290, 365)
                            draw_text('Hp- ' +str(itemHP[clickedrect]), font24, SKYBLUE, DISPLAYSURF, 230, 425)
                            draw_text("Armor- " +str(itemarmor[clickedrect]), font24, SKYBLUE, DISPLAYSURF, 230, 465)
                            draw_text("Attack- " +str(itemAttack[clickedrect]), font24, SKYBLUE, DISPLAYSURF, 230, 505)
                            draw_text("Spec Att- " +str(itemspecialattack[clickedrect]), font24, SKYBLUE, DISPLAYSURF, 230, 545)
                            draw_text("Speed- " +str(itemspeed[clickedrect]), font24, SKYBLUE, DISPLAYSURF, 230, 585)
                            draw_text("luck- " +str(itemluck[clickedrect]), font24, SKYBLUE, DISPLAYSURF, 230, 625)
                            draw_text_center("Lore", font5, SLEEPPURPLE, DISPLAYSURF, halfdisplay + 5, 940)
                            draw_text_center("Rarity- ", font24, CLOUD, DISPLAYSURF, 1368, 440)

                if helmetrect.collidepoint(mouse_pos):
                    pygame.draw.ellipse(DISPLAYSURF, rainbow, helmetrect, 6)

                if chestplaterect.collidepoint(mouse_pos):
                    pygame.draw.ellipse(DISPLAYSURF, rainbow, chestplaterect, 6)

                if pantsrect.collidepoint(mouse_pos):
                    pygame.draw.ellipse(DISPLAYSURF, rainbow, pantsrect, 6)

                if bootsrect.collidepoint(mouse_pos):
                    pygame.draw.ellipse(DISPLAYSURF, rainbow, bootsrect, 6)

                if jewelry1rect.collidepoint(mouse_pos):
                    pygame.draw.rect(DISPLAYSURF, rainbow, jewelry1rect, 5)

                if jewelry2rect.collidepoint(mouse_pos):
                    pygame.draw.rect(DISPLAYSURF, rainbow, jewelry2rect, 5)

                if weaponrect.collidepoint(mouse_pos):
                    pygame.draw.rect(DISPLAYSURF, rainbow, weaponrect, 5)

                equipeditems = load_teamcreatures("equipeditems.txt")
                if (len(equipeditems) >= 1 and equipeditems[0] != {} and equipmentimages[0] != []):
                    DISPLAYSURF.blit(equipmentimages[0], (600, 364))
                if (len(equipeditems) >= 2 and equipeditems[1] != {} and equipmentimages[1] != []):
                    DISPLAYSURF.blit(equipmentimages[1], (600, 457))
                if (len(equipeditems) >= 3 and equipeditems[2] != {} and equipmentimages[2] != []):
                    DISPLAYSURF.blit(equipmentimages[2], (600, 557))
                if (len(equipeditems) >= 4 and equipeditems[3] != {} and equipmentimages[3] != []):
                    DISPLAYSURF.blit(equipmentimages[3], (600, 652))
                if (len(equipeditems) >= 5 and equipeditems[4] != {} and equipmentimages[4] != []):
                    DISPLAYSURF.blit(equipmentimages[4], (501, 360))
                if (len(equipeditems) >= 6 and equipeditems[5] != {} and equipmentimages[5] != []):
                    DISPLAYSURF.blit(equipmentimages[5], (501, 440))
                if (len(equipeditems) >= 7 and equipeditems[6] != {} and equipmentimages[6] != []):
                    DISPLAYSURF.blit(equipmentimages[6], (499, 533))
                draw_text('x', font4, RED, DISPLAYSURF, 669, 414)
                draw_text('x', font4, RED, DISPLAYSURF, 669, 510)
                draw_text('x', font4, RED, DISPLAYSURF, 669, 610)
                draw_text('x', font4, RED, DISPLAYSURF, 669, 710)
                draw_text('x', font4, RED, DISPLAYSURF, 465, 354)
                draw_text('x', font4, RED, DISPLAYSURF, 469, 428)
                draw_text('x', font4, RED, DISPLAYSURF, 460, 540)

                helmetxrect = pygame.Rect(669, 414, 40, 40)
                chestplatexrect = pygame.Rect(669, 510, 40, 40)
                pantsxrect = pygame.Rect(669, 610, 40, 40)
                bootsxrect = pygame.Rect(669, 710, 40, 40)
                jewelry1xrect = pygame.Rect(465, 354, 40, 40)
                jewelry2xrect = pygame.Rect(469, 428, 40, 40)
                swordxrect = pygame.Rect(460, 540, 40, 40)

                if helmetxrect.collidepoint(mouse_pos):
                    draw_text('x', font4, rainbow, DISPLAYSURF, 669, 414)
                if chestplatexrect.collidepoint(mouse_pos):
                    draw_text('x', font4, rainbow, DISPLAYSURF, 669, 510)
                if pantsxrect.collidepoint(mouse_pos):
                    draw_text('x', font4, rainbow, DISPLAYSURF, 669, 610)
                if bootsxrect.collidepoint(mouse_pos):
                    draw_text('x', font4, rainbow, DISPLAYSURF, 669, 710)
                if jewelry1xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, rainbow, DISPLAYSURF, 465, 354)
                if jewelry2xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, rainbow, DISPLAYSURF, 469, 428)
                if swordxrect.collidepoint(mouse_pos):
                    draw_text('x', font4, rainbow, DISPLAYSURF, 460, 540)
                trashcanrect = pygame.Rect(930, 800, 80, 80)
                if trashcanrect.collidepoint(mouse_pos):
                    pygame.draw.ellipse(DISPLAYSURF, RED, trashcanrect, 4)
                    draw_text_center("click trash can to delete item", font11, rainbow, DISPLAYSURF, halfdisplay,797)

                armoryrect = pygame.Rect(815, 210, 150, 60)
                companionrect = pygame.Rect(975, 210, 150, 60)
                pygame.draw.rect(DISPLAYSURF, rainbow, armoryrect, 5)

                leftarrowrect = pygame.Rect(685, 835, 125, 60)
                rightarrowrect = pygame.Rect(1130, 830, 125, 60)

                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 120, 70)
                if leftarrowrect.collidepoint(mouse_pos):
                    pygame.draw.rect(DISPLAYSURF, ORANGEDESERT, leftarrowrect, 5, 5)
                if rightarrowrect.collidepoint(mouse_pos):
                    pygame.draw.rect(DISPLAYSURF, ORANGEDESERT, rightarrowrect, 5, 5)
                if armoryrect.collidepoint(mouse_pos):
                    pygame.draw.rect(DISPLAYSURF, EMERALD, armoryrect, 5)
                if companionrect.collidepoint(mouse_pos):
                    pygame.draw.rect(DISPLAYSURF, EMERALD, companionrect, 5)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if leftarrowrect.collidepoint(mouse_pos):
                            sound_effect = pygame.mixer.Sound(resource_path("audio/scrollsound.mp3"))
                            sound_effect.play()
                            if (itempage != 1):
                                itempage = itempage - 1
                        if rightarrowrect.collidepoint(mouse_pos):
                            sound_effect = pygame.mixer.Sound(resource_path("audio/scrollsound.mp3"))
                            sound_effect.play()
                            itempage = itempage + 1
                        if returnarrowrect.collidepoint(mouse_pos):
                            video.release()
                            transition(6)
                            self.stashloop = False
                        if armoryrect.collidepoint(mouse_pos):
                            sound_effect = pygame.mixer.Sound(resource_path("audio/pcsound.wav"))
                            sound_effect.play()
                            clickedrect = -1
                            self.gamescene = 2
                        if companionrect.collidepoint(mouse_pos):
                            sound_effect = pygame.mixer.Sound(resource_path("audio/pcsound.wav"))
                            sound_effect.play()
                            clickedrect = -1
                            self.gamescene = 3
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            video.release()
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()
                        if helmetrect.collidepoint(mouse_pos):
                            equipeditems = load_teamcreatures("equipeditems.txt")
                            attributes = list(equipeditems[0].values())
                            if (clickedrect != -1):
                                if (len(equipeditems) >= 1 and (itemname[clickedrect] == "Leather Cap" or itemname[clickedrect] == "Plated Helmet" or itemname[clickedrect] == "Ascendent Helmet")):
                                    if (clickedrect > ((itempage - 1) * 36) - 1) and (
                                            clickedrect <= ((itempage * 36) - 1)):
                                        if(equipeditems[0]):
                                            save_creature(equipeditems[0], "itemdata.txt")
                                            strength = 0
                                            defense = 0
                                            health = 0
                                            speed = 0
                                            specattack = 0
                                            luck = 0
                                            with open(resource_path("gamedata.txt"), "r") as file:
                                                lines = file.readlines()
                                                strength = lines[16].strip()
                                                strength = int(strength[11:])
                                                defense = lines[17].strip()
                                                defense = int(defense[10:])
                                                health = lines[18].strip()
                                                health = int(health[9:])
                                                speed = lines[19].strip()
                                                speed = int(speed[8:])
                                                specattack = lines[20].strip()
                                                specattack = int(specattack[13:])
                                                luck = lines[21].strip()
                                                luck = int(luck[7:])
                                            with open(resource_path("gamedata.txt"), "r") as file:
                                                lines = file.readlines()
                                                lines[16] = (f"strength = {strength - attributes[4]}\n")
                                                lines[17] = (f"defense = {defense - attributes[3]}\n")
                                                lines[18] = (f"health = {health - attributes[2]}\n")
                                                lines[19] = (f"speed = {speed - attributes[6]}\n")
                                                lines[20] = (f"specattack = {specattack - attributes[5]}\n")
                                                lines[21] = (f"luck = {luck - attributes[7]}\n")
                                            with open(resource_path("gamedata.txt"), "w") as file:
                                                file.writelines(lines)
                                        modify_teamcreature(0, {
                                        "name": itemname[clickedrect],
                                        "imagecore": regularimage[clickedrect],
                                        "HP": itemHP[clickedrect],
                                        "armor": itemarmor[clickedrect],
                                        "Attack": itemAttack[clickedrect],
                                        "specialattack": itemspecialattack[clickedrect],
                                        "speed": itemspeed[clickedrect],
                                        "luck": itemluck[clickedrect]}, "equipeditems.txt")
                                        with open(resource_path("gamedata.txt"), "r") as file:
                                            lines = file.readlines()
                                            strength = lines[16].strip()
                                            strength = int(strength[11:])
                                            defense = lines[17].strip()
                                            defense = int(defense[10:])
                                            health = lines[18].strip()
                                            health = int(health[9:])
                                            speed = lines[19].strip()
                                            speed = int(speed[8:])
                                            specattack = lines[20].strip()
                                            specattack = int(specattack[13:])
                                            luck = lines[21].strip()
                                            luck = int(luck[7:])
                                        with open(resource_path("gamedata.txt"), "r") as file:
                                            lines = file.readlines()
                                            lines[16] = (f"strength = {strength + itemAttack[clickedrect]}\n")
                                            lines[17] = (f"defense = {defense + itemarmor[clickedrect]}\n")
                                            lines[18] = (f"health = {health + itemHP[clickedrect]}\n")
                                            lines[19] = (f"speed = {speed + itemspeed[clickedrect]}\n")
                                            lines[20] = (f"specattack = {specattack + itemspecialattack[clickedrect]}\n")
                                            lines[21] = (f"luck = {luck + itemluck[clickedrect]}\n")
                                        with open(resource_path("gamedata.txt"), "w") as file:
                                            file.writelines(lines)
                                        delete_creature_by_index(clickedrect, "itemdata.txt")

                                        itemname.clear()
                                        regularimage.clear()
                                        itemimagecore.clear()
                                        itemHP.clear()
                                        itemarmor.clear()
                                        itemAttack.clear()
                                        itemspecialattack.clear()
                                        itemspeed.clear()
                                        itemluck.clear()

                                        items = load_creatures("itemdata.txt")

                                        for item in items:
                                            attributes = list(item.values())
                                            itemname.append(attributes[0])
                                            regularimage.append(attributes[1])
                                            tempimage = pygame.image.load(attributes[1])
                                            tempimage = pygame.transform.scale(tempimage, (60, 60))
                                            itemimagecore.append(tempimage)
                                            itemHP.append(attributes[2])
                                            itemarmor.append(attributes[3])
                                            itemAttack.append(attributes[4])
                                            itemspecialattack.append(attributes[5])
                                            itemspeed.append(attributes[6])
                                            itemluck.append(attributes[7])

                                        sound_effect = pygame.mixer.Sound(resource_path("audio/swordsound.mp3"))
                                        pygame.mixer.music.set_volume(0.4)
                                        sound_effect.play()
                                        equipmentimages = [[], [], [], [], [], [], []]
                                        equipeditems = load_teamcreatures("equipeditems.txt")
                                        if (len(equipeditems) >= 1 and equipeditems[0] != {}):
                                            attributes = list(equipeditems[0].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[0] = tempimg
                                        if (len(equipeditems) >= 2 and equipeditems[1] != {}):
                                            attributes = list(equipeditems[1].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[1] = tempimg
                                        if (len(equipeditems) >= 3 and equipeditems[2] != {}):
                                            attributes = list(equipeditems[2].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[2] = tempimg
                                        if (len(equipeditems) >= 4 and equipeditems[3] != {}):
                                            attributes = list(equipeditems[3].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[3] = tempimg
                                        if (len(equipeditems) >= 5 and equipeditems[4] != {}):
                                            attributes = list(equipeditems[4].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[4] = tempimg
                                        if (len(equipeditems) >= 6 and equipeditems[5] != {}):
                                            attributes = list(equipeditems[5].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[5] = tempimg
                                        if (len(equipeditems) >= 7 and equipeditems[6] != {}):
                                            attributes = list(equipeditems[6].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[6] = tempimg
                            clickedrect = -1
                        if chestplaterect.collidepoint(mouse_pos):
                            equipeditems = load_teamcreatures("equipeditems.txt")
                            attributes = list(equipeditems[1].values())
                            if (clickedrect != -1):
                                if (len(equipeditems) >= 2 and (itemname[clickedrect] == "Leather Chestplate" or itemname[clickedrect] == "Plated Chestplate" or itemname[clickedrect] == "Ascendent Chestplate")):
                                    if (clickedrect > ((itempage - 1) * 36) - 1) and (
                                            clickedrect <= ((itempage * 36) - 1)):
                                        if(equipeditems[1] != {}):
                                            save_creature(equipeditems[1], "itemdata.txt")
                                            strength = 0
                                            defense = 0
                                            health = 0
                                            speed = 0
                                            specattack = 0
                                            luck = 0
                                            with open(resource_path("gamedata.txt"), "r") as file:
                                                lines = file.readlines()
                                                strength = lines[16].strip()
                                                strength = int(strength[11:])
                                                defense = lines[17].strip()
                                                defense = int(defense[10:])
                                                health = lines[18].strip()
                                                health = int(health[9:])
                                                speed = lines[19].strip()
                                                speed = int(speed[8:])
                                                specattack = lines[20].strip()
                                                specattack = int(specattack[13:])
                                                luck = lines[21].strip()
                                                luck = int(luck[7:])
                                            with open(resource_path("gamedata.txt"), "r") as file:
                                                lines = file.readlines()
                                                lines[16] = (f"strength = {strength - attributes[4]}\n")
                                                lines[17] = (f"defense = {defense - attributes[3]}\n")
                                                lines[18] = (f"health = {health - attributes[2]}\n")
                                                lines[19] = (f"speed = {speed - attributes[6]}\n")
                                                lines[20] = (f"specattack = {specattack - attributes[5]}\n")
                                                lines[21] = (f"luck = {luck - attributes[7]}\n")
                                            with open(resource_path("gamedata.txt"), "w") as file:
                                                file.writelines(lines)
                                        modify_teamcreature(1, {
                                            "name": itemname[clickedrect],
                                            "imagecore": regularimage[clickedrect],
                                            "HP": itemHP[clickedrect],
                                            "armor": itemarmor[clickedrect],
                                            "Attack": itemAttack[clickedrect],
                                            "specialattack": itemspecialattack[clickedrect],
                                            "speed": itemspeed[clickedrect],
                                            "luck": itemluck[clickedrect],
                                        }, resource_path("equipeditems.txt"))
                                        strength = 0
                                        defense = 0
                                        health = 0
                                        speed = 0
                                        specattack = 0
                                        luck = 0
                                        with open(resource_path("gamedata.txt"), "r") as file:
                                            lines = file.readlines()
                                            strength = lines[16].strip()
                                            strength = int(strength[11:])
                                            defense = lines[17].strip()
                                            defense = int(defense[10:])
                                            health = lines[18].strip()
                                            health = int(health[9:])
                                            speed = lines[19].strip()
                                            speed = int(speed[8:])
                                            specattack = lines[20].strip()
                                            specattack = int(specattack[13:])
                                            luck = lines[21].strip()
                                            luck = int(luck[7:])
                                        with open(resource_path("gamedata.txt"), "r") as file:
                                            lines = file.readlines()
                                            lines[16] = (f"strength = {strength + itemAttack[clickedrect]}\n")
                                            lines[17] = (f"defense = {defense + itemarmor[clickedrect]}\n")
                                            lines[18] = (f"health = {health + itemHP[clickedrect]}\n")
                                            lines[19] = (f"speed = {speed + itemspeed[clickedrect]}\n")
                                            lines[20] = (f"specattack = {specattack + itemspecialattack[clickedrect]}\n")
                                            lines[21] = (f"luck = {luck + itemluck[clickedrect]}\n")
                                        with open(resource_path("gamedata.txt"), "w") as file:
                                            file.writelines(lines)
                                        delete_creature_by_index(clickedrect, "itemdata.txt")

                                        itemname.clear()
                                        regularimage.clear()
                                        itemimagecore.clear()
                                        itemHP.clear()
                                        itemarmor.clear()
                                        itemAttack.clear()
                                        itemspecialattack.clear()
                                        itemspeed.clear()
                                        itemluck.clear()

                                        items = load_creatures("itemdata.txt")

                                        for item in items:
                                            attributes = list(item.values())
                                            itemname.append(attributes[0])
                                            regularimage.append(attributes[1])
                                            tempimage = pygame.image.load(resource_path(attributes[1]))
                                            tempimage = pygame.transform.scale(tempimage, (60, 60))
                                            itemimagecore.append(tempimage)
                                            itemHP.append(attributes[2])
                                            itemarmor.append(attributes[3])
                                            itemAttack.append(attributes[4])
                                            itemspecialattack.append(attributes[5])
                                            itemspeed.append(attributes[6])
                                            itemluck.append(attributes[7])

                                        sound_effect = pygame.mixer.Sound(resource_path("audio/swordsound.mp3"))
                                        pygame.mixer.music.set_volume(0.4)
                                        sound_effect.play()
                                        equipmentimages = [[], [], [], [], [], [], []]
                                        equipeditems = load_teamcreatures("equipeditems.txt")
                                        if (len(equipeditems) >= 1 and equipeditems[0] != {}):
                                            attributes = list(equipeditems[0].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[0] = tempimg
                                        if (len(equipeditems) >= 2 and equipeditems[1] != {}):
                                            attributes = list(equipeditems[1].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[1] = tempimg
                                        if (len(equipeditems) >= 3 and equipeditems[2] != {}):
                                            attributes = list(equipeditems[2].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[2] = tempimg
                                        if (len(equipeditems) >= 4 and equipeditems[3] != {}):
                                            attributes = list(equipeditems[3].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[3] = tempimg
                                        if (len(equipeditems) >= 5 and equipeditems[4] != {}):
                                            attributes = list(equipeditems[4].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[4] = tempimg
                                        if (len(equipeditems) >= 6 and equipeditems[5] != {}):
                                            attributes = list(equipeditems[5].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[5] = tempimg
                                        if (len(equipeditems) >= 7 and equipeditems[6] != {}):
                                            attributes = list(equipeditems[6].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[6] = tempimg
                            clickedrect = -1
                        if pantsrect.collidepoint(mouse_pos):
                            equipeditems = load_teamcreatures("equipeditems.txt")
                            attributes = list(equipeditems[2].values())
                            if (clickedrect != -1 and (itemname[clickedrect] == "Leather Greeves" or itemname[clickedrect] == "Plated Greeves" or itemname[clickedrect] == "Ascendent Greeves")):
                                if (len(equipeditems) >= 3):
                                    if (clickedrect > ((itempage - 1) * 36) - 1) and (
                                            clickedrect <= ((itempage * 36) - 1)):
                                        if(equipeditems[2] != {}):
                                            save_creature(equipeditems[2], "itemdata.txt")
                                            strength = 0
                                            defense = 0
                                            health = 0
                                            speed = 0
                                            specattack = 0
                                            luck = 0
                                            with open(resource_path("gamedata.txt"), "r") as file:
                                                lines = file.readlines()
                                                strength = lines[16].strip()
                                                strength = int(strength[11:])
                                                defense = lines[17].strip()
                                                defense = int(defense[10:])
                                                health = lines[18].strip()
                                                health = int(health[9:])
                                                speed = lines[19].strip()
                                                speed = int(speed[8:])
                                                specattack = lines[20].strip()
                                                specattack = int(specattack[13:])
                                                luck = lines[21].strip()
                                                luck = int(luck[7:])
                                            with open(resource_path("gamedata.txt"), "r") as file:
                                                lines = file.readlines()
                                                lines[16] = (f"strength = {strength - attributes[4]}\n")
                                                lines[17] = (f"defense = {defense - attributes[3]}\n")
                                                lines[18] = (f"health = {health - attributes[2]}\n")
                                                lines[19] = (f"speed = {speed - attributes[6]}\n")
                                                lines[20] = (f"specattack = {specattack - attributes[5]}\n")
                                                lines[21] = (f"luck = {luck - attributes[7]}\n")
                                            with open(resource_path("gamedata.txt"), "w") as file:
                                                file.writelines(lines)
                                        modify_teamcreature(2, {
                                            "name": itemname[clickedrect],
                                            "imagecore": regularimage[clickedrect],
                                            "HP": itemHP[clickedrect],
                                            "armor": itemarmor[clickedrect],
                                            "Attack": itemAttack[clickedrect],
                                            "specialattack": itemspecialattack[clickedrect],
                                            "speed": itemspeed[clickedrect],
                                            "luck": itemluck[clickedrect],
                                        }, resource_path("equipeditems.txt"))
                                        strength = 0
                                        defense = 0
                                        health = 0
                                        speed = 0
                                        specattack = 0
                                        luck = 0
                                        with open(resource_path("gamedata.txt"), "r") as file:
                                            lines = file.readlines()
                                            strength = lines[16].strip()
                                            strength = int(strength[11:])
                                            defense = lines[17].strip()
                                            defense = int(defense[10:])
                                            health = lines[18].strip()
                                            health = int(health[9:])
                                            speed = lines[19].strip()
                                            speed = int(speed[8:])
                                            specattack = lines[20].strip()
                                            specattack = int(specattack[13:])
                                            luck = lines[21].strip()
                                            luck = int(luck[7:])
                                        with open(resource_path("gamedata.txt"), "r") as file:
                                            lines = file.readlines()
                                            lines[16] = (f"strength = {strength + itemAttack[clickedrect]}\n")
                                            lines[17] = (f"defense = {defense + itemarmor[clickedrect]}\n")
                                            lines[18] = (f"health = {health + itemHP[clickedrect]}\n")
                                            lines[19] = (f"speed = {speed + itemspeed[clickedrect]}\n")
                                            lines[20] = (f"specattack = {specattack + itemspecialattack[clickedrect]}\n")
                                            lines[21] = (f"luck = {luck + itemluck[clickedrect]}\n")
                                        with open(resource_path("gamedata.txt"), "w") as file:
                                            file.writelines(lines)
                                        delete_creature_by_index(clickedrect, "itemdata.txt")

                                        itemname.clear()
                                        regularimage.clear()
                                        itemimagecore.clear()
                                        itemHP.clear()
                                        itemarmor.clear()
                                        itemAttack.clear()
                                        itemspecialattack.clear()
                                        itemspeed.clear()
                                        itemluck.clear()

                                        items = load_creatures("itemdata.txt")

                                        for item in items:
                                            attributes = list(item.values())
                                            itemname.append(attributes[0])
                                            regularimage.append(attributes[1])
                                            tempimage = pygame.image.load(resource_path(attributes[1]))
                                            tempimage = pygame.transform.scale(tempimage, (60, 60))
                                            itemimagecore.append(tempimage)
                                            itemHP.append(attributes[2])
                                            itemarmor.append(attributes[3])
                                            itemAttack.append(attributes[4])
                                            itemspecialattack.append(attributes[5])
                                            itemspeed.append(attributes[6])
                                            itemluck.append(attributes[7])

                                        sound_effect = pygame.mixer.Sound(resource_path("audio/swordsound.mp3"))
                                        pygame.mixer.music.set_volume(0.4)
                                        sound_effect.play()
                                        equipmentimages = [[], [], [], [], [], [], []]
                                        equipeditems = load_teamcreatures("equipeditems.txt")
                                        if (len(equipeditems) >= 1 and equipeditems[0] != {}):
                                            attributes = list(equipeditems[0].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[0] = tempimg
                                        if (len(equipeditems) >= 2 and equipeditems[1] != {}):
                                            attributes = list(equipeditems[1].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[1] = tempimg
                                        if (len(equipeditems) >= 3 and equipeditems[2] != {}):
                                            attributes = list(equipeditems[2].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[2] = tempimg
                                        if (len(equipeditems) >= 4 and equipeditems[3] != {}):
                                            attributes = list(equipeditems[3].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[3] = tempimg
                                        if (len(equipeditems) >= 5 and equipeditems[4] != {}):
                                            attributes = list(equipeditems[4].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[4] = tempimg
                                        if (len(equipeditems) >= 6 and equipeditems[5] != {}):
                                            attributes = list(equipeditems[5].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[5] = tempimg
                                        if (len(equipeditems) >= 7 and equipeditems[6] != {}):

                                            attributes = list(equipeditems[6].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[6] = tempimg

                            clickedrect = -1
                        if bootsrect.collidepoint(mouse_pos):
                            equipeditems = load_teamcreatures("equipeditems.txt")
                            attributes = list(equipeditems[3].values())
                            if (clickedrect != -1 and (itemname[clickedrect] == "Leather Boots" or itemname[clickedrect] == "Plated Boots" or itemname[clickedrect] == "Ascendent Boots")):
                                if (len(equipeditems) >= 4):
                                    if (clickedrect > ((itempage - 1) * 36) - 1) and (
                                            clickedrect <= ((itempage * 36) - 1)):
                                        if(equipeditems[3] != {}):
                                            save_creature(equipeditems[3], "itemdata.txt")
                                            strength = 0
                                            defense = 0
                                            health = 0
                                            speed = 0
                                            specattack = 0
                                            luck = 0
                                            with open(resource_path("gamedata.txt"), "r") as file:
                                                lines = file.readlines()
                                                strength = lines[16].strip()
                                                strength = int(strength[11:])
                                                defense = lines[17].strip()
                                                defense = int(defense[10:])
                                                health = lines[18].strip()
                                                health = int(health[9:])
                                                speed = lines[19].strip()
                                                speed = int(speed[8:])
                                                specattack = lines[20].strip()
                                                specattack = int(specattack[13:])
                                                luck = lines[21].strip()
                                                luck = int(luck[7:])
                                            with open(resource_path("gamedata.txt"), "r") as file:
                                                lines = file.readlines()
                                                lines[16] = (f"strength = {strength - attributes[4]}\n")
                                                lines[17] = (f"defense = {defense - attributes[3]}\n")
                                                lines[18] = (f"health = {health - attributes[2]}\n")
                                                lines[19] = (f"speed = {speed - attributes[6]}\n")
                                                lines[20] = (f"specattack = {specattack - attributes[5]}\n")
                                                lines[21] = (f"luck = {luck - attributes[7]}\n")
                                            with open(resource_path("gamedata.txt"), "w") as file:
                                                file.writelines(lines)
                                        modify_teamcreature(3, {
                                            "name": itemname[clickedrect],
                                            "imagecore": regularimage[clickedrect],
                                            "HP": itemHP[clickedrect],
                                            "armor": itemarmor[clickedrect],
                                            "Attack": itemAttack[clickedrect],
                                            "specialattack": itemspecialattack[clickedrect],
                                            "speed": itemspeed[clickedrect],
                                            "luck": itemluck[clickedrect],
                                        }, resource_path("equipeditems.txt"))
                                        strength = 0
                                        defense = 0
                                        health = 0
                                        speed = 0
                                        specattack = 0
                                        luck = 0
                                        with open(resource_path("gamedata.txt"), "r") as file:
                                            lines = file.readlines()
                                            strength = lines[16].strip()
                                            strength = int(strength[11:])
                                            defense = lines[17].strip()
                                            defense = int(defense[10:])
                                            health = lines[18].strip()
                                            health = int(health[9:])
                                            speed = lines[19].strip()
                                            speed = int(speed[8:])
                                            specattack = lines[20].strip()
                                            specattack = int(specattack[13:])
                                            luck = lines[21].strip()
                                            luck = int(luck[7:])
                                        with open(resource_path("gamedata.txt"), "r") as file:
                                            lines = file.readlines()
                                            lines[16] = (f"strength = {strength + itemAttack[clickedrect]}\n")
                                            lines[17] = (f"defense = {defense + itemarmor[clickedrect]}\n")
                                            lines[18] = (f"health = {health + itemHP[clickedrect]}\n")
                                            lines[19] = (f"speed = {speed + itemspeed[clickedrect]}\n")
                                            lines[20] = (f"specattack = {specattack + itemspecialattack[clickedrect]}\n")
                                            lines[21] = (f"luck = {luck + itemluck[clickedrect]}\n")
                                        with open(resource_path("gamedata.txt"), "w") as file:
                                            file.writelines(lines)
                                        delete_creature_by_index(clickedrect, "itemdata.txt")

                                        itemname.clear()
                                        regularimage.clear()
                                        itemimagecore.clear()
                                        itemHP.clear()
                                        itemarmor.clear()
                                        itemAttack.clear()
                                        itemspecialattack.clear()
                                        itemspeed.clear()
                                        itemluck.clear()

                                        items = load_creatures("itemdata.txt")

                                        for item in items:
                                            attributes = list(item.values())
                                            itemname.append(attributes[0])
                                            regularimage.append(attributes[1])
                                            tempimage = pygame.image.load(resource_path(attributes[1]))
                                            tempimage = pygame.transform.scale(tempimage, (60, 60))
                                            itemimagecore.append(tempimage)
                                            itemHP.append(attributes[2])
                                            itemarmor.append(attributes[3])
                                            itemAttack.append(attributes[4])
                                            itemspecialattack.append(attributes[5])
                                            itemspeed.append(attributes[6])
                                            itemluck.append(attributes[7])

                                        sound_effect = pygame.mixer.Sound(resource_path("audio/swordsound.mp3"))
                                        pygame.mixer.music.set_volume(0.4)
                                        sound_effect.play()
                                        equipmentimages = [[], [], [], [], [], [], []]
                                        equipeditems = load_teamcreatures("equipeditems.txt")
                                        if (len(equipeditems) >= 1 and equipeditems[0] != {}):
                                            attributes = list(equipeditems[0].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[0] = tempimg
                                        if (len(equipeditems) >= 2 and equipeditems[1] != {}):
                                            attributes = list(equipeditems[1].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[1] = tempimg
                                        if (len(equipeditems) >= 3 and equipeditems[2] != {}):
                                            attributes = list(equipeditems[2].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[2] = tempimg
                                        if (len(equipeditems) >= 4 and equipeditems[3] != {}):
                                            attributes = list(equipeditems[3].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[3] = tempimg
                                        if (len(equipeditems) >= 5 and equipeditems[4] != {}):
                                            attributes = list(equipeditems[4].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[4] = tempimg
                                        if (len(equipeditems) >= 6 and equipeditems[5] != {}):
                                            attributes = list(equipeditems[5].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[5] = tempimg
                                        if (len(equipeditems) >= 7 and equipeditems[6] != {}):

                                            attributes = list(equipeditems[6].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[6] = tempimg

                            clickedrect = -1
                        if jewelry1rect.collidepoint(mouse_pos):
                            equipeditems = load_teamcreatures("equipeditems.txt")
                            attributes = list(equipeditems[4].values())
                            if (clickedrect != -1 and (itemname[clickedrect] == "Aqua Amulet" or itemname[clickedrect] == "Lava Amulet" or itemname[clickedrect] == "Amulet of Heaven" or itemname[clickedrect] == "Lost Crown")):
                                if (len(equipeditems) >= 5):
                                    if (clickedrect > ((itempage - 1) * 36) - 1) and (
                                            clickedrect <= ((itempage * 36) - 1)):
                                        if(equipeditems[4] != {}):
                                            save_creature(equipeditems[4], "itemdata.txt")
                                            strength = 0
                                            defense = 0
                                            health = 0
                                            speed = 0
                                            specattack = 0
                                            luck = 0
                                            with open(resource_path("gamedata.txt"), "r") as file:
                                                lines = file.readlines()
                                                strength = lines[16].strip()
                                                strength = int(strength[11:])
                                                defense = lines[17].strip()
                                                defense = int(defense[10:])
                                                health = lines[18].strip()
                                                health = int(health[9:])
                                                speed = lines[19].strip()
                                                speed = int(speed[8:])
                                                specattack = lines[20].strip()
                                                specattack = int(specattack[13:])
                                                luck = lines[21].strip()
                                                luck = int(luck[7:])
                                            with open(resource_path("gamedata.txt"), "r") as file:
                                                lines = file.readlines()
                                                lines[16] = (f"strength = {strength - attributes[4]}\n")
                                                lines[17] = (f"defense = {defense - attributes[3]}\n")
                                                lines[18] = (f"health = {health - attributes[2]}\n")
                                                lines[19] = (f"speed = {speed - attributes[6]}\n")
                                                lines[20] = (f"specattack = {specattack - attributes[5]}\n")
                                                lines[21] = (f"luck = {luck - attributes[7]}\n")
                                            with open(resource_path("gamedata.txt"), "w") as file:
                                                file.writelines(lines)
                                        modify_teamcreature(4, {
                                            "name": itemname[clickedrect],
                                            "imagecore": regularimage[clickedrect],
                                            "HP": itemHP[clickedrect],
                                            "armor": itemarmor[clickedrect],
                                            "Attack": itemAttack[clickedrect],
                                            "specialattack": itemspecialattack[clickedrect],
                                            "speed": itemspeed[clickedrect],
                                            "luck": itemluck[clickedrect],
                                        }, resource_path("equipeditems.txt"))
                                        strength = 0
                                        defense = 0
                                        health = 0
                                        speed = 0
                                        specattack = 0
                                        luck = 0
                                        with open(resource_path("gamedata.txt"), "r") as file:
                                            lines = file.readlines()
                                            strength = lines[16].strip()
                                            strength = int(strength[11:])
                                            defense = lines[17].strip()
                                            defense = int(defense[10:])
                                            health = lines[18].strip()
                                            health = int(health[9:])
                                            speed = lines[19].strip()
                                            speed = int(speed[8:])
                                            specattack = lines[20].strip()
                                            specattack = int(specattack[13:])
                                            luck = lines[21].strip()
                                            luck = int(luck[7:])
                                        with open(resource_path("gamedata.txt"), "r") as file:
                                            lines = file.readlines()
                                            lines[16] = (f"strength = {strength + itemAttack[clickedrect]}\n")
                                            lines[17] = (f"defense = {defense + itemarmor[clickedrect]}\n")
                                            lines[18] = (f"health = {health + itemHP[clickedrect]}\n")
                                            lines[19] = (f"speed = {speed + itemspeed[clickedrect]}\n")
                                            lines[20] = (f"specattack = {specattack + itemspecialattack[clickedrect]}\n")
                                            lines[21] = (f"luck = {luck + itemluck[clickedrect]}\n")
                                        with open(resource_path("gamedata.txt"), "w") as file:
                                            file.writelines(lines)
                                        delete_creature_by_index(clickedrect, "itemdata.txt")

                                        itemname.clear()
                                        regularimage.clear()
                                        itemimagecore.clear()
                                        itemHP.clear()
                                        itemarmor.clear()
                                        itemAttack.clear()
                                        itemspecialattack.clear()
                                        itemspeed.clear()
                                        itemluck.clear()

                                        items = load_creatures("itemdata.txt")

                                        for item in items:
                                            attributes = list(item.values())
                                            itemname.append(attributes[0])
                                            regularimage.append(attributes[1])
                                            tempimage = pygame.image.load(resource_path(attributes[1]))
                                            tempimage = pygame.transform.scale(tempimage, (60, 60))
                                            itemimagecore.append(tempimage)
                                            itemHP.append(attributes[2])
                                            itemarmor.append(attributes[3])
                                            itemAttack.append(attributes[4])
                                            itemspecialattack.append(attributes[5])
                                            itemspeed.append(attributes[6])
                                            itemluck.append(attributes[7])

                                        sound_effect = pygame.mixer.Sound(resource_path("audio/swordsound.mp3"))
                                        pygame.mixer.music.set_volume(0.4)
                                        sound_effect.play()
                                        equipmentimages = [[], [], [], [], [], [], []]
                                        equipeditems = load_teamcreatures("equipeditems.txt")
                                        if (len(equipeditems) >= 1 and equipeditems[0] != {}):
                                            attributes = list(equipeditems[0].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[0] = tempimg
                                        if (len(equipeditems) >= 2 and equipeditems[1] != {}):
                                            attributes = list(equipeditems[1].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[1] = tempimg
                                        if (len(equipeditems) >= 3 and equipeditems[2] != {}):
                                            attributes = list(equipeditems[2].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[2] = tempimg
                                        if (len(equipeditems) >= 4 and equipeditems[3] != {}):
                                            attributes = list(equipeditems[3].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[3] = tempimg
                                        if (len(equipeditems) >= 5 and equipeditems[4] != {}):
                                            attributes = list(equipeditems[4].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[4] = tempimg
                                        if (len(equipeditems) >= 6 and equipeditems[5] != {}):
                                            attributes = list(equipeditems[5].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[5] = tempimg
                                        if (len(equipeditems) >= 7 and equipeditems[6] != {}):

                                            attributes = list(equipeditems[6].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[6] = tempimg

                            clickedrect = -1
                        if jewelry2rect.collidepoint(mouse_pos):
                            equipeditems = load_teamcreatures("equipeditems.txt")
                            attributes = list(equipeditems[5].values())
                            if (clickedrect != -1 and (itemname[clickedrect] == "Aqua Amulet" or itemname[clickedrect] == "Lava Amulet" or itemname[clickedrect] == "Amulet of Heaven" or itemname[clickedrect] == "Lost Crown")):
                                if (len(equipeditems) >= 6):
                                    if (clickedrect > ((itempage - 1) * 36) - 1) and (
                                            clickedrect <= ((itempage * 36) - 1)):
                                        if(equipeditems[5] != {}):
                                            save_creature(equipeditems[5], "itemdata.txt")
                                            strength = 0
                                            defense = 0
                                            health = 0
                                            speed = 0
                                            specattack = 0
                                            luck = 0
                                            with open(resource_path("gamedata.txt"), "r") as file:
                                                lines = file.readlines()
                                                strength = lines[16].strip()
                                                strength = int(strength[11:])
                                                defense = lines[17].strip()
                                                defense = int(defense[10:])
                                                health = lines[18].strip()
                                                health = int(health[9:])
                                                speed = lines[19].strip()
                                                speed = int(speed[8:])
                                                specattack = lines[20].strip()
                                                specattack = int(specattack[13:])
                                                luck = lines[21].strip()
                                                luck = int(luck[7:])
                                            with open(resource_path("gamedata.txt"), "r") as file:
                                                lines = file.readlines()
                                                lines[16] = (f"strength = {strength - attributes[4]}\n")
                                                lines[17] = (f"defense = {defense - attributes[3]}\n")
                                                lines[18] = (f"health = {health - attributes[2]}\n")
                                                lines[19] = (f"speed = {speed - attributes[6]}\n")
                                                lines[20] = (f"specattack = {specattack - attributes[5]}\n")
                                                lines[21] = (f"luck = {luck - attributes[7]}\n")
                                            with open(resource_path("gamedata.txt"), "w") as file:
                                                file.writelines(lines)
                                        modify_teamcreature(5, {
                                            "name": itemname[clickedrect],
                                            "imagecore": regularimage[clickedrect],
                                            "HP": itemHP[clickedrect],
                                            "armor": itemarmor[clickedrect],
                                            "Attack": itemAttack[clickedrect],
                                            "specialattack": itemspecialattack[clickedrect],
                                            "speed": itemspeed[clickedrect],
                                            "luck": itemluck[clickedrect],
                                        }, resource_path("equipeditems.txt"))
                                        strength = 0
                                        defense = 0
                                        health = 0
                                        speed = 0
                                        specattack = 0
                                        luck = 0
                                        with open(resource_path("gamedata.txt"), "r") as file:
                                            lines = file.readlines()
                                            strength = lines[16].strip()
                                            strength = int(strength[11:])
                                            defense = lines[17].strip()
                                            defense = int(defense[10:])
                                            health = lines[18].strip()
                                            health = int(health[9:])
                                            speed = lines[19].strip()
                                            speed = int(speed[8:])
                                            specattack = lines[20].strip()
                                            specattack = int(specattack[13:])
                                            luck = lines[21].strip()
                                            luck = int(luck[7:])
                                        with open(resource_path("gamedata.txt"), "r") as file:
                                            lines = file.readlines()
                                            lines[16] = (f"strength = {strength + itemAttack[clickedrect]}\n")
                                            lines[17] = (f"defense = {defense + itemarmor[clickedrect]}\n")
                                            lines[18] = (f"health = {health + itemHP[clickedrect]}\n")
                                            lines[19] = (f"speed = {speed + itemspeed[clickedrect]}\n")
                                            lines[20] = (f"specattack = {specattack + itemspecialattack[clickedrect]}\n")
                                            lines[21] = (f"luck = {luck + itemluck[clickedrect]}\n")
                                        with open(resource_path("gamedata.txt"), "w") as file:
                                            file.writelines(lines)
                                        delete_creature_by_index(clickedrect, "itemdata.txt")

                                        itemname.clear()
                                        regularimage.clear()
                                        itemimagecore.clear()
                                        itemHP.clear()
                                        itemarmor.clear()
                                        itemAttack.clear()
                                        itemspecialattack.clear()
                                        itemspeed.clear()
                                        itemluck.clear()

                                        items = load_creatures("itemdata.txt")

                                        for item in items:
                                            attributes = list(item.values())
                                            itemname.append(attributes[0])
                                            regularimage.append(attributes[1])
                                            tempimage = pygame.image.load(resource_path(attributes[1]))
                                            tempimage = pygame.transform.scale(tempimage, (60, 60))
                                            itemimagecore.append(tempimage)
                                            itemHP.append(attributes[2])
                                            itemarmor.append(attributes[3])
                                            itemAttack.append(attributes[4])
                                            itemspecialattack.append(attributes[5])
                                            itemspeed.append(attributes[6])
                                            itemluck.append(attributes[7])

                                        sound_effect = pygame.mixer.Sound(resource_path("audio/swordsound.mp3"))
                                        pygame.mixer.music.set_volume(0.4)
                                        sound_effect.play()
                                        equipmentimages = [[], [], [], [], [], [], []]
                                        equipeditems = load_teamcreatures("equipeditems.txt")
                                        if (len(equipeditems) >= 1 and equipeditems[0] != {}):
                                            attributes = list(equipeditems[0].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[0] = tempimg
                                        if (len(equipeditems) >= 2 and equipeditems[1] != {}):
                                            attributes = list(equipeditems[1].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[1] = tempimg
                                        if (len(equipeditems) >= 3 and equipeditems[2] != {}):
                                            attributes = list(equipeditems[2].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[2] = tempimg
                                        if (len(equipeditems) >= 4 and equipeditems[3] != {}):
                                            attributes = list(equipeditems[3].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[3] = tempimg
                                        if (len(equipeditems) >= 5 and equipeditems[4] != {}):
                                            attributes = list(equipeditems[4].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[4] = tempimg
                                        if (len(equipeditems) >= 6 and equipeditems[5] != {}):
                                            attributes = list(equipeditems[5].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[5] = tempimg
                                        if (len(equipeditems) >= 7 and equipeditems[6] != {}):

                                            attributes = list(equipeditems[6].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[6] = tempimg

                            clickedrect = -1
                        if weaponrect.collidepoint(mouse_pos):
                            equipeditems = load_teamcreatures("equipeditems.txt")
                            attributes = list(equipeditems[6].values())
                            if (clickedrect != -1 and (itemname[clickedrect] == "Rusty Sword" or itemname[clickedrect] == "Bronze Sword" or itemname[clickedrect] == "Silverline Sword" or itemname[clickedrect] == "Adamantine Sword" or itemname[clickedrect] == "Simple Staff")):
                                if (len(equipeditems) >= 7):
                                    if (clickedrect > ((itempage - 1) * 36) - 1) and (
                                            clickedrect <= ((itempage * 36) - 1)):
                                        if(equipeditems[6] != {}):
                                            print("Why is this not wokring")
                                            save_creature(equipeditems[6], "itemdata.txt")
                                            strength = 0
                                            defense = 0
                                            health = 0
                                            speed = 0
                                            specattack = 0
                                            luck = 0
                                            with open(resource_path("gamedata.txt"), "r") as file:
                                                lines = file.readlines()
                                                strength = lines[16].strip()
                                                strength = int(strength[11:])
                                                defense = lines[17].strip()
                                                defense = int(defense[10:])
                                                health = lines[18].strip()
                                                health = int(health[9:])
                                                speed = lines[19].strip()
                                                speed = int(speed[8:])
                                                specattack = lines[20].strip()
                                                specattack = int(specattack[13:])
                                                luck = lines[21].strip()
                                                luck = int(luck[7:])
                                            with open(resource_path("gamedata.txt"), "r") as file:
                                                lines = file.readlines()
                                                lines[16] = (f"strength = {strength - attributes[4]}\n")
                                                lines[17] = (f"defense = {defense - attributes[3]}\n")
                                                lines[18] = (f"health = {health - attributes[2]}\n")
                                                lines[19] = (f"speed = {speed - attributes[6]}\n")
                                                lines[20] = (f"specattack = {specattack - attributes[5]}\n")
                                                lines[21] = (f"luck = {luck - attributes[7]}\n")
                                            with open(resource_path("gamedata.txt"), "w") as file:
                                                file.writelines(lines)
                                        modify_teamcreature(6, {
                                            "name": itemname[clickedrect],
                                            "imagecore": regularimage[clickedrect],
                                            "HP": itemHP[clickedrect],
                                            "armor": itemarmor[clickedrect],
                                            "Attack": itemAttack[clickedrect],
                                            "specialattack": itemspecialattack[clickedrect],
                                            "speed": itemspeed[clickedrect],
                                            "luck": itemluck[clickedrect],
                                        }, resource_path("equipeditems.txt"))
                                        strength = 0
                                        defense = 0
                                        health = 0
                                        speed = 0
                                        specattack = 0
                                        luck = 0
                                        with open(resource_path("gamedata.txt"), "r") as file:
                                            lines = file.readlines()
                                            strength = lines[16].strip()
                                            strength = int(strength[11:])
                                            defense = lines[17].strip()
                                            defense = int(defense[10:])
                                            health = lines[18].strip()
                                            health = int(health[9:])
                                            speed = lines[19].strip()
                                            speed = int(speed[8:])
                                            specattack = lines[20].strip()
                                            specattack = int(specattack[13:])
                                            luck = lines[21].strip()
                                            luck = int(luck[7:])
                                        with open(resource_path("gamedata.txt"), "r") as file:
                                            lines = file.readlines()
                                            lines[16] = (f"strength = {strength + itemAttack[clickedrect]}\n")
                                            lines[17] = (f"defense = {defense + itemarmor[clickedrect]}\n")
                                            lines[18] = (f"health = {health + itemHP[clickedrect]}\n")
                                            lines[19] = (f"speed = {speed + itemspeed[clickedrect]}\n")
                                            lines[20] = (f"specattack = {specattack + itemspecialattack[clickedrect]}\n")
                                            lines[21] = (f"luck = {luck + itemluck[clickedrect]}\n")
                                        with open(resource_path("gamedata.txt"), "w") as file:
                                            file.writelines(lines)
                                        delete_creature_by_index(clickedrect, "itemdata.txt")

                                        itemname.clear()
                                        regularimage.clear()
                                        itemimagecore.clear()
                                        itemHP.clear()
                                        itemarmor.clear()
                                        itemAttack.clear()
                                        itemspecialattack.clear()
                                        itemspeed.clear()
                                        itemluck.clear()

                                        items = load_creatures("itemdata.txt")

                                        for item in items:
                                            attributes = list(item.values())
                                            itemname.append(attributes[0])
                                            regularimage.append(attributes[1])
                                            tempimage = pygame.image.load(resource_path(attributes[1]))
                                            tempimage = pygame.transform.scale(tempimage, (60, 60))
                                            itemimagecore.append(tempimage)
                                            itemHP.append(attributes[2])
                                            itemarmor.append(attributes[3])
                                            itemAttack.append(attributes[4])
                                            itemspecialattack.append(attributes[5])
                                            itemspeed.append(attributes[6])
                                            itemluck.append(attributes[7])

                                        sound_effect = pygame.mixer.Sound(resource_path("audio/swordsound.mp3"))
                                        pygame.mixer.music.set_volume(0.4)
                                        sound_effect.play()
                                        equipmentimages = [[], [], [], [], [], [], []]
                                        equipeditems = load_teamcreatures("equipeditems.txt")
                                        if (len(equipeditems) >= 1 and equipeditems[0] != {}):
                                            attributes = list(equipeditems[0].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[0] = tempimg
                                        if (len(equipeditems) >= 2 and equipeditems[1] != {}):
                                            attributes = list(equipeditems[1].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[1] = tempimg
                                        if (len(equipeditems) >= 3 and equipeditems[2] != {}):
                                            attributes = list(equipeditems[2].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[2] = tempimg
                                        if (len(equipeditems) >= 4 and equipeditems[3] != {}):
                                            attributes = list(equipeditems[3].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[3] = tempimg
                                        if (len(equipeditems) >= 5 and equipeditems[4] != {}):
                                            attributes = list(equipeditems[4].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[4] = tempimg
                                        if (len(equipeditems) >= 6 and equipeditems[5] != {}):
                                            attributes = list(equipeditems[5].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[5] = tempimg
                                        if (len(equipeditems) >= 7 and equipeditems[6] != {}):
                                            attributes = list(equipeditems[6].values())
                                            tempimg = pygame.image.load(resource_path(attributes[1]))
                                            tempimg = pygame.transform.scale(tempimg, (60, 60))
                                            equipmentimages[6] = tempimg

                            clickedrect = -1
                        if helmetxrect.collidepoint(mouse_pos):
                            equipeditems = load_teamcreatures("equipeditems.txt")
                            sound_effect = pygame.mixer.Sound(resource_path("audio/scifinoise.mp3"))
                            sound_effect.play()
                            if (len(equipeditems) >= 1 and equipeditems[0] != {}):
                                save_creature(equipeditems[0], "itemdata.txt")
                                equipeditems = load_teamcreatures("equipeditems.txt")
                                attributes = list(equipeditems[0].values())
                                strength = 0
                                defense = 0
                                health = 0
                                speed = 0
                                specattack = 0
                                luck = 0
                                with open(resource_path("gamedata.txt"), "r") as file:
                                    lines = file.readlines()
                                    strength = lines[16].strip()
                                    strength = int(strength[11:])
                                    defense = lines[17].strip()
                                    defense = int(defense[10:])
                                    health = lines[18].strip()
                                    health = int(health[9:])
                                    speed = lines[19].strip()
                                    speed = int(speed[8:])
                                    specattack = lines[20].strip()
                                    specattack = int(specattack[13:])
                                    luck = lines[21].strip()
                                    luck = int(luck[7:])
                                with open(resource_path("gamedata.txt"), "r") as file:
                                    lines = file.readlines()
                                    lines[16] = (f"strength = {strength - attributes[4]}\n")
                                    lines[17] = (f"defense = {defense - attributes[3]}\n")
                                    lines[18] = (f"health = {health - attributes[2]}\n")
                                    lines[19] = (f"speed = {speed - attributes[6]}\n")
                                    lines[20] = (f"specattack = {specattack - attributes[5]}\n")
                                    lines[21] = (f"luck = {luck - attributes[7]}\n")
                                with open(resource_path("gamedata.txt"), "w") as file:
                                    file.writelines(lines)
                                itemname.clear()
                                regularimage.clear()
                                itemimagecore.clear()
                                itemHP.clear()
                                itemarmor.clear()
                                itemAttack.clear()
                                itemspecialattack.clear()
                                itemspeed.clear()
                                itemluck.clear()

                                items = load_creatures("itemdata.txt")

                                for item in items:
                                    attributes = list(item.values())
                                    itemname.append(attributes[0])
                                    regularimage.append(attributes[1])
                                    tempimage = pygame.image.load(resource_path(attributes[1]))
                                    tempimage = pygame.transform.scale(tempimage, (60, 60))
                                    itemimagecore.append(tempimage)
                                    itemHP.append(attributes[2])
                                    itemarmor.append(attributes[3])
                                    itemAttack.append(attributes[4])
                                    itemspecialattack.append(attributes[5])
                                    itemspeed.append(attributes[6])
                                    itemluck.append(attributes[7])
                                clickedrect = -1
                                empty_item(0, "equipeditems.txt")
                                equipmentimages = [[], [], [], [], [], [], []]
                                equipeditems = load_teamcreatures("equipeditems.txt")
                                if (len(equipeditems) >= 1 and equipeditems[0] != {}):
                                    attributes = list(equipeditems[0].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[0] = tempimg
                                if (len(equipeditems) >= 2 and equipeditems[1] != {}):
                                    attributes = list(equipeditems[1].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[1] = tempimg
                                if (len(equipeditems) >= 3 and equipeditems[2] != {}):
                                    attributes = list(equipeditems[2].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[2] = tempimg
                                if (len(equipeditems) >= 4 and equipeditems[3] != {}):
                                    attributes = list(equipeditems[3].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[3] = tempimg
                                if (len(equipeditems) >= 5 and equipeditems[4] != {}):
                                    attributes = list(equipeditems[4].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[4] = tempimg
                                if (len(equipeditems) >= 6 and equipeditems[5] != {}):
                                    attributes = list(equipeditems[5].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[5] = tempimg
                                if (len(equipeditems) >= 7 and equipeditems[6] != {}):

                                    attributes = list(equipeditems[6].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[6] = tempimg
                        if chestplatexrect.collidepoint(mouse_pos):
                            sound_effect = pygame.mixer.Sound(resource_path("audio/scifinoise.mp3"))
                            sound_effect.play()
                            equipeditems = load_teamcreatures("equipeditems.txt")
                            if (len(equipeditems) >= 2 and equipeditems[1] != {}):
                                save_creature(equipeditems[1], "itemdata.txt")
                                equipeditems = load_teamcreatures("equipeditems.txt")
                                attributes = list(equipeditems[1].values())
                                strength = 0
                                defense = 0
                                health = 0
                                speed = 0
                                specattack = 0
                                luck = 0
                                with open(resource_path("gamedata.txt"), "r") as file:
                                    lines = file.readlines()
                                    strength = lines[16].strip()
                                    strength = int(strength[11:])
                                    defense = lines[17].strip()
                                    defense = int(defense[10:])
                                    health = lines[18].strip()
                                    health = int(health[9:])
                                    speed = lines[19].strip()
                                    speed = int(speed[8:])
                                    specattack = lines[20].strip()
                                    specattack = int(specattack[13:])
                                    luck = lines[21].strip()
                                    luck = int(luck[7:])
                                with open(resource_path("gamedata.txt"), "r") as file:
                                    lines = file.readlines()
                                    lines[16] = (f"strength = {strength - attributes[4]}\n")
                                    lines[17] = (f"defense = {defense - attributes[3]}\n")
                                    lines[18] = (f"health = {health - attributes[2]}\n")
                                    lines[19] = (f"speed = {speed - attributes[6]}\n")
                                    lines[20] = (f"specattack = {specattack - attributes[5]}\n")
                                    lines[21] = (f"luck = {luck - attributes[7]}\n")
                                with open(resource_path("gamedata.txt"), "w") as file:
                                    file.writelines(lines)
                                itemname.clear()
                                regularimage.clear()
                                itemimagecore.clear()
                                itemHP.clear()
                                itemarmor.clear()
                                itemAttack.clear()
                                itemspecialattack.clear()
                                itemspeed.clear()
                                itemluck.clear()

                                items = load_creatures("itemdata.txt")

                                for item in items:
                                    attributes = list(item.values())
                                    itemname.append(attributes[0])
                                    regularimage.append(attributes[1])
                                    tempimage = pygame.image.load(resource_path(attributes[1]))
                                    tempimage = pygame.transform.scale(tempimage, (60, 60))
                                    itemimagecore.append(tempimage)
                                    itemHP.append(attributes[2])
                                    itemarmor.append(attributes[3])
                                    itemAttack.append(attributes[4])
                                    itemspecialattack.append(attributes[5])
                                    itemspeed.append(attributes[6])
                                    itemluck.append(attributes[7])
                                clickedrect = -1
                                empty_item(1, "equipeditems.txt")
                                equipmentimages = [[], [], [], [], [], [], []]
                                equipeditems = load_teamcreatures("equipeditems.txt")
                                if (len(equipeditems) >= 1 and equipeditems[0] != {}):
                                    attributes = list(equipeditems[0].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[0] = tempimg
                                if (len(equipeditems) >= 2 and equipeditems[1] != {}):
                                    attributes = list(equipeditems[1].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[1] = tempimg
                                if (len(equipeditems) >= 3 and equipeditems[2] != {}):
                                    attributes = list(equipeditems[2].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[2] = tempimg
                                if (len(equipeditems) >= 4 and equipeditems[3] != {}):
                                    attributes = list(equipeditems[3].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[3] = tempimg
                                if (len(equipeditems) >= 5 and equipeditems[4] != {}):
                                    attributes = list(equipeditems[4].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[4] = tempimg
                                if (len(equipeditems) >= 6 and equipeditems[5] != {}):
                                    attributes = list(equipeditems[5].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[5] = tempimg
                                if (len(equipeditems) >= 7 and equipeditems[6] != {}):

                                    attributes = list(equipeditems[6].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[6] = tempimg
                        if pantsxrect.collidepoint(mouse_pos):
                            sound_effect = pygame.mixer.Sound(resource_path("audio/scifinoise.mp3"))
                            sound_effect.play()
                            equipeditems = load_teamcreatures("equipeditems.txt")
                            if (len(equipeditems) >= 3 and equipeditems[2] != {}):
                                save_creature(equipeditems[2], "itemdata.txt")
                                equipeditems = load_teamcreatures("equipeditems.txt")
                                attributes = list(equipeditems[2].values())
                                strength = 0
                                defense = 0
                                health = 0
                                speed = 0
                                specattack = 0
                                luck = 0
                                with open(resource_path("gamedata.txt"), "r") as file:
                                    lines = file.readlines()
                                    strength = lines[16].strip()
                                    strength = int(strength[11:])
                                    defense = lines[17].strip()
                                    defense = int(defense[10:])
                                    health = lines[18].strip()
                                    health = int(health[9:])
                                    speed = lines[19].strip()
                                    speed = int(speed[8:])
                                    specattack = lines[20].strip()
                                    specattack = int(specattack[13:])
                                    luck = lines[21].strip()
                                    luck = int(luck[7:])
                                with open(resource_path("gamedata.txt"), "r") as file:
                                    lines = file.readlines()
                                    lines[16] = (f"strength = {strength - attributes[4]}\n")
                                    lines[17] = (f"defense = {defense - attributes[3]}\n")
                                    lines[18] = (f"health = {health - attributes[2]}\n")
                                    lines[19] = (f"speed = {speed - attributes[6]}\n")
                                    lines[20] = (f"specattack = {specattack - attributes[5]}\n")
                                    lines[21] = (f"luck = {luck - attributes[7]}\n")
                                with open(resource_path("gamedata.txt"), "w") as file:
                                    file.writelines(lines)
                                itemname.clear()
                                regularimage.clear()
                                itemimagecore.clear()
                                itemHP.clear()
                                itemarmor.clear()
                                itemAttack.clear()
                                itemspecialattack.clear()
                                itemspeed.clear()
                                itemluck.clear()

                                items = load_creatures("itemdata.txt")

                                for item in items:
                                    attributes = list(item.values())
                                    itemname.append(attributes[0])
                                    regularimage.append(attributes[1])
                                    tempimage = pygame.image.load(resource_path(attributes[1]))
                                    tempimage = pygame.transform.scale(tempimage, (60, 60))
                                    itemimagecore.append(tempimage)
                                    itemHP.append(attributes[2])
                                    itemarmor.append(attributes[3])
                                    itemAttack.append(attributes[4])
                                    itemspecialattack.append(attributes[5])
                                    itemspeed.append(attributes[6])
                                    itemluck.append(attributes[7])
                                clickedrect = -1
                                empty_item(2, "equipeditems.txt")
                                equipmentimages = [[], [], [], [], [], [], []]
                                equipeditems = load_teamcreatures("equipeditems.txt")
                                if (len(equipeditems) >= 1 and equipeditems[0] != {}):
                                    attributes = list(equipeditems[0].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[0] = tempimg
                                if (len(equipeditems) >= 2 and equipeditems[1] != {}):
                                    attributes = list(equipeditems[1].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[1] = tempimg
                                if (len(equipeditems) >= 3 and equipeditems[2] != {}):
                                    attributes = list(equipeditems[2].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[2] = tempimg
                                if (len(equipeditems) >= 4 and equipeditems[3] != {}):
                                    attributes = list(equipeditems[3].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[3] = tempimg
                                if (len(equipeditems) >= 5 and equipeditems[4] != {}):
                                    attributes = list(equipeditems[4].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[4] = tempimg
                                if (len(equipeditems) >= 6 and equipeditems[5] != {}):
                                    attributes = list(equipeditems[5].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[5] = tempimg
                                if (len(equipeditems) >= 7 and equipeditems[6] != {}):

                                    attributes = list(equipeditems[6].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[6] = tempimg
                        if bootsxrect.collidepoint(mouse_pos):
                            equipeditems = load_teamcreatures("equipeditems.txt")
                            sound_effect = pygame.mixer.Sound(resource_path("audio/scifinoise.mp3"))
                            sound_effect.play()
                            if (len(equipeditems) >= 4 and equipeditems[3] != {}):
                                save_creature(equipeditems[3], "itemdata.txt")
                                equipeditems = load_teamcreatures("equipeditems.txt")
                                attributes = list(equipeditems[3].values())
                                strength = 0
                                defense = 0
                                health = 0
                                speed = 0
                                specattack = 0
                                luck = 0
                                with open(resource_path("gamedata.txt"), "r") as file:
                                    lines = file.readlines()
                                    strength = lines[16].strip()
                                    strength = int(strength[11:])
                                    defense = lines[17].strip()
                                    defense = int(defense[10:])
                                    health = lines[18].strip()
                                    health = int(health[9:])
                                    speed = lines[19].strip()
                                    speed = int(speed[8:])
                                    specattack = lines[20].strip()
                                    specattack = int(specattack[13:])
                                    luck = lines[21].strip()
                                    luck = int(luck[7:])
                                with open(resource_path("gamedata.txt"), "r") as file:
                                    lines = file.readlines()
                                    lines[16] = (f"strength = {strength - attributes[4]}\n")
                                    lines[17] = (f"defense = {defense - attributes[3]}\n")
                                    lines[18] = (f"health = {health - attributes[2]}\n")
                                    lines[19] = (f"speed = {speed - attributes[6]}\n")
                                    lines[20] = (f"specattack = {specattack - attributes[5]}\n")
                                    lines[21] = (f"luck = {luck - attributes[7]}\n")
                                with open(resource_path("gamedata.txt"), "w") as file:
                                    file.writelines(lines)
                                itemname.clear()
                                regularimage.clear()
                                itemimagecore.clear()
                                itemHP.clear()
                                itemarmor.clear()
                                itemAttack.clear()
                                itemspecialattack.clear()
                                itemspeed.clear()
                                itemluck.clear()

                                items = load_creatures("itemdata.txt")

                                for item in items:
                                    attributes = list(item.values())
                                    itemname.append(attributes[0])
                                    regularimage.append(attributes[1])
                                    tempimage = pygame.image.load(resource_path(attributes[1]))
                                    tempimage = pygame.transform.scale(tempimage, (60, 60))
                                    itemimagecore.append(tempimage)
                                    itemHP.append(attributes[2])
                                    itemarmor.append(attributes[3])
                                    itemAttack.append(attributes[4])
                                    itemspecialattack.append(attributes[5])
                                    itemspeed.append(attributes[6])
                                    itemluck.append(attributes[7])
                                clickedrect = -1
                                empty_item(3, "equipeditems.txt")
                                equipmentimages = [[], [], [], [], [], [], []]
                                equipeditems = load_teamcreatures("equipeditems.txt")
                                if (len(equipeditems) >= 1 and equipeditems[0] != {}):
                                    attributes = list(equipeditems[0].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[0] = tempimg
                                if (len(equipeditems) >= 2 and equipeditems[1] != {}):
                                    attributes = list(equipeditems[1].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[1] = tempimg
                                if (len(equipeditems) >= 3 and equipeditems[2] != {}):
                                    attributes = list(equipeditems[2].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[2] = tempimg
                                if (len(equipeditems) >= 4 and equipeditems[3] != {}):
                                    attributes = list(equipeditems[3].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[3] = tempimg
                                if (len(equipeditems) >= 5 and equipeditems[4] != {}):
                                    attributes = list(equipeditems[4].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[4] = tempimg
                                if (len(equipeditems) >= 6 and equipeditems[5] != {}):
                                    attributes = list(equipeditems[5].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[5] = tempimg
                                if (len(equipeditems) >= 7 and equipeditems[6] != {}):

                                    attributes = list(equipeditems[6].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[6] = tempimg
                        if jewelry1xrect.collidepoint(mouse_pos):
                            equipeditems = load_teamcreatures("equipeditems.txt")
                            sound_effect = pygame.mixer.Sound(resource_path("audio/scifinoise.mp3"))
                            sound_effect.play()
                            if (len(equipeditems) >= 5 and equipeditems[4] != {}):
                                save_creature(equipeditems[4], "itemdata.txt")
                                equipeditems = load_teamcreatures("equipeditems.txt")
                                attributes = list(equipeditems[4].values())
                                strength = 0
                                defense = 0
                                health = 0
                                speed = 0
                                specattack = 0
                                luck = 0
                                with open(resource_path("gamedata.txt"), "r") as file:
                                    lines = file.readlines()
                                    strength = lines[16].strip()
                                    strength = int(strength[11:])
                                    defense = lines[17].strip()
                                    defense = int(defense[10:])
                                    health = lines[18].strip()
                                    health = int(health[9:])
                                    speed = lines[19].strip()
                                    speed = int(speed[8:])
                                    specattack = lines[20].strip()
                                    specattack = int(specattack[13:])
                                    luck = lines[21].strip()
                                    luck = int(luck[7:])
                                with open(resource_path("gamedata.txt"), "r") as file:
                                    lines = file.readlines()
                                    lines[16] = (f"strength = {strength - attributes[4]}\n")
                                    lines[17] = (f"defense = {defense - attributes[3]}\n")
                                    lines[18] = (f"health = {health - attributes[2]}\n")
                                    lines[19] = (f"speed = {speed - attributes[6]}\n")
                                    lines[20] = (f"specattack = {specattack - attributes[5]}\n")
                                    lines[21] = (f"luck = {luck - attributes[7]}\n")
                                with open(resource_path("gamedata.txt"), "w") as file:
                                    file.writelines(lines)
                                itemname.clear()
                                regularimage.clear()
                                itemimagecore.clear()
                                itemHP.clear()
                                itemarmor.clear()
                                itemAttack.clear()
                                itemspecialattack.clear()
                                itemspeed.clear()
                                itemluck.clear()

                                items = load_creatures("itemdata.txt")

                                for item in items:
                                    attributes = list(item.values())
                                    itemname.append(attributes[0])
                                    regularimage.append(attributes[1])
                                    tempimage = pygame.image.load(resource_path(attributes[1]))
                                    tempimage = pygame.transform.scale(tempimage, (60, 60))
                                    itemimagecore.append(tempimage)
                                    itemHP.append(attributes[2])
                                    itemarmor.append(attributes[3])
                                    itemAttack.append(attributes[4])
                                    itemspecialattack.append(attributes[5])
                                    itemspeed.append(attributes[6])
                                    itemluck.append(attributes[7])
                                clickedrect = -1
                                empty_item(4, "equipeditems.txt")
                                equipmentimages = [[], [], [], [], [], [], []]
                                equipeditems = load_teamcreatures("equipeditems.txt")
                                if (len(equipeditems) >= 1 and equipeditems[0] != {}):
                                    attributes = list(equipeditems[0].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[0] = tempimg
                                if (len(equipeditems) >= 2 and equipeditems[1] != {}):
                                    attributes = list(equipeditems[1].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[1] = tempimg
                                if (len(equipeditems) >= 3 and equipeditems[2] != {}):
                                    attributes = list(equipeditems[2].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[2] = tempimg
                                if (len(equipeditems) >= 4 and equipeditems[3] != {}):
                                    attributes = list(equipeditems[3].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[3] = tempimg
                                if (len(equipeditems) >= 5 and equipeditems[4] != {}):
                                    attributes = list(equipeditems[4].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[4] = tempimg
                                if (len(equipeditems) >= 6 and equipeditems[5] != {}):
                                    attributes = list(equipeditems[5].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[5] = tempimg
                                if (len(equipeditems) >= 7 and equipeditems[6] != {}):
                                    attributes = list(equipeditems[6].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[6] = tempimg
                        if jewelry2xrect.collidepoint(mouse_pos):
                            equipeditems = load_teamcreatures("equipeditems.txt")
                            sound_effect = pygame.mixer.Sound(resource_path("audio/scifinoise.mp3"))
                            sound_effect.play()
                            if (len(equipeditems) >= 6 and equipeditems[5] != {}):
                                save_creature(equipeditems[5], "itemdata.txt")
                                equipeditems = load_teamcreatures("equipeditems.txt")
                                attributes = list(equipeditems[5].values())
                                strength = 0
                                defense = 0
                                health = 0
                                speed = 0
                                specattack = 0
                                luck = 0
                                with open(resource_path("gamedata.txt"), "r") as file:
                                    lines = file.readlines()
                                    strength = lines[16].strip()
                                    strength = int(strength[11:])
                                    defense = lines[17].strip()
                                    defense = int(defense[10:])
                                    health = lines[18].strip()
                                    health = int(health[9:])
                                    speed = lines[19].strip()
                                    speed = int(speed[8:])
                                    specattack = lines[20].strip()
                                    specattack = int(specattack[13:])
                                    luck = lines[21].strip()
                                    luck = int(luck[7:])
                                with open(resource_path("gamedata.txt"), "r") as file:
                                    lines = file.readlines()
                                    lines[16] = (f"strength = {strength - attributes[4]}\n")
                                    lines[17] = (f"defense = {defense - attributes[3]}\n")
                                    lines[18] = (f"health = {health - attributes[2]}\n")
                                    lines[19] = (f"speed = {speed - attributes[6]}\n")
                                    lines[20] = (f"specattack = {specattack - attributes[5]}\n")
                                    lines[21] = (f"luck = {luck - attributes[7]}\n")
                                with open(resource_path("gamedata.txt"), "w") as file:
                                    file.writelines(lines)
                                itemname.clear()
                                regularimage.clear()
                                itemimagecore.clear()
                                itemHP.clear()
                                itemarmor.clear()
                                itemAttack.clear()
                                itemspecialattack.clear()
                                itemspeed.clear()
                                itemluck.clear()

                                items = load_creatures("itemdata.txt")

                                for item in items:
                                    attributes = list(item.values())
                                    itemname.append(attributes[0])
                                    regularimage.append(attributes[1])
                                    tempimage = pygame.image.load(resource_path(attributes[1]))
                                    tempimage = pygame.transform.scale(tempimage, (60, 60))
                                    itemimagecore.append(tempimage)
                                    itemHP.append(attributes[2])
                                    itemarmor.append(attributes[3])
                                    itemAttack.append(attributes[4])
                                    itemspecialattack.append(attributes[5])
                                    itemspeed.append(attributes[6])
                                    itemluck.append(attributes[7])
                                clickedrect = -1
                                empty_item(5, "equipeditems.txt")
                                equipmentimages = [[], [], [], [], [], [], []]
                                equipeditems = load_teamcreatures("equipeditems.txt")
                                if (len(equipeditems) >= 1 and equipeditems[0] != {}):
                                    attributes = list(equipeditems[0].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[0] = tempimg
                                if (len(equipeditems) >= 2 and equipeditems[1] != {}):
                                    attributes = list(equipeditems[1].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[1] = tempimg
                                if (len(equipeditems) >= 3 and equipeditems[2] != {}):
                                    attributes = list(equipeditems[2].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[2] = tempimg
                                if (len(equipeditems) >= 4 and equipeditems[3] != {}):
                                    attributes = list(equipeditems[3].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[3] = tempimg
                                if (len(equipeditems) >= 5 and equipeditems[4] != {}):
                                    attributes = list(equipeditems[4].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[4] = tempimg
                                if (len(equipeditems) >= 6 and equipeditems[5] != {}):
                                    attributes = list(equipeditems[5].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[5] = tempimg
                                if (len(equipeditems) >= 7 and equipeditems[6] != {}):
                                    attributes = list(equipeditems[6].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[6] = tempimg
                        if swordxrect.collidepoint(mouse_pos):
                            equipeditems = load_teamcreatures("equipeditems.txt")
                            sound_effect = pygame.mixer.Sound(resource_path("audio/scifinoise.mp3"))
                            sound_effect.play()
                            if (len(equipeditems) >= 7 and equipeditems[6] != {}):
                                save_creature(equipeditems[6], "itemdata.txt")
                                equipeditems = load_teamcreatures("equipeditems.txt")
                                attributes = list(equipeditems[6].values())
                                strength = 0
                                defense = 0
                                health = 0
                                speed = 0
                                specattack = 0
                                luck = 0
                                with open(resource_path("gamedata.txt"), "r") as file:
                                    lines = file.readlines()
                                    strength = lines[16].strip()
                                    strength = int(strength[11:])
                                    defense = lines[17].strip()
                                    defense = int(defense[10:])
                                    health = lines[18].strip()
                                    health = int(health[9:])
                                    speed = lines[19].strip()
                                    speed = int(speed[8:])
                                    specattack = lines[20].strip()
                                    specattack = int(specattack[13:])
                                    luck = lines[21].strip()
                                    luck = int(luck[7:])
                                with open(resource_path("gamedata.txt"), "r") as file:
                                    lines = file.readlines()
                                    lines[16] = (f"strength = {strength - attributes[4]}\n")
                                    lines[17] = (f"defense = {defense - attributes[3]}\n")
                                    lines[18] = (f"health = {health - attributes[2]}\n")
                                    lines[19] = (f"speed = {speed - attributes[6]}\n")
                                    lines[20] = (f"specattack = {specattack - attributes[5]}\n")
                                    lines[21] = (f"luck = {luck - attributes[7]}\n")
                                with open(resource_path("gamedata.txt"), "w") as file:
                                    file.writelines(lines)
                                itemname.clear()
                                regularimage.clear()
                                itemimagecore.clear()
                                itemHP.clear()
                                itemarmor.clear()
                                itemAttack.clear()
                                itemspecialattack.clear()
                                itemspeed.clear()
                                itemluck.clear()

                                items = load_creatures("itemdata.txt")

                                for item in items:
                                    attributes = list(item.values())
                                    itemname.append(attributes[0])
                                    regularimage.append(attributes[1])
                                    tempimage = pygame.image.load(resource_path(attributes[1]))
                                    tempimage = pygame.transform.scale(tempimage, (60, 60))
                                    itemimagecore.append(tempimage)
                                    itemHP.append(attributes[2])
                                    itemarmor.append(attributes[3])
                                    itemAttack.append(attributes[4])
                                    itemspecialattack.append(attributes[5])
                                    itemspeed.append(attributes[6])
                                    itemluck.append(attributes[7])
                                clickedrect = -1
                                empty_item(6, "equipeditems.txt")
                                equipmentimages = [[], [], [], [], [], [], []]
                                equipeditems = load_teamcreatures("equipeditems.txt")
                                if (len(equipeditems) >= 1 and equipeditems[0] != {}):
                                    attributes = list(equipeditems[0].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[0] = tempimg
                                if (len(equipeditems) >= 2 and equipeditems[1] != {}):
                                    attributes = list(equipeditems[1].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[1] = tempimg
                                if (len(equipeditems) >= 3 and equipeditems[2] != {}):
                                    attributes = list(equipeditems[2].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[2] = tempimg
                                if (len(equipeditems) >= 4 and equipeditems[3] != {}):
                                    attributes = list(equipeditems[3].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[3] = tempimg
                                if (len(equipeditems) >= 5 and equipeditems[4] != {}):
                                    attributes = list(equipeditems[4].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[4] = tempimg
                                if (len(equipeditems) >= 6 and equipeditems[5] != {}):
                                    attributes = list(equipeditems[5].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[5] = tempimg
                                if (len(equipeditems) >= 7 and equipeditems[6] != {}):
                                    attributes = list(equipeditems[6].values())
                                    tempimg = pygame.image.load(resource_path(attributes[1]))
                                    tempimg = pygame.transform.scale(tempimg, (60, 60))
                                    equipmentimages[6] = tempimg
                        if trashcanrect.collidepoint(mouse_pos):
                            if (clickedrect != -1):
                                if (clickedrect > ((itempage - 1) * 36) - 1) and (
                                        clickedrect <= ((itempage * 36) - 1)):
                                    delete_creature_by_index(clickedrect, "itemdata.txt")
                                    randomgold = random.randint(1, 200)
                                    with open(resource_path("gamedata.txt"), "r") as file:
                                        lines = file.readlines()
                                        lines[0] = f"gold = {gold + randomgold}\n"
                                    with open(resource_path("gamedata.txt"), "w") as file:
                                        file.writelines(lines)
                                    sound_effect = pygame.mixer.Sound(resource_path("audio/thundersound1.mp3"))
                                    sound_effect.play()
                                    looptimeg = pygame.time.get_ticks() + 700
                                    timerg = pygame.time.get_ticks()
                                    while (looptimeg > timerg):
                                        draw_text('gained ' + str(randomgold) + " gold", font24, GOLD, DISPLAYSURF,
                                                  1388, 710)
                                        timerg = pygame.time.get_ticks()
                                        for event in pygame.event.get():
                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                print("stop clicking so much")
                                        pygame.display.update()

                                    itemname.clear()
                                    regularimage.clear()
                                    itemimagecore.clear()
                                    itemHP.clear()
                                    itemarmor.clear()
                                    itemAttack.clear()
                                    itemspecialattack.clear()
                                    itemspeed.clear()
                                    itemluck.clear()

                                    items = load_creatures("itemdata.txt")

                                    for item in items:
                                        attributes = list(item.values())
                                        itemname.append(attributes[0])
                                        regularimage.append(attributes[1])
                                        tempimage = pygame.image.load(resource_path(attributes[1]))
                                        tempimage = pygame.transform.scale(tempimage, (60, 60))
                                        itemimagecore.append(tempimage)
                                        itemHP.append(attributes[2])
                                        itemarmor.append(attributes[3])
                                        itemAttack.append(attributes[4])
                                        itemspecialattack.append(attributes[5])
                                        itemspeed.append(attributes[6])
                                        itemluck.append(attributes[7])
                                    clickedrect = -1
                pygame.display.update()

            if (self.gamescene == 3):
                DISPLAYSURF.fill(BLACK)
                mouse_pos = pygame.mouse.get_pos()
                mouseX, mouseY = pygame.mouse.get_pos()
                #print("x and y = " + str(mouseX) + " " + str(mouseY))

                image264.set_alpha(150)
                DISPLAYSURF.blit(image264, (197, 100))

                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))

                ret, frame = video.read()
                if not ret:
                    video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    continue  # Continue to the next loop iteration
                frame = cv2.resize(frame, (1550, 880))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_surface = pygame.surfarray.make_surface(frame)
                frame_surface = pygame.transform.rotate(frame_surface, -90)  # Rotate if necessary
                frame_surface = pygame.transform.flip(frame_surface, True, False)
                frame_surface.set_alpha(70)
                DISPLAYSURF.blit(frame_surface, (190, 100))

                DISPLAYSURF.blit(image266, (490, 190))

                draw_text_center('Armory', font23, RED, DISPLAYSURF, 885, 222)
                draw_text_center('Beasts', font23, PURPLE, DISPLAYSURF, 1043, 222)
                draw_text_center('Companions', font23, AQUA, DISPLAYSURF, 595, 361)
                draw_text_center('Page ' + str(creaturepage), font23, EMERALD, DISPLAYSURF, halfdisplay + 5, 875)

                DISPLAYSURF.blit(image133, (mouseX - 41, mouseY - 37))

                rects = []
                i = 0
                amountBeasts = len(creatureimage)
                while(i != amountBeasts):

                    ii = (i + (creaturepage - 1) * 36)
                    size = len(creatureimage) - 1

                    if(i >= 0 and i <= 5):
                        if(size >= ii):
                            DISPLAYSURF.blit(smallBeasts[creatureimage[ii]], (699 + (94 * i), 288))
                            rect = pygame.Rect(695 + (94 * i), 282, 73, 71)
                            rects.append(rect)
                    if(i >=6 and i <= 11):
                        if(size >= ii):
                            DISPLAYSURF.blit(smallBeasts[creatureimage[ii]], (699 + (94 * (i - 6)), 379))
                            rect = pygame.Rect(695 + (94 * (i - 6)), 373, 73, 71)
                            rects.append(rect)
                    if(i >= 12 and i <= 17):
                        if(size >= ii):
                            DISPLAYSURF.blit(smallBeasts[creatureimage[ii]], (699 +(94 * (i - 12)), 465))
                            rect = pygame.Rect(695 + (94 * (i - 12)), 460, 73, 71)
                            rects.append(rect)
                    if(i >= 18 and i <= 23):
                        if(size >= ii):
                            DISPLAYSURF.blit(smallBeasts[creatureimage[ii]], (699 + (94 * (i - 18)), 555))
                            rect = pygame.Rect(695 + (94 * (i - 18)), 549, 73, 71)
                            rects.append(rect)
                    if(i >= 24 and i <= 29):
                        if(size >= ii):
                            DISPLAYSURF.blit(smallBeasts[creatureimage[ii]], (699 + (94 * (i - 24)), 642))
                            rect = pygame.Rect(695 + (94 * (i - 24)), 636, 73, 71)
                            rects.append(rect)
                    if(i >= 30 and i <= 35):
                        if(size >= ii):
                            DISPLAYSURF.blit(smallBeasts[creatureimage[ii]], (699 + (94 * (i - 30)), 731))
                            rect = pygame.Rect(695 + (94 * (i - 30)), 726, 73, 71)
                            rects.append(rect)

                    i = i + 1

                s1 = " "
                s2 = " "
                s3 = " "
                s4 = " "
                s5 = " "
                s6 = " "
                showbool = True
                x = 0
                team1 = pygame.Rect(509, 410, 174, 75)
                team2 = pygame.Rect(509, 500, 174, 75)
                team3 = pygame.Rect(507, 590, 174, 75)

                for rect in rects:
                    pygame.draw.rect(DISPLAYSURF,PINK, rect, 6, 10)
                    if rect.collidepoint(mouse_pos):
                        showbool = False
                        xx = x + ((creaturepage - 1) * 36)
                        s1 = ('Lvl- ' + str(creaturelvl[xx]))
                        s2 = ('Hp- ' + str(int((creaturehp[xx] + (creaturehp[xx] * .2 * creaturelvl[xx]) + (1 * creaturelvl[xx])) * (1 + creaturetier[xx] * .1))))
                        s3 = ('Def- ' + str(int((creaturedefense[xx] + (creaturedefense[xx] * .2 * creaturelvl[xx]) + (1 * creaturelvl[xx])) * (1 + creaturetier[xx] * .1))))
                        s4 = ('Str- ' + str(int((creaturestrength[xx] + (creaturestrength[xx] * .2 * creaturelvl[xx]) + (1 * creaturelvl[xx])) * (1 + creaturetier[xx] * .1))))
                        s5 = ('Spec- ' + str(int((creaturespecattack[xx] + (creaturespecattack[xx] * .2 * creaturelvl[xx]) + (1 * creaturelvl[xx])) * (1 + creaturetier[xx] * .1))))
                        s6 = ('Speed- ' + str(int((creaturespeed[xx] + (creaturespeed[xx] * .2 * creaturelvl[xx]) + (1 * creaturelvl[xx])) * (1 + creaturetier[xx] * .1))))
                        pygame.draw.rect(DISPLAYSURF, GOLD, rect, 6, 10)
                        draw_text_center(str(creaturename[xx]), font24, LIGHTGREEN, DISPLAYSURF, 1405, 365)
                        draw_text_center(str(beast_lore[creatureimage[xx]]), font11, DARKPURPLE, DISPLAYSURF, 960, 930)
                        draw_text_center("lvl- " +str(creaturelvl[xx]), font24, GREEN, DISPLAYSURF, 1405, 415)
                        draw_text(str(creaturemove1[xx]), font24, DARKGREEN, DISPLAYSURF, 1260, 475)
                        draw_text(str(creaturemove2[xx]), font24, DARKGREEN, DISPLAYSURF, 1260, 520)
                        draw_text(str(creaturemove3[xx]), font24, DARKGREEN, DISPLAYSURF, 1260, 565)
                        draw_text(str(creaturemove4[xx]), font24, DARKGREEN, DISPLAYSURF, 1260, 610)
                        draw_text_center("stats", font24, BLUE, DISPLAYSURF, 320, 365)
                        draw_text(s2, font24, SKYBLUE, DISPLAYSURF, 260, 425)
                        draw_text(s3, font24, SKYBLUE, DISPLAYSURF, 260, 465)
                        draw_text(s4, font24, SKYBLUE, DISPLAYSURF, 260, 505)
                        draw_text(s5, font24, SKYBLUE, DISPLAYSURF, 260, 545)
                        draw_text(s6, font24, SKYBLUE, DISPLAYSURF, 260, 585)
                        exprect = pygame.Rect(690, 157, 0  + creatureexp[xx], 50)
                        exprect2 = pygame.Rect(690, 157, 555, 50)
                        draw_text_center("exp", font24, PINK, DISPLAYSURF, halfdisplay + 5, 105)
                        pygame.draw.rect(DISPLAYSURF, PINK, exprect, 0, 12)
                        pygame.draw.rect(DISPLAYSURF, GREY, exprect2, 6, 12)
                        draw_text_center("type- " +creaturetype[xx], font24, GREEN, DISPLAYSURF, 1398, 315)
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                clickedrect = x + ((creaturepage - 1) * 36)

                    x = x + 1
                if (clickedrect != -1):
                     if (clickedrect > ((creaturepage - 1) * 36) - 1) and (clickedrect <= ((creaturepage * 36) - 1)):
                        pygame.draw.rect(DISPLAYSURF, AQUA, rects[clickedrect - ((creaturepage - 1) * 36)], 6, 10)

                if (showbool == True):
                    if team1.collidepoint(mouse_pos):
                        teamcreatures = load_teamcreatures()
                        if (len(teamcreatures) >= 1):
                            attributes = list(teamcreatures[0].values())
                            s1 = ('Lvl- ' + str(attributes[1]))
                            s2 = ('Hp- ' + str(int((attributes[2] + (attributes[2] * .2 * attributes[1]) + (1 * attributes[1])) * (1 + attributes[7] * .1))))
                            s3 = ('Def- ' + str(int((attributes[3] + (attributes[3] * .2 * attributes[1]) + (1 * attributes[1])) * (1 + attributes[7] * .1))))
                            s4 = ('Str- ' + str(int((attributes[4] + (attributes[4] * .2 * attributes[1]) + (1 * attributes[1])) * (1 + attributes[7] * .1))))
                            s5 = ('Spec- ' + str(int((attributes[5] + (attributes[5] * .2 * attributes[1]) + (1 * attributes[1])) * (1 + attributes[7] * .1))))
                            s6 = ('Speed- ' + str(int((attributes[6] + (attributes[6] * .2 * attributes[1]) + (1 * attributes[1])) * (1 + attributes[7] * .1))))
                            draw_text_center(str(attributes[0]), font24, LIGHTGREEN, DISPLAYSURF, 1405,365)
                            draw_text_center(str(beast_lore[attributes[8]]), font11, DARKPURPLE,DISPLAYSURF, 960, 930)
                            draw_text_center("lvl- " + str(attributes[1]), font24, GREEN, DISPLAYSURF,1405, 415)
                            draw_text(str(attributes[9]), font24, DARKGREEN, DISPLAYSURF, 1260, 475)
                            draw_text(str(attributes[10]), font24, DARKGREEN, DISPLAYSURF, 1260, 520)
                            draw_text(str(attributes[11]), font24, DARKGREEN, DISPLAYSURF, 1260, 565)
                            draw_text(str(attributes[12]), font24, DARKGREEN, DISPLAYSURF, 1260, 610)
                            draw_text_center("stats", font24, BLUE, DISPLAYSURF, 320, 365)
                            draw_text(s2, font24, SKYBLUE, DISPLAYSURF, 260, 425)
                            draw_text(s3, font24, SKYBLUE, DISPLAYSURF, 260, 465)
                            draw_text(s4, font24, SKYBLUE, DISPLAYSURF, 260, 505)
                            draw_text(s5, font24, SKYBLUE, DISPLAYSURF, 260, 545)
                            draw_text(s6, font24, SKYBLUE, DISPLAYSURF, 260, 585)
                            exprect = pygame.Rect(690, 157, 0 + attributes[14], 50)
                            exprect2 = pygame.Rect(690, 157, 555, 50)
                            draw_text_center("exp", font24, PINK, DISPLAYSURF, halfdisplay + 5, 105)
                            pygame.draw.rect(DISPLAYSURF, PINK, exprect, 0, 12)
                            pygame.draw.rect(DISPLAYSURF, GREY, exprect2, 6, 12)
                            draw_text_center("type- " + attributes[13], font24, GREEN, DISPLAYSURF, 1398,315)
                    elif team2.collidepoint(mouse_pos):
                        teamcreatures = load_teamcreatures()
                        if (len(teamcreatures) >= 2):
                            attributes = list(teamcreatures[1].values())
                            s1 = ('Lvl- ' + str(attributes[1]))
                            s2 = ('Hp- ' + str(int((attributes[2] + (attributes[2] * .2 * attributes[1]) + (1 * attributes[1])) * (1 + attributes[7] * .1))))
                            s3 = ('Def- ' + str(int((attributes[3] + (attributes[3] * .2 * attributes[1]) + (1 * attributes[1])) * (1 + attributes[7] * .1))))
                            s4 = ('Str- ' + str(int((attributes[4] + (attributes[4] * .2 * attributes[1]) + (1 * attributes[1])) * (1 + attributes[7] * .1))))
                            s5 = ('Spec- ' + str(int((attributes[5] + (attributes[5] * .2 * attributes[1]) + (1 * attributes[1])) * (1 + attributes[7] * .1))))
                            s6 = ('Speed- ' + str(int((attributes[6] + (attributes[6] * .2 * attributes[1]) + (1 * attributes[1])) * (1 + attributes[7] * .1))))
                            draw_text_center(str(attributes[0]), font24, LIGHTGREEN, DISPLAYSURF, 1405,365)
                            draw_text_center(str(beast_lore[attributes[8]]), font11, DARKPURPLE,DISPLAYSURF, 960, 930)
                            draw_text_center("lvl- " + str(attributes[1]), font24, GREEN, DISPLAYSURF,1405, 415)
                            draw_text(str(attributes[9]), font24, DARKGREEN, DISPLAYSURF, 1260, 475)
                            draw_text(str(attributes[10]), font24, DARKGREEN, DISPLAYSURF, 1260, 515)
                            draw_text(str(attributes[11]), font24, DARKGREEN, DISPLAYSURF, 1260, 555)
                            draw_text(str(attributes[12]), font24, DARKGREEN, DISPLAYSURF, 1260, 595)
                            draw_text_center("stats", font24, BLUE, DISPLAYSURF, 320, 365)
                            draw_text(s2, font24, SKYBLUE, DISPLAYSURF, 260, 425)
                            draw_text(s3, font24, SKYBLUE, DISPLAYSURF, 260, 465)
                            draw_text(s4, font24, SKYBLUE, DISPLAYSURF, 260, 505)
                            draw_text(s5, font24, SKYBLUE, DISPLAYSURF, 260, 545)
                            draw_text(s6, font24, SKYBLUE, DISPLAYSURF, 260, 585)
                            exprect = pygame.Rect(690, 157, 0 + attributes[14], 50)
                            exprect2 = pygame.Rect(690, 157, 555, 50)
                            draw_text_center("exp", font24, PINK, DISPLAYSURF, halfdisplay + 5, 105)
                            pygame.draw.rect(DISPLAYSURF, PINK, exprect, 0, 12)
                            pygame.draw.rect(DISPLAYSURF, GREY, exprect2, 6, 12)
                            draw_text_center("type- " + attributes[13], font24, GREEN, DISPLAYSURF, 1398,315)
                    elif team3.collidepoint(mouse_pos):
                        teamcreatures = load_teamcreatures()
                        if (len(teamcreatures) >= 3):
                            attributes = list(teamcreatures[2].values())
                            s1 = ('Lvl- ' + str(attributes[1]))
                            s2 = ('Hp- ' + str(int((attributes[2] + (attributes[2] * .2 * attributes[1]) + (1 * attributes[1])) * (1 + attributes[7] * .1))))
                            s3 = ('Def- ' + str(int((attributes[3] + (attributes[3] * .2 * attributes[1]) + (1 * attributes[1])) * (1 + attributes[7] * .1))))
                            s4 = ('Str- ' + str(int((attributes[4] + (attributes[4] * .2 * attributes[1]) + (1 * attributes[1])) * (1 + attributes[7] * .1))))
                            s5 = ('Spec- ' + str(int((attributes[5] + (attributes[5] * .2 * attributes[1]) + (1 * attributes[1])) * (1 + attributes[7] * .1))))
                            s6 = ('Speed- ' + str(int((attributes[6] + (attributes[6] * .2 * attributes[1]) + (1 * attributes[1])) * (1 + attributes[7] * .1))))
                            draw_text_center(str(attributes[0]), font24, LIGHTGREEN, DISPLAYSURF, 1405,365)
                            draw_text_center(str(beast_lore[attributes[8]]), font11, DARKPURPLE,DISPLAYSURF, 960, 930)
                            draw_text_center("lvl- " + str(attributes[1]), font24, GREEN, DISPLAYSURF,1405, 415)
                            draw_text(str(attributes[9]), font24, DARKGREEN, DISPLAYSURF, 1260, 475)
                            draw_text(str(attributes[10]), font24, DARKGREEN, DISPLAYSURF, 1260, 520)
                            draw_text(str(attributes[11]), font24, DARKGREEN, DISPLAYSURF, 1260, 565)
                            draw_text(str(attributes[12]), font24, DARKGREEN, DISPLAYSURF, 1260, 610)
                            draw_text_center("stats", font24, BLUE, DISPLAYSURF, 320, 365)
                            draw_text(s2, font24, SKYBLUE, DISPLAYSURF, 260, 425)
                            draw_text(s3, font24, SKYBLUE, DISPLAYSURF, 260, 465)
                            draw_text(s4, font24, SKYBLUE, DISPLAYSURF, 260, 505)
                            draw_text(s5, font24, SKYBLUE, DISPLAYSURF, 260, 545)
                            draw_text(s6, font24, SKYBLUE, DISPLAYSURF, 260, 585)
                            exprect = pygame.Rect(690, 157, 0 + attributes[14], 50)
                            exprect2 = pygame.Rect(690, 157, 555, 50)
                            draw_text_center("exp", font24, PINK, DISPLAYSURF, halfdisplay + 5, 105)
                            pygame.draw.rect(DISPLAYSURF, PINK, exprect, 0, 12)
                            pygame.draw.rect(DISPLAYSURF, GREY, exprect2, 6, 12)
                            draw_text_center("type- " + attributes[13], font24, GREEN, DISPLAYSURF, 1398,315)
                    elif (clickedrect != -1):
                        if (clickedrect > ((creaturepage - 1) * 36) - 1) and (clickedrect <= ((creaturepage * 36) - 1)):
                            s1 = ('Lvl- ' + str(creaturelvl[clickedrect]))
                            s2 = ('Hp- ' + str(int((creaturehp[clickedrect] + (creaturehp[clickedrect] * .2 * creaturelvl[clickedrect]) + (
                                        1 * creaturelvl[clickedrect])) * (1 + creaturetier[clickedrect] * .1))))
                            s3 = ('Def- ' + str(int((creaturedefense[clickedrect] + (
                                        creaturedefense[clickedrect] * .2 * creaturelvl[clickedrect]) + (1 * creaturelvl[clickedrect])) * (
                                                                1 + creaturetier[clickedrect] * .1))))
                            s4 = ('Str- ' + str(int((creaturestrength[clickedrect] + (
                                        creaturestrength[clickedrect] * .2 * creaturelvl[clickedrect]) + (1 * creaturelvl[clickedrect])) * (
                                                                1 + creaturetier[clickedrect] * .1))))
                            s5 = ('Spec- ' + str(int((creaturespecattack[clickedrect] + (
                                        creaturespecattack[clickedrect] * .2 * creaturelvl[clickedrect]) + (1 * creaturelvl[clickedrect])) * (
                                                                 1 + creaturetier[clickedrect] * .1))))
                            s6 = ('Speed- ' + str(int((creaturespeed[clickedrect] + (
                                        creaturespeed[clickedrect] * .2 * creaturelvl[clickedrect]) + (1 * creaturelvl[clickedrect])) * (
                                                                  1 + creaturetier[clickedrect] * .1))))
                            pygame.draw.rect(DISPLAYSURF, AQUA, rects[clickedrect - ((creaturepage - 1) * 36)], 6,10)
                            draw_text_center(str(creaturename[clickedrect]), font24, LIGHTGREEN, DISPLAYSURF, 1405, 365)
                            draw_text_center(str(beast_lore[creatureimage[clickedrect]]), font11, DARKPURPLE, DISPLAYSURF,960, 930)
                            draw_text_center("lvl- " + str(creaturelvl[clickedrect]), font24, GREEN, DISPLAYSURF, 1405, 415)
                            draw_text(str(creaturemove1[clickedrect]), font24, DARKGREEN, DISPLAYSURF, 1260, 475)
                            draw_text(str(creaturemove2[clickedrect]), font24, DARKGREEN, DISPLAYSURF, 1260, 520)
                            draw_text(str(creaturemove3[clickedrect]), font24, DARKGREEN, DISPLAYSURF, 1260, 565)
                            draw_text(str(creaturemove4[clickedrect]), font24, DARKGREEN, DISPLAYSURF, 1260, 610)
                            draw_text_center("stats", font24, BLUE, DISPLAYSURF, 320, 365)
                            draw_text(s2, font24, SKYBLUE, DISPLAYSURF, 260, 425)
                            draw_text(s3, font24, SKYBLUE, DISPLAYSURF, 260, 465)
                            draw_text(s4, font24, SKYBLUE, DISPLAYSURF, 260, 505)
                            draw_text(s5, font24, SKYBLUE, DISPLAYSURF, 260, 545)
                            draw_text(s6, font24, SKYBLUE, DISPLAYSURF, 260, 585)
                            exprect = pygame.Rect(690, 157, 0 + creatureexp[clickedrect], 50)
                            exprect2 = pygame.Rect(690, 157, 555, 50)
                            draw_text_center("exp", font24, PINK, DISPLAYSURF, halfdisplay + 5, 105)
                            pygame.draw.rect(DISPLAYSURF, PINK, exprect, 0, 12)
                            pygame.draw.rect(DISPLAYSURF, GREY, exprect2, 6, 12)
                            draw_text_center("type- " + creaturetype[clickedrect], font24, GREEN, DISPLAYSURF, 1398, 315)

                pygame.draw.ellipse(DISPLAYSURF, (rainbowcolor2,rainbowcolor3,46), team1, 6)
                pygame.draw.ellipse(DISPLAYSURF, (rainbowcolor2,rainbowcolor3,46), team2, 6)
                pygame.draw.ellipse(DISPLAYSURF, (rainbowcolor2,rainbowcolor3,46), team3, 6)

                if team1.collidepoint(mouse_pos):
                    pygame.draw.ellipse(DISPLAYSURF, rainbow, team1, 5)

                if team2.collidepoint(mouse_pos):
                    pygame.draw.ellipse(DISPLAYSURF, rainbow, team2, 5)

                if team3.collidepoint(mouse_pos):
                    pygame.draw.ellipse(DISPLAYSURF, rainbow, team3, 5)

                teamcreatures = load_teamcreatures()
                if (len(teamcreatures) >= 1):
                    attributes = list(teamcreatures[0].values())
                    DISPLAYSURF.blit(smallBeasts[attributes[8]], (563, 415))
                if (len(teamcreatures) >= 2):
                    attributes = list(teamcreatures[1].values())
                    DISPLAYSURF.blit(smallBeasts[attributes[8]], (563, 515))
                if (len(teamcreatures) >= 3):
                    attributes = list(teamcreatures[2].values())
                    DISPLAYSURF.blit(smallBeasts[attributes[8]], (563, 605))

                draw_text('x', font4, RED, DISPLAYSURF, 474, 412)
                draw_text('x', font4, RED, DISPLAYSURF, 474, 501)
                draw_text('x', font4, RED, DISPLAYSURF, 474, 595)

                team1xrect = pygame.Rect(470, 430, 40, 40)
                team2xrect = pygame.Rect(470, 517, 40, 40)
                team3xrect = pygame.Rect(470, 612, 40, 40)
                if team1xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, rainbow, DISPLAYSURF, 474, 412)

                if team2xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, rainbow, DISPLAYSURF, 474, 501)

                if team3xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, rainbow, DISPLAYSURF, 474, 595)

                trashcanrect = pygame.Rect(930, 800, 80, 80)
                if trashcanrect.collidepoint(mouse_pos):
                    pygame.draw.ellipse(DISPLAYSURF, RED, trashcanrect, 4)
                    draw_text_center("click trash can to delete creature", font11, rainbow, DISPLAYSURF, halfdisplay, 797)

                armoryrect = pygame.Rect(815, 210, 150, 60)
                companionrect = pygame.Rect(975, 210, 150, 60)
                pygame.draw.rect(DISPLAYSURF, rainbow, companionrect, 5)

                move1rect = pygame.Rect(1257, 476, 450, 45)
                move2rect = pygame.Rect(1257, 520, 450, 45)
                move3rect = pygame.Rect(1257, 567, 450, 45)
                move4rect = pygame.Rect(1257, 615, 450, 45)

                if move1rect.collidepoint(mouse_pos):
                    if(clickedrect != -1):
                        if (creaturemove1[clickedrect] != " "):
                            pygame.draw.rect(DISPLAYSURF,  (rainbowcolor2, 192, rainbowcolor2), move1rect, 5, 5)
                            imagebackdrop.set_alpha(240)
                            DISPLAYSURF.blit(imagebackdrop, (585, 195))
                            draw_text_center(str(creaturemove1[clickedrect]), font24, LIME, DISPLAYSURF, halfdisplay + 5, 245)
                            for index, move in enumerate(moves):
                                if(creaturemove1[clickedrect] == move[0]):
                                    draw_text_center("Power  " +str(move[1]), font26, VELVET, DISPLAYSURF, halfdisplay, 300)
                                    draw_text_center(move[5] +" Category", font26, SLEEPPURPLE, DISPLAYSURF, halfdisplay, 360)
                                    if(move[2] != "empty"):
                                        draw_text_center(moveprint(move[2], "opponent"), font10, LIGHTYELLOW, DISPLAYSURF, halfdisplay, 400)
                                    if(move[3] != "empty"):
                                        draw_text_center("Enemy Effect", font10, YELLOW, DISPLAYSURF, halfdisplay, 425)
                                        draw_text_center(moveprint(move[3], "opponent"), font10, LIGHTYELLOW, DISPLAYSURF, halfdisplay, 450)
                                    if(move[4] != "empty"):
                                        draw_text_center("Self Effect", font10, YELLOW, DISPLAYSURF, halfdisplay, 475)
                                        draw_text_center(moveprint(move[4], "self"), font10, LIGHTYELLOW, DISPLAYSURF, halfdisplay, 500)
                                    draw_text_center(moves_lore[index], font27, CLOUD, DISPLAYSURF, halfdisplay + 5, 710)
                                    draw_text_center(str(move[6]) +"PP", font10, CLOUD, DISPLAYSURF, halfdisplay + 5, 778)

                if move2rect.collidepoint(mouse_pos):
                    if(clickedrect != -1):
                        if (creaturemove2[clickedrect] != " "):
                            pygame.draw.rect(DISPLAYSURF,  (rainbowcolor2, 192, rainbowcolor2), move2rect, 5, 5)
                            imagebackdrop.set_alpha(240)
                            DISPLAYSURF.blit(imagebackdrop, (585, 195))
                            draw_text_center(str(creaturemove2[clickedrect]), font24, LIME, DISPLAYSURF, halfdisplay + 5, 245)
                            for index, move in enumerate(moves):
                                if(creaturemove2[clickedrect] == move[0]):
                                    draw_text_center("Power  " +str(move[1]), font26, VELVET, DISPLAYSURF, halfdisplay, 300)
                                    draw_text_center(move[5] +" Category", font26, SLEEPPURPLE, DISPLAYSURF, halfdisplay, 360)
                                    if(move[2] != "empty"):
                                        draw_text_center(moveprint(move[2], "opponent"), font10, LIGHTYELLOW, DISPLAYSURF, halfdisplay, 400)
                                    if(move[3] != "empty"):
                                        draw_text_center("Enemy Effect", font10, YELLOW, DISPLAYSURF, halfdisplay, 425)
                                        draw_text_center(moveprint(move[3], "opponent"), font10, LIGHTYELLOW, DISPLAYSURF, halfdisplay, 450)
                                    if(move[4] != "empty"):
                                        draw_text_center("Self Effect", font10, YELLOW, DISPLAYSURF, halfdisplay, 475)
                                        draw_text_center(moveprint(move[4], "self"), font10, LIGHTYELLOW, DISPLAYSURF, halfdisplay, 500)
                                    draw_text_center(moves_lore[index], font27, CLOUD, DISPLAYSURF, halfdisplay + 5, 710)
                                    draw_text_center(str(move[6]) +"PP", font10, CLOUD, DISPLAYSURF, halfdisplay + 5, 778)
                if move3rect.collidepoint(mouse_pos):
                    if(clickedrect != -1):
                        if (creaturemove3[clickedrect] != " "):
                            pygame.draw.rect(DISPLAYSURF,  (rainbowcolor2, 192, rainbowcolor2), move3rect, 5, 5)
                            imagebackdrop.set_alpha(240)
                            DISPLAYSURF.blit(imagebackdrop, (585, 195))
                            draw_text_center(str(creaturemove3[clickedrect]), font24, LIME, DISPLAYSURF, halfdisplay + 5, 245)
                            for index, move in enumerate(moves):
                                if(creaturemove3[clickedrect] == move[0]):
                                    draw_text_center("Power  " +str(move[1]), font26, VELVET, DISPLAYSURF, halfdisplay, 300)
                                    draw_text_center(move[5] +" Category", font26, SLEEPPURPLE, DISPLAYSURF, halfdisplay, 360)
                                    if(move[2] != "empty"):
                                        draw_text_center(moveprint(move[2], "opponent"), font10, LIGHTYELLOW, DISPLAYSURF, halfdisplay, 400)
                                    if(move[3] != "empty"):
                                        draw_text_center("Enemy Effect", font10, YELLOW, DISPLAYSURF, halfdisplay, 425)
                                        draw_text_center(moveprint(move[3], "opponent"), font10, LIGHTYELLOW, DISPLAYSURF, halfdisplay, 450)
                                    if(move[4] != "empty"):
                                        draw_text_center("Self Effect", font10, YELLOW, DISPLAYSURF, halfdisplay, 475)
                                        draw_text_center(moveprint(move[4], "self"), font10, LIGHTYELLOW, DISPLAYSURF, halfdisplay, 500)
                                    draw_text_center(moves_lore[index], font27, CLOUD, DISPLAYSURF, halfdisplay + 5, 710)
                                    draw_text_center(str(move[6]) +"PP", font10, CLOUD, DISPLAYSURF, halfdisplay + 5, 778)
                if move4rect.collidepoint(mouse_pos):
                    if(clickedrect != -1):
                        if (creaturemove4[clickedrect] != " "):
                            pygame.draw.rect(DISPLAYSURF,  (rainbowcolor2, 192, rainbowcolor2), move4rect, 5, 5)
                            imagebackdrop.set_alpha(240)
                            DISPLAYSURF.blit(imagebackdrop, (585, 195))
                            draw_text_center(str(creaturemove4[clickedrect]), font24, LIME, DISPLAYSURF, halfdisplay + 5, 245)
                            for index, move in enumerate(moves):
                                if(creaturemove4[clickedrect] == move[0]):
                                    draw_text_center("Power  " +str(move[1]), font26, VELVET, DISPLAYSURF, halfdisplay, 300)
                                    draw_text_center(move[5] +" Category", font26, SLEEPPURPLE, DISPLAYSURF, halfdisplay, 360)
                                    if(move[2] != "empty"):
                                        draw_text_center(moveprint(move[2], "opponent"), font10, LIGHTYELLOW, DISPLAYSURF, halfdisplay, 400)
                                    if(move[3] != "empty"):
                                        draw_text_center("Enemy Effect", font10, YELLOW, DISPLAYSURF, halfdisplay, 425)
                                        draw_text_center(moveprint(move[3], "opponent"), font10, LIGHTYELLOW, DISPLAYSURF, halfdisplay, 450)
                                    if(move[4] != "empty"):
                                        draw_text_center("Self Effect", font10, YELLOW, DISPLAYSURF, halfdisplay, 475)
                                        draw_text_center(moveprint(move[4], "self"), font10, LIGHTYELLOW, DISPLAYSURF, halfdisplay, 500)
                                    draw_text_center(moves_lore[index], font27, CLOUD, DISPLAYSURF, halfdisplay + 5, 710)
                                    draw_text_center(str(move[6]) +"PP", font10, CLOUD, DISPLAYSURF, halfdisplay + 5, 778)

                leftarrowrect = pygame.Rect(685, 835, 125, 60)
                rightarrowrect = pygame.Rect(1130, 830, 125, 60)

                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 120, 70)
                if leftarrowrect.collidepoint(mouse_pos):
                    pygame.draw.rect(DISPLAYSURF, ORANGEDESERT, leftarrowrect, 5, 5)
                if rightarrowrect.collidepoint(mouse_pos):
                    pygame.draw.rect(DISPLAYSURF, ORANGEDESERT, rightarrowrect, 5, 5)
                if armoryrect.collidepoint(mouse_pos):
                    pygame.draw.rect(DISPLAYSURF, EMERALD, armoryrect, 5)
                if companionrect.collidepoint(mouse_pos):
                    pygame.draw.rect(DISPLAYSURF, EMERALD, companionrect, 5)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if leftarrowrect.collidepoint(mouse_pos):
                            sound_effect = pygame.mixer.Sound(resource_path("audio/scrollsound.mp3"))
                            sound_effect.play()
                            if(creaturepage != 1):
                                creaturepage = creaturepage - 1
                        if rightarrowrect.collidepoint(mouse_pos):
                            sound_effect = pygame.mixer.Sound(resource_path("audio/scrollsound.mp3"))
                            sound_effect.play()
                            creaturepage = creaturepage + 1
                        if returnarrowrect.collidepoint(mouse_pos):
                            video.release()
                            transition(6)
                            self.stashloop = False
                        if armoryrect.collidepoint(mouse_pos):
                            sound_effect = pygame.mixer.Sound(resource_path("audio/pcsound.wav"))
                            sound_effect.play()
                            clickedrect = -1
                            self.gamescene = 2
                        if companionrect.collidepoint(mouse_pos):
                            sound_effect = pygame.mixer.Sound(resource_path("audio/pcsound.wav"))
                            sound_effect.play()
                            clickedrect = -1
                            self.gamescene = 3
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            video.release()
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()
                        if team1.collidepoint(mouse_pos):
                            teamcreatures = load_teamcreatures()
                            if (clickedrect != -1):
                                if(len(teamcreatures) >= 1):
                                    if (clickedrect > ((creaturepage - 1) * 36) - 1) and (clickedrect <= ((creaturepage * 36) - 1)):
                                        save_creature(teamcreatures[0], "creaturedata.txt")
                                        modify_teamcreature(0, {"name": creaturename[clickedrect],
                                                                "lvl": creaturelvl[clickedrect],
                                                                "hp": creaturehp[clickedrect],
                                                                "defense": creaturedefense[clickedrect],
                                                                "strength": creaturestrength[clickedrect],
                                                                "special attack": creaturespecattack[clickedrect],
                                                                "speed": creaturespeed[clickedrect],
                                                                "tier": creaturetier[clickedrect],
                                                                "beastimage": creatureimage[clickedrect],
                                                                "move1": creaturemove1[clickedrect],
                                                                "move2": creaturemove2[clickedrect],
                                                                "move3": creaturemove3[clickedrect],
                                                                "move4": creaturemove4[clickedrect],
                                                                "type": creaturetype[clickedrect],
                                                                "experience": creatureexp[
                                                                    clickedrect]})  # Updates Dragon's health and attack
                                        delete_creature_by_index(clickedrect)

                                        creaturename.clear()
                                        creaturelvl.clear()
                                        creaturehp.clear()
                                        creaturedefense.clear()
                                        creaturestrength.clear()
                                        creaturespecattack.clear()
                                        creaturespecattack.clear()
                                        creaturespeed.clear()
                                        creaturetier.clear()
                                        creatureimage.clear()
                                        creaturemove1.clear()
                                        creaturemove2.clear()
                                        creaturemove3.clear()
                                        creaturemove4.clear()
                                        creaturetype.clear()
                                        creatureexp.clear()

                                        creatures = load_creatures("creaturedata.txt")

                                        for creature in creatures:
                                            attributes = list(creature.values())
                                            creaturename.append(attributes[0])
                                            creaturelvl.append(attributes[1])
                                            creaturehp.append(attributes[2])
                                            creaturedefense.append(attributes[3])
                                            creaturestrength.append(attributes[4])
                                            creaturespecattack.append(attributes[5])
                                            creaturespeed.append(attributes[6])
                                            creaturetier.append(attributes[7])
                                            creatureimage.append(attributes[8])
                                            creaturemove1.append(attributes[9])
                                            creaturemove2.append(attributes[10])
                                            creaturemove3.append(attributes[11])
                                            creaturemove4.append(attributes[12])
                                            creaturetype.append(attributes[13])
                                            creatureexp.append(attributes[14])

                                        sound_effect = pygame.mixer.Sound(resource_path("audio/pokemonnoise.mp3"))
                                        pygame.mixer.music.set_volume(0.4)
                                        sound_effect.play()

                                        clickedrect = -1
                                else:
                                    tempcreature = {
                                        "name": creaturename[clickedrect],
                                        "lvl": creaturelvl[clickedrect],
                                        "hp": creaturehp[clickedrect],
                                        "defense": creaturedefense[clickedrect],
                                        "strength": creaturestrength[clickedrect],
                                        "special attack": creaturespecattack[clickedrect],
                                        "speed": creaturespeed[clickedrect],
                                        "tier": creaturetier[clickedrect],
                                        "beastimage": creatureimage[clickedrect],
                                        "move1": creaturemove1[clickedrect],
                                        "move2": creaturemove2[clickedrect],
                                        "move3": creaturemove3[clickedrect],
                                        "move4": creaturemove4[clickedrect],
                                        "type": creaturetype[clickedrect],
                                        "experience": creatureexp[clickedrect],
                                    }

                                    save_teamcreature(tempcreature, "teamdata.txt")
                                    delete_creature_by_index(clickedrect)

                                    creaturename.clear()
                                    creaturelvl.clear()
                                    creaturehp.clear()
                                    creaturedefense.clear()
                                    creaturestrength.clear()
                                    creaturespecattack.clear()
                                    creaturespecattack.clear()
                                    creaturespeed.clear()
                                    creaturetier.clear()
                                    creatureimage.clear()
                                    creaturemove1.clear()
                                    creaturemove2.clear()
                                    creaturemove3.clear()
                                    creaturemove4.clear()
                                    creaturetype.clear()
                                    creatureexp.clear()

                                    creatures = load_creatures("creaturedata.txt")

                                    for creature in creatures:
                                        attributes = list(creature.values())
                                        creaturename.append(attributes[0])
                                        creaturelvl.append(attributes[1])
                                        creaturehp.append(attributes[2])
                                        creaturedefense.append(attributes[3])
                                        creaturestrength.append(attributes[4])
                                        creaturespecattack.append(attributes[5])
                                        creaturespeed.append(attributes[6])
                                        creaturetier.append(attributes[7])
                                        creatureimage.append(attributes[8])
                                        creaturemove1.append(attributes[9])
                                        creaturemove2.append(attributes[10])
                                        creaturemove3.append(attributes[11])
                                        creaturemove4.append(attributes[12])
                                        creaturetype.append(attributes[13])
                                        creatureexp.append(attributes[14])

                                    sound_effect = pygame.mixer.Sound(resource_path("audio/pokemonnoise.mp3"))
                                    pygame.mixer.music.set_volume(0.4)
                                    sound_effect.play()

                            clickedrect = -1
                        if team2.collidepoint(mouse_pos):
                            teamcreatures = load_teamcreatures()
                            if (clickedrect != -1):
                                if(len(teamcreatures) >= 2):
                                    if (clickedrect > ((creaturepage - 1) * 36) - 1) and (clickedrect <= ((creaturepage * 36) - 1)):
                                        save_creature(teamcreatures[1], "creaturedata.txt")
                                        modify_teamcreature(1, {"name": creaturename[clickedrect], "lvl": creaturelvl[clickedrect], "hp": creaturehp[clickedrect], "defense": creaturedefense[clickedrect], "strength": creaturestrength[clickedrect], "special attack": creaturespecattack[clickedrect], "speed": creaturespeed[clickedrect], "tier": creaturetier[clickedrect], "beastimage": creatureimage[clickedrect], "move1": creaturemove1[clickedrect], "move2": creaturemove2[clickedrect], "move3": creaturemove3[clickedrect], "move4": creaturemove4[clickedrect], "type": creaturetype[clickedrect], "experience": creatureexp[clickedrect]})  # Updates Dragon's health and attack
                                        delete_creature_by_index(clickedrect)

                                        creaturename.clear()
                                        creaturelvl.clear()
                                        creaturehp.clear()
                                        creaturedefense.clear()
                                        creaturestrength.clear()
                                        creaturespecattack.clear()
                                        creaturespecattack.clear()
                                        creaturespeed.clear()
                                        creaturetier.clear()
                                        creatureimage.clear()
                                        creaturemove1.clear()
                                        creaturemove2.clear()
                                        creaturemove3.clear()
                                        creaturemove4.clear()
                                        creaturetype.clear()
                                        creatureexp.clear()

                                        creatures = load_creatures("creaturedata.txt")

                                        for creature in creatures:
                                            attributes = list(creature.values())
                                            creaturename.append(attributes[0])
                                            creaturelvl.append(attributes[1])
                                            creaturehp.append(attributes[2])
                                            creaturedefense.append(attributes[3])
                                            creaturestrength.append(attributes[4])
                                            creaturespecattack.append(attributes[5])
                                            creaturespeed.append(attributes[6])
                                            creaturetier.append(attributes[7])
                                            creatureimage.append(attributes[8])
                                            creaturemove1.append(attributes[9])
                                            creaturemove2.append(attributes[10])
                                            creaturemove3.append(attributes[11])
                                            creaturemove4.append(attributes[12])
                                            creaturetype.append(attributes[13])
                                            creatureexp.append(attributes[14])

                                        sound_effect = pygame.mixer.Sound(resource_path("audio/pokemonnoise.mp3"))
                                        pygame.mixer.music.set_volume(0.4)
                                        sound_effect.play()

                                        clickedrect = -1
                                else:
                                    tempcreature = {
                                        "name": creaturename[clickedrect],
                                        "lvl": creaturelvl[clickedrect],
                                        "hp": creaturehp[clickedrect],
                                        "defense": creaturedefense[clickedrect],
                                        "strength": creaturestrength[clickedrect],
                                        "special attack": creaturespecattack[clickedrect],
                                        "speed": creaturespeed[clickedrect],
                                        "tier": creaturetier[clickedrect],
                                        "beastimage": creatureimage[clickedrect],
                                        "move1": creaturemove1[clickedrect],
                                        "move2": creaturemove2[clickedrect],
                                        "move3": creaturemove3[clickedrect],
                                        "move4": creaturemove4[clickedrect],
                                        "type": creaturetype[clickedrect],
                                        "experience": creatureexp[clickedrect],
                                    }

                                    save_teamcreature(tempcreature, "teamdata.txt")
                                    delete_creature_by_index(clickedrect)

                                    creaturename.clear()
                                    creaturelvl.clear()
                                    creaturehp.clear()
                                    creaturedefense.clear()
                                    creaturestrength.clear()
                                    creaturespecattack.clear()
                                    creaturespecattack.clear()
                                    creaturespeed.clear()
                                    creaturetier.clear()
                                    creatureimage.clear()
                                    creaturemove1.clear()
                                    creaturemove2.clear()
                                    creaturemove3.clear()
                                    creaturemove4.clear()
                                    creaturetype.clear()
                                    creatureexp.clear()

                                    creatures = load_creatures("creaturedata.txt")

                                    for creature in creatures:
                                        attributes = list(creature.values())
                                        creaturename.append(attributes[0])
                                        creaturelvl.append(attributes[1])
                                        creaturehp.append(attributes[2])
                                        creaturedefense.append(attributes[3])
                                        creaturestrength.append(attributes[4])
                                        creaturespecattack.append(attributes[5])
                                        creaturespeed.append(attributes[6])
                                        creaturetier.append(attributes[7])
                                        creatureimage.append(attributes[8])
                                        creaturemove1.append(attributes[9])
                                        creaturemove2.append(attributes[10])
                                        creaturemove3.append(attributes[11])
                                        creaturemove4.append(attributes[12])
                                        creaturetype.append(attributes[13])
                                        creatureexp.append(attributes[14])

                                    sound_effect = pygame.mixer.Sound(resource_path("audio/pokemonnoise.mp3"))
                                    pygame.mixer.music.set_volume(0.4)
                                    sound_effect.play()

                            clickedrect = -1
                        if team3.collidepoint(mouse_pos):
                            teamcreatures = load_teamcreatures()
                            if (clickedrect != -1):
                                if(len(teamcreatures) >= 3):
                                    if (clickedrect > ((creaturepage - 1) * 36) - 1) and (clickedrect <= ((creaturepage * 36) - 1)):
                                        save_creature(teamcreatures[2], "creaturedata.txt")
                                        modify_teamcreature(2, {"name": creaturename[clickedrect], "lvl": creaturelvl[clickedrect], "hp": creaturehp[clickedrect], "defense": creaturedefense[clickedrect], "strength": creaturestrength[clickedrect], "special attack": creaturespecattack[clickedrect], "speed": creaturespeed[clickedrect], "tier": creaturetier[clickedrect], "beastimage": creatureimage[clickedrect], "move1": creaturemove1[clickedrect], "move2": creaturemove2[clickedrect], "move3": creaturemove3[clickedrect], "move4": creaturemove4[clickedrect], "type": creaturetype[clickedrect], "experience": creatureexp[clickedrect]})  # Updates Dragon's health and attack
                                        delete_creature_by_index(clickedrect)

                                        creaturename.clear()
                                        creaturelvl.clear()
                                        creaturehp.clear()
                                        creaturedefense.clear()
                                        creaturestrength.clear()
                                        creaturespecattack.clear()
                                        creaturespecattack.clear()
                                        creaturespeed.clear()
                                        creaturetier.clear()
                                        creatureimage.clear()
                                        creaturemove1.clear()
                                        creaturemove2.clear()
                                        creaturemove3.clear()
                                        creaturemove4.clear()
                                        creaturetype.clear()
                                        creatureexp.clear()

                                        creatures = load_creatures("creaturedata.txt")

                                        for creature in creatures:
                                            attributes = list(creature.values())
                                            creaturename.append(attributes[0])
                                            creaturelvl.append(attributes[1])
                                            creaturehp.append(attributes[2])
                                            creaturedefense.append(attributes[3])
                                            creaturestrength.append(attributes[4])
                                            creaturespecattack.append(attributes[5])
                                            creaturespeed.append(attributes[6])
                                            creaturetier.append(attributes[7])
                                            creatureimage.append(attributes[8])
                                            creaturemove1.append(attributes[9])
                                            creaturemove2.append(attributes[10])
                                            creaturemove3.append(attributes[11])
                                            creaturemove4.append(attributes[12])
                                            creaturetype.append(attributes[13])
                                            creatureexp.append(attributes[14])

                                        sound_effect = pygame.mixer.Sound(resource_path("audio/pokemonnoise.mp3"))
                                        pygame.mixer.music.set_volume(0.4)
                                        sound_effect.play()

                                        clickedrect = -1

                                else:
                                    tempcreature = {
                                        "name": creaturename[clickedrect],
                                        "lvl": creaturelvl[clickedrect],
                                        "hp": creaturehp[clickedrect],
                                        "defense": creaturedefense[clickedrect],
                                        "strength": creaturestrength[clickedrect],
                                        "special attack": creaturespecattack[clickedrect],
                                        "speed": creaturespeed[clickedrect],
                                        "tier": creaturetier[clickedrect],
                                        "beastimage": creatureimage[clickedrect],
                                        "move1": creaturemove1[clickedrect],
                                        "move2": creaturemove2[clickedrect],
                                        "move3": creaturemove3[clickedrect],
                                        "move4": creaturemove4[clickedrect],
                                        "type": creaturetype[clickedrect],
                                        "experience": creatureexp[clickedrect],
                                    }

                                    save_teamcreature(tempcreature, "teamdata.txt")
                                    delete_creature_by_index(clickedrect)

                                    creaturename.clear()
                                    creaturelvl.clear()
                                    creaturehp.clear()
                                    creaturedefense.clear()
                                    creaturestrength.clear()
                                    creaturespecattack.clear()
                                    creaturespecattack.clear()
                                    creaturespeed.clear()
                                    creaturetier.clear()
                                    creatureimage.clear()
                                    creaturemove1.clear()
                                    creaturemove2.clear()
                                    creaturemove3.clear()
                                    creaturemove4.clear()
                                    creaturetype.clear()
                                    creatureexp.clear()

                                    creatures = load_creatures("creaturedata.txt")

                                    for creature in creatures:
                                        attributes = list(creature.values())
                                        creaturename.append(attributes[0])
                                        creaturelvl.append(attributes[1])
                                        creaturehp.append(attributes[2])
                                        creaturedefense.append(attributes[3])
                                        creaturestrength.append(attributes[4])
                                        creaturespecattack.append(attributes[5])
                                        creaturespeed.append(attributes[6])
                                        creaturetier.append(attributes[7])
                                        creatureimage.append(attributes[8])
                                        creaturemove1.append(attributes[9])
                                        creaturemove2.append(attributes[10])
                                        creaturemove3.append(attributes[11])
                                        creaturemove4.append(attributes[12])
                                        creaturetype.append(attributes[13])
                                        creatureexp.append(attributes[14])

                                    sound_effect = pygame.mixer.Sound(resource_path("audio/pokemonnoise.mp3"))
                                    pygame.mixer.music.set_volume(0.4)
                                    sound_effect.play()

                            clickedrect = -1
                        if team1xrect.collidepoint(mouse_pos):
                            teamcreatures = load_teamcreatures()
                            sound_effect = pygame.mixer.Sound(resource_path("audio/scifinoise.mp3"))
                            sound_effect.play()
                            if (len(teamcreatures) >= 1):
                                teamattributes = list(teamcreatures[0].values())
                                save_creature(teamcreatures[0], "creaturedata.txt")
                                creaturename.clear()
                                creaturelvl.clear()
                                creaturehp.clear()
                                creaturedefense.clear()
                                creaturestrength.clear()
                                creaturespecattack.clear()
                                creaturespecattack.clear()
                                creaturespeed.clear()
                                creaturetier.clear()
                                creatureimage.clear()
                                creaturemove1.clear()
                                creaturemove2.clear()
                                creaturemove3.clear()
                                creaturemove4.clear()
                                creaturetype.clear()
                                creatureexp.clear()

                                creatures = load_creatures("creaturedata.txt")

                                for creature in creatures:
                                    attributes = list(creature.values())
                                    creaturename.append(attributes[0])
                                    creaturelvl.append(attributes[1])
                                    creaturehp.append(attributes[2])
                                    creaturedefense.append(attributes[3])
                                    creaturestrength.append(attributes[4])
                                    creaturespecattack.append(attributes[5])
                                    creaturespeed.append(attributes[6])
                                    creaturetier.append(attributes[7])
                                    creatureimage.append(attributes[8])
                                    creaturemove1.append(attributes[9])
                                    creaturemove2.append(attributes[10])
                                    creaturemove3.append(attributes[11])
                                    creaturemove4.append(attributes[12])
                                    creaturetype.append(attributes[13])
                                    creatureexp.append(attributes[14])
                                delete_creature_by_index(0, "teamdata.txt")
                        if team2xrect.collidepoint(mouse_pos):
                            sound_effect = pygame.mixer.Sound(resource_path("audio/scifinoise.mp3"))
                            sound_effect.play()
                            teamcreatures = load_teamcreatures()
                            if (len(teamcreatures) >= 2):
                                teamattributes = list(teamcreatures[1].values())
                                save_creature(teamcreatures[1], "creaturedata.txt")
                                creaturename.clear()
                                creaturelvl.clear()
                                creaturehp.clear()
                                creaturedefense.clear()
                                creaturestrength.clear()
                                creaturespecattack.clear()
                                creaturespecattack.clear()
                                creaturespeed.clear()
                                creaturetier.clear()
                                creatureimage.clear()
                                creaturemove1.clear()
                                creaturemove2.clear()
                                creaturemove3.clear()
                                creaturemove4.clear()
                                creaturetype.clear()
                                creatureexp.clear()

                                creatures = load_creatures("creaturedata.txt")

                                for creature in creatures:
                                    attributes = list(creature.values())
                                    creaturename.append(attributes[0])
                                    creaturelvl.append(attributes[1])
                                    creaturehp.append(attributes[2])
                                    creaturedefense.append(attributes[3])
                                    creaturestrength.append(attributes[4])
                                    creaturespecattack.append(attributes[5])
                                    creaturespeed.append(attributes[6])
                                    creaturetier.append(attributes[7])
                                    creatureimage.append(attributes[8])
                                    creaturemove1.append(attributes[9])
                                    creaturemove2.append(attributes[10])
                                    creaturemove3.append(attributes[11])
                                    creaturemove4.append(attributes[12])
                                    creaturetype.append(attributes[13])
                                    creatureexp.append(attributes[14])
                                delete_creature_by_index(1, "teamdata.txt")
                        if team3xrect.collidepoint(mouse_pos):
                            sound_effect = pygame.mixer.Sound(resource_path("audio/scifinoise.mp3"))
                            sound_effect.play()
                            teamcreatures = load_teamcreatures()
                            if (len(teamcreatures) >= 3):
                                teamattributes = list(teamcreatures[2].values())
                                save_creature(teamcreatures[2], "creaturedata.txt")
                                creaturename.clear()
                                creaturelvl.clear()
                                creaturehp.clear()
                                creaturedefense.clear()
                                creaturestrength.clear()
                                creaturespecattack.clear()
                                creaturespecattack.clear()
                                creaturespeed.clear()
                                creaturetier.clear()
                                creatureimage.clear()
                                creaturemove1.clear()
                                creaturemove2.clear()
                                creaturemove3.clear()
                                creaturemove4.clear()
                                creaturetype.clear()
                                creatureexp.clear()

                                creatures = load_creatures("creaturedata.txt")

                                for creature in creatures:
                                    attributes = list(creature.values())
                                    creaturename.append(attributes[0])
                                    creaturelvl.append(attributes[1])
                                    creaturehp.append(attributes[2])
                                    creaturedefense.append(attributes[3])
                                    creaturestrength.append(attributes[4])
                                    creaturespecattack.append(attributes[5])
                                    creaturespeed.append(attributes[6])
                                    creaturetier.append(attributes[7])
                                    creatureimage.append(attributes[8])
                                    creaturemove1.append(attributes[9])
                                    creaturemove2.append(attributes[10])
                                    creaturemove3.append(attributes[11])
                                    creaturemove4.append(attributes[12])
                                    creaturetype.append(attributes[13])
                                    creatureexp.append(attributes[14])
                                delete_creature_by_index(2, "teamdata.txt")
                        if trashcanrect.collidepoint(mouse_pos):
                            if (clickedrect != -1):
                                if (clickedrect > ((creaturepage - 1) * 36) - 1) and (
                                        clickedrect <= ((creaturepage * 36) - 1)):
                                    delete_creature_by_index(clickedrect)
                                    randomgem = random.randint(1, int(creaturelvl[clickedrect] / 4) + 2)
                                    with open(resource_path("gamedata.txt"), "r") as file:
                                        lines = file.readlines()
                                        lines[1] = f"gem = {gem + randomgem}\n"
                                    with open(resource_path("gamedata.txt"), "w") as file:
                                        file.writelines(lines)
                                    sound_effect = pygame.mixer.Sound(resource_path("audio/creaturetrashnoise.mp3"))
                                    sound_effect.play()
                                    looptimeg = pygame.time.get_ticks() + 700
                                    timerg = pygame.time.get_ticks()
                                    while (looptimeg > timerg):
                                        draw_text('gained ' + str(randomgem) + " gems", font24, PURPLE, DISPLAYSURF,
                                                  1388, 710)
                                        timerg = pygame.time.get_ticks()
                                        for event in pygame.event.get():
                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                print("stop clicking so much")
                                        pygame.display.update()

                                    creaturename.clear()
                                    creaturelvl.clear()
                                    creaturehp.clear()
                                    creaturedefense.clear()
                                    creaturestrength.clear()
                                    creaturespecattack.clear()
                                    creaturespecattack.clear()
                                    creaturespeed.clear()
                                    creaturetier.clear()
                                    creatureimage.clear()
                                    creaturemove1.clear()
                                    creaturemove2.clear()
                                    creaturemove3.clear()
                                    creaturemove4.clear()
                                    creaturetype.clear()
                                    creatureexp.clear()

                                    creatures = load_creatures("creaturedata.txt")

                                    for creature in creatures:
                                        attributes = list(creature.values())
                                        creaturename.append(attributes[0])
                                        creaturelvl.append(attributes[1])
                                        creaturehp.append(attributes[2])
                                        creaturedefense.append(attributes[3])
                                        creaturestrength.append(attributes[4])
                                        creaturespecattack.append(attributes[5])
                                        creaturespeed.append(attributes[6])
                                        creaturetier.append(attributes[7])
                                        creatureimage.append(attributes[8])
                                        creaturemove1.append(attributes[9])
                                        creaturemove2.append(attributes[10])
                                        creaturemove3.append(attributes[11])
                                        creaturemove4.append(attributes[12])
                                        creaturetype.append(attributes[13])
                                        creatureexp.append(attributes[14])
                                    clickedrect = -1
                pygame.display.update()

########################################################################################################################
class colleseum(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.colleseumloop = True
        self.colleseumcombat()
########################################################################################################################
    def colleseumcombat(self):
        global FaderBool
        global Fader
        global textFader
        opacityvalue = 1
        opacitybool = True
        startTime = pygame.time.get_ticks()
        self.gamescene = 1
        mouse_pos = pygame.mouse.get_pos()
        pygame.mixer.music.load(resource_path("audio/rebornmusic.mp3"))
        pygame.mixer.music.queue(resource_path("audio/colleseummusic1.mp3"))
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        print("Stash initialized")
        global textFader
        global characterName
        global gold
        global gem
        video = cv2.VideoCapture(resource_path("video/glowparticlevideo.mp4"))
        startTime = pygame.time.get_ticks()
        endTime = startTime + 3000
        npcdifficulty = 2
########################################################################################################################
        while self.colleseumloop:
            rainbowcolor1 = int((math.sin(startTime * 0.002) + 1) * 127.5)
            rainbowcolor2 = int((math.sin(startTime * 0.003 + 2) + 1) * 127.5)
            rainbowcolor3 = int((math.sin(startTime * 0.005 + 2) + 1) * 127.5)
            rainbow = (rainbowcolor1, rainbowcolor2, rainbowcolor3)
            with open(resource_path("gamedata.txt"), "r") as file:
                lines = file.readlines()
                goldline = lines[0].strip()
                goldline = goldline[7:]
                gemline = lines[1].strip()
                gemline = gemline[6:]
                gold = int(goldline)
                gem = int(gemline)

            startTime = pygame.time.get_ticks()
            mouseX, mouseY = pygame.mouse.get_pos()

            if(opacitybool == True):
                opacityvalue = opacityvalue + 1
            if(opacitybool == False):
                opacityvalue = opacityvalue - 1
            if(opacityvalue >= 250):
                opacitybool = False
            if (opacityvalue <= 5):
                opacitybool = True
########################################################################################################################
            if (self.gamescene == 1):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image275, (197, 100))

                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))

                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 120, 70)

                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 0 <= mouseX <= 1920 and 250 <= mouseY <= 1080:
                            sound_effect = pygame.mixer.Sound(resource_path("audio/vaultopen.mp3"))
                            sound_effect.play()
                            self.gamescene = self.gamescene + 1
                        if returnarrowrect.collidepoint(mouse_pos):
                            transition(6)
                            video.release()
                            self.colleseumloop = False
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            video.release()
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()
                pygame.display.update()
            if (self.gamescene == 2):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image275, (197, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                draw_text_center('To live on your knees, or die standing.', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('which do you desire?', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 925)


                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))
                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 120, 70)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 0 <= mouseX <= 1920 and 250 <= mouseY <= 1080:
                            sound_effect = pygame.mixer.Sound(resource_path("audio/vaultopen.mp3"))
                            sound_effect.play()
                            self.gamescene = self.gamescene + 1
                        if returnarrowrect.collidepoint(mouse_pos):
                            transition(6)
                            video.release()
                            self.colleseumloop = False
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            video.release()
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()
                pygame.display.update()
            if (self.gamescene == 3):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image275, (197, 100))

                ret, frame = video.read()
                if not ret:
                    video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    continue  # Continue to the next loop iteration
                frame = cv2.resize(frame, (1550, 880))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_surface = pygame.surfarray.make_surface(frame)
                frame_surface = pygame.transform.rotate(frame_surface, -90)  # Rotate if necessary
                frame_surface = pygame.transform.flip(frame_surface, True, False)
                frame_surface.set_alpha(100)

                DISPLAYSURF.blit(frame_surface, (190, 100))
                DISPLAYSURF.blit(image276, (630, 190))

                choice1 = pygame.Rect(691, 290, 190, 300)
                choice2 = pygame.Rect(896, 290, 190, 300)
                choice3 = pygame.Rect(1105, 290, 190, 300)

                mouseX, mouseY = pygame.mouse.get_pos()
                print("x and y = " + str(mouseX) + " " + str(mouseY))

                if choice1.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image277, (630, 190))
                if choice2.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image278, (630, 190))
                if choice3.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image279, (630, 190))

                DISPLAYSURF.blit(redgloww, (mouseX - 47, mouseY - 44))

                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))
                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 120, 70)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 0 <= mouseX <= 1920 and 250 <= mouseY <= 1080:
                            sound_effect = pygame.mixer.Sound(resource_path("audio/vaultopen.mp3"))
                            sound_effect.play()
                            self.gamescene = self.gamescene + 1
                        if returnarrowrect.collidepoint(mouse_pos):
                            transition(6)
                            video.release()
                            self.colleseumloop = False
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            video.release()
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()
                        if choice1.collidepoint(mouse_pos):
                            transition(6)
                            sound_effect = pygame.mixer.Sound(resource_path("audio/underwaterimpact.mp3"))
                            sound_effect.play()
                            self.gamescene = 10
                        if choice2.collidepoint(mouse_pos):
                            transition(6)
                        if choice3.collidepoint(mouse_pos):
                            transition(6)
                pygame.display.update()

            if (self.gamescene == 10):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image280, (197, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                draw_text_center('Click to Begin', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 890)

                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))
                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 120, 70)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 0 <= mouseX <= 1920 and 250 <= mouseY <= 1080:
                            sound_effect = pygame.mixer.Sound(resource_path("audio/vaultopen.mp3"))
                            sound_effect.play()
                            startTime = pygame.time.get_ticks()
                            endTime = startTime + 3000
                            npcdifficulty = random.randint(1,6)
                            self.gamescene = self.gamescene + 1
                        if returnarrowrect.collidepoint(mouse_pos):
                            transition(6)
                            video.release()
                            self.colleseumloop = False
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            video.release()
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()
                pygame.display.update()
            if (self.gamescene == 11):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image280, (197, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                draw_text_center('Generating Opponent...', font22, VELVET, DISPLAYSURF, halfdisplay, 290)

                if(endTime > startTime):
                    startTime = pygame.time.get_ticks()
                    randomcipher = ""
                    loop = 10
                    while(loop > 0):
                        loop = loop - 1
                        randomcipher = randomcipher+(random.choice(string.ascii_letters))

                    draw_text_center(randomcipher, font22, VELVET, DISPLAYSURF, halfdisplay, 390)

                if(endTime < startTime):
                    if(npcdifficulty == 1):
                        draw_text_center("Difficulty: Easy", font22, WHITE, DISPLAYSURF, halfdisplay, 390)
                    if(npcdifficulty == 2):
                        draw_text_center("Difficulty: Medium", font22, LIGHTYELLOW, DISPLAYSURF, halfdisplay, 390)
                    if(npcdifficulty == 3):
                        draw_text_center("Difficulty: Hard", font22, EMERALD, DISPLAYSURF, halfdisplay, 390)
                    if(npcdifficulty == 4):
                        draw_text_center("Difficulty: Try Hard", font22, DARKGEMBLUE, DISPLAYSURF, halfdisplay, 390)
                    if(npcdifficulty == 5):
                        draw_text_center("Difficulty: Insane", font22, RED, DISPLAYSURF, halfdisplay, 390)
                    if(npcdifficulty == 6):
                        draw_text_center("Difficulty: God", font22, BLACK, DISPLAYSURF, halfdisplay, 390)

                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))
                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 120, 70)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if (endTime < startTime):
                            if 0 <= mouseX <= 1920 and 250 <= mouseY <= 1080:
                                sound_effect = pygame.mixer.Sound(resource_path("audio/vaultopen.mp3"))
                                sound_effect.play()
                                self.gamescene = self.gamescene + 1
                        if returnarrowrect.collidepoint(mouse_pos):
                            transition(6)
                            video.release()
                            self.colleseumloop = False
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            video.release()
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()
                pygame.display.update()
            if (self.gamescene == 12):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image280, (197, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                draw_text_center('Battle!', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 890)

                mouse_pos = pygame.mouse.get_pos()
                draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
                DISPLAYSURF.blit(image164, (198, 110))
                xrect = pygame.Rect(1680, 123, 35, 35)
                returnarrowrect = pygame.Rect(153, 110, 120, 70)
                if xrect.collidepoint(mouse_pos):
                    draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
                if returnarrowrect.collidepoint(mouse_pos):
                    DISPLAYSURF.blit(image165, (198, 110))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 0 <= mouseX <= 1920 and 250 <= mouseY <= 1080:
                            sound_effect = pygame.mixer.Sound(resource_path("audio/vaultopen.mp3"))
                            sound_effect.play()
                            self.gamescene = self.gamescene + 1
                        if returnarrowrect.collidepoint(mouse_pos):
                            transition(6)
                            video.release()
                            self.colleseumloop = False
                        if xrect.collidepoint(mouse_pos):
                            print("Quit clicked")
                            video.release()
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()
                pygame.display.update()
########################################################################################################################