import pygame
from pygame.locals import *
import sys
import math
import moviepy.editor
import random
import cv2
pygame.init()
pygame.mixer.init()
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
imagebeast1 = pygame.image.load('f1.png')
imagebeast2 = pygame.image.load('f2.png')
imagebeast3 = pygame.image.load('f3.png')
imagebeast4 = pygame.image.load('f4.png')
imagebeast5 = pygame.image.load('f5.png')
imagebeast6 = pygame.image.load('f6.png')
imagebeast7 = pygame.image.load('f7.png')
imagebeast8 = pygame.image.load('f8.png')
imagebeast9 = pygame.image.load('f9.png')
imagebeast10 = pygame.image.load('f10.png')
imagebeast11 = pygame.image.load('f11.png')
imagebeast12 = pygame.image.load('f12.png')
imagebeast13 = pygame.image.load('f13.png')
imagebeast14 = pygame.image.load('f14.png')
imagebeast15 = pygame.image.load('f15.png')
imagebeast16 = pygame.image.load('f16.png')
imagebeast17 = pygame.image.load('f17.png')
imagebeast18 = pygame.image.load('f18.png')
imagebeast19 = pygame.image.load('f19.png')
imagebeast20 = pygame.image.load('f20.png')
imagebeast21 = pygame.image.load('f21.png')
imagebeast22 = pygame.image.load('f22.png')
imagebeast23 = pygame.image.load('f23.png')
imagebeast24 = pygame.image.load('f24.png')
imagebeast25 = pygame.image.load('f25.png')
imagebeast26 = pygame.image.load('f26.png')
imagebeast27 = pygame.image.load('f27.png')
imagebeast28 = pygame.image.load('f28.png')
imagebeast29 = pygame.image.load('f29.png')
imagebeast30 = pygame.image.load('f30.png')
imagebeast31 = pygame.image.load('f31.png')
imagebeast32 = pygame.image.load('f32.png')
imagebeast33 = pygame.image.load('f33.png')
imagebeast34 = pygame.image.load('f34.png')
imagebeast35 = pygame.image.load('f35.png')
imagebeast36 = pygame.image.load('f36.png')
imagebeast37 = pygame.image.load('f37.png')
imagebeast38 = pygame.image.load('f38.png')
imagebeast39 = pygame.image.load('f39.png')
imagebeast40 = pygame.image.load('f40.png')
imagebeast41 = pygame.image.load('f41.png')
imagebeast42 = pygame.image.load('f42.png')
imagebeast43 = pygame.image.load('f43.png')
imagebeast44 = pygame.image.load('f44.png')
imagebeast45 = pygame.image.load('f45.png')
imagebeast46 = pygame.image.load('f46.png')
imagebeast47 = pygame.image.load('f47.png')
imagebeast48 = pygame.image.load('f48.png')
imagebeast49 = pygame.image.load('f49.png')
imagebeast50 = pygame.image.load('f50.png')
imagebeast51 = pygame.image.load('f51.png')
imagebeast52 = pygame.image.load('f52.png')
imagebeast53 = pygame.image.load('f53.png')
imagebeast54 = pygame.image.load('f54.png')
imagebeast55 = pygame.image.load('f55.png')
imagebeast56 = pygame.image.load('f56.png')
imagebeast57 = pygame.image.load('f57.png')
imagebeast58 = pygame.image.load('f58.png')
imagebeast59 = pygame.image.load('f59.png')
imagebeast60 = pygame.image.load('f60.png')
imagebeast61 = pygame.image.load('f61.png')
imagebeast62 = pygame.image.load('f62.png')
imagebeast63 = pygame.image.load('f63.png')
imagebeast64 = pygame.image.load('f64.png')
imagebeast65 = pygame.image.load('f65.png')
imagebeast66 = pygame.image.load('f66.png')
imagebeast67 = pygame.image.load('f67.png')
imagebeast68 = pygame.image.load('f68.png')
imagebeast69 = pygame.image.load('f69.png')
imagebeast70 = pygame.image.load('f70.png')
imagebeast71 = pygame.image.load('f71.png')
imagebeast72 = pygame.image.load('f72.png')
imagebeast73 = pygame.image.load('f73.png')
imagebeast74 = pygame.image.load('f74.png')
imagebeast75 = pygame.image.load('f75.png')
imagebeast76 = pygame.image.load('f76.png')



beasts = [imagebeast1,imagebeast2,imagebeast3,imagebeast4,imagebeast5,imagebeast6,imagebeast7,imagebeast8,imagebeast9,imagebeast10,
imagebeast11,imagebeast12,imagebeast13,imagebeast14,imagebeast15,imagebeast16,imagebeast17,imagebeast18,imagebeast19,imagebeast20,
imagebeast21,imagebeast22,imagebeast23,imagebeast24,imagebeast25,imagebeast26,imagebeast27,imagebeast28,imagebeast29,imagebeast30,
imagebeast31,imagebeast32,imagebeast33,imagebeast34,imagebeast35,imagebeast36,imagebeast37,imagebeast38,imagebeast39,imagebeast40,
imagebeast41,imagebeast42,imagebeast43,imagebeast44,imagebeast45,imagebeast46,imagebeast47,imagebeast48,imagebeast49,imagebeast50,
imagebeast51,imagebeast52,imagebeast53,imagebeast54,imagebeast55,imagebeast56,imagebeast57,imagebeast58,imagebeast59,imagebeast60,
imagebeast61,imagebeast62,imagebeast63,imagebeast64,imagebeast65,imagebeast66,imagebeast67,imagebeast68,imagebeast69,imagebeast70,
imagebeast71,imagebeast72,imagebeast73,imagebeast74,imagebeast75,imagebeast76]

#Each element corresponds to the following
#0 - crate level
#1 - hp
#2 - defense
#3 - strength
#4 - spec attack
#5 - speed
#6 - Tier
#7 - Name
#8 - image location with beast[]
beastattributes = [
    [1, 4, 4, 4, 4, 4, 1, "gallo", 0],
    [25, 4, 4, 4, 4, 4, 2, "gallodus", 1],
    [1, 7, 12, 6, 3, 5, 1, "Krillith", 2],
    [1, 4, 4, 9, 9, 7, 1, "Lux", 3],
    [1, 8, 13, 5, 3, 2, 1, "Verdescent", 4],
    [1, 7, 3, 5, 7, 7, 1, "axo", 5],
    [1, 5, 5, 5, 10, 6, 1, "PoisonLight Goop", 6],
    [1, 4, 3, 3, 3, 12, 1, "Aether Terror", 7],
    [1, 5, 3, 9, 3, 13, 1, "Mimi", 8],
    [1, 5, 11, 1, 3, 1, 1, "Nauty", 9],
    [1, 5, 9, 2, 7, 4, 1, "Pearlos", 10],
    [1, 7, 5, 5, 5, 4, 1, "Dust Pill", 11],
    [1, 10, 3, 2, 10, 2, 1, "Assimule", 12],
    [1, 4, 6, 7, 7, 8, 1, "Crowpeck", 13],
    [1, 8, 5, 9, 2, 7, 1, "Depthtracer", 14],
    [1, 6, 4, 11, 1, 6, 1, "Nautizark", 15],
    [1, 5, 3, 1, 12, 6, 1, "Ripple", 16],
    [1, 5, 4, 6, 7, 4, 1, "Marene", 17],
    [1, 3, 14, 6, 2, 3, 1, "Scalex", 18],
    [1, 5, 4, 8, 9, 9, 1, "Abyssal Newt", 19],
    [1, 7, 3, 11, 3, 3, 1, "Hollow Mimic", 20],
    [1, 4, 4, 7, 7, 4, 1, "Corpse Puppet", 21],
    [1, 8, 8, 5, 5, 1, 1, "Amica", 22],
    [1, 3, 3, 5, 3, 6, 1, "Noodle", 23],
    [1, 6, 4, 5, 5, 8, 1, "Weiner", 24],
    [1, 7, 6, 7, 10, 7, 1, "Gleamfin", 25],
    [1, 6, 6, 10, 7, 9, 1, "Mistfin", 26],
    [1, 6, 7, 7, 10, 7, 1, "Magmafin", 27],
    [25, 7, 6, 7, 10, 7, 2, "AquaWalker", 28],
    [25, 6, 7, 7, 10, 7, 2, "MagmaWalker", 29],
    [25, 7, 3, 5, 7, 7, 2, "Axolus", 30],
    [50, 7, 3, 5, 7, 7, 3, "Axoluminous", 31],
    [25, 7, 7, 7, 7, 7, 2, "Sacred Lumenous", 32],
    [25, 8, 13, 5, 3, 2, 2, "Terra Verdescence", 33],
    [1, 6, 6, 13, 13, 9, 1, "Snowblossom", 34],
    [25, 5, 5, 5, 10, 6, 2, "PoisonLight Carp", 35],
    [25, 10, 3, 2, 10, 2, 2, "Assimilation", 36],
    [25, 8, 5, 9, 2, 7, 2, "DepthWing", 37],
    [25, 5, 11, 1, 3, 1, 2, "Nautileous", 38],
    [25, 5, 3, 1, 12, 6, 2, "Ripshade", 39],
    [25, 6, 4, 11, 1, 6, 2, "Hydrosark", 40],
    [25, 5, 4, 6, 7, 4, 2, "Marenara", 41],
    [25, 3, 14, 6, 2, 3, 2, "Scalex Ripper", 42],
    [25, 7, 3, 11, 3, 3, 2, "Ethereal Mimic", 43],
    [1, 4, 5, 5, 5, 4, 1, "Undead Soul", 44],
    [1, 7, 7, 5, 12, 11, 1, "Cinderfrost", 45],
    [1, 7, 7, 7, 7, 7, 1, "Sacred Lumen", 46],
    [1, 10, 10, 7, 1, 4, 1, "FrostTip", 47],
    [1, 10, 5, 14, 1, 3, 1, "Cryolo", 48],
    [1, 3, 3, 13, 3, 8, 1, "minnowClaw", 49],
    [25, 5, 3, 9, 3, 13, 2, "Clyrix", 50],
    [50, 4, 4, 9, 9, 7, 3, "Luxerous", 51],
    [25, 8, 8, 8, 4, 4, 2, "Seafrost", 52],
    [25, 10, 5, 14, 1, 3, 2, "Cryolodon", 53],
    [25, 5, 3, 9, 3, 13, 2, "Shadow Wing", 54],
    [1, 8, 5, 3, 8, 5, 1, "Shade Wing", 55],
    [50, 3, 3, 13, 3, 8, 3, "Brineclaw", 56],
    [25, 3, 3, 13, 3, 8, 2, "SereneClaw", 57],
    [50, 10, 10, 7, 1, 4, 3, "FrostHyperion", 58],
    [25, 10, 10, 7, 1, 4, 2, "Frosthorn", 59],
    [25, 7, 7, 5, 12, 11, 3, "Cinderglace", 60],
    [50, 5, 5, 5, 10, 6, 3, "PoisonLight Wyvern", 61],
    [25, 5, 5, 1, 9, 5, 2, "Sirenyx", 62],
    [75, 7, 7, 7, 7, 7, 4, "Opheus The Forbidden", 63],
    [50, 5, 4, 8, 9, 9, 3, "Abyssal Basilisk", 64],
    [50, 4, 4, 7, 7, 4, 3, "Corpse Puppet King", 65],
    [50, 8, 5, 9, 2, 7, 3, "Depth Lord", 66],
    [50, 6, 6, 10, 7, 9, 3, "Mistrace", 67],
    [50, 6, 6, 13, 13, 9, 3, "Phoenix of Death", 68],
    [50, 6, 6, 13, 13, 9, 3, "Phoenix of Life", 69],
    [50, 7, 7, 7, 7, 7, 3, "Sacred Oceanix", 70],
    [50, 7, 6, 7, 10, 7, 3, "Aqua Dragon", 71],
    [50, 6, 7, 7, 10, 7, 3, "Flame Dragon", 72],
    [25, 5, 4, 8, 9, 9, 2, "Abyssal Viper", 73],
    [25, 4, 5, 5, 5, 4, 2, "Undead Emperor", 74],
    [50, 9, 9, 9, 9, 9, 3, "Gigantorok", 75]
]



image00 = pygame.image.load('bubble.png')
image00 = pygame.transform.scale(image00, (15, 15))
image01 = pygame.image.load('bubble.png')
image01 = pygame.transform.scale(image01, (25, 25))
image02 = pygame.image.load('bubble.png')
image02 = pygame.transform.scale(image02, (35, 35))

imagen6 = pygame.image.load('goldglow.png')
imagen6 = pygame.transform.scale(imagen6, (100, 100))

imagewhite = pygame.image.load('blankwhitepage.jpg')
imagewhitehalo = pygame.image.load('whiteglowhalo.png')
imagewhiteground = pygame.image.load('whitehaloground.png')
imagewhitecircle = pygame.image.load('whitehalocircle.png')

image4 = pygame.image.load('blackscreen.jpg')
image4 = pygame.transform.scale(image4, (3920, 1080))
image30 = pygame.image.load('skipbutton.png')
image30 = pygame.transform.scale(image30, (90, 50))
image31 = pygame.image.load('purplerect.png')
image31 = pygame.transform.scale(image31, (50, 80))
image42 = pygame.image.load('yellowdiamond.png')
image42 = pygame.transform.scale(image42, (30, 30))
image52 = pygame.image.load('knightwalkthrough.png')
image52 = pygame.transform.scale(image52, (500, 250))
image53 = pygame.image.load('speechbubble.png')
image53 = pygame.transform.scale(image53, (500, 230))
image56 = pygame.image.load('blueglow.png')
image56 = pygame.transform.scale(image56, (100, 100))
#######paimons shop images##############
image58 = pygame.image.load('paimonshop.webp')
image58 = pygame.transform.scale(image58, (1550, 870))
image59 = pygame.image.load('paimonmenushop.png')
image59 = pygame.transform.scale(image59, (900, 900))
imageBlack = pygame.image.load('blackscreen.jpg')
imageBlack = pygame.transform.scale(imageBlack, (765, 700))
image60 = pygame.image.load('returnarrow.png')
image60 = pygame.transform.scale(image60, (75, 75))
image61 = pygame.image.load('whitereturnarrow.png')
image61 = pygame.transform.scale(image61, (75, 75))
########################################################################################################################
image62 = pygame.image.load('purplepotion.png')
image62 = pygame.transform.scale(image62, (50, 50))
image63 = pygame.image.load('bluepotion.png')
image63 = pygame.transform.scale(image63, (50, 50))
image64 = pygame.image.load('greenpotion.png')
image64 = pygame.transform.scale(image64, (50, 50))
image65 = pygame.image.load('whitepotion.png')
image65 = pygame.transform.scale(image65, (50, 50))
image66 = pygame.image.load('healingpotion.png')
image66 = pygame.transform.scale(image66, (50, 50))
image67 = pygame.image.load('apple.png')
image67 = pygame.transform.scale(image67, (50, 50))
image68 = pygame.image.load('goldenapple.png')
image68 = pygame.transform.scale(image68, (50, 50))

image69 = pygame.image.load('enchantedbook1.png')
image69 = pygame.transform.scale(image69, (50, 50))
image70 = pygame.image.load('whiteamulet.png')
image70 = pygame.transform.scale(image70, (50, 50))
image71 = pygame.image.load('redamulet.png')
image71 = pygame.transform.scale(image71, (50, 50))
image72 = pygame.image.load('purpleamulet.png')
image72 = pygame.transform.scale(image72, (50, 50))
image73 = pygame.image.load('underwatercrown.png')
image73 = pygame.transform.scale(image73, (50, 50))
image74 = pygame.image.load('mysterybag.png')
image74 = pygame.transform.scale(image74, (50, 50))
image75 = pygame.image.load('supermysterybag.png')
image75 = pygame.transform.scale(image75, (50, 50))

image76 = pygame.image.load('rustysword.png')
image76 = pygame.transform.scale(image76, (50, 50))
image77 = pygame.image.load('bronzesword.png')
image77 = pygame.transform.scale(image77, (50, 50))
image78 = pygame.image.load('Ironsword.png')
image78 = pygame.transform.scale(image78, (50, 50))
image79 = pygame.image.load('diamondsword.png')
image79 = pygame.transform.scale(image79, (50, 50))
image80 = pygame.image.load('simplestaff.png')
image80 = pygame.transform.scale(image80, (50, 50))
image81 = pygame.image.load('leatherhelmet.png')
image81 = pygame.transform.scale(image81, (50, 50))
image82 = pygame.image.load('leatherchestplate.png')
image82 = pygame.transform.scale(image82, (50, 50))

imageesneak83 = pygame.image.load('leatherpants.png')
imageesneak83 = pygame.transform.scale(imageesneak83, (50, 50))
imageesneak84 = pygame.image.load('leatherboots.png')
imageesneak84 = pygame.transform.scale(imageesneak84, (50, 50))
image83 = pygame.image.load('metalhelmet.png')
image83 = pygame.transform.scale(image83, (50, 50))
image84 = pygame.image.load('metalchestplate.png')
image84 = pygame.transform.scale(image84, (50, 50))
image85 = pygame.image.load('metalgreeves.png')
image85 = pygame.transform.scale(image85, (50, 50))
image86 = pygame.image.load('metalboots.png')
image86 = pygame.transform.scale(image86, (50, 50))
image87 = pygame.image.load('coralhelmet.png')
image87 = pygame.transform.scale(image87, (50, 50))

image88 = pygame.image.load('coralchestplate.png')
image88 = pygame.transform.scale(image88, (50, 50))
image89 = pygame.image.load('coralpants.png')
image89 = pygame.transform.scale(image89, (50, 50))
image90 = pygame.image.load('coralshoes.png')
image90 = pygame.transform.scale(image90, (50, 50))
image91 = pygame.image.load('expouch.png')
image91 = pygame.transform.scale(image91, (50, 50))
image92 = pygame.image.load('largeexppouch.png')
image92 = pygame.transform.scale(image92, (50, 50))
image93 = pygame.image.load('timedilator.png')
image93 = pygame.transform.scale(image93, (50, 50))
########################################################################################################################
image94 = pygame.image.load('purplepotion.png')
image94 = pygame.transform.scale(image94, (350, 350))
image95 = pygame.image.load('enchantedbook1.png')
image95 = pygame.transform.scale(image95, (350, 350))
image96 = pygame.image.load('rustysword.png')
image96 = pygame.transform.scale(image96, (350, 350))
image97 = pygame.image.load('leatherpants.png')
image97 = pygame.transform.scale(image97, (350, 350))
image98 = pygame.image.load('coralchestplate.png')
image98 = pygame.transform.scale(image98, (350, 350))

image99 = pygame.image.load('bluepotion.png')
image99 = pygame.transform.scale(image99, (350, 350))
image100 = pygame.image.load('whiteamulet.png')
image100 = pygame.transform.scale(image100, (350, 350))
image101 = pygame.image.load('bronzesword.png')
image101 = pygame.transform.scale(image101, (350, 350))
image102 = pygame.image.load('leatherboots.png')
image102 = pygame.transform.scale(image102, (350, 350))
image103 = pygame.image.load('coralpants.png')
image103 = pygame.transform.scale(image103, (350, 350))

image104 = pygame.image.load('greenpotion.png')
image104 = pygame.transform.scale(image104, (350, 350))
image105 = pygame.image.load('redamulet.png')
image105 = pygame.transform.scale(image105, (350, 350))
image106 = pygame.image.load('Ironsword.png')
image106 = pygame.transform.scale(image106, (350, 350))
image107 = pygame.image.load('metalhelmet.png')
image107 = pygame.transform.scale(image107, (350, 350))
image108 = pygame.image.load('coralshoes.png')
image108 = pygame.transform.scale(image108, (350, 350))

image109 = pygame.image.load('whitepotion.png')
image109 = pygame.transform.scale(image109, (350, 350))
image110 = pygame.image.load('purpleamulet.png')
image110 = pygame.transform.scale(image110, (350, 350))
image111 = pygame.image.load('diamondsword.png')
image111 = pygame.transform.scale(image111, (350, 350))
image112 = pygame.image.load('metalchestplate.png')
image112 = pygame.transform.scale(image112, (350, 350))
image113 = pygame.image.load('expouch.png')
image113 = pygame.transform.scale(image113, (350, 350))

image114 = pygame.image.load('healingpotion.png')
image114 = pygame.transform.scale(image114, (350, 350))
image115 = pygame.image.load('underwatercrown.png')
image115 = pygame.transform.scale(image115, (350, 350))
image116 = pygame.image.load('simplestaff.png')
image116 = pygame.transform.scale(image116, (350, 350))
image117 = pygame.image.load('metalgreeves.png')
image117 = pygame.transform.scale(image117, (350, 350))
image118 = pygame.image.load('largeexppouch.png')
image118 = pygame.transform.scale(image118, (350, 350))

image119 = pygame.image.load('apple.png')
image119 = pygame.transform.scale(image119, (350, 350))
image120 = pygame.image.load('mysterybag.png')
image120 = pygame.transform.scale(image120, (350, 350))
image121 = pygame.image.load('leatherhelmet.png')
image121 = pygame.transform.scale(image121, (350, 350))
image122 = pygame.image.load('metalboots.png')
image122 = pygame.transform.scale(image122, (350, 350))
image123 = pygame.image.load('timedilator.png')
image123 = pygame.transform.scale(image123, (350, 350))

image124 = pygame.image.load('goldenapple.png')
image124 = pygame.transform.scale(image124, (350, 350))
image125 = pygame.image.load('supermysterybag.png')
image125 = pygame.transform.scale(image125, (350, 350))
image126 = pygame.image.load('leatherchestplate.png')
image126 = pygame.transform.scale(image126, (350, 350))
image127 = pygame.image.load('coralhelmet.png')
image127 = pygame.transform.scale(image127, (350, 350))

########################################################################################################################
image128 = pygame.image.load('stars.png')
image128 = pygame.transform.scale(image128, ((770, 740)))
image129 = pygame.image.load('itemframe.png')
image129 = pygame.transform.scale(image129, ((950, 1150)))
image130 = pygame.image.load('buybutton.png')
image130 = pygame.transform.scale(image130, ((300, 300)))
image131 = pygame.image.load('glowbuybutton.png')
image131 = pygame.transform.scale(image131, ((300, 300)))
imageBlack2 = pygame.image.load('blackscreen.jpg')
imageBlack2 = pygame.transform.scale(imageBlack2, (275, 85))


image132 = pygame.image.load('mainmap.JPG')
image132 = pygame.transform.scale(image132, (1550, 870))
image0133 = pygame.image.load('workmap.jpg')
image0133 = pygame.transform.scale(image0133, (1550, 870))
image0134 = pygame.image.load('gamblemap.jpg')
image0134 = pygame.transform.scale(image0134, (1550, 870))
image0135 = pygame.image.load('paimonmap.jpg')
image0135 = pygame.transform.scale(image0135, (1550, 870))
image0136 = pygame.image.load('castlemap.jpg')
image0136 = pygame.transform.scale(image0136, (1550, 870))
image0137 = pygame.image.load('colleseummap.jpg')
image0137 = pygame.transform.scale(image0137, (1550, 870))
image0138 = pygame.image.load('adventuremap.jpg')
image0138 = pygame.transform.scale(image0138, (1550, 870))
image0139 = pygame.image.load('guildmap.jpg')
image0139 = pygame.transform.scale(image0139, (1550, 870))
image0140 = pygame.image.load('stashmap.jpg')
image0140 = pygame.transform.scale(image0140, (1550, 870))
image0141 = pygame.image.load('blackmarketmap.jpg')
image0141 = pygame.transform.scale(image0141, (1550, 870))


image133 = pygame.image.load('greenglow.png')
image133 = pygame.transform.scale(image133, (80, 80))
imagee133 = pygame.image.load('redglow.png')
imagee133 = pygame.transform.scale(imagee133, (80, 80))
image134 = pygame.image.load('returnbutton.png')
image134 = pygame.transform.scale(image134, (125, 125))
image135 = pygame.image.load('returnbutton2.png')
image135 = pygame.transform.scale(image135, (125, 125))
image136 = pygame.image.load('returnbutton2.png')
image136 = pygame.transform.scale(image136, (250, 250))
########################################################################################################################
image137 = pygame.image.load('goblin.jpg')
image137 = pygame.transform.scale(image137, (1550, 870))
image138 = pygame.image.load('laborchoices.png')
image138 = pygame.transform.scale(image138, (800, 600))
image139 = pygame.image.load('redx.png')
image139 = pygame.transform.scale(image139, (400, 100))
image140 = pygame.image.load('laborchoiceshover1.png')
image140 = pygame.transform.scale(image140, (800, 600))
image141 = pygame.image.load('mininggameworld.jpg')
image142 = pygame.image.load('betacharacter.png')
image142 = pygame.transform.scale(image142, (50, 50))
image143 = pygame.image.load('lightbluegem.png')
image144 = pygame.image.load('pinkgem.png')
image145 = pygame.image.load('rubygem.png')
image146 = pygame.image.load('heartgem.png')
image147 = pygame.image.load('diamondgem.png')
image148 = pygame.image.load('purplegem.png')
image149 = pygame.image.load('darkbluegem.png')
image150 = pygame.image.load('miningworldgame2.jpg')
image151 = pygame.image.load('dighole.png')
image151 = pygame.transform.scale(image151, (60, 60))
image152 = pygame.image.load('digholereturnarro.png')
image152 = pygame.transform.scale(image152, (60, 60))
image153 = pygame.image.load('digholereturnarrow.png')
image153 = pygame.transform.scale(image153, (60, 60))
image154 = pygame.image.load('trilobite.png')
image155 = pygame.image.load('gems.png')
image156 = pygame.image.load('dinosaurbones.png')
image157 = pygame.image.load('crown.png')
image158 = pygame.image.load('spider.png')
image159 = pygame.image.load('egg.png')
image160 = pygame.image.load('digchest1.png')
image161 = pygame.image.load('digchest2.png')
image162 = pygame.image.load('digchest3.png')
image163 = pygame.image.load('digchest4.png')
image164 = pygame.image.load('invertreturnsign.png')
image164 = pygame.transform.scale(image164, (60, 60))
image165 = pygame.image.load('invertreturnsignpurple.png')
image165 = pygame.transform.scale(image165, (60, 60))
image166 = pygame.image.load('lava1.png')
image167 = pygame.image.load('lava2.png')
image168 = pygame.image.load('miningstatsimage1.png')
image169 = pygame.image.load('miningstatsimage2.png')
image170 = pygame.image.load('digginggameupgradescreen.png')
image171 = pygame.image.load('statfilledbox.jpg')
########################################################################################################################
image172 = pygame.image.load('casinoimage1.webp')
image172 = pygame.transform.scale(image172, (1550, 870))
image173 = pygame.image.load('gamblingchoices.webp')
image173 = pygame.transform.scale(image173, (800, 800))
image174 = pygame.image.load('roulette1.jpg')
image174 = pygame.transform.scale(image174, (1550, 870))
image175 = pygame.image.load('reddownarrow.png')
image176 = pygame.image.load('slotsimage.webp')
image176 = pygame.transform.scale(image176, (1550, 870))
image177 = pygame.image.load('slotimage.png')
image178 = pygame.image.load('slotimage2.png')
image179 = pygame.image.load('slotimage3.png')
image180 = pygame.image.load('goldbackground.jpg')

image181 = pygame.image.load('slotnum1.jpg')
image182 = pygame.image.load('slotnum2.jpg')
image183 = pygame.image.load('slotnum3.jpg')
image184 = pygame.image.load('slotnum4.jpg')
image185 = pygame.image.load('slotnum5.jpg')
image186 = pygame.image.load('slotnum6.jpg')
image187 = pygame.image.load('slotnum7.jpg')
image188 = pygame.image.load('slotnum8.jpg')
image189 = pygame.image.load('slotnum9.jpg')

image190 = pygame.image.load('slotimage4.png')

image191 = pygame.image.load('diceimage.jpg')
image191 = pygame.transform.scale(image191, (1550, 870))

image192 = pygame.image.load('dice1.jpg')
image192 = pygame.transform.scale(image192, (320, 320))
image193 = pygame.image.load('dice2.jpg')
image193 = pygame.transform.scale(image193, (320, 320))
image194 = pygame.image.load('dice3.jpg')
image194 = pygame.transform.scale(image194, (320, 320))
image195 = pygame.image.load('dice4.jpg')
image195 = pygame.transform.scale(image195, (320, 320))
image196 = pygame.image.load('dice5.jpg')
image196 = pygame.transform.scale(image196, (320, 320))
image197 = pygame.image.load('dice6.jpg')
image197 = pygame.transform.scale(image197, (320, 320))
image198 = pygame.image.load('dice7.png')
image198 = pygame.transform.scale(image198, (320, 320))

image199 = pygame.image.load('bluebakcground.jpg')

image201 = pygame.transform.scale(image192, (150, 150))
image202 = pygame.transform.scale(image193, (150, 150))
image203 = pygame.transform.scale(image194, (150, 150))
image204 = pygame.transform.scale(image195, (150, 150))
image205 = pygame.transform.scale(image196, (150, 150))
image206 = pygame.transform.scale(image197, (150, 150))

image207 = pygame.image.load('guildroom.png')
image207 = pygame.transform.scale(image207, (1550, 870))
image208 = pygame.image.load('questboard.jpg')
image208 = pygame.transform.scale(image208, (1550, 870))
image209 = pygame.image.load('alchemyroom.jpg')
image209 = pygame.transform.scale(image209, (1550, 870))

image210 = pygame.image.load('cauldron.png')
image211 = pygame.image.load('stopbutton.png')
image212 = pygame.image.load('glowstopbutton.png')
image213 = pygame.image.load('meterimage.jpg')
image214 = pygame.image.load('meterline.png')

image215 = pygame.image.load('pot1.png')
image216 = pygame.image.load('pot2.png')
image217 = pygame.image.load('pot3.png')
image218 = pygame.image.load('pot4.png')
image219 = pygame.image.load('pot5.png')

image220 = pygame.image.load('goldlabel.png')
image221 = pygame.image.load('lvllabel.png')
image222 = pygame.image.load('gemlabel.png')

image223 = pygame.image.load('cauldronstars.png')
image224 = pygame.image.load('sunlight.png')

image225 = pygame.image.load('chestopened.png')
image226 = pygame.image.load('chestclosed.png')
########################################################################################################################
image227 = pygame.image.load('bluechip.png')
image228 = pygame.image.load('redchip.png')
image229 = pygame.image.load('blackchip.png')
image230 = pygame.image.load('allchip.png')
image231 = pygame.image.load('goldchip.png')

image232 = pygame.image.load('pokertable.webp')
image232 = pygame.transform.scale(image232, (1550, 870))

image233 = pygame.image.load('outlinechipblue.png')
image234 = pygame.image.load('outlinechipred.png')
image235 = pygame.image.load('outlinechipblack.png')
image236 = pygame.image.load('outlinechipall.png')
image237 = pygame.image.load('outlinechipgold.png')

image238 = pygame.image.load('hearts.png')
image239 = pygame.image.load('diamonds.png')
image240 = pygame.image.load('spades.png')
image241 = pygame.image.load('clovers.png')
image242 = pygame.image.load('facedowncard.png')

image243 = pygame.image.load('blackmarketbyron.jpg')
image243 = pygame.transform.scale(image243, (1550, 870))
image244 = pygame.image.load('blackmarketloot.webp')
image244 = pygame.transform.scale(image244, (1550, 870))

image245 = pygame.image.load('arrowleft.png')
image246 = pygame.image.load('arrowright.png')

image247 = pygame.image.load('woodchest.png')
image248 = pygame.image.load('diamondchest.png')
image249 = pygame.image.load('emeraldchest.png')
image250 = pygame.image.load('blackdoor.png')
image251 = pygame.image.load('redarrowleft.png')
image252 = pygame.image.load('redarrowright.png')

image253 = pygame.image.load('glowwoodentreasurechest.png')
image254 = pygame.image.load('glowdiamondtreasurechest.png')
image255 = pygame.image.load('glowemeraldtreasurechest.png')
image256 = pygame.image.load('glowblackdoor.png')
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
font6 = pygame.font.Font("Danger.otf", 25)
font7 = pygame.font.Font("eroded.ttf", 20)
font8 = pygame.font.Font("HelpMe.ttf", 20)
font9 = pygame.font.Font("Overwave.otf", 20)
font10 = pygame.font.Font("Comfy.otf", 22)
font11 = pygame.font.Font("anime.otf", 15)
font12 = pygame.font.Font("oldenFont.otf", 50)
font13 = pygame.font.Font("SwordsmanFont.TTF", 20)
font14 = pygame.font.Font("AsianFont.ttf", 20)
font15 = pygame.font.Font("womenfont.ttf", 20)
font16 = pygame.font.Font("runefont.otf", 20)
font17 = pygame.font.Font("dragonfont.ttf", 20)
font18 = pygame.font.Font("oldenFont.otf", 70)
font19 = pygame.font.Font("Danger.otf", 100)
font20 = pygame.font.Font("AsianFont.ttf", 60)

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
        pygame.mixer.music.load("fantasyhomemusic.mp3")
        pygame.mixer.music.queue("fantasyhomemusic2.mp3")
        pygame.mixer.music.play(-1)
        mainloop = True

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
            with open("gamedata.txt", "r") as file:
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

            draw_text("Paimons Shop", font13, PINK, DISPLAYSURF, 1340, 415)
            draw_text("Labor Market", font13, RED, DISPLAYSURF, 1340, 735)
            draw_text("Gambling Den", font13, GOLD, DISPLAYSURF, 1415, 547)
            draw_text("Guild Hall", font13, SKYBLUE, DISPLAYSURF, 630, 550)
            draw_text("Black Market", font13, PURPLE, DISPLAYSURF, 250, 575)

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
            if guildrect.collidepoint(mouse_pos):
                DISPLAYSURF.blit(image0139, (195, 100))
                draw_text("Guild Hall", font13, rainbow, DISPLAYSURF, 630, 550)
            if stashrect.collidepoint(mouse_pos):
                DISPLAYSURF.blit(image0140, (195, 100))
            if blackmarketrect.collidepoint(mouse_pos):
                DISPLAYSURF.blit(image0141, (195, 100))
                draw_text("Black Market", font13, rainbow, DISPLAYSURF, 250, 575)

            if adventurerect.collidepoint(mouse_pos):
                DISPLAYSURF.blit(image0138, (195, 100))


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
            draw_text(str(gold), font5, GOLD, DISPLAYSURF, 480, 152)
            draw_text(str(gem), font5, PURPLE, DISPLAYSURF, 1385, 152)
            draw_text(str(level), font5, GREY, DISPLAYSURF, 706, 150)
            draw_text(str(level), font5, GREY, DISPLAYSURF, 1208, 150)

            # print("x and y = " +str(mouseX) +" " +str(mouseY))

            draw_text("Coming Soon", font13, DARKRED, DISPLAYSURF, 900, 460)
            draw_text("Coming Soon", font13, DARKRED, DISPLAYSURF, 714, 254)
            draw_text("Coming Soon", font13, DARKRED, DISPLAYSURF, 900, 620)
            draw_text("Coming Soon", font13, DARKRED, DISPLAYSURF, 550, 685)

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

            for event in pygame.event.get():
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
                            sound_effect = pygame.mixer.Sound("nextlevel.mp3")
                            pygame.mixer.music.set_volume(0.5)
                            sound_effect.play()
                            chestbool = 150
                            chestcollected = chesttimer
                    if paimonrect.collidepoint(mouse_pos):
                        transition(6)
                        sound_effect = pygame.mixer.Sound("dissapearwhoosh.mp3")
                        sound_effect.play()
                        PaimonShop()
                        pygame.mixer.music.load("fantasyhomemusic.mp3")
                        pygame.mixer.music.queue("fantasyhomemusic2.mp3")
                        pygame.mixer.music.play(-1)
                    if labormarketrect.collidepoint(mouse_pos):
                        transition(6)
                        sound_effect = pygame.mixer.Sound("dissapearwhoosh.mp3")
                        sound_effect.play()
                        labormarket()
                        pygame.mixer.music.load("fantasyhomemusic.mp3")
                        pygame.mixer.music.queue("fantasyhomemusic2.mp3")
                        pygame.mixer.music.play(-1)
                    if gamblingdenrect.collidepoint(mouse_pos):
                        transition(6)
                        sound_effect = pygame.mixer.Sound("dissapearwhoosh.mp3")
                        sound_effect.play()
                        casino()
                        pygame.mixer.music.load("fantasyhomemusic.mp3")
                        pygame.mixer.music.queue("fantasyhomemusic2.mp3")
                        pygame.mixer.music.play(-1)
                    if guildrect.collidepoint(mouse_pos):
                        transition(6)
                        sound_effect = pygame.mixer.Sound("dissapearwhoosh.mp3")
                        sound_effect.play()
                        guild()
                        pygame.mixer.music.load("fantasyhomemusic.mp3")
                        pygame.mixer.music.queue("fantasyhomemusic2.mp3")
                        pygame.mixer.music.play(-1)
                    if blackmarketrect.collidepoint(mouse_pos):
                        transition(6)
                        sound_effect = pygame.mixer.Sound("dissapearwhoosh.mp3")
                        sound_effect.play()
                        blackmarket()
                        pygame.mixer.music.load("fantasyhomemusic.mp3")
                        pygame.mixer.music.queue("fantasyhomemusic2.mp3")
                        pygame.mixer.music.play(-1)
                    if xrect.collidepoint(mouse_pos):
                        print("Quit clicked")
                        pygame.mixer.music.stop()
                        pygame.quit()
                        sys.exit()
            with open("gamedata.txt", "r") as file:
                lines = file.readlines()
                lines[0] = f"gold = {gold}\n"
                lines[1] = f"gem = {gem}\n"
            with open("gamedata.txt", "w") as file:
                file.writelines(lines)
            pygame.display.update()
########################################################################################################################
class PaimonShop(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.menu_activepaimon = True
        self.paimonshop()
########################################################################################################################
    def displayitemscene(self, itemdisplay, gamescene, name, temporary, image, attack=0, armor=0, speed=0,
                         critical=0, specialattack=0, luck=0, price=0):
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
        draw_text(str(critical), font11, WHITE, DISPLAYSURF, 1270, 781)
        draw_text(str(specialattack), font11, WHITE, DISPLAYSURF, 1270, 806)
        draw_text(str(luck), font11, SKYBLUE, DISPLAYSURF, 1270, 831)
        if ((temporary != 0) and (temporary != -1)):
            draw_text("Temporary- " + str(temporary) + " min", font13,
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
                        sound_effect = pygame.mixer.Sound("coinsound.mp3")
                        itemboughtswitch = True
                        sound_effect.play()
                        return (0, 7)
                    else:
                        sound_effect = pygame.mixer.Sound("error.mp3")
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
                        sound_effect = pygame.mixer.Sound("clicknoise.mp3")
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
        pygame.mixer.music.load("celestialmusic.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        print("Paimons shop initialized")
        global textFader
        global characterName
        global firsttimepaimon

        with open("gamedata.txt", "r") as file:
            lines = file.readlines()
            paimonshopline = lines[11].strip()
            paimonshopline = paimonshopline[18:]

        if(paimonshopline == 'true'):
            self.gamescene = 1
        elif(paimonshopline == 'false'):
            self.gamescene = 10

        while self.menu_activepaimon:
            with open("gamedata.txt", "r") as file:
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
                with open("gamedata.txt", "r") as file:
                    lines = file.readlines()
                    lines[11] = f"firstpaimonshop = false\n"
                with open("gamedata.txt", "w") as file:
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
                        sound_effect = pygame.mixer.Sound("shopclicksound.mp3")
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
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Purple Potion", 10, image94, 1, 2, 3, 4, 5, 6, 100)
                draw_text('Increases Attack stat by 15% for 10 min', font5, TAN, DISPLAYSURF, 675, 730)

            if(itemdisplay == 2):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Codex", -1, image95, 1, 2, 3, 4, 5, 6, 100)
                draw_text('A codex filled with the knowledge of', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('the gods. Use this item to gain ', font5, TAN, DISPLAYSURF, 675, 760)
                draw_text('1-5000 user experience points', font5, TAN, DISPLAYSURF, 675, 790)

            if(itemdisplay == 3):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Rusty Sword", 0, image96, 1, 2, 3, 4, 5, 6, 1)
                draw_text('A sword with a forgotten story.', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('This sword is the bare minimum', font5, TAN, DISPLAYSURF, 675, 760)
                draw_text('for surviving in this world.', font5, TAN, DISPLAYSURF, 675, 790)

            if(itemdisplay == 4):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Leather Greeves", 0, image97, 1, 2, 3, 4, 5, 6, 100)
                draw_text('Can barely be called armor.', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('Made to be cheap and light.', font5, TAN, DISPLAYSURF, 675, 760)

            if(itemdisplay == 5):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Ascendent Scale Chestplate", 0, image98, 1, 2, 3, 4, 5, 6, 100)
                draw_text('A chestplate crafted from the divine', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('blacksmith of Lucidea. Gain permanent 10%', font5, TAN, DISPLAYSURF, 675, 760)
                draw_text('stat boost to all stats while wearing.', font5, TAN, DISPLAYSURF, 675, 790)

            if(itemdisplay == 6):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Wind Potion", 10, image99, 1, 2, 3, 4, 5, 6, 100)
                draw_text('Increases Speed stat by 15% for 10 min', font5, TAN, DISPLAYSURF, 675, 730)

            if(itemdisplay == 7):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Aqua Amulet", 0, image100, 1, 2, 3, 4, 5, 6, 100)
                draw_text('An amulet inbued with the power of water.', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('Increases water resistence by 25%', font5, TAN, DISPLAYSURF, 675, 760)
                draw_text('(equipable jewelry slot)', font5, TAN, DISPLAYSURF, 675, 790)

            if(itemdisplay == 8):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Bronze Sword", 0, image101, 1, 2, 3, 4, 5, 6, 100)
                draw_text('A sword forged by an amateur.', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('A sword for beginners, to create', font5, TAN, DISPLAYSURF, 675, 760)
                draw_text('new beginnings.', font5, TAN, DISPLAYSURF, 675, 790)

            if(itemdisplay == 9):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Leather Boots", 0, image102, 1, 2, 3, 4, 5, 6, 100)
                draw_text('Can barely be called armor.', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('Made to be cheap and light.', font5, TAN, DISPLAYSURF, 675, 760)

            if(itemdisplay == 10):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Ascendent Scale Greeves", 0, image103, 1, 2, 3, 4, 5, 6, 100)
                draw_text('Greeves crafted from the divine', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('blacksmith of Lucidea. Gain permanent 10%', font5, TAN, DISPLAYSURF, 675, 760)
                draw_text('stat boost to all stats while wearing.', font5, TAN, DISPLAYSURF, 675, 790)

            if (itemdisplay == 11):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Lucky Potion", 10, image104,1, 2, 3, 4, 5, 6, 100)
                draw_text('Increases Luck by 15% for 10 min', font5, TAN, DISPLAYSURF, 675, 730)

            if (itemdisplay == 12):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Lava Amulet", 0, image105, 1, 2,3, 4, 5, 6, 100)
                draw_text('An amulet inbued with the power of Lava.', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('Increases fire resistence by 25%', font5, TAN, DISPLAYSURF, 675, 760)
                draw_text('(equipable jewelry slot)', font5, TAN, DISPLAYSURF, 675, 790)

            if (itemdisplay == 13):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Silverline Sword", 0, image106,1, 2, 3, 4, 5, 6, 100)
                draw_text('A sword used by all knights of the kingdom', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('A sword worshipped by the light and dreaded', font5, TAN, DISPLAYSURF, 675, 760)
                draw_text('by the dark.', font5, TAN, DISPLAYSURF, 705, 790)

            if (itemdisplay == 14):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Plated Helmet", 0,image107, 1, 2, 3, 4, 5, 6, 100)
                draw_text('Heavy and reliable', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('this armor is made for war.', font5, TAN, DISPLAYSURF, 675, 760)

            if (itemdisplay == 15):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Ascendent Scale Boots",0, image108, 1, 2, 3, 4, 5, 6, 100)
                draw_text('Boots crafted from the divine', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('blacksmith of Lucidea. Gain permanent 10%', font5, TAN, DISPLAYSURF, 675, 760)
                draw_text('stat boost to all stats.', font5, TAN, DISPLAYSURF, 675, 790)

            if (itemdisplay == 16):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Resistence Potion", 10, image109,1, 2, 3, 4, 5, 6, 100)
                draw_text('Increases Defense stat by 15% for 10 min', font5, TAN, DISPLAYSURF, 675, 730)

            if (itemdisplay == 17):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Amulet of Heaven", 0, image110, 1, 2,3, 4, 5, 6, 100)
                draw_text('An amulet of unknown origins,', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('blessed by the goddess of the sea.', font5, TAN, DISPLAYSURF, 675, 760)
                draw_text('Increases all elemental resistence by 10%', font5, TAN, DISPLAYSURF, 675, 790)

            if (itemdisplay == 18):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Adamantine Sword", 0, image111,1, 2, 3, 4, 5, 6, 100)
                draw_text('A sword made for heroes.', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('Unlock the way of the sword.', font5, TAN, DISPLAYSURF, 675, 760)
                draw_text('100% increase critical chance', font5, TAN, DISPLAYSURF, 675, 790)

            if (itemdisplay == 19):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Plated Chestplate", 0,image112, 1, 2, 3, 4, 5, 6, 100)
                draw_text('Heavy and reliable', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('this armor is made for war.', font5, TAN, DISPLAYSURF, 675, 760)

            if (itemdisplay == 20):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Small EXP Pouch",-1, image113, 1, 2, 3, 4, 5, 6, 100)
                draw_text('Used by Beast Tamers for fast results.', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('Increase a Beasts exp by 1-1,000 exp', font5, TAN, DISPLAYSURF, 675, 760)

            if (itemdisplay == 21):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Healing Potion", 10, image114, 1, 2, 3, 4, 5, 6, 100)
                draw_text('Heals 25% hp', font5, TAN, DISPLAYSURF, 675, 730)

            if (itemdisplay == 22):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Lost Crown", 0, image115, 1,2, 3, 4, 5, 6, 100)
                draw_text('The power of the king.', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('Stand on the corpse of a trillion souls,', font5, TAN, DISPLAYSURF, 675, 760)
                draw_text('and ask them how important honor is?', font5, TAN, DISPLAYSURF, 675, 790)

            if (itemdisplay == 23):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Simple Staff", 0,image116, 1, 2, 3, 4, 5, 6, 100)
                draw_text('Tired of using a sword?', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('Become a wizard!', font5, TAN, DISPLAYSURF, 675, 760)
                draw_text('(equipable weapon slot)', font5, TAN, DISPLAYSURF, 675, 790)

            if (itemdisplay == 24):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Plated Greeves", 0,image117, 1, 2, 3, 4, 5, 6, 100)
                draw_text('Heavy and reliable', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('this armor is made for war.', font5, TAN, DISPLAYSURF, 675, 760)

            if (itemdisplay == 25):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene,"Large EXP Pouch", -1, image118, 1, 2,3, 4, 5, 6, 100)
                draw_text('Used by wealthy Beast Tamers for fast results.', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('Increase a Beasts exp by 1,000-10,000 exp', font5, TAN, DISPLAYSURF, 675, 760)

            if (itemdisplay == 26):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Apple", -1, image119, 1,2, 3, 4, 5, 6, 100)
                draw_text('Apples exist underwater?', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('Heals 25 hp', font5, TAN, DISPLAYSURF, 675, 760)

            if (itemdisplay == 27):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Mystery bag", -1,image120, 1, 2, 3, 4, 5, 6, 100)
                draw_text('obtain an #$*@ item', font5, TAN, DISPLAYSURF, 675, 730)

            if (itemdisplay == 28):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Leather Cap", 0,image121, 1, 2, 3, 4, 5, 6, 100)
                draw_text('Can barely be called armor.', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('Made to be cheap and light.', font5, TAN, DISPLAYSURF, 675, 760)

            if (itemdisplay == 29):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene,"Plated Boots", 0, image122, 1, 2,3, 4, 5, 6, 100)
                draw_text('Heavy and reliable', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('this armor is made for war.', font5, TAN, DISPLAYSURF, 675, 760)

            if (itemdisplay == 30):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Time Dilator", -1, image123,1, 2, 3, 4, 5, 6, 100)
                draw_text('??#?#$???9?????5????9?@?#??', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('Revert a creature back to lvl 1', font5, TAN, DISPLAYSURF, 675, 760)
                draw_text('??#?#$???9?????5????9?@?#??', font5, TAN, DISPLAYSURF, 675, 790)

            if (itemdisplay == 31):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Golden Apple", -1,image124, 1, 2, 3, 4, 5, 6, 100)
                draw_text('whats next, enchanted golden apple?', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('Heals 100 HP', font5, TAN, DISPLAYSURF, 675, 760)

            if (itemdisplay == 32):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Mysterious Dao Bag",-1, image125, 1, 2, 3, 4, 5, 6, 100)
                draw_text('obtain an rare or higher #$*@ item', font5, TAN, DISPLAYSURF, 675, 730)

            if (itemdisplay == 33):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Leather Chestplate",0, image126, 1, 2, 3, 4, 5, 6, 100)
                draw_text('You are broke arent you?', font5, TAN, DISPLAYSURF, 675, 730)

            if (itemdisplay == 34):
                itemdisplay, self.gamescene = self.displayitemscene(itemdisplay, self.gamescene, "Ascendent Scale Helmet",0, image127, 1, 2, 3, 4, 5, 6, 100)
                draw_text('A helmet crafted from the divine', font5, TAN, DISPLAYSURF, 675, 730)
                draw_text('blacksmith of Lucidea. Gain permanent 10%', font5, TAN, DISPLAYSURF, 675, 760)
                draw_text('stat boost to all stats.', font5, TAN, DISPLAYSURF, 675, 790)
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
                                sound_effect = pygame.mixer.Sound("clicknoise.mp3")
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
                                sound_effect = pygame.mixer.Sound("clicknoise.mp3")
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
                                sound_effect = pygame.mixer.Sound("clicknoise.mp3")
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
        with open("gamedata.txt", "r") as file:
            lines = file.readlines()
            lines[0] = f"gold = {gold}\n"
            lines[1] = f"gem = {gem}\n"
        with open("gamedata.txt", "w") as file:
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
                        sound_effect = pygame.mixer.Sound("clicknoise.mp3")
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
        video = cv2.VideoCapture("goldglitterbackground.mp4")
        startTime = pygame.time.get_ticks()
        self.gamescene = 1
        mouse_pos = pygame.mouse.get_pos()
        pygame.mixer.music.load("goblindancemusic.mp3")
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
            mouse_pos = pygame.mouse.get_pos()
            pygame.mixer.music.load("beachmusic.mp3")
            pygame.mixer.music.queue("fantasyhomemusic2.mp3")
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
                with open("gamedata.txt", "r") as file:
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
                        if(len(digs) > 700):
                            digs.pop(0)
                            digs.pop(1)
                            digs.pop(2)

                    if (5 <= miningspeedtemp < 10):
                        if(len(digs) > 500):
                            digs.pop(0)
                            digs.pop(1)
                            digs.pop(2)

                    if (10 <= miningspeedtemp):
                        if(len(digs) > 300):
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
                    i = 3
                    for element in digs:
                        i = i + 1
                        if (miningspeedtemp < 5):
                            if (i % 20 == 3):
                                DISPLAYSURF.blit(image151, (element[0] + x, element[1] + y))
                        if (5 <= miningspeedtemp < 10):
                            if (i % 12 == 3):
                                DISPLAYSURF.blit(image151, (element[0] + x, element[1] + y))
                        if (10 <= miningspeedtemp):
                            if (i % 6 == 3):
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

                            DISPLAYSURF.blit(image156, (xlocation[itemgenerationcounter + 5000] + x, ylocation[itemgenerationcounter + 5000] + y + 8000))
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

                            gem9rect = pygame.Rect((xlocation[itemgenerationcounter + 5000] + x - 16, ylocation[itemgenerationcounter + 5000] + y - 30 + 8000, 240, 190))
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
                                sound_effect = pygame.mixer.Sound("nextlevel.mp3")
                                sound_effect.play()
                                secondstouch = 5
                                secondsextra = secondsextra + 5
                                looptimet = pygame.time.get_ticks() + 2000
                                timert = pygame.time.get_ticks()
                            if text2rect.collidepoint((screen_center[0], screen_center[1])):
                                print("time collected!")
                                xlocation[itemgenerationcounter + 8700] = (-20000)
                                ylocation[itemgenerationcounter + 8700] = (-20000)
                                sound_effect = pygame.mixer.Sound("nextlevel.mp3")
                                sound_effect.play()
                                secondstouch = 3
                                secondsextra = secondsextra + 3
                                looptimet = pygame.time.get_ticks() + 2000
                                timert = pygame.time.get_ticks()
                            if text3rect.collidepoint((screen_center[0], screen_center[1])):
                                print("time collected!")
                                xlocation[itemgenerationcounter + 8900] = (-20000)
                                ylocation[itemgenerationcounter + 8900] = (-20000)
                                sound_effect = pygame.mixer.Sound("nextlevel.mp3")
                                sound_effect.play()
                                secondstouch = 1
                                secondsextra = secondsextra + 1
                                looptimet = pygame.time.get_ticks() + 2000
                                timert = pygame.time.get_ticks()
                            if gem9rect.collidepoint((screen_center[0], screen_center[1])):
                                print("dinosaur collected!")
                                xlocation[itemgenerationcounter + 5000] = (-20000)
                                ylocation[itemgenerationcounter + 5000] = (-20000)
                                sound_effect = pygame.mixer.Sound("nextlevel.mp3")
                                sound_effect.play()
                                tempgold = int(tempgold + (500 * (1 + (.1 * specialefficiency))))
                                looptime = pygame.time.get_ticks() + 2000
                                timer = pygame.time.get_ticks()
                                goldamount = int((500 * (1 + (.1 * specialefficiency))))
                            if gem10rect.collidepoint((screen_center[0] + 10, screen_center[1] + 10)):
                                print("crown collected!")
                                xlocation[itemgenerationcounter + 5500] = (-20000)
                                ylocation[itemgenerationcounter + 5500] = (-20000)
                                sound_effect = pygame.mixer.Sound("nextlevel.mp3")
                                sound_effect.play()
                                tempgold = int(tempgold + (100 * (1 + (.1 * specialefficiency))))
                                looptime = pygame.time.get_ticks() + 2000
                                timer = pygame.time.get_ticks()
                                goldamount = int((100 * (1 + (.1 * specialefficiency))))
                            if gem11rect.collidepoint((screen_center[0] + 10, screen_center[1] + 10)):
                                xlocation[itemgenerationcounter + 6000] = (-20000)
                                ylocation[itemgenerationcounter + 6000] = (-20000)
                                print("spider attacked!")
                                gold = gold + tempgold
                                gem = gem + tempgem
                                tempgold = 0
                                tempgem = 0
                                with open("gamedata.txt", "r") as file:
                                    lines = file.readlines()
                                    lines[0] = f"gold = {gold}\n"
                                    lines[1] = f"gem = {gem}\n"
                                with open("gamedata.txt", "w") as file:
                                    file.writelines(lines)
                                scene = 4
                            if gem12rect.collidepoint((screen_center[0] + 10, screen_center[1] + 10)):
                                print("egg collected!")
                                xlocation[itemgenerationcounter + 6500] = (-20000)
                                ylocation[itemgenerationcounter + 6500] = (-20000)
                                sound_effect = pygame.mixer.Sound("nextlevel.mp3")
                                sound_effect.play()
                                tempgold = int(tempgold + (2000 * (1 + (.1 * specialefficiency))))
                                looptime = pygame.time.get_ticks() + 2000
                                timer = pygame.time.get_ticks()
                                goldamount = int((2000 * (1 + (.1 * specialefficiency))))
                            if gem13rect.collidepoint((screen_center[0] + 10, screen_center[1] + 10)):
                                print("Chest collected!")
                                xlocation[itemgenerationcounter + 7000] = (-20000)
                                ylocation[itemgenerationcounter + 7000] = (-20000)
                                sound_effect = pygame.mixer.Sound("nextlevel.mp3")
                                sound_effect.play()
                                goldamount = int(random.randint(int(200 + (10 * luck)), int(400 * (1 + (.1 * specialefficiency)))))
                                tempgold = tempgold + goldamount
                                looptime = pygame.time.get_ticks() + 2000
                                timer = pygame.time.get_ticks()
                            if gem14rect.collidepoint((screen_center[0] + 10, screen_center[1] + 10)):
                                print("Chest collected!")
                                xlocation[itemgenerationcounter + 7500] = (-20000)
                                ylocation[itemgenerationcounter + 7500] = (-20000)
                                sound_effect = pygame.mixer.Sound("nextlevel.mp3")
                                sound_effect.play()
                                goldamount = int(random.randint(int(200 + (10 * luck)), int(500 * (1 + (.1 * specialefficiency)))))
                                tempgold = tempgold + goldamount
                                looptime = pygame.time.get_ticks() + 2000
                                timer = pygame.time.get_ticks()
                            if gem15rect.collidepoint((screen_center[0] + 10, screen_center[1] + 10)):
                                print("Chest collected!")
                                xlocation[itemgenerationcounter + 8000] = (-20000)
                                ylocation[itemgenerationcounter + 8000] = (-20000)
                                sound_effect = pygame.mixer.Sound("nextlevel.mp3")
                                sound_effect.play()
                                goldamount = int(random.randint(int(10 + (30 * luck)), int(1000 * (1 + (.1 * specialefficiency)))))
                                tempgold = tempgold + goldamount
                                looptime = pygame.time.get_ticks() + 2000
                                timer = pygame.time.get_ticks()
                            if gem8rect.collidepoint((screen_center[0] + 10, screen_center[1] + 10)):
                                print("Chest collected!")
                                xlocation[itemgenerationcounter + 4500] = (-20000)
                                ylocation[itemgenerationcounter + 4500] = (-20000)
                                sound_effect = pygame.mixer.Sound("nextlevel.mp3")
                                sound_effect.play()
                                goldamount = int(random.randint(int(20 + (2 * luck)), int(50 * (1 + (.1 * specialefficiency)))))
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

                        gem1rect = pygame.Rect((xlocation[itemgenerationcounter] + x - 15, ylocation[itemgenerationcounter] + y - 40, 70, 70))
                        gem2rect = pygame.Rect((xlocation[itemgenerationcounter + 1000] + x - 20, ylocation[itemgenerationcounter + 1000] + y - 35, 65, 65))
                        gem3rect = pygame.Rect((xlocation[itemgenerationcounter + 2000] + x - 20, ylocation[itemgenerationcounter + 2000] + y - 25 + 1000, 65, 65))
                        gem4rect = pygame.Rect((xlocation[itemgenerationcounter + 3000] + x - 20, ylocation[itemgenerationcounter + 3000] + y - 25 + 2000, 65, 65))
                        gem5rect = pygame.Rect((xlocation[itemgenerationcounter + 4000] + x - 20, ylocation[itemgenerationcounter + 4000] + y - 25 + 5000, 65, 65))

                        gem6rect = pygame.Rect((xlocation[itemgenerationcounter + 2500] + x - 20, ylocation[itemgenerationcounter + 2500] + y - 25 + 1000, 65, 60))
                        gem7rect = pygame.Rect((xlocation[itemgenerationcounter + 3500] + x - 20, ylocation[itemgenerationcounter + 3500] + y - 25 + 1500, 65, 65))

                        lava1rect = pygame.Rect((xlocation[itemgenerationcounter + 3700] + x + 100, ylocation[itemgenerationcounter + 3700] + y - 45 + 4500, 250, 250))
                        lava2rect = pygame.Rect((xlocation[itemgenerationcounter + 3900] + x  - 20, ylocation[itemgenerationcounter + 3900] + y - 25 + 7500, 330, 450))

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
                        if lava1rect.collidepoint((screen_center[0] + 10, screen_center[1] + 10)):
                            xlocation[itemgenerationcounter + 3700] = (-20000)
                            ylocation[itemgenerationcounter + 3700] = (-20000)
                            print("Jumped into Lava!")
                            gold = gold + tempgold
                            gem = gem + tempgem
                            tempgold = 0
                            tempgem = 0
                            with open("gamedata.txt", "r") as file:
                                lines = file.readlines()
                                lines[0] = f"gold = {gold}\n"
                                lines[1] = f"gem = {gem}\n"
                            with open("gamedata.txt", "w") as file:
                                file.writelines(lines)
                            scene = 4
                        if lava2rect.collidepoint((screen_center[0] + 10, screen_center[1] + 10)):
                            xlocation[itemgenerationcounter + 3900] = (-20000)
                            ylocation[itemgenerationcounter + 3900] = (-20000)
                            print("Jumped into Lava!")
                            gold = gold + tempgold
                            gem = gem + tempgem
                            tempgold = 0
                            tempgem = 0
                            with open("gamedata.txt", "r") as file:
                                lines = file.readlines()
                                lines[0] = f"gold = {gold}\n"
                                lines[1] = f"gem = {gem}\n"
                            with open("gamedata.txt", "w") as file:
                                file.writelines(lines)
                            scene = 4
                        if gem1rect.collidepoint((screen_center[0],screen_center[1])):
                            print("gem collected!")
                            xlocation[itemgenerationcounter] = (-20000)
                            ylocation[itemgenerationcounter] = (-20000)
                            sound_effect = pygame.mixer.Sound("nextlevel.mp3")
                            sound_effect.play()
                            tempgold = int(tempgold + (5 * (1 + (.1 * miningefficiency))))
                            looptime = pygame.time.get_ticks() + 2000
                            timer = pygame.time.get_ticks()
                            goldamount = int((5 * (1 + (.1 * miningefficiency))))
                        if gem2rect.collidepoint((screen_center[0] + 10, screen_center[1] + 10)):
                            print("gem collected!")
                            xlocation[itemgenerationcounter + 1000] = (-20000)
                            ylocation[itemgenerationcounter + 1000] = (-20000)
                            sound_effect = pygame.mixer.Sound("nextlevel.mp3")
                            sound_effect.play()
                            tempgold = int(tempgold + (2 * (1 + (.1 * miningefficiency))))
                            looptime = pygame.time.get_ticks() + 2000
                            timer = pygame.time.get_ticks()
                            goldamount = int((2 * (1 + (.1 * miningefficiency))))
                        if gem3rect.collidepoint((screen_center[0] + 10, screen_center[1] + 10)):
                            print("gem collected!")
                            xlocation[itemgenerationcounter + 2000] = (-20000)
                            ylocation[itemgenerationcounter + 2000] = (-20000)
                            sound_effect = pygame.mixer.Sound("nextlevel.mp3")
                            sound_effect.play()
                            tempgold = int(tempgold + (3 * (1 + (.1 * miningefficiency))))
                            looptime = pygame.time.get_ticks() + 2000
                            timer = pygame.time.get_ticks()
                            goldamount = int((3 * (1 + (.1 * miningefficiency))))
                        if gem4rect.collidepoint((screen_center[0] + 10, screen_center[1] + 10)):
                            print("gem collected!")
                            xlocation[itemgenerationcounter + 3000] = (-20000)
                            ylocation[itemgenerationcounter + 3000] = (-20000)
                            sound_effect = pygame.mixer.Sound("nextlevel.mp3")
                            sound_effect.play()
                            tempgold = int(tempgold + (10 * (1 + (.1 * miningefficiency))))
                            looptime = pygame.time.get_ticks() + 2000
                            timer = pygame.time.get_ticks()
                            goldamount = int((10 * (1 + (.1 * miningefficiency))))
                        if gem5rect.collidepoint((screen_center[0] + 10, screen_center[1] + 10)):
                            print("gem collected!")
                            xlocation[itemgenerationcounter + 4000] = (-20000)
                            ylocation[itemgenerationcounter + 4000] = (-20000)
                            sound_effect = pygame.mixer.Sound("nextlevel.mp3")
                            sound_effect.play()
                            tempgold = int(tempgold + (1 * (1 + (.1 * miningefficiency))))
                            looptime = pygame.time.get_ticks() + 2000
                            timer = pygame.time.get_ticks()
                            goldamount = int((1 * (1 + (.1 * miningefficiency))))
                        if gem6rect.collidepoint((screen_center[0] + 10, screen_center[1] + 10)):
                            print("trilobite collected!")
                            xlocation[itemgenerationcounter + 2500] = (-20000)
                            ylocation[itemgenerationcounter + 2500] = (-20000)
                            sound_effect = pygame.mixer.Sound("nextlevel.mp3")
                            sound_effect.play()
                            tempgold = int(tempgold + (1 * (1 + (.5 * specialefficiency))))
                            looptime = pygame.time.get_ticks() + 2000
                            timer = pygame.time.get_ticks()
                            goldamount = int((1 * (1 + (.5 * specialefficiency))))
                        if gem7rect.collidepoint((screen_center[0] + 10, screen_center[1] + 10)):
                            print("special gem collected!")
                            xlocation[itemgenerationcounter + 3500] = (-20000)
                            ylocation[itemgenerationcounter + 3500] = (-20000)
                            sound_effect = pygame.mixer.Sound("nextlevel.mp3")
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
                                y = y - speed
                                digs.append(((-x + screen_width / 2), (-y + screen_height / 2)))
                            elif event.key == pygame.K_w:
                                y = y + speed
                                digs.append(((-x + screen_width / 2), (-y + screen_height / 2)))
                            elif event.key == pygame.K_d:
                                x = x - speed
                                digs.append(((-x + screen_width / 2), (-y + screen_height / 2)))
                            elif event.key == pygame.K_a:
                                x = x + speed
                                digs.append(((-x + screen_width / 2), (-y + screen_height / 2)))
                            elif event.key == pygame.K_UP:
                                y = y + speed
                                digs.append(((-x + screen_width / 2), (-y + screen_height / 2)))
                            elif event.key == pygame.K_DOWN:
                                y = y - speed
                                digs.append(((-x + screen_width / 2), (-y + screen_height / 2)))
                            elif event.key == pygame.K_LEFT:
                                x = x + speed
                                digs.append(((-x + screen_width / 2), (-y + screen_height / 2)))
                            elif event.key == pygame.K_RIGHT:
                                x = x - speed
                                randomdig = random.randint(1, 3)
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
                        y = y - speed
                        digs.append(((-x + screen_width / 2), (-y + screen_height / 2)))
                    if keys[pygame.K_w]:
                        y = y + speed
                        digs.append(((-x + screen_width / 2), (-y + screen_height / 2)))
                    if keys[pygame.K_d]:
                        x = x - speed
                        digs.append(((-x + screen_width / 2), (-y + screen_height / 2)))
                    if keys[pygame.K_a]:
                        x = x + speed
                        digs.append(((-x + screen_width / 2), (-y + screen_height / 2)))
                    if keys[pygame.K_UP]:
                        y = y + speed
                        digs.append(((-x + screen_width / 2), (-y + screen_height / 2)))
                    if keys[pygame.K_DOWN]:
                        y = y - speed
                        digs.append(((-x + screen_width / 2), (-y + screen_height / 2)))
                    if keys[pygame.K_LEFT]:
                        x = x + speed
                        digs.append(((-x + screen_width / 2), (-y + screen_height / 2)))
                    if keys[pygame.K_RIGHT]:
                        x = x - speed
                        digs.append(((-x + screen_width / 2), (-y + screen_height / 2)))
                    draw_text_center(str(seconds) +" seconds remaining", font4, rainbowcol, DISPLAYSURF, halfdisplay, screen_height/2 - 400)
                    if seconds <= 0:
                        print("Time's up!")
                        gold = gold + tempgold
                        gem = gem + tempgem
                        tempgold = 0
                        tempgem = 0
                        with open("gamedata.txt", "r") as file:
                            lines = file.readlines()
                            lines[0] = f"gold = {gold}\n"
                            lines[1] = f"gem = {gem}\n"
                        with open("gamedata.txt", "w") as file:
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
                                transition(6)
                                self.diggingbool = False
                                tempgold2 = 0
                                tempgem2 = 0
                            if returnarrowrect.collidepoint(mouse_pos):
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
                            if plusrect5.collidepoint(mouse_pos):
                                if(miningefficiency != 16):
                                    if(gem >= (5 * miningefficiency)):
                                        gem = gem - ((5 * miningefficiency))
                                        miningefficiency = miningefficiency + 1
                            if plusrect4.collidepoint(mouse_pos):
                                if(time != 16):
                                    if(gem >= (3 * time)):
                                        gem = gem - ((3 * time))
                                        time = time + 1
                            if plusrect3.collidepoint(mouse_pos):
                                if(luck != 16):
                                    if(gem >= (3 * luck)):
                                        gem = gem - ((3 * luck))
                                        luck = luck + 1
                            if plusrect2.collidepoint(mouse_pos):
                                if(spawnchance != 16):
                                    if(gem >= (8 * spawnchance)):
                                        gem = (gem - (8 * spawnchance))
                                        spawnchance = spawnchance + 1
                            if plusrect1.collidepoint(mouse_pos):
                                if(specialefficiency != 16):
                                    if(gem >= (10 * specialefficiency)):
                                        gem = (gem - (10 * specialefficiency))
                                        specialefficiency = specialefficiency + 1
                            with open("gamedata.txt", "r") as file:
                                lines = file.readlines()
                                lines[0] = f"gold = {gold}\n"
                                lines[1] = f"gem = {gem}\n"
                                lines[5] = f"miningspeed = {miningspeed}\n"
                                lines[6] = f"miningefficiency = {miningefficiency}\n"
                                lines[7] = f"time = {time}\n"
                                lines[8] = f"luck = {luck}\n"
                                lines[9] = f"spawnchance = {spawnchance}\n"
                                lines[10] = f"specialefficiency = {specialefficiency}\n"
                            with open("gamedata.txt", "w") as file:
                                file.writelines(lines)

                pygame.display.update()
########################################################################################################################

class casino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.casinomenubool = True
        self.casinomenu()
########################################################################################################################
    def casinomenu(self):
        global FaderBool
        global Fader
        global textFader
        video = cv2.VideoCapture("casinobackgroundglow.mp4")
        startTime = pygame.time.get_ticks()
        self.gamescene = 1
        mouse_pos = pygame.mouse.get_pos()
        pygame.mixer.music.load("casinostartmusic.mp3")
        pygame.mixer.music.queue("slotsmusic.mp3")
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
                            sound_effect = pygame.mixer.Sound("clicknoise.mp3")
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
                            sound_effect = pygame.mixer.Sound("clicknoise.mp3")
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
                            sound_effect = pygame.mixer.Sound("clicknoise.mp3")
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
                            sound_effect = pygame.mixer.Sound("clicknoise.mp3")
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
        cap1 = cv2.VideoCapture("roulettered.mov")
        cap2 = cv2.VideoCapture("rouletteblack.mov")
        itemchoosen = " "
        blackorred = 0
        moneychoosen = 0
        while(self.repeatcasinoloop):
            self.casinogamebool = True
            startTime = pygame.time.get_ticks()
            scene = 1
            won = False
            pygame.mixer.music.load("roulettemusic.mp3")
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)
            while(self.casinogamebool):
                with open("gamedata.txt", "r") as file:
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
                            if ((itemchoosen != ' ') and (moneychoosen != 0)):
                                if beginrect.collidepoint(mouse_pos):
                                    cap1 = cv2.VideoCapture("roulettered.mov")
                                    cap2 = cv2.VideoCapture("rouletteblack.mov")
                                    scene = scene + 1
                            if blackrect.collidepoint(mouse_pos):
                                itemchoosen = 'black'
                            if redrect.collidepoint(mouse_pos):
                                itemchoosen = 'red'
                            if (spend10rect.collidepoint(mouse_pos) & (gold >= 10)):
                                moneychoosen = 10
                            if (spend100rect.collidepoint(mouse_pos) & (gold >= 100)):
                                moneychoosen = 100
                            if (spend1000rect.collidepoint(mouse_pos) & (gold >= 1000)):
                                moneychoosen = 1000
                            if (spend10000rect.collidepoint(mouse_pos) & (gold >= 10000)):
                                moneychoosen = 10000
                            if (spend100000rect.collidepoint(mouse_pos) & (gold >= 100000)):
                                moneychoosen = 100000
                            if (spend1000000rect.collidepoint(mouse_pos) & (gold >= 1000000)):
                                moneychoosen = 1000000
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
                    sound_effect = pygame.mixer.Sound("roulettespinsound.mp3")
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
                        with open("gamedata.txt", "r") as file:
                            lines = file.readlines()
                            lines[0] = f"gold = {gold}\n"
                        with open("gamedata.txt", "w") as file:
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
            pygame.mixer.music.load("slotsmusic.mp3")
            pygame.mixer.music.queue("slotsmusic2.mp3")
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)
            while(self.casinogamebool):
                with open("gamedata.txt", "r") as file:
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
                                sound_effect = pygame.mixer.Sound("clicknoise.mp3")
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
                                sound_effect = pygame.mixer.Sound("clicknoise.mp3")
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
                            if (spend10rect.collidepoint(mouse_pos) & (gold >= 10)):
                                moneychoosen = 10
                            if (spend100rect.collidepoint(mouse_pos) & (gold >= 100)):
                                moneychoosen = 100
                            if (spend1000rect.collidepoint(mouse_pos) & (gold >= 1000)):
                                moneychoosen = 1000
                            if (spend10000rect.collidepoint(mouse_pos) & (gold >= 10000)):
                                moneychoosen = 10000
                            if (spend100000rect.collidepoint(mouse_pos) & (gold >= 100000)):
                                moneychoosen = 100000
                            if (moneychoosen != 0) & (beginrect.collidepoint(mouse_pos)):
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
                    sound_effect = pygame.mixer.Sound("spin.mp3")
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
                                sound_effect = pygame.mixer.Sound("slotwin1.mp3")
                                sound_effect.play()
                                gold = gold + (moneychoosen * 1000)
                                draw_text('gained ' + str(moneychoosen * 1000) + ' gold!', font3, GOLD, DISPLAYSURF, screen_width / 2 - 155, screen_height / 2 - 45)
                            else:
                                if((randomnumber1 == randomnumber2) and (randomnumber1 == randomnumber3) and (randomnumber2 == randomnumber3)):
                                    sound_effect = pygame.mixer.Sound("slotwin2.mp3")
                                    sound_effect.play()
                                    gold = gold + (moneychoosen * 80)
                                    draw_text('gained ' + str(moneychoosen * 80) + ' gold!', font3, GOLD, DISPLAYSURF, screen_width / 2 - 155, screen_height / 2 - 45)

                                else:
                                    if(randomnumber1 == randomnumber2):
                                        sound_effect = pygame.mixer.Sound("minislotwin.mp3")
                                        sound_effect.play()
                                        gold = gold + (moneychoosen * 1)
                                        draw_text('You won ' + str(moneychoosen * 1) + ' gold!', font3, GOLD, DISPLAYSURF, screen_width / 2 - 155, screen_height / 2 - 45)

                                    if(randomnumber3 == randomnumber2):
                                        sound_effect = pygame.mixer.Sound("minislotwin.mp3")
                                        sound_effect.play()
                                        gold = gold + (moneychoosen * 1)
                                        draw_text('You won ' + str(moneychoosen * 1) + ' gold!', font3, GOLD, DISPLAYSURF, screen_width / 2 - 155, screen_height / 2 - 45)

                                    if(randomnumber3 == randomnumber1):
                                        sound_effect = pygame.mixer.Sound("minislotwin.mp3")
                                        sound_effect.play()
                                        gold = gold + (moneychoosen * 1)
                                        draw_text('You won ' + str(moneychoosen * 1) + ' gold!', font3, GOLD, DISPLAYSURF, screen_width / 2 - 155, screen_height / 2 - 45)

                            loop = False
                            with open("gamedata.txt", "r") as file:
                                lines = file.readlines()
                                lines[0] = f"gold = {gold}\n"
                                lines[1] = f"gem = {gem}\n"
                            with open("gamedata.txt", "w") as file:
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
                                sound_effect = pygame.mixer.Sound("clicknoise.mp3")
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
            pygame.mixer.music.load("dicemusic.mp3")
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)
            while(self.casinogamebool):
                with open("gamedata.txt", "r") as file:
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
                            if (spend100rect.collidepoint(mouse_pos) & (gold >= 100)):
                                moneychoosen = 100
                            if (spend1000rect.collidepoint(mouse_pos) & (gold >= 1000)):
                                moneychoosen = 1000
                            if (spend10000rect.collidepoint(mouse_pos) & (gold >= 10000)):
                                moneychoosen = 10000
                            if (spend100000rect.collidepoint(mouse_pos) & (gold >= 100000)):
                                moneychoosen = 100000
                            if (spend1000000rect.collidepoint(mouse_pos) & (gold >= 1000000)):
                                moneychoosen = 1000000
                            if (moneychoosen != 0) & (beginrect.collidepoint(mouse_pos)):
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
                                gold = gold - moneychoosen
                                scene = scene + 1
                    pygame.display.update()
                if (scene == 2):
                    DISPLAYSURF.blit(image191, (190, 100))
                    image199.set_alpha(150)
                    DISPLAYSURF.blit(image199, (0, 0))
                    draw_text('gold - ', font5, WHITE, DISPLAYSURF, 375, 135)
                    draw_text(str(gold), font5, YELLOW, DISPLAYSURF, 445, 135)
                    sound_effect = pygame.mixer.Sound("dicerollsound.mp3")
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

                    dicevideo = cv2.VideoCapture("dicerolling.mov")
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
                        sound_effect = pygame.mixer.Sound("minislotwin.mp3")
                        sound_effect.play()
                        gold = gold + (moneychoosen * 6)
                        draw_text('You won ' + str(moneychoosen * 6) + ' gold!', font2, GOLD, DISPLAYSURF, screen_width / 2 - 215, screen_height / 2 - 345)
                    else:
                        draw_text('You lost, try again.', font2, PURPLE, DISPLAYSURF, screen_width / 2 - 215, screen_height / 2 - 345)
                    print("dice random = " +str(randomnumber1))
                    print("dice choosen = " +str(dicechoosen))

                    with open("gamedata.txt", "r") as file:
                        lines = file.readlines()
                        lines[0] = f"gold = {gold}\n"
                        lines[1] = f"gem = {gem}\n"
                    with open("gamedata.txt", "w") as file:
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
                                sound_effect = pygame.mixer.Sound("clicknoise.mp3")
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
            pygame.mixer.music.load("blackjack1.mp3")
            pygame.mixer.music.play(-1)
            while(self.casinogamebool):
                with open("gamedata.txt", "r") as file:
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

                            if (spend100rect.collidepoint(mouse_pos) & (gold >= (moneychoosen + 100))):
                                moneychoosen = moneychoosen + 100
                            if (spend1000rect.collidepoint(mouse_pos) & (gold >= (moneychoosen + 1000))):
                                moneychoosen = moneychoosen + 1000
                            if (spend10000rect.collidepoint(mouse_pos) & (gold >= (moneychoosen + 10000))):
                                moneychoosen = moneychoosen + 10000
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
                                    sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                    sound_effect.play()
                                    scene = 98
                                elif (CARDVALUE3 + CARDVALUE4 > 21):
                                    sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                    sound_effect.play()
                                    scene = 99
                                elif(CARDVALUE1 + CARDVALUE2 >= 17):
                                    if (CARDVALUE3 + CARDVALUE4 < CARDVALUE1 + CARDVALUE2):
                                        sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                        sound_effect.play()
                                        scene = 99
                                    if (CARDVALUE3 + CARDVALUE4 >= CARDVALUE1 + CARDVALUE2):
                                        sound_effect = pygame.mixer.Sound("coinsound.mp3")
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
                                        sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                        sound_effect.play()
                                        scene = 98
                                    if (dealerhand > 21):
                                        sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                        sound_effect.play()
                                        scene = 99
                                    if(dealerhand != 21 and dealerhand < 21):
                                        if(dealerhand >= playerhand):
                                            sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                            sound_effect.play()
                                            scene = 98
                                        if(dealerhand < playerhand):
                                            sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
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
                                            sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                            sound_effect.play()
                                            scene = 98
                                        if(dealerhand > 21):
                                            sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                            sound_effect.play()
                                            scene = 99
                                        if (dealerhand != 21 and dealerhand < 21):
                                            if (dealerhand >= playerhand):
                                                sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                                sound_effect.play()
                                                scene = 98
                                            if (dealerhand < playerhand):
                                                sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
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
                                                sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                                sound_effect.play()
                                                scene = 98
                                            if (dealerhand > 21):
                                                sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                                sound_effect.play()
                                                scene = 99
                                            if (dealerhand != 21 and dealerhand < 21):
                                                if (dealerhand >= playerhand):
                                                    sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                                    sound_effect.play()
                                                    scene = 98
                                                if (dealerhand < playerhand):
                                                    sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
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
                                                    sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                                    sound_effect.play()
                                                    scene = 98
                                                if (dealerhand > 21):
                                                    sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                                    sound_effect.play()
                                                    scene = 99
                                                if (dealerhand != 21 and dealerhand < 21):
                                                    if (dealerhand >= playerhand):
                                                        sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                                        sound_effect.play()
                                                        scene = 98
                                                    if (dealerhand < playerhand):
                                                        sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                                        sound_effect.play()
                                                        scene = 99
                                            else:
                                                if (dealerhand >= playerhand):
                                                    sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                                    sound_effect.play()
                                                    scene = 98
                                                if (dealerhand < playerhand):
                                                    sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                                    sound_effect.play()
                                                    scene = 99

                        if(CARDVALUE1 + CARDVALUE2 > 21):
                            sound_effect = pygame.mixer.Sound("coinsound.mp3")
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
                                    sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                    sound_effect.play()
                                    scene = 98
                                elif (CARDVALUE3 + CARDVALUE4 > 21):
                                    sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                    sound_effect.play()
                                    scene = 99
                                elif(CARDVALUE1 + CARDVALUE2 >= 17):
                                    if (CARDVALUE3 + CARDVALUE4 < CARDVALUE1 + CARDVALUE2+ CARDVALUE5):
                                        sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                        sound_effect.play()
                                        scene = 99
                                    if (CARDVALUE3 + CARDVALUE4 >= CARDVALUE1 + CARDVALUE2 + CARDVALUE5):
                                        sound_effect = pygame.mixer.Sound("coinsound.mp3")
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
                                        sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                        sound_effect.play()
                                        scene = 98
                                    if (dealerhand > 21):
                                        sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                        sound_effect.play()
                                        scene = 99
                                    if(dealerhand != 21 and dealerhand < 21):
                                        if(dealerhand >= playerhand):
                                            sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                            sound_effect.play()
                                            scene = 98
                                        if(dealerhand < playerhand):
                                            sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
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
                                            sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                            sound_effect.play()
                                            scene = 98
                                        if(dealerhand > 21):
                                            sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                            sound_effect.play()
                                            scene = 99
                                        if (dealerhand != 21 and dealerhand < 21):
                                            if (dealerhand >= playerhand):
                                                sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                                sound_effect.play()
                                                scene = 98
                                            if (dealerhand < playerhand):
                                                sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
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
                                                sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                                sound_effect.play()
                                                scene = 98
                                            if (dealerhand > 21):
                                                sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                                sound_effect.play()
                                                scene = 99
                                            if (dealerhand != 21 and dealerhand < 21):
                                                if (dealerhand >= playerhand):
                                                    sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                                    sound_effect.play()
                                                    scene = 98
                                                if (dealerhand < playerhand):
                                                    sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
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
                                                    sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                                    sound_effect.play()
                                                    scene = 98
                                                if (dealerhand > 21):
                                                    sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                                    sound_effect.play()
                                                    scene = 99
                                                if (dealerhand != 21 and dealerhand < 21):
                                                    if (dealerhand >= playerhand):
                                                        sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                                        sound_effect.play()
                                                        scene = 98
                                                    if (dealerhand < playerhand):
                                                        sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                                        sound_effect.play()
                                                        scene = 99
                                            else:
                                                if (dealerhand >= playerhand):
                                                    sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                                    sound_effect.play()
                                                    scene = 98
                                                if (dealerhand < playerhand):
                                                    sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                                    sound_effect.play()
                                                    scene = 99

                            elif(CARDVALUE3 + CARDVALUE4 == 21):
                                sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                sound_effect.play()
                                scene = 98
                            elif (CARDVALUE3 + CARDVALUE4 > 21):
                                sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                sound_effect.play()
                                scene = 99
                            else:
                                if (CARDVALUE3 + CARDVALUE4 < CARDVALUE1 + CARDVALUE2 + CARDVALUE5):
                                    sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                    sound_effect.play()
                                    scene = 99
                                if (CARDVALUE3 + CARDVALUE4 >= CARDVALUE1 + CARDVALUE2 + CARDVALUE5):
                                    sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                    sound_effect.play()
                                    scene = 98

                        if((CARDVALUE1 + CARDVALUE2 + CARDVALUE5) > 21):
                            sound_effect = pygame.mixer.Sound("coinsound.mp3")
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
                                    sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                    sound_effect.play()
                                    scene = 98
                                elif (CARDVALUE3 + CARDVALUE4 > 21):
                                    sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                    sound_effect.play()
                                    scene = 99
                                elif(CARDVALUE1 + CARDVALUE2 >= 17):
                                    if (CARDVALUE3 + CARDVALUE4 < CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6):
                                        sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                        sound_effect.play()
                                        scene = 99
                                    if (CARDVALUE3 + CARDVALUE4 >= CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6):
                                        sound_effect = pygame.mixer.Sound("coinsound.mp3")
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
                                        sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                        sound_effect.play()
                                        scene = 98
                                    if (dealerhand > 21):
                                        sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                        sound_effect.play()
                                        scene = 99
                                    if(dealerhand != 21 and dealerhand < 21):
                                        if(dealerhand >= playerhand):
                                            sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                            sound_effect.play()
                                            scene = 98
                                        if(dealerhand < playerhand):
                                            sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
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
                                            sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                            sound_effect.play()
                                            scene = 98
                                        if(dealerhand > 21):
                                            sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                            sound_effect.play()
                                            scene = 99
                                        if (dealerhand != 21 and dealerhand < 21):
                                            if (dealerhand >= playerhand):
                                                sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                                sound_effect.play()
                                                scene = 98
                                            if (dealerhand < playerhand):
                                                sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
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
                                                sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                                sound_effect.play()
                                                scene = 98
                                            if (dealerhand > 21):
                                                sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                                sound_effect.play()
                                                scene = 99
                                            if (dealerhand != 21 and dealerhand < 21):
                                                if (dealerhand >= playerhand):
                                                    sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                                    sound_effect.play()
                                                    scene = 98
                                                if (dealerhand < playerhand):
                                                    sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
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
                                                    sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                                    sound_effect.play()
                                                    scene = 98
                                                if (dealerhand > 21):
                                                    sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                                    sound_effect.play()
                                                    scene = 99
                                                if (dealerhand != 21 and dealerhand < 21):
                                                    if (dealerhand >= playerhand):
                                                        sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                                        sound_effect.play()
                                                        scene = 98
                                                    if (dealerhand < playerhand):
                                                        sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                                        sound_effect.play()
                                                        scene = 99
                                            else:
                                                if (dealerhand >= playerhand):
                                                    sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                                    sound_effect.play()
                                                    scene = 98
                                                if (dealerhand < playerhand):
                                                    sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                                    sound_effect.play()
                                                    scene = 99

                            elif(CARDVALUE3 + CARDVALUE4 == 21):
                                sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                sound_effect.play()
                                scene = 98
                            elif (CARDVALUE3 + CARDVALUE4 > 21):
                                sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                sound_effect.play()
                                scene = 99
                            else:
                                if (CARDVALUE3 + CARDVALUE4 < CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6):
                                    sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                    sound_effect.play()
                                    scene = 99
                                if (CARDVALUE3 + CARDVALUE4 >= CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6):
                                    sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                    sound_effect.play()
                                    scene = 98

                        if((CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6) > 21):
                            sound_effect = pygame.mixer.Sound("coinsound.mp3")
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
                                    sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                    sound_effect.play()
                                    scene = 98
                                elif (CARDVALUE3 + CARDVALUE4 > 21):
                                    sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                    sound_effect.play()
                                    scene = 99
                                elif(CARDVALUE1 + CARDVALUE2 >= 17):
                                    if (CARDVALUE3 + CARDVALUE4 < CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6 + CARDVALUE7):
                                        sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                        sound_effect.play()
                                        scene = 99
                                    if (CARDVALUE3 + CARDVALUE4 >= CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6 + CARDVALUE7):
                                        sound_effect = pygame.mixer.Sound("coinsound.mp3")
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
                                        sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                        sound_effect.play()
                                        scene = 98
                                    if (dealerhand > 21):
                                        sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                        sound_effect.play()
                                        scene = 99
                                    if(dealerhand != 21 and dealerhand < 21):
                                        if(dealerhand >= playerhand):
                                            sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                            sound_effect.play()
                                            scene = 98
                                        if(dealerhand < playerhand):
                                            sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
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
                                            sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                            sound_effect.play()
                                            scene = 98
                                        if(dealerhand > 21):
                                            sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                            sound_effect.play()
                                            scene = 99
                                        if (dealerhand != 21 and dealerhand < 21):
                                            if (dealerhand >= playerhand):
                                                sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                                sound_effect.play()
                                                scene = 98
                                            if (dealerhand < playerhand):
                                                sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
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
                                                sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                                sound_effect.play()
                                                scene = 98
                                            if (dealerhand > 21):
                                                sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                                sound_effect.play()
                                                scene = 99
                                            if (dealerhand != 21 and dealerhand < 21):
                                                if (dealerhand >= playerhand):
                                                    sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                                    sound_effect.play()
                                                    scene = 98
                                                if (dealerhand < playerhand):
                                                    sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
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
                                                    sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                                    sound_effect.play()
                                                    scene = 98
                                                if (dealerhand > 21):
                                                    sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                                    sound_effect.play()
                                                    scene = 99
                                                if (dealerhand != 21 and dealerhand < 21):
                                                    if (dealerhand >= playerhand):
                                                        sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                                        sound_effect.play()
                                                        scene = 98
                                                    if (dealerhand < playerhand):
                                                        sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                                        sound_effect.play()
                                                        scene = 99
                                            else:
                                                if (dealerhand >= playerhand):
                                                    sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                                    sound_effect.play()
                                                    scene = 98
                                                if (dealerhand < playerhand):
                                                    sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                                    sound_effect.play()
                                                    scene = 99

                            elif(CARDVALUE3 + CARDVALUE4 == 21):
                                sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                sound_effect.play()
                                scene = 98
                            elif (CARDVALUE3 + CARDVALUE4 > 21):
                                sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                sound_effect.play()
                                scene = 99
                            else:
                                if (CARDVALUE3 + CARDVALUE4 < CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6 + CARDVALUE7):
                                    sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                    sound_effect.play()
                                    scene = 99
                                if (CARDVALUE3 + CARDVALUE4 >= CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6 + CARDVALUE7):
                                    sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                    sound_effect.play()
                                    scene = 98

                        if((CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6 + CARDVALUE7) > 21):
                            sound_effect = pygame.mixer.Sound("coinsound.mp3")
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
                                    sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                    sound_effect.play()
                                    scene = 98
                                elif (CARDVALUE3 + CARDVALUE4 > 21):
                                    sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                    sound_effect.play()
                                    scene = 99
                                elif(CARDVALUE1 + CARDVALUE2 >= 17):
                                    if (CARDVALUE3 + CARDVALUE4 < CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6 + CARDVALUE7 + CARDVALUE8):
                                        sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                        sound_effect.play()
                                        scene = 99
                                    if (CARDVALUE3 + CARDVALUE4 >= CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6 + CARDVALUE7 + CARDVALUE8):
                                        sound_effect = pygame.mixer.Sound("coinsound.mp3")
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
                                        sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                        sound_effect.play()
                                        scene = 98
                                    if (dealerhand > 21):
                                        sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                        sound_effect.play()
                                        scene = 99
                                    if(dealerhand != 21 and dealerhand < 21):
                                        if(dealerhand >= playerhand):
                                            sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                            sound_effect.play()
                                            scene = 98
                                        if(dealerhand < playerhand):
                                            sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
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
                                            sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                            sound_effect.play()
                                            scene = 98
                                        if(dealerhand > 21):
                                            sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                            sound_effect.play()
                                            scene = 99
                                        if (dealerhand != 21 and dealerhand < 21):
                                            if (dealerhand >= playerhand):
                                                sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                                sound_effect.play()
                                                scene = 98
                                            if (dealerhand < playerhand):
                                                sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
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
                                                sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                                sound_effect.play()
                                                scene = 98
                                            if (dealerhand > 21):
                                                sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                                sound_effect.play()
                                                scene = 99
                                            if (dealerhand != 21 and dealerhand < 21):
                                                if (dealerhand >= playerhand):
                                                    sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                                    sound_effect.play()
                                                    scene = 98
                                                if (dealerhand < playerhand):
                                                    sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
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
                                                        sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                                        sound_effect.play()
                                                        scene = 98
                                                    if (dealerhand > 21):
                                                        sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                                        sound_effect.play()
                                                        scene = 99
                                                    if (dealerhand != 21 and dealerhand < 21):
                                                        if (dealerhand >= playerhand):
                                                            sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                                            sound_effect.play()
                                                            scene = 98
                                                        if (dealerhand < playerhand):
                                                            sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                                            sound_effect.play()
                                                            scene = 99
                                                else:
                                                    if (dealerhand >= playerhand):
                                                        sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                                        sound_effect.play()
                                                        scene = 98
                                                    if (dealerhand < playerhand):
                                                        sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                                        sound_effect.play()
                                                        scene = 99

                            elif(CARDVALUE3 + CARDVALUE4 == 21):
                                sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                sound_effect.play()
                                scene = 98
                            elif (CARDVALUE3 + CARDVALUE4 > 21):
                                sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                sound_effect.play()
                                scene = 99
                            else:
                                if (CARDVALUE3 + CARDVALUE4 < CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6 + CARDVALUE7 + CARDVALUE8):
                                    sound_effect = pygame.mixer.Sound("blackjackwin.mp3")
                                    sound_effect.play()
                                    scene = 99
                                if (CARDVALUE3 + CARDVALUE4 >= CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6 + CARDVALUE7 + CARDVALUE8):
                                    sound_effect = pygame.mixer.Sound("coinsound.mp3")
                                    sound_effect.play()
                                    scene = 98

                        if((CARDVALUE1 + CARDVALUE2 + CARDVALUE5 + CARDVALUE6 + CARDVALUE7 + CARDVALUE8) > 21):
                            sound_effect = pygame.mixer.Sound("coinsound.mp3")
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
                                with open("gamedata.txt", "r") as file:
                                    lines = file.readlines()
                                    gold = gold - moneychoosen
                                    lines[0] = f"gold = {gold}\n"
                                with open("gamedata.txt", "w") as file:
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
                                with open("gamedata.txt", "r") as file:
                                    lines = file.readlines()
                                    gold = gold - moneychoosen
                                    lines[0] = f"gold = {gold}\n"
                                with open("gamedata.txt", "w") as file:
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
                                with open("gamedata.txt", "r") as file:
                                    lines = file.readlines()
                                    gold = gold + moneychoosen
                                    lines[0] = f"gold = {gold}\n"
                                with open("gamedata.txt", "w") as file:
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
        video = cv2.VideoCapture("glowparticlevideo.mp4")

        startTime = pygame.time.get_ticks()
        self.gamescene = 1
        x = 390
        y = 600
        alchemylevelupbool = False
        boolleftorright = True
        mouse_pos = pygame.mouse.get_pos()
        pygame.mixer.music.load("bardmusic.mp3")
        pygame.mixer.music.queue("bardmusic2.mp3")
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
        while self.guildbool1:
            with open("gamedata.txt", "r") as file:
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
                guildtutorial = int(guildtutorial)

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

            with open("gamedata.txt", "r") as file:
                lines = file.readlines()
                guildguide = lines[14].strip()
                guildguide = guildguide[16:]

            if (guildguide == 'true'):
                self.gamescene = 1
            elif (guildguide == 'false'):
                self.gamescene = 11


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
                            sound_effect = pygame.mixer.Sound("clicknoise.mp3")
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
                            sound_effect = pygame.mixer.Sound("clicknoise.mp3")
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
                            sound_effect = pygame.mixer.Sound("clicknoise.mp3")
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
                            sound_effect = pygame.mixer.Sound("clicknoise.mp3")
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
                            sound_effect = pygame.mixer.Sound("clicknoise.mp3")
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
                            sound_effect = pygame.mixer.Sound("clicknoise.mp3")
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
                            sound_effect = pygame.mixer.Sound("clicknoise.mp3")
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
                            sound_effect = pygame.mixer.Sound("clicknoise.mp3")
                            sound_effect.play()

                            with open("gamedata.txt", "r") as file:
                                lines = file.readlines()
                                lines[14] = f"guildtutorial = false\n"
                            with open("gamedata.txt", "w") as file:
                                file.writelines(lines)  # Write the modified lines back to the file



                            self.gamescene = self.gamescene + 1
                            print("guild join initiated")
                        if norect.collidepoint(mouse_pos):
                            sound_effect = pygame.mixer.Sound("clicknoise.mp3")
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
                            sound_effect = pygame.mixer.Sound("clicknoise.mp3")
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
                            if(guildtutorial == 1):
                                self.gamescene = 54
                            elif (guildtutorial == 0):
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
                            sound_effect = pygame.mixer.Sound("clicknoise.mp3")
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
                            sound_effect = pygame.mixer.Sound("clicknoise.mp3")
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
                            sound_effect = pygame.mixer.Sound("clicknoise.mp3")
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
                            sound_effect = pygame.mixer.Sound("clicknoise.mp3")
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
                            sound_effect = pygame.mixer.Sound("clicknoise.mp3")
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
                            sound_effect = pygame.mixer.Sound("clicknoise.mp3")
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
                guildtutorial = 1
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
                            sound_effect = pygame.mixer.Sound("clicknoise.mp3")
                            pygame.mixer.music.load("alchemy2.mp3")
                            pygame.mixer.music.play(-1)
                            pygame.mixer.music.queue("alchemy3.mp3")
                            pygame.mixer.music.queue("alchemy1.mp3")
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
                randompotionvalue = random.randint(1,4)
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
                pygame.display.update()

                if alchemyhitrect.collidepoint(x + 47, 150):
                    sound_effect = pygame.mixer.Sound("potioncreation.mp3")
                    sound_effect.play()
                    streak = streak + 1
                    alchemyexp = alchemyexp + 1 + streak
                    gold = int(gold + (randompotionvalue * (alchemylevel + (streak / 4))))
                    if(alchemyexp >= (alchemylevel * 100)):
                        alchemyexp = 0
                        alchemylevel = alchemylevel + 1
                        alchemylevelupbool = True
                if alchemyhitrect2.collidepoint(x + 47, 150):
                    sound_effect = pygame.mixer.Sound("potioncreation.mp3")
                    sound_effect.play()
                    streak = streak + 1
                    alchemyexp = alchemyexp + 1 + streak
                    gold = int(gold + (randompotionvalue * (alchemylevel + (streak / 4))))
                    if(alchemyexp >= (alchemylevel * 100)):
                        alchemyexp = 0
                        alchemylevel = alchemylevel + 1
                        alchemylevelupbool = True
                if superalchemyhitrect.collidepoint(x + 47, 150):
                    sound_effect = pygame.mixer.Sound("potioncreation.mp3")
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
                    sound_effect = pygame.mixer.Sound("messedupalchemy.mp3")
                    sound_effect.play()

                with open("gamedata.txt", "r") as file:
                    lines = file.readlines()
                    lines[0] = f"gold = {gold}\n"
                    lines[1] = f"gem = {gem}\n"
                    lines[12] = f"alchemyexp = {alchemyexp}\n"
                    lines[13] = f"alchemylevel = {alchemylevel}\n"
                    lines[14] = f"guildtutorial = {1}\n"
                with open("gamedata.txt", "w") as file:
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
                            sound_effect = pygame.mixer.Sound("clicknoise.mp3")
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
                            sound_effect = pygame.mixer.Sound("clicknoise.mp3")
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
                        sound_effect = pygame.mixer.Sound("clicknoise.mp3")
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
        video3 = cv2.VideoCapture("starglitter2.mp4")
        video = cv2.VideoCapture("starglitter.mp4")
        video2 = cv2.VideoCapture("unboxingcreature.mp4")
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
        pygame.mixer.music.load("battletheme.mp3")
        pygame.mixer.music.queue("etherealmusic.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        print("blackmarket shop initialized")
        global textFader
        global characterName
        global firsttimeblackmarket

        with open("gamedata.txt", "r") as file:
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

            with open("gamedata.txt", "r") as file:
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
                draw_text_center('Hehehe, welcome welcome human. Your quite', font5, DARKGREEN, DISPLAYSURF, 1300, 200)
                draw_text_center('handsome arent you. You can call me Byron,', font5, DARKGREEN, DISPLAYSURF, 1300, 225)
                draw_text_center('im the owner of this humble establishment.', font5, DARKGREEN, DISPLAYSURF, 1300, 250)
                draw_text_center('Come let me show you the merchandise.', font5, DARKGREEN, DISPLAYSURF, 1300, 275)

                self.gamescene = self.xbutton(self.gamescene)
                pygame.display.update()
            if (self.gamescene == 3):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image243, (195, 100))
                DISPLAYSURF.blit(image53, (1050, 150))

                draw_text_center('Your not collaborating with the royal guards', font5, DARKGREEN, DISPLAYSURF, 1300, 200)
                draw_text_center('are you? Those bastards have been on my ass', font5, DARKGREEN, DISPLAYSURF, 1300, 225)
                draw_text_center('for a while. Not that it matters much anyways,', font5, DARKGREEN, DISPLAYSURF, 1300, 250)
                draw_text_center('ill just take care of you like the rest', font5, DARKGREEN, DISPLAYSURF, 1300, 275)
                self.gamescene = self.xbutton(self.gamescene)
                pygame.display.update()
            if (self.gamescene == 4):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image243, (195, 100))
                DISPLAYSURF.blit(image53, (1050, 150))

                draw_text_center('Im just kidding, dont be so tense handsome.', font5, DARKGREEN, DISPLAYSURF, 1300, 200)
                draw_text_center(' I dont bite, much...', font5, DARKGREEN, DISPLAYSURF, 1300, 225)
                self.gamescene = self.xbutton(self.gamescene)
                pygame.display.update()
            if (self.gamescene == 5):
                with open("gamedata.txt", "r") as file:
                    lines = file.readlines()
                    lines[22] = f"firstblackmarket = false\n"
                with open("gamedata.txt", "w") as file:
                    file.writelines(lines)  # Write the modified lines back to the file
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image243, (195, 100))
                DISPLAYSURF.blit(image53, (1050, 150))

                draw_text_center('Now tell, are you here to purchase some', font5, DARKGREEN, DISPLAYSURF, 1300, 200)
                draw_text_center('creatures or are you here for me? *wink*', font5, DARKGREEN, DISPLAYSURF, 1300, 225)
                draw_text_center('p', font15, SKYBLUE, DISPLAYSURF, 1300, 250)
                self.gamescene = self.xbutton(self.gamescene)
                pygame.display.update()
            if (self.gamescene == 6):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image243, (195, 100))
                DISPLAYSURF.blit(image53, (1050, 150))

                draw_text_center('hehe,', font5, DARKGREEN, DISPLAYSURF, 1300, 200)
                draw_text_center('Follow me ill show you our merchandise.', font5, DARKGREEN, DISPLAYSURF, 1300, 225)

                self.gamescene = self.xbutton(self.gamescene)
                pygame.display.update()
                music1 = True
            if (self.gamescene == 7):
                if(music1):
                    pygame.mixer.music.load("angels.mp3")
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

                Bigswordfont= pygame.font.Font("SwordsmanFont.TTF", 50)

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
                            sound_effect = pygame.mixer.Sound("shopclicksound.mp3")
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
                                    sound_effect = pygame.mixer.Sound("ingamepurchase.mp3")
                                    sound_effect.play()
                                    with open("gamedata.txt", "r") as file:
                                        lines = file.readlines()
                                        lines[0] = f"gold = {gold}\n"
                                    with open("gamedata.txt", "w") as file:
                                        file.writelines(lines)
                                    transition(1)
                                    sound_effect = pygame.mixer.Sound("treasureopen.mp3")
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
                            sound_effect = pygame.mixer.Sound("shopclicksound.mp3")
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
                                    sound_effect = pygame.mixer.Sound("ingamepurchase.mp3")
                                    sound_effect.play()
                                    with open("gamedata.txt", "r") as file:
                                        lines = file.readlines()
                                        lines[0] = f"gold = {gold}\n"
                                    with open("gamedata.txt", "w") as file:
                                        file.writelines(lines)
                                    transition(1)
                                    sound_effect = pygame.mixer.Sound("treasureopen.mp3")
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
                            sound_effect = pygame.mixer.Sound("shopclicksound.mp3")
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
                                    sound_effect = pygame.mixer.Sound("ingamepurchase.mp3")
                                    sound_effect.play()
                                    with open("gamedata.txt", "r") as file:
                                        lines = file.readlines()
                                        lines[0] = f"gold = {gold}\n"
                                    with open("gamedata.txt", "w") as file:
                                        file.writelines(lines)

                                    transition(1)
                                    sound_effect = pygame.mixer.Sound("treasureopen.mp3")
                                    sound_effect.play()
                                    self.gamescene = 15

                if(itemdisplay == 3):
                    draw_text('100 Gems', font11, rainbow, DISPLAYSURF, 1430, 260)
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
                            draw_text_center('lvl10 Req', Fontbig, BLUE, DISPLAYSURF, halfdisplay, 797)
                            draw_text_center('lvl10 Req', Fontbig, RED, DISPLAYSURF, halfdisplay, 797, int(opacitynum / 2))
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
                            sound_effect = pygame.mixer.Sound("shopclicksound.mp3")
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
                                if (gem >= 100 and level >= 10):
                                    gem = gem - 100
                                    sound_effect = pygame.mixer.Sound("ingamepurchase.mp3")
                                    sound_effect.play()
                                    with open("gamedata.txt", "r") as file:
                                        lines = file.readlines()
                                        lines[1] = f"gem = {gem}\n"
                                    with open("gamedata.txt", "w") as file:
                                        file.writelines(lines)

                                    transition(1)
                                    sound_effect = pygame.mixer.Sound("scaryhowlverb.mp3")
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
                                sound_effect = pygame.mixer.Sound("clicknoise.mp3")
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
                                sound_effect = pygame.mixer.Sound("clicknoise.mp3")
                                sound_effect.play()
                                pygame.mixer.music.set_volume(0.4)
                                pygame.display.update()
                                textFader = 0
                                self.gamescene = self.gamescene + 1

                if(randomtext == 0):
                    draw_text_center('Hey cutie your back again I see!', font5, DARKGREEN, DISPLAYSURF, 1300, 200)
                elif(randomtext == 1):
                    draw_text_center('Awwww did you miss me that much? You are' +characterName +"?", font5, DARKGREEN, DISPLAYSURF, 1300, 200)
                    draw_text_center('back already '+str(characterName), font5, DARKGREEN, DISPLAYSURF, 1300, 225)
                elif(randomtext == 2):
                    draw_text_center('My richest customer is back again!', font5, DARKGREEN, DISPLAYSURF, 1300, 200)
                    draw_text_center(' please be gentle with me '+str(characterName) +"!", font5, DARKGREEN, DISPLAYSURF, 1300, 225)

                elif(randomtext == 3):
                    draw_text_center('Well well well, look who it is,', font5, DARKGREEN, DISPLAYSURF, 1300, 200)
                    draw_text_center('my cutest customer.', font5, DARKGREEN, DISPLAYSURF, 1300, 225)

                elif(randomtext == 4):
                    draw_text_center('Where have you been? You havent visited', font5, DARKGREEN, DISPLAYSURF, 1300, 200)
                    draw_text_center('in so long! Humphh', font5, DARKGREEN, DISPLAYSURF, 1300, 225)
                elif(randomtext == 5):
                    draw_text_center('hufph, Im not in a good mood, the siren', font5, DARKGREEN, DISPLAYSURF, 1300, 200)
                    draw_text_center('slave shipment escaped earlier...', font5, DARKGREEN, DISPLAYSURF, 1300, 225)

                elif(randomtext == 6):
                    draw_text_center('I got some interesting new mechandise just', font5, DARKGREEN, DISPLAYSURF, 1300, 200)
                    draw_text_center('for you sweetheart!', font5, DARKGREEN, DISPLAYSURF, 1300, 225)
                elif(randomtext == 7):
                    draw_text_center('Should I open a brothel, im sure you', font5, DARKGREEN, DISPLAYSURF, 1300, 200)
                    draw_text_center('would be my biggest customer..', font5, DARKGREEN, DISPLAYSURF, 1300, 225)
                    draw_text_center('or would you like to work there?', font5, DARKGREEN, DISPLAYSURF, 1300, 250)

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
                                sound_effect = pygame.mixer.Sound("clicknoise.mp3")
                                sound_effect.play()
                                pygame.mixer.music.set_volume(0.4)
                                pygame.display.update()
                                textFader = 0
                                self.gamescene = self.gamescene + 1
                draw_text_center('what are you waiting for darling,', font5, DARKGREEN, DISPLAYSURF, 1300, 200)
                draw_text_center('go on and take a look around', font5, DARKGREEN, DISPLAYSURF, 1300, 225)
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
                        sound_effect = pygame.mixer.Sound("beastsummon.mp3")
                        sound_effect.play()

                    DISPLAYSURF.blit(beasts[randombeast], (700, 380))
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

                draw_text('Lvl- ' +str(Beastlevel), font20, WHITE, DISPLAYSURF, 1375, 300)
                draw_text('Hp- ' +str(int((basehp + (basehp * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 400)
                draw_text('Def- ' +str(int((basedefense + (basehp * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 500)
                draw_text('Str- ' +str(int((basestrength + (basehp * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 600)
                draw_text('Sp. Att- ' +str(int((basespecattack + (basehp * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 700)
                draw_text('Speed- ' +str(int((basespeed + (basehp * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 800)
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
                        sound_effect = pygame.mixer.Sound("beastsummon2.wav")
                        sound_effect.play()

                    DISPLAYSURF.blit(beasts[randombeast], (700, 380))
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

                draw_text('Lvl- ' +str(Beastlevel), font20, WHITE, DISPLAYSURF, 1375, 300)
                draw_text('Hp- ' +str(int((basehp + (basehp * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 400)
                draw_text('Def- ' +str(int((basedefense + (basehp * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 500)
                draw_text('Str- ' +str(int((basestrength + (basehp * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 600)
                draw_text('Sp. Att- ' +str(int((basespecattack + (basehp * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 700)
                draw_text('Speed- ' +str(int((basespeed + (basehp * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 800)
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
                        randombeast = random.randint(0, 50)
                    if(i == lootcratespeed):
                        i = 0
                    if(lootcratespeed == 20):
                        transition(10)
                        sound_effect = pygame.mixer.Sound("beastsummon2.wav")
                        sound_effect.play()

                    DISPLAYSURF.blit(beasts[randombeast], (700, 380))
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

                draw_text('Lvl- ' +str(Beastlevel), font20, WHITE, DISPLAYSURF, 1375, 300)
                draw_text('Hp- ' +str(int((basehp + (basehp * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 400)
                draw_text('Def- ' +str(int((basedefense + (basehp * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 500)
                draw_text('Str- ' +str(int((basestrength + (basehp * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 600)
                draw_text('Sp. Att- ' +str(int((basespecattack + (basehp * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 700)
                draw_text('Speed- ' +str(int((basespeed + (basehp * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 800)
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
                        randombeast = random.randint(0, 25)
                    if(i == lootcratespeed):
                        i = 0
                    if(lootcratespeed == 20):
                        transition(10)
                        sound_effect = pygame.mixer.Sound("beastsummon2.wav")
                        sound_effect.play()

                    DISPLAYSURF.blit(beasts[randombeast], (700, 380))
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

                draw_text('Lvl- ' +str(Beastlevel), font20, WHITE, DISPLAYSURF, 1375, 300)
                draw_text('Hp- ' +str(int((basehp + (basehp * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 400)
                draw_text('Def- ' +str(int((basedefense + (basehp * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 500)
                draw_text('Str- ' +str(int((basestrength + (basehp * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 600)
                draw_text('Sp. Att- ' +str(int((basespecattack + (basehp * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 700)
                draw_text('Speed- ' +str(int((basespeed + (basehp * .2 * Beastlevel) + (1 * Beastlevel)) * (1 + tier * .1))), font20, WHITE, DISPLAYSURF, 1375, 800)
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
                            lootcratespeed = 1
                            self.gamescene = 7


        with open("gamedata.txt", "r") as file:
            lines = file.readlines()
            lines[0] = f"gold = {gold}\n"
            lines[1] = f"gem = {gem}\n"
        with open("gamedata.txt", "w") as file:
            file.writelines(lines)
        return 0
########################################################################################################################
########################################################################################################################