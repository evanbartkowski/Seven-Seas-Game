import pygame
from pygame.locals import *
import sys
import math
import random
import game
import string
import cv2
import os
import time
import json

pygame.init()
pygame.mixer.init()
########################################################################################################################
image0 = pygame.image.load('images/sevenseaslogo.webp')
pygame.display.set_caption("Seven Seas")
pygame.display.set_icon(image0)
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
menu3_active = False
cutscene1 = False
completetutorial = True

FaderBool = True
Fader = 1.00
textFader = 0
characterName = ''
gold = 0

cap = cv2.VideoCapture("video/intromovie3.mov")
capv2 = cv2.VideoCapture("video/monsterdissapear.mov")
capv3 = cv2.VideoCapture("video/characterchoosevideo.mp4")
capv4 = cv2.VideoCapture("video/wavetransitionknight.mp4")

imagen1 = pygame.image.load('images/scroll1.png')
imagen1 = pygame.transform.scale(imagen1, (300, 100))
imagen2 = pygame.image.load('images/scroll2.png')
imagen2 = pygame.transform.scale(imagen2, (300, 100))
imagen3 = pygame.image.load('images/scroll3.png')
imagen3 = pygame.transform.scale(imagen3, (300, 100))
imagen4 = pygame.image.load('images/scroll4.png')
imagen4 = pygame.transform.scale(imagen4, (300, 100))
imagen6 = pygame.image.load('images/goldglow.png')
imagen6 = pygame.transform.scale(imagen6, (100, 100))
image1 = pygame.image.load('images/SevenSeasStartScreen.jfif')
image1 = pygame.transform.scale(image1, (1550, 870))
image2 = pygame.image.load('images/parchment.png')
image2 = pygame.transform.scale(image2, (750, 800))
image3 = pygame.transform.rotate(image2, 180)
image4 = pygame.image.load('images/blackscreen.jpg')
image4 = pygame.transform.scale(image4, (3920, 1080))
image5 = pygame.image.load('images/loadmenu.jpg')
image5 = pygame.transform.scale(image5, (1550, 870))
image6 = pygame.image.load('images/goldbox.png')
image12 = pygame.image.load('images/darkwater1.webp')
image12 = pygame.transform.scale(image12, (1550, 870))
image13 = pygame.image.load('images/darkwater2.webp')
image13 = pygame.transform.scale(image13, (1550, 870))
image14 = pygame.image.load('images/darkwater3.webp')
image14 = pygame.transform.scale(image14, (1550, 870))
image15 = pygame.image.load('images/darkwater4.webp')
image15 = pygame.transform.scale(image15, (1550, 870))
image16 = pygame.image.load('images/strangefish.webp')
image16 = pygame.transform.scale(image16, (1550, 870))
image17 = pygame.image.load('images/mermaid1.jpg')
image17 = pygame.transform.scale(image17, (1550, 870))

imagemermaid1 = pygame.image.load('images/mermaidd1.jpeg')
imagemermaid1 = pygame.transform.scale(imagemermaid1, (1550, 870))
imagemermaid2 = pygame.image.load('images/mermaidd2.jpeg')
imagemermaid2 = pygame.transform.scale(imagemermaid2, (1550, 870))
imagemermaid3 = pygame.image.load('images/mermaidd3.webp')
imagemermaid3 = pygame.transform.scale(imagemermaid3, (1550, 870))


image19 = pygame.image.load('images/lucidea.jpg')
image19 = pygame.transform.scale(image19, (1550, 870))

image21 = pygame.image.load('images/nightmare1.jpg')
image21 = pygame.transform.scale(image21, (1550, 870))
image22 = pygame.image.load('images/orb.webp')
image22 = pygame.transform.scale(image22, (300, 300))
image23 = pygame.image.load('images/injured.jpg')
image23 = pygame.transform.scale(image23, (1550, 870))
image24 = pygame.image.load('images/mermaidguards.jpg')
image24 = pygame.transform.scale(image24, (1550, 870))
image25 = pygame.image.load('images/nightmare2.jpg')
image25 = pygame.transform.scale(image25, (1550, 870))
image26 = pygame.image.load('images/goldendragon.webp')
image26 = pygame.transform.scale(image26, (1550, 870))
image27 = pygame.image.load('images/goldbeam1.jfif')
image27 = pygame.transform.scale(image27, (1550, 870))
image28 = pygame.image.load('images/goldbeam2.jfif')
image28 = pygame.transform.scale(image28, (1550, 870))
image29 = pygame.image.load('images/aura.png')
image29 = pygame.transform.scale(image29, (500, 500))
image30 = pygame.image.load('images/skipbutton.png')
image30 = pygame.transform.scale(image30, (90, 50))
image31 = pygame.image.load('images/purplerect.png')
image31 = pygame.transform.scale(image31, (50, 80))
image32 = pygame.image.load('images/button.png')
image32 = pygame.transform.scale(image32, (700, 700))
image33 = pygame.image.load('images/greencircle.png')
image33 = pygame.transform.scale(image33, (630, 630))
image34 = pygame.image.load('images/kneelingknight.webp')
image34 = pygame.transform.scale(image34, (1550, 870))
image35 = pygame.image.load('images/standingknight.webp')
image35 = pygame.transform.scale(image35, (1550, 870))
image36 = pygame.image.load('images/Nightmarecloseup.webp')
image36 = pygame.transform.scale(image36, (1550, 870))
image37 = pygame.image.load('images/teleportingnightmare.webp')
image37 = pygame.transform.scale(image37, (1550, 870))
image38 = pygame.image.load('images/seafloordark.webp')
image38 = pygame.transform.scale(image38, (1550, 870))
image39 = pygame.image.load('images/fancygoldline.webp')
image39 = pygame.transform.scale(image39, (700, 200))
image40 = pygame.image.load('images/tridentstab.webp')
image41 = pygame.image.load('images/mainmap.JPG')
image41 = pygame.transform.scale(image41, (1550, 870))
image42 = pygame.image.load('images/yellowdiamond.png')
image42 = pygame.transform.scale(image42, (30, 30))
image43 = pygame.image.load('images/gamblemap.jpg')
image43 = pygame.transform.scale(image43, (1550, 870))
image44 = pygame.image.load('images/paimonmap.jpg')
image44 = pygame.transform.scale(image44, (1550, 870))
image45 = pygame.image.load('images/colleseummap.jpg')
image45 = pygame.transform.scale(image45, (1550, 870))
image46 = pygame.image.load('images/workmap.jpg')
image46 = pygame.transform.scale(image46, (1550, 870))
image47 = pygame.image.load('images/castlemap.jpg')
image47 = pygame.transform.scale(image47, (1550, 870))
image48 = pygame.image.load('images/adventuremap.jpg')
image48 = pygame.transform.scale(image48, (1550, 870))
image49 = pygame.image.load('images/guildmap.jpg')
image49 = pygame.transform.scale(image49, (1550, 870))
image50 = pygame.image.load('images/stashmap.jpg')
image50 = pygame.transform.scale(image50, (1550, 870))
image51 = pygame.image.load('images/blackmarketmap.jpg')
image51 = pygame.transform.scale(image51, (1550, 870))
image52 = pygame.image.load('images/knightwalkthrough.png')
image52 = pygame.transform.scale(image52, (500, 250))
image53 = pygame.image.load('images/speechbubble.png')
image53 = pygame.transform.scale(image53, (400, 200))
image55 = pygame.image.load('images/mainmap.JPG')
image55 = pygame.transform.scale(image55, (1550, 870))
image56 = pygame.image.load('images/blueglow.png')
image56 = pygame.transform.scale(image56, (100, 100))
image57 = pygame.image.load('images/crack.png')
image57 = pygame.transform.scale(image57, (1200, 1200))
image58 = pygame.image.load('images/paimonshop.webp')
image58 = pygame.transform.scale(image58, (1550, 870))
image59 = pygame.image.load('images/bubble.png')
image59 = pygame.transform.scale(image59, (25, 25))
image60 = pygame.image.load('images/bubble.png')
image60 = pygame.transform.scale(image60, (35, 35))
image61 = pygame.image.load('images/bubble.png')
image61 = pygame.transform.scale(image61, (55, 55))
image62 = pygame.image.load('images/cardboardbox.png')
image62 = pygame.transform.scale(image62, (120, 100))
image63 = pygame.image.load('images/glowbox.png')
image63 = pygame.transform.scale(image63, (120, 100))
image64 = pygame.image.load('images/sillycrab.png')
image64 = pygame.transform.scale(image64, (100, 100))
image65 = pygame.image.load('images/reddownarrow.png')
image65 = pygame.transform.scale(image65, (75, 150))
########################################################################################################################
displaylength = 1920
displayheight = 1080
halfdisplay = displaylength / 2
DISPLAYSURF = pygame.display.set_mode((displaylength, displayheight))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
font = pygame.font.SysFont(None, 75)
font2 = pygame.font.SysFont("Arial", 60)
font3 = pygame.font.SysFont("Times New Roman", 40)
font4 = pygame.font.SysFont("Comic Sans", 40)
font5 = pygame.font.SysFont("Comic Sans", 20)
font6 = pygame.font.Font("fonts/Danger.otf", 25)
font7 = pygame.font.Font("fonts/eroded.ttf", 20)
font8 = pygame.font.Font("fonts/HelpMe.ttf", 20)
font9 = pygame.font.Font("fonts/Overwave.otf", 20)
font10 = pygame.font.Font("fonts/Comfy.otf", 22)
font11 = pygame.font.Font("fonts/anime.otf", 15)
font12 = pygame.font.Font("fonts/oldenFont.otf", 50)
font13 = pygame.font.Font("fonts/SwordsmanFont.TTF", 20)
font14 = pygame.font.Font("fonts/AsianFont.ttf", 20)
font15 = pygame.font.Font("fonts/womenfont.ttf", 20)
font16 = pygame.font.Font("fonts/runefont.otf", 50)
font17 = pygame.font.Font("fonts/dragonfont.ttf", 20)
font18 = pygame.font.Font("fonts/oldenFont.otf", 70)
font19 = pygame.font.Font("fonts/Danger.otf", 100)
font20 = pygame.font.Font("fonts/AsianFont.ttf", 60)
font21 = pygame.font.SysFont("Comic Sans", 16)
font22 = pygame.font.Font("fonts/AsianFont.ttf", 50)
font23 = pygame.font.Font("fonts/oldenFont.otf", 35)
font24 = pygame.font.Font("fonts/AsianFont.ttf", 40)
font25 = pygame.font.SysFont("Comic Sans", 30)
font26 = pygame.font.Font("fonts/AsianFont.ttf", 30)

gameStatus = True
########################################################################################################################
# Function to display text on the screen
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
def save_teamcreature(creature_data, filename="teamdata.txt"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)  # Load existing data
    except (FileNotFoundError, json.JSONDecodeError):
        data = []  # If file doesn't exist or is empty, start with an empty list

    data.append(creature_data)  # Add new creature data

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)  # Save updated data
########################################################################################################################
class StartMenu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.menu_active = True
    def StartupScreen(self):
        fade_in = True  # Boolean to control fade direction
        clickAlpha = 20  # Initial alpha value
        fade_speed = .25 # Speed of fade

        fade_inLoadScreen = True  # Boolean to control fade direction
        clickAlphaLoadScreen = 0  # Initial alpha value
        fade_speedLoadScreen = .4 # Speed of fade

        fade_surface = pygame.Surface(DISPLAYSURF.get_size())
        fade_surface.fill(BLACK)
        pygame.mixer.music.load("audio/background_music1.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        scrollflip1 = False
        scrollflip2 = False

        bubbles = 500
        bubblex = []
        bubbley = []
        bubblechooser = []
        while(bubbles != 0):
            bubblex.append(random.randint(1, 2000))
            bubbley.append((bubbles * 140) + (random.randint(1, 12000)))
            bubblechooser.append(random.randint(0, 2))
            bubbles = bubbles - 1

        while self.menu_active:
            startTime = pygame.time.get_ticks()
            DISPLAYSURF.fill(WHITE)
            DISPLAYSURF.blit(image1, (191, 105))
            rainbowcolor1 = int((math.sin(startTime * 0.002) + 1) * 127.5)
            rainbowcolor2 = int((math.sin(startTime * 0.003 + 2) + 1) * 127.5)
            rainbowcolor3 = int((math.sin(startTime * 0.004 + 2) + 1) * 127.5)

            scrollrect1 = pygame.Rect(207, 150, 315, 100)
            scrollrect2 = pygame.Rect(1410, 150, 315, 100)
            scrollrect3 = pygame.Rect(180, 249, 1600, 900)
            mouseX, mouseY = pygame.mouse.get_pos()
            mouse_pos = pygame.mouse.get_pos()

            bubblecounter = 499
            while (bubblecounter > 0):
                bubbley[bubblecounter] = bubbley[bubblecounter] - 2
                image59.set_alpha(170)
                image60.set_alpha(170)
                image61.set_alpha(170)
                if(bubblechooser[bubblecounter] == 0):
                    DISPLAYSURF.blit(image59, (bubblex[bubblecounter], bubbley[bubblecounter]))
                elif(bubblechooser[bubblecounter] == 1):
                    DISPLAYSURF.blit(image60, (bubblex[bubblecounter], bubbley[bubblecounter]))
                elif(bubblechooser[bubblecounter] == 2):
                    DISPLAYSURF.blit(image61, (bubblex[bubblecounter], bubbley[bubblecounter]))
                bubblecounter = bubblecounter - 1


            if(scrollflip1 == False):
                imagen1.set_alpha(220)
                if scrollrect1.collidepoint(mouse_pos):
                    imagen3.set_alpha(250)
                    DISPLAYSURF.blit(imagen3, (220, 155))
                else:
                    DISPLAYSURF.blit(imagen1, (220, 155))
            if (scrollflip2 == False):
                imagen2.set_alpha(220)
                if scrollrect2.collidepoint(mouse_pos):
                    imagen4.set_alpha(250)
                    DISPLAYSURF.blit(imagen4, (1410, 155))
                else:
                    DISPLAYSURF.blit(imagen2, (1410, 155))

            if(scrollflip1):
                DISPLAYSURF.blit(image2, (-20, 155))
                draw_text('Update Log', font4, WHITE, DISPLAYSURF, 245, 210, 200)
                draw_text('- Smoother Transitions', font5, WHITE, DISPLAYSURF, 250, 310, 200)
                draw_text('- Custom Names', font5, WHITE, DISPLAYSURF, 250, 350, 200)
                draw_text('- Load Game Screen', font5, WHITE, DISPLAYSURF, 250, 390, 200)
                draw_text('- Mermaid Lore', font5, WHITE, DISPLAYSURF, 250, 430, 200)
                draw_text('- Character Creation', font5, WHITE, DISPLAYSURF, 250, 470, 200)
                draw_text('- AI Art', font5, WHITE, DISPLAYSURF, 250, 510, 200)
            if (scrollflip2):
                DISPLAYSURF.blit(image3, (1190, 155))
                draw_text('Legends', font4, WHITE, DISPLAYSURF, 1490, 210, 200)
                draw_text('- Creatures larger than ', font5, WHITE, DISPLAYSURF, 1450, 310, 200)
                draw_text('mountains have been', font5, WHITE, DISPLAYSURF, 1450, 330, 200)
                draw_text('spotted around Eurealian', font5, WHITE, DISPLAYSURF, 1450, 350, 200)
                draw_text('Territory', font5, WHITE, DISPLAYSURF, 1450, 370, 200)
                draw_text('- The beginning of a', font5, WHITE, DISPLAYSURF, 1440, 420, 200)
                draw_text('a thousand year prophecy,', font5, WHITE, DISPLAYSURF, 1440, 440, 200)
                draw_text('will you bring peace back', font5, WHITE, DISPLAYSURF, 1440, 460,200)
                draw_text('to the Seven Seas?', font5, WHITE, DISPLAYSURF, 1440, 480, 200)

                # Display the Start Menu options
            rect_position = (DISPLAYSURF.get_width() - 40, 10, 50, 50)
            pygame.draw.rect(DISPLAYSURF, WHITE, rect_position)
            draw_text_center('hjygfdkfogaijklsavcsfam', font16, (20, 20, rainbowcolor1), DISPLAYSURF, halfdisplay, 125, 200)
            draw_text_center('[ Click to Begin Journey ]', font4, (rainbowcolor1, rainbowcolor2, rainbowcolor3), DISPLAYSURF, halfdisplay, 730, clickAlpha)
            draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
            if 1680 <= mouse_pos[0] <= 1920 and 0 <= mouse_pos[1] <= 155:
                draw_text('x', font4, (rainbowcolor2,rainbowcolor3, rainbowcolor1), DISPLAYSURF,1685, 105)
            # Adjust alpha for fade effect
            if fade_in:
                clickAlpha += fade_speed
                if clickAlpha >= 255:  # If fully visible
                    clickAlpha = 255
                    fade_in = False  # Start fading out
            else:
                clickAlpha -= fade_speed - .25
                if clickAlpha <= 0:  # If fully transparent
                    clickAlpha = 50
                    fade_in = True  # Start fading in

            # Adjust alpha for fade effect on loading screen
            if fade_inLoadScreen:
                clickAlphaLoadScreen += fade_speedLoadScreen
                if clickAlphaLoadScreen >= 255:  # If fully visible
                    clickAlphaLoadScreen = 255
                    fade_inLoadScreen = False  # Start fading out
            fade_surface.set_alpha(255 - clickAlphaLoadScreen)  # Inverse alpha for fade-in
            DISPLAYSURF.blit(fade_surface, (0, 0))

            mouseX, mouseY = pygame.mouse.get_pos()
            imagen6.set_alpha(140)
            DISPLAYSURF.blit(imagen6, (mouseX - 47, mouseY - 54))
            # Check for user input
            for event in pygame.event.get():
                mouseX, mouseY = pygame.mouse.get_pos()
                imagen6.set_alpha(140)
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    # Check if "Start Game" is clicked
                    if scrollrect3.collidepoint(mouse_pos):
                        sound_effect = pygame.mixer.Sound("audio/nextlevel.mp3")
                        pygame.mixer.music.set_volume(0.5)
                        sound_effect.play()
                        print("Game Exited")
                        for i in range(235):
                            image4.set_alpha(i)
                            DISPLAYSURF.blit(image4, (0,0))
                            draw_text_center('Mermaids have ruled the seas since the dawn of time. Once united, now divided by greed. There absolute power has dwindled into lesser 4 factions.', font5, WHITE, DISPLAYSURF, halfdisplay, 900)
                            pygame.display.update()
                        pygame.mixer.music.stop()  # Stop the music when quitting
                        self.menu_active = False  # Exit the menu, start game
                    # Check if "Quit" is clicked
                    if scrollrect1.collidepoint(mouse_pos):
                        sound_effect = pygame.mixer.Sound("audio/scrollsound.mp3")
                        sound_effect.play()
                        if(scrollflip1 == False):
                            scrollflip1 = True
                        else:
                            scrollflip1 = False
                    if scrollrect2.collidepoint(mouse_pos):
                        sound_effect = pygame.mixer.Sound("audio/scrollsound.mp3")
                        pygame.mixer.music.set_volume(0.5)
                        sound_effect.play()
                        if(scrollflip2 == False):
                            scrollflip2 = True
                        else:
                            scrollflip2 = False
                    if 1680 <= mouseX <= 1920 and 0 <= mouseY <= 155:
                        print("Quit clicked")
                        pygame.mixer.music.stop()  # Stop the music when quitting
                        pygame.quit()
                        sys.exit()


            pygame.display.update()
########################################################################################################################
class StartMenu2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.menu_active2 = True
########################################################################################################################
    def ChooseMenu(self):
        pygame.mixer.music.load("audio/background_music2.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        print("Choose Menu initialized")
        video = cv2.VideoCapture("video/SevenSeasMenu.mov")
        global gold
        global completetutorial
        global characterName
        global menu3_active
        crabswitch = False
        xcounter = 0
        caveswitch = False
        cavecounter = 0
        runes = 200
        runenum = []
        runelocation = []
        while(runes != 0):
            runenum.append(''.join(random.choice(string.ascii_letters) for x in range(12)))
            runelocation.append((runes * -50) - 400)
            runes = runes - 1

        while self.menu_active2:
            startTime = pygame.time.get_ticks()
            mouse_pos = pygame.mouse.get_pos()
            rainbowcolor1 = int((math.sin(startTime * 0.002) + 1) * 127.5)
            rainbowcolor2 = int((math.sin(startTime * 0.003 + 2) + 1) * 127.5)
            rainbowcolor3 = int((math.sin(startTime * 0.004 + 2) + 1) * 127.5)
            DISPLAYSURF.fill(BLACK)
#####################
            ret, frame = video.read()
            if not ret:
                video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue  # Continue to the next loop iteration
            frame = cv2.resize(frame, (1550, 880))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_surface = pygame.surfarray.make_surface(frame)
            frame_surface = pygame.transform.rotate(frame_surface, -90)  # Rotate if necessary
            frame_surface = pygame.transform.flip(frame_surface, True, False)
            DISPLAYSURF.blit(frame_surface, (190, 100))
######################

            draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
            if 1680 <= mouse_pos[0] <= 1920 and 0 <= mouse_pos[1] <= 155:
                draw_text('x', font4, (rainbowcolor2,rainbowcolor3, rainbowcolor3), DISPLAYSURF,1685, 105)

            runescounter = 0
            while (runescounter != 200):
                runelocation[runescounter] = runelocation[runescounter] + .3
                draw_text(str(runenum[runescounter]), font16, (1, rainbowcolor2, 80), DISPLAYSURF, 180, runelocation[runescounter], 50)
                runescounter = runescounter + 1

            runescounter2 = 199
            while (runescounter2 >= 0):
                draw_text(str(runenum[runescounter2]), font16, (50, rainbowcolor2, 80), DISPLAYSURF, 1300, runelocation[runescounter2], 50)
                runescounter2 = runescounter2 - 1

            hover_rect = pygame.Rect(816, 534, 300, 60)
            hover_rect2 = pygame.Rect(816, 622, 300, 60)
            hover_rect3 = pygame.Rect(816, 708, 300, 60)
            hover_rect4 = pygame.Rect(1200, 885, 95, 100)
            hover_rect5 = pygame.Rect(630, 885, 125, 200)

            image62.set_alpha(220)
            DISPLAYSURF.blit(image62, (1190, 880))
            DISPLAYSURF.blit(image62, (630, 880))

            if (crabswitch):
                DISPLAYSURF.blit(image64, (1197, 808))
                if (xcounter < 100):
                    xcounter = xcounter + 1
                else:
                    xcounter = 0
                    crabswitch = False

            if (caveswitch):
                DISPLAYSURF.blit(image63, (631, 883))
                if (cavecounter < 70):
                    cavecounter = cavecounter + 1
                else:
                    cavecounter = 0
                    caveswitch = False

            mouseX, mouseY = pygame.mouse.get_pos()
            imagen6.set_alpha(180)
            DISPLAYSURF.blit(imagen6, (mouseX - 47, mouseY - 54))
            mouse_pos = pygame.mouse.get_pos()
            if hover_rect.collidepoint(mouse_pos):
                pygame.draw.rect(DISPLAYSURF, (0, 255, 0), hover_rect, 3, 25)  # (color, rect, border thickness)
            if hover_rect2.collidepoint(mouse_pos):
                pygame.draw.rect(DISPLAYSURF, (0, 255, 0), hover_rect2, 3, 25)  # (color, rect, border thickness)
            if hover_rect3.collidepoint(mouse_pos):
                pygame.draw.rect(DISPLAYSURF, (0, 255, 0), hover_rect3, 3, 25)  # (color, rect, border thickness)
            if hover_rect4.collidepoint(mouse_pos):
                DISPLAYSURF.blit(image63, (1191, 883))
            if hover_rect5.collidepoint(mouse_pos):
                DISPLAYSURF.blit(image63, (631, 883))
            pygame.display.update()

            # Check for user input
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if(0 <= mouseY <= 900):
                        sound_effect = pygame.mixer.Sound("audio/nextlevel.mp3")
                        sound_effect.play()
                    mouseX, mouseY = pygame.mouse.get_pos()
                    # IF LOAD GAME IS CLICKED
                    if hover_rect5.collidepoint(mouse_pos):
                        caveswitch = True
                        sound_effect = pygame.mixer.Sound("audio/dragonroar.mp3")
                        sound_effect.play()
                    if hover_rect4.collidepoint(mouse_pos):
                        crabswitch = True
                        sound_effect = pygame.mixer.Sound("audio/shopclicksound.mp3")
                        sound_effect.play()
                    if 810 <= mouseX <= 1110 and 535 <= mouseY <= 595:
                        print("Clicked load game")
                        with open("gamedata.txt", "r") as file:
                            lines = file.readlines()
                            if len(lines) >= 4:
                                first_line = lines[0].strip()  # Access the first line and strip newline
                                first_line = first_line[7:]
                                third_line = lines[2].strip()  # Access the first line and strip newline
                                third_line = third_line[7:]
                                fourth_line = lines[3].strip()  # Access the first line and strip newline
                                fourth_line = fourth_line[19:]
                                gold = first_line
                                characterName = third_line
                                print("fourth line = " +fourth_line)
                                if(str(fourth_line) == 'true'):
                                    completetutorial = False
                                    menu3_active = True
                                    print("You have already completed the tutorial")
                        for i in range(235):
                            image4.set_alpha(i)
                            DISPLAYSURF.blit(image4, (0,0))
                            draw_text_center('Born from the darkness, Nightmares came to exist beneath the sea. They come in all sizes and are', font5, WHITE, DISPLAYSURF, halfdisplay, 900)
                            draw_text_center('cursed with ravenous hunger. Eternally at war with the Mermaids.', font5, WHITE, DISPLAYSURF, halfdisplay, 935)
                            pygame.display.update()
                        pygame.mixer.music.stop()
                        self.menu_active2 = False
                    if 810 <= mouseX <= 1110 and 623 <= mouseY <= 683:
                        print("Clicked new game")
                        for i in range(235):
                            image4.set_alpha(i)
                            DISPLAYSURF.blit(image4, (0, 0))
                            draw_text_center(
                                'Along with the curse of darkness came hope as well. Mythical creatures born from light, fought valiantly back against the Nightmares.',
                                font5, WHITE, DISPLAYSURF, halfdisplay, 900)
                            pygame.display.update()
                        pygame.mixer.music.stop()
                        completetutorial = True
                        self.menu_active2 = False
                    # IF TUTORIAL IS CLICKED
                    if 810 <= mouseX <= 1110 and 709 <= mouseY <= 769:
                        tutorialLoop = True
                        print("Clicked Tutorial")
                        for i in range(235):
                            image4.set_alpha(i)
                            DISPLAYSURF.blit(image4, (0, 0))
                            draw_text_center(
                                'King Exodius, 79th Emperor of the Seventh Sea in his desperation, created a technique to tame Mythical creatures, ending the age of extinction. ',
                                font5, WHITE, DISPLAYSURF, halfdisplay, 900)
                            pygame.display.update()
                        DISPLAYSURF.fill(BLACK)
                        while tutorialLoop:
                            DISPLAYSURF.fill(BLACK)
                            draw_text_center('Tutorial', font5, WHITE, DISPLAYSURF, halfdisplay, 200)
                            draw_text_center('1. get gud', font5, WHITE, DISPLAYSURF, halfdisplay, 300)

                            xrect = pygame.Rect(1084, 170, 25, 25)
                            mouse_pos = pygame.mouse.get_pos()
                            if xrect.collidepoint(mouse_pos):
                                pygame.draw.rect(DISPLAYSURF, (127, 0, 255), xrect,3)  # (color, rect, border thickness)
                            draw_text('x', font5, WHITE, DISPLAYSURF, 1090, 165)
                            for event in pygame.event.get():
                                if event.type == MOUSEBUTTONDOWN:
                                    if xrect.collidepoint(mouse_pos):
                                        tutorialLoop = False
                            pygame.display.update()
                        pygame.display.update()

                    if 1680 <= mouseX <= 1920 and 0 <= mouseY <= 155:
                        print("Quit clicked")
                        pygame.mixer.music.stop()
                        pygame.quit()
                        sys.exit()
        video.release()
########################################################################################################################
class gameintro(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.menu_active3 = True

########################################################################################################################
    def xbutton(self, gamescene):
        global FaderBool
        global Fader
        global displaylength
        global displayheight
        global textFader
        if(FaderBool):
            Fader = Fader + .5
            if(Fader > 110):
                FaderBool = False
        if(FaderBool == False):
            Fader =  Fader - .5
            if(Fader < 10):
                FaderBool = True
        mouse_pos = pygame.mouse.get_pos()
        mouseX, mouseY = pygame.mouse.get_pos()
        image56.set_alpha(200)
        DISPLAYSURF.blit(image56, (mouseX - 47, mouseY - 44))
        xrect = pygame.Rect(1680, 123, 35, 35)
        xrect2 = pygame.Rect(130, 100, 120, 80)
        mouseX, mouseY = pygame.mouse.get_pos()
        mouse_pos = pygame.mouse.get_pos()
        image42.set_alpha(Fader)
        DISPLAYSURF.blit(image42, (1655, 917))
        if ((gamescene >= 0) and(gamescene < 103)):
            DISPLAYSURF.blit(image30, (180, 115))
        draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
        if xrect.collidepoint(mouse_pos):
            draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)
        elif xrect2.collidepoint(mouse_pos):
            DISPLAYSURF.blit(image31, (198, 98))
        for event in pygame.event.get():
            mouseX, mouseY = pygame.mouse.get_pos()
            if xrect.collidepoint(mouse_pos):
                if event.type == MOUSEBUTTONDOWN:
                    if xrect.collidepoint(mouse_pos):
                        print("Quit clicked")
                        pygame.mixer.music.stop()
                        pygame.quit()
                        sys.exit()
            elif xrect2.collidepoint(mouse_pos):
                if event.type == MOUSEBUTTONDOWN:
                    sound_effect = pygame.mixer.Sound("audio/teleportnoise.mp3")
                    sound_effect.play()
                    pygame.display.update()
                    if(gamescene < 55):
                        capv3.release()
                        cap.release()
                        return (56)
                    if (gamescene > 55):
                        capv3.release()
                        cap.release()
                        capv2.release()
                        capv4.release()
                        return (154)
            else:
                if event.type == MOUSEBUTTONDOWN:
                    if 0 <= mouseX <= 1920 and 150 <= mouseY <= 1080:
                        sound_effect = pygame.mixer.Sound("audio/clicknoise.mp3")
                        sound_effect.play()
                        pygame.display.update()
                        textFader = 0
                        return (gamescene + 1)
        pygame.display.update()
        return gamescene

########################################################################################################################
    def gameintrocutscene(self):
        mouse_pos = pygame.mouse.get_pos()
        i = 255
        gamescene = -2;
        halfdisplay = displaylength / 2
        music1 = True #controls music playing
        music2 = True #controls music playing using alternation
        choice1 = False #for question choice from user
        choice2 = False #for question choice from user
        video1 = True #for toggling videos
        video2 = True #for toggling videos
        print("Choose Menu initialized")
        global textFader
        global characterName
        global menu3_active
        with open("gamedata.txt", "w") as file:
            file.write("gold = 0\n")
            file.write("gem = 0\n")
            file.write("name = 0\n")
            file.write("finishedtutorial = 0\n")
            file.write("itemlist = 0\n")
            file.write("miningspeed = 1\n")
            file.write("miningefficiency = 1\n")
            file.write("time = 1\n")
            file.write("luck = 1\n")
            file.write("spawnchance = 1\n")
            file.write("specialefficiency = 1\n")
            file.write("firstpaimonshop = true\n")
            file.write("alchemyexp = 1\n")
            file.write("alchemylevel = 1\n")
            file.write("guildtutorial = true\n")
            file.write("level = 1   \n")
            file.write("strength = 1 \n")
            file.write("defense = 1 \n")
            file.write("health = 1 \n")
            file.write("speed = 1 \n")
            file.write("specattack = 1 \n")
            file.write("luck = 1 \n")
            file.write("firstblackmarket = true \n")

            with open("creaturedata.txt", "w") as file:
                file.truncate(0)

            with open("teamdata.txt", "w") as file:
                file.truncate(0)

            with open("itemdata.txt", "w") as file:
                file.truncate(0)

            with open("equipeditems.txt", "w") as file:
                file.truncate(0)
            blankitem1 = {}
            save_teamcreature(blankitem1, "equipeditems.txt")
            save_teamcreature(blankitem1, "equipeditems.txt")
            save_teamcreature(blankitem1, "equipeditems.txt")
            save_teamcreature(blankitem1, "equipeditems.txt")
            save_teamcreature(blankitem1, "equipeditems.txt")
            save_teamcreature(blankitem1, "equipeditems.txt")
            save_teamcreature(blankitem1, "equipeditems.txt")

            creature = {
                "name": "Sacred Lumen",
                "lvl": 1,
                "hp": 10,
                "defense": 10,
                "strength": 10,
                "special attack": 10,
                "speed": 10,
                "tier": 1,
                "beastimage": 46,
                "move1": "Celestial Cascade",
                "move2": "Light Bringer",
                "move3": " ",
                "move4": " ",
                "type": "light",
                "experience": 0,
            }

            save_teamcreature(creature)
        while self.menu_active3:
            mouseX, mouseY = pygame.mouse.get_pos()
            DISPLAYSURF.fill(BLACK)
            DISPLAYSURF.blit(image5, (190, 105))
            if(gamescene == -2):
                sound_effect = pygame.mixer.Sound("audio/intromoviesound.mp3")
                sound_effect.play()
                fps = int(cap.get(cv2.CAP_PROP_FPS))
                clock = pygame.time.Clock()
                while cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        break
                    frame = cv2.resize(frame, (1650, 940))
                    frame = cv2.flip(frame, 1)
                    frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame = pygame.surfarray.make_surface(frame).convert()
                    DISPLAYSURF.blit(frame, (140, 100))
                    pygame.display.flip()
                    clock.tick(fps)
                    for event in pygame.event.get():
                        if (event.type == MOUSEBUTTONDOWN):
                            print("stop clicking so much")
                cap.release()
                gamescene = gamescene + 1

            if(gamescene == -1):
                if(music1):
                    pygame.mixer.music.load("audio/thundermusic.mp3")
                    pygame.mixer.music.set_volume(0.8)
                    pygame.mixer.music.play(-1)
                    music1 = False
                    music2 = True
                DISPLAYSURF.fill(BLACK)
                while(gamescene >= -1 and gamescene <= 19):
                    capv3.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    while capv3.isOpened():
                        ret, frame = capv3.read()
                        if not ret:
                            break  # Break the inner loop if the video ends
                        frame = cv2.resize(frame, (1650, 940))
                        frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
                        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        frame = pygame.surfarray.make_surface(frame).convert()
                        DISPLAYSURF.blit(frame, (140, 100))
                        if (gamescene == -1):
                            image4.set_alpha(i)
                            DISPLAYSURF.blit(image4, (0, 0))
                            if(i > 6):
                                i = i - 5
                            if (music2):
                                sound_effect = pygame.mixer.Sound("audio/choose1.mp3")
                                pygame.mixer.music.set_volume(0.3)
                                sound_effect.play()
                                pygame.mixer.music.play(-1)
                                music2 = False
                            draw_text_center('"Choose your Character', font2, DARKGREEN, DISPLAYSURF, halfdisplay,130)

                            # mouseX, mouseY = pygame.mouse.get_pos()
                            # print("x and y = " + str(mouseX) + " " + str(mouseY))

                            draw_text("+5 Defense", font13, DARKRED, DISPLAYSURF, 453, 480)
                            draw_text("+5 Strength", font13, DARKRED, DISPLAYSURF, 682, 470)
                            draw_text("+5 Health", font13, DARKRED, DISPLAYSURF, 893, 480)
                            draw_text("+5 Speed", font13, DARKRED, DISPLAYSURF, 1075, 490)
                            draw_text("+5 Spec Attack", font13, DARKRED, DISPLAYSURF, 1230, 490)
                            draw_text("+5 Luck", font13, DARKRED, DISPLAYSURF, 1405, 490)



                            DISPLAYSURF.blit(image65, (450, 230))
                            DISPLAYSURF.blit(image65, (700, 210))
                            DISPLAYSURF.blit(image65, (900, 230))
                            DISPLAYSURF.blit(image65, (1090, 240))
                            DISPLAYSURF.blit(image65, (1274, 240))
                            DISPLAYSURF.blit(image65, (1430, 240))
                            mouseX, mouseY = pygame.mouse.get_pos()
                            for event in pygame.event.get():
                                if(mouseX > 390 and mouseX < 590):
                                    if(mouseY > 380 and mouseY < 870):
                                        firstchar = pygame.Rect(420, 370, 180, 500)
                                        pygame.draw.rect(DISPLAYSURF, PURPLE, firstchar, 4)
                                        if(event.type == MOUSEBUTTONDOWN):
                                            sound_effect = pygame.mixer.Sound("audio/chosencharacternoise.mp3")
                                            with open("gamedata.txt", "r") as file:
                                                lines = file.readlines()
                                                lines[17] = f"defense = {6}\n"
                                            with open("gamedata.txt", "w") as file:
                                                file.writelines(lines)
                                            sound_effect.play()
                                            gamescene = gamescene + 1
                                if(mouseX > 660 and mouseX < 850):
                                    if(mouseY > 370 and mouseY < 870):
                                        secondchar = pygame.Rect(660, 360, 170, 500)
                                        pygame.draw.rect(DISPLAYSURF, PURPLE, secondchar, 4)
                                        if(event.type == MOUSEBUTTONDOWN):
                                            sound_effect = pygame.mixer.Sound("audio/chosencharacternoise.mp3")
                                            with open("gamedata.txt", "r") as file:
                                                lines = file.readlines()
                                                lines[16] = f"strength = {6}\n"
                                            with open("gamedata.txt", "w") as file:
                                                file.writelines(lines)
                                            sound_effect.play()
                                            gamescene = gamescene + 1
                                if(mouseX > 870 and mouseX < 1020):
                                    if(mouseY > 390 and mouseY < 870):
                                        thirdchar = pygame.Rect(860, 380, 170, 500)
                                        pygame.draw.rect(DISPLAYSURF, PURPLE, thirdchar, 4)
                                        if(event.type == MOUSEBUTTONDOWN):
                                            sound_effect = pygame.mixer.Sound("audio/chosencharacternoise.mp3")
                                            with open("gamedata.txt", "r") as file:
                                                lines = file.readlines()
                                                lines[18] = f"health = {6}\n"
                                            with open("gamedata.txt", "w") as file:
                                                file.writelines(lines)
                                            sound_effect.play()
                                            gamescene = gamescene + 1
                                if(mouseX > 1040 and mouseX < 1230):
                                    if(mouseY > 390 and mouseY < 870):
                                        fourthchar = pygame.Rect(1050, 380, 140, 500)
                                        pygame.draw.rect(DISPLAYSURF, PURPLE, fourthchar, 4)
                                        if(event.type == MOUSEBUTTONDOWN):
                                            sound_effect = pygame.mixer.Sound("audio/chosencharacternoise.mp3")
                                            with open("gamedata.txt", "r") as file:
                                                lines = file.readlines()
                                                lines[19] = f"speed = {6}\n"
                                            with open("gamedata.txt", "w") as file:
                                                file.writelines(lines)
                                            sound_effect.play()
                                            gamescene = gamescene + 1
                                if(mouseX > 1210 and mouseX < 1380):
                                    if(mouseY > 390 and mouseY < 870):
                                        fifthchar = pygame.Rect(1220, 380, 140, 500)
                                        pygame.draw.rect(DISPLAYSURF, PURPLE, fifthchar, 4)
                                        if(event.type == MOUSEBUTTONDOWN):
                                            sound_effect = pygame.mixer.Sound("audio/chosencharacternoise.mp3")
                                            with open("gamedata.txt", "r") as file:
                                                lines = file.readlines()
                                                lines[20] = f"specattack = {6}\n"
                                            with open("gamedata.txt", "w") as file:
                                                file.writelines(lines)
                                            sound_effect.play()
                                            gamescene = gamescene + 1
                                if(mouseX > 1385 and mouseX < 1580):
                                    if(mouseY > 390 and mouseY < 870):
                                        sixthchar = pygame.Rect(1380, 380, 150, 500)
                                        pygame.draw.rect(DISPLAYSURF, PURPLE, sixthchar, 4)
                                        if(event.type == MOUSEBUTTONDOWN):
                                            sound_effect = pygame.mixer.Sound("audio/chosencharacternoise.mp3")
                                            with open("gamedata.txt", "r") as file:
                                                lines = file.readlines()
                                                lines[21] = f"luck = {6}\n"
                                            with open("gamedata.txt", "w") as file:
                                                file.writelines(lines)
                                            sound_effect.play()
                                            gamescene = gamescene + 1
                            pygame.display.update()
                        if (gamescene == 0):
                            image4.set_alpha(240)
                            DISPLAYSURF.blit(image4, (0, 880))
                            if (textFader != 4000):
                                textFader = textFader + 15
                            draw_text_center('"Well, well… here we have the dregs of the kingdom, crawling about my deck like insects. You’ve all', font5, RED, DISPLAYSURF, halfdisplay,880)
                            draw_text_center('been such a delightful nuisance, whispering your little plans in the darkness. Did you truly believe I', font5, RED, DISPLAYSURF, halfdisplay,905)
                            draw_text_center('wouldn’t hear your pathetic little plans?"', font5, RED, DISPLAYSURF, halfdisplay,930)
                            image4.set_alpha(255)
                            DISPLAYSURF.blit(image4, ((textFader + 400), 880))
                            DISPLAYSURF.blit(image4, ((textFader + -500), 910))
                            DISPLAYSURF.blit(image4, ((textFader + -1200), 935))
                            gamescene = self.xbutton(gamescene)
                        if (gamescene == 1):
                            image4.set_alpha(240)
                            DISPLAYSURF.blit(image4, (0, 880))
                            if (textFader != 3000):
                                textFader = textFader + 15
                            draw_text_center('The captains heavy boots thud against drenched wood, his coat fluttering in the wind.', font5, WHITE, DISPLAYSURF, halfdisplay, 905)
                            draw_text_center('As he paces in front of them you can see a cruel smile as he plays with the revolver in his hands.)', font5, WHITE, DISPLAYSURF, halfdisplay, 880)
                            image4.set_alpha(255)
                            DISPLAYSURF.blit(image4, ((textFader + 500), 880))
                            DISPLAYSURF.blit(image4, ((textFader + -100), 910))
                            gamescene = self.xbutton(gamescene)
                        if (gamescene == 2):
                            image4.set_alpha(240)
                            DISPLAYSURF.blit(image4, (0, 880))
                            if (textFader != 3000):
                                textFader = textFader + 12
                            draw_text_center('(One of the prisoners, a younger man, swallows his fear and dares to speak.)', font5, WHITE, DISPLAYSURF, halfdisplay, 880)
                            draw_text_center('"WE aren’t insects were still huma—"', font5, YELLOW, DISPLAYSURF, halfdisplay, 905)
                            image4.set_alpha(255)
                            DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                            DISPLAYSURF.blit(image4, ((textFader + -100), 910))
                            music1 = True
                            gamescene = self.xbutton(gamescene)
                        if (gamescene == 3):
                            if (music1):
                                sound_effect = pygame.mixer.Sound("audio/kick.mp3")
                                sound_effect.play()
                                music1 = False
                            image4.set_alpha(240)
                            DISPLAYSURF.blit(image4, (0, 880))
                            if (textFader != 4000):
                                textFader = textFader + 15
                            draw_text_center('(The Captain Kicks his throat sending him to his knees with a sickening crunch)', font5, RED, DISPLAYSURF, halfdisplay, 880)
                            draw_text_center('"Who else wants to speak?"', font5, RED, DISPLAYSURF, halfdisplay, 905)
                            image4.set_alpha(255)
                            DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                            DISPLAYSURF.blit(image4, ((textFader + -100), 910))
                            gamescene = self.xbutton(gamescene)
                            music2 = True
                        if (gamescene == 4):
                            if (music2):
                                sound_effect = pygame.mixer.Sound("audio/thundersound2.mp3")
                                sound_effect.play()
                                music2 = False
                            image4.set_alpha(240)
                            DISPLAYSURF.blit(image4, (0, 880))
                            if (textFader != 3000):
                                textFader = textFader + 15
                            draw_text_center('"Ive grown tired of lugging you worthless wretches across the sea..."', font5, RED,DISPLAYSURF, halfdisplay, 880)
                            draw_text_center('"It pisses me off seeing traitors like you still alive."', font5, RED,DISPLAYSURF, halfdisplay, 905)
                            draw_text_center('"Your very existence is a sin"', font7, RED, DISPLAYSURF, halfdisplay, 935)
                            image4.set_alpha(255)
                            DISPLAYSURF.blit(image4, ((textFader + 500), 880))
                            DISPLAYSURF.blit(image4, ((textFader + -100), 910))
                            DISPLAYSURF.blit(image4, ((textFader + -700), 935))
                            gamescene = self.xbutton(gamescene)
                        if (gamescene == 5):
                            image4.set_alpha(240)
                            DISPLAYSURF.blit(image4, (0, 880))
                            if (textFader != 3000):
                                textFader = textFader + 15
                            draw_text_center('"I just had a great idea, what if we made this… interesting?"', font5, RED, DISPLAYSURF, halfdisplay, 880)
                            draw_text_center('"How about I just kill one of you!"', font5, RED, DISPLAYSURF, halfdisplay, 905)
                            image4.set_alpha(255)
                            DISPLAYSURF.blit(image4, ((textFader + 500), 880))
                            DISPLAYSURF.blit(image4, ((textFader + 100), 910))
                            gamescene = self.xbutton(gamescene)
                            music1 = True
                        if (gamescene == 6):
                            if (music1):
                                sound_effect = pygame.mixer.Sound("audio/giantwaves.mp3")
                                sound_effect.play()
                                music1 = False
                            image4.set_alpha(240)
                            DISPLAYSURF.blit(image4, (0, 880))
                            if (textFader != 3000):
                                textFader = textFader + 15
                            draw_text_center('"but its no fun if its like that, how about we play a little game! That sounds fun doesnt it?', font5, RED, DISPLAYSURF, halfdisplay, 880)
                            draw_text_center('Were all such good friends after all!"', font5, RED, DISPLAYSURF, halfdisplay, 905)
                            image4.set_alpha(255)
                            DISPLAYSURF.blit(image4, ((textFader + 500), 880))
                            DISPLAYSURF.blit(image4, ((textFader + -100), 910))
                            gamescene = self.xbutton(gamescene)
                        if (gamescene == 7):
                            image4.set_alpha(240)
                            DISPLAYSURF.blit(image4, (0, 880))
                            if (textFader != 3000):
                                textFader = textFader + 15
                            draw_text_center('Each of you will choose and vote for one person,', font5, RED, DISPLAYSURF, halfdisplay, 880)
                            draw_text_center('and whoever gets the most votes ill kill."', font5, RED, DISPLAYSURF, halfdisplay, 905)
                            image4.set_alpha(255)
                            DISPLAYSURF.blit(image4, ((textFader + 500), 880))
                            DISPLAYSURF.blit(image4, ((textFader + 0), 910))
                            gamescene = self.xbutton(gamescene)
                        if (gamescene == 8):
                            image4.set_alpha(240)
                            DISPLAYSURF.blit(image4, (0, 880))
                            if (textFader != 3000):
                                textFader = textFader + 15
                            draw_text_center('Ahhh, im such a righteous man. Arent I? You will judge yourselves on the crimes youve commited.', font5, RED, DISPLAYSURF, halfdisplay, 880)
                            draw_text_center('"Its so amusing to watch scum like you pointing fingers at each other."', font5, RED, DISPLAYSURF, halfdisplay, 905)
                            image4.set_alpha(255)
                            DISPLAYSURF.blit(image4, ((textFader + 500), 880))
                            DISPLAYSURF.blit(image4, ((textFader + -300), 910))
                            gamescene = self.xbutton(gamescene)
                            music1 = True
                        if (gamescene == 9):
                            if (music1):
                                sound_effect = pygame.mixer.Sound("audio/thundersound1.mp3")
                                sound_effect.play()
                                music1 = False
                            image4.set_alpha(240)
                            DISPLAYSURF.blit(image4, (0, 880))
                            if (textFader != 3000):
                                textFader = textFader + 15
                            draw_text_center('"Well, I dont have all day, I have your families to take care of later.',font5, RED, DISPLAYSURF, halfdisplay, 880)
                            draw_text_center('Lets get on with this, choose someone to die... Or would you rather I pick at random?', font5, RED,DISPLAYSURF, halfdisplay, 905)
                            draw_text_center('"Perhaps I should line you all up and put a bullet in each of you?"', font5, RED,DISPLAYSURF, halfdisplay, 930)
                            image4.set_alpha(255)
                            DISPLAYSURF.blit(image4, ((textFader + 500), 880))
                            DISPLAYSURF.blit(image4, ((textFader + -100), 910))
                            DISPLAYSURF.blit(image4, ((textFader + -900), 935))
                            gamescene = self.xbutton(gamescene)
                        if (gamescene == 10):
                            image4.set_alpha(240)
                            DISPLAYSURF.blit(image4, (0, 880))
                            if (textFader != 3000):
                                textFader = textFader + 15
                            draw_text_center('(A hushed, horrified silence follows. The wind howls through the rigging, rain slashing down. No one speaks. No one moves.)',font5, WHITE, DISPLAYSURF, halfdisplay, 880)
                            image4.set_alpha(255)
                            DISPLAYSURF.blit(image4, ((textFader + 400), 880))
                            DISPLAYSURF.blit(image4, ((textFader + -500), 910))
                            gamescene = self.xbutton(gamescene)
                        if (gamescene == 11):
                            image4.set_alpha(240)
                            DISPLAYSURF.blit(image4, (0, 880))
                            if (textFader != 3000):
                                textFader = textFader + 15
                            draw_text_center('(Then—slowly, the slaves look amongst each other, eyes shifting about with no remorse or pity in their lightless pupils.)',font5, WHITE, DISPLAYSURF, halfdisplay, 880)
                            image4.set_alpha(255)
                            DISPLAYSURF.blit(image4, ((textFader + 400), 880))
                            gamescene = self.xbutton(gamescene)
                        if (gamescene == 12):
                            image4.set_alpha(240)
                            DISPLAYSURF.blit(image4, (0, 880))
                            if (textFader != 3000):
                                textFader = textFader + 15
                            draw_text_center('Eventually there hesitating ends, leaving everyone looks towards you, whos head is down',font5, WHITE, DISPLAYSURF, halfdisplay, 880)
                            image4.set_alpha(255)
                            music2 = True
                            DISPLAYSURF.blit(image4, ((textFader + 500), 880))
                            gamescene = self.xbutton(gamescene)
                        if (gamescene == 13):
                            if (music2):
                                sound_effect = pygame.mixer.Sound("audio/gunload.mp3")
                                sound_effect.play()
                                music2 = False
                            image4.set_alpha(240)
                            DISPLAYSURF.blit(image4, (0, 880))
                            if (textFader != 3000):
                                textFader = textFader + 15
                            draw_text_center('"Oh? it seems like we have a winner. You are one unlucky fella arent you? Tell me, how does it feel to be', font5, RED, DISPLAYSURF, halfdisplay, 880)
                            draw_text_center('betrayed? Dont take it too personally, maybe well meet again in hell, dont you think?"', font5, RED, DISPLAYSURF, halfdisplay, 905)
                            draw_text_center('*Slowly he raises his gun to your head, a metallic click sounds, inches away from your skull*', font5, WHITE, DISPLAYSURF, halfdisplay, 930)
                            image4.set_alpha(255)
                            DISPLAYSURF.blit(image4, ((textFader + 500), 880))
                            DISPLAYSURF.blit(image4, ((textFader + -300), 910))
                            DISPLAYSURF.blit(image4, ((textFader + -1000), 935))
                            music1 = True
                            gamescene = self.xbutton(gamescene)
                        if (gamescene == 14):
                            if (music1):
                                sound_effect = pygame.mixer.Sound("audio/pistolshot.mp3")
                                sound_effect.play()
                                music1 = False
                            image4.set_alpha(240)
                            DISPLAYSURF.blit(image4, (0, 880))
                            if (textFader != 3000):
                                textFader = textFader + 15
                            draw_text_center('*BANG*', font7, WHITE, DISPLAYSURF, halfdisplay, 880)
                            image4.set_alpha(255)
                            gamescene = self.xbutton(gamescene)
                        if (gamescene == 15):
                            if (music1):
                                sound_effect = pygame.mixer.Sound("audio/kick.mp3")
                                sound_effect.play()
                                music1 = False
                            image4.set_alpha(240)
                            DISPLAYSURF.blit(image4, (0, 880))
                            if (textFader != 3000):
                                textFader = textFader + 15
                            draw_text_center('(Your body tenses. But… no pain. No darkness)', font5, WHITE, DISPLAYSURF, halfdisplay, 880)
                            draw_text_center('(Instead, around you, bodies collapse. Five of them. Lifeless. Blood flows onto the deck,', font5, WHITE, DISPLAYSURF, halfdisplay, 905)
                            draw_text_center('painting it crimson as a puddle starts to form. The scent of gunpowder and death lingers in the cold air)', font5, WHITE, DISPLAYSURF, halfdisplay, 930)
                            image4.set_alpha(255)
                            DISPLAYSURF.blit(image4, ((textFader + 400), 880))
                            DISPLAYSURF.blit(image4, ((textFader + -200), 910))
                            DISPLAYSURF.blit(image4, ((textFader + -1000), 935))
                            gamescene = self.xbutton(gamescene)
                        if (gamescene == 16):
                            image4.set_alpha(240)
                            DISPLAYSURF.blit(image4, (0, 880))
                            if (textFader != 3000):
                                textFader = textFader + 15
                            draw_text_center('(As you watch their dead corpses fall to the deck, breathe shaking,', font5, WHITE,DISPLAYSURF, halfdisplay, 880)
                            draw_text_center('the captain turns and locks eyes with you)', font5, WHITE, DISPLAYSURF, halfdisplay, 905)
                            image4.set_alpha(255)
                            DISPLAYSURF.blit(image4, ((textFader + 500), 880))
                            DISPLAYSURF.blit(image4, ((textFader + -100), 910))
                            gamescene = self.xbutton(gamescene)
                        if (gamescene == 17):
                            image4.set_alpha(240)
                            DISPLAYSURF.blit(image4, (0, 880))
                            if (textFader != 3000):
                                textFader = textFader + 15
                            draw_text_center('Heh, those worthless shits actually thought id spare them. You are lucky kid, ', font5, RED,DISPLAYSURF, halfdisplay, 880)
                            draw_text_center('you survived for being the biggest piece of shit out of them all.', font5, RED, DISPLAYSURF, halfdisplay, 905)
                            image4.set_alpha(255)
                            DISPLAYSURF.blit(image4, ((textFader + 400), 880))
                            DISPLAYSURF.blit(image4, ((textFader + -200), 910))
                            gamescene = self.xbutton(gamescene)
                        if (gamescene == 18):
                            image4.set_alpha(240)
                            DISPLAYSURF.blit(image4, (0, 880))
                            if (textFader != 3000):
                                textFader = textFader + 15
                            draw_text_center('Well, you havent survived just yet...', font5, RED,DISPLAYSURF, halfdisplay, 880)
                            draw_text_center('Lets teach you how to swim first.', font5, RED, DISPLAYSURF, halfdisplay, 905)
                            image4.set_alpha(255)
                            DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                            DISPLAYSURF.blit(image4, ((textFader + 200), 910))
                            gamescene = self.xbutton(gamescene)
                        if (gamescene == 19):
                            music2 = True
                            gamescene = 23
                            break
                        pygame.display.flip()  # Update display only once per frame
                        clock.tick(fps)  # Maintain video FPS

                capv3.release()
            if (gamescene == 23):
                if(music2):
                    pygame.mixer.music.load("audio/ominiousmusic.mp3")
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.set_volume(0.6)
                    sound_effect = pygame.mixer.Sound("audio/kick.mp3")
                    sound_effect.play()
                    music2 = False
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image13, (195, 110))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 15
                draw_text_center('VOOSH *KICK*',font8, WHITE, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('"Have fun being fishfood for those f*cking monsters"',font5, RED, DISPLAYSURF, halfdisplay, 925)
                image4.set_alpha(255)
                DISPLAYSURF.blit(image4, ((textFader + 700), 880))
                DISPLAYSURF.blit(image4, ((textFader + 300), 920))
                music1 = True
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 24):
                if(music1):
                    pygame.mixer.music.set_volume(0.7)
                    sound_effect = pygame.mixer.Sound("audio/splash2.mp3")
                    sound_effect.play()
                    music1 = False
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image12, (195, 110))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 15
                draw_text_center('You plunge into the freezing and turbulent storm water,',font5, WHITE, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('shocked and with the oxygen knocked out of your lungs.',font5, WHITE, DISPLAYSURF, halfdisplay, 925)
                image4.set_alpha(255)
                DISPLAYSURF.blit(image4, ((textFader + 500), 880))
                DISPLAYSURF.blit(image4, ((textFader + -50), 920))
                DISPLAYSURF.blit(image4, ((textFader + -800), 960))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
                music2 = True
            if (gamescene == 25):
                if(music2):
                    pygame.mixer.music.set_volume(0.7)
                    sound_effect = pygame.mixer.Sound("audio/heartbeat.mp3")
                    sound_effect.play()
                    music2 = False
                DISPLAYSURF.fill(BLACK)
                image15.set_alpha(220)
                DISPLAYSURF.blit(image12, (195, 110))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 15
                draw_text_center('You struggle to reach the surface but to no avail as the ropes still bind you. Your body is broken. Weak. Useless.',font5, WHITE, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('Freezing ocean water fills your burning lungs as you gasp for nonexistent oxygen.',font5, WHITE, DISPLAYSURF, halfdisplay, 925)
                image4.set_alpha(255)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + 00), 920))
                DISPLAYSURF.blit(image4, ((textFader + -800), 960))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 26):
                DISPLAYSURF.fill(BLACK)
                image15.set_alpha(180)
                DISPLAYSURF.blit(image14, (195, 110))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 15
                draw_text_center('(Your vision blurs) Why is this happening to me? I only did what I thought was right.',font5, WHITE, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('Is this the end for me, after everything that ive been through?',font5, WHITE, DISPLAYSURF, halfdisplay, 925)
                image4.set_alpha(255)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + 100), 920))
                DISPLAYSURF.blit(image4, ((textFader + -800), 960))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
                music2 = True
            if (gamescene == 27):
                if(music2):
                    sound_effect = pygame.mixer.Sound("audio/bubbles.mp3")
                    sound_effect.play()
                    music2 = False
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image14, (195, 110))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 15
                draw_text_center('*GarGle GeRGeL*', font5, WHITE, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('if only I got a a second chance...', font5, WHITE, DISPLAYSURF, halfdisplay, 925)
                image4.set_alpha(255)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + 100), 920))
                DISPLAYSURF.blit(image4, ((textFader + -800), 960))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 28):
                DISPLAYSURF.fill(BLACK)
                image15.set_alpha(200)
                DISPLAYSURF.blit(image15, (195, 110))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 20
                draw_text_center('I would take back whats rightfully mine!',font6, DARKRED, DISPLAYSURF, halfdisplay, 885)
                draw_text_center(' ',font6, DARKRED, DISPLAYSURF, halfdisplay, 925)
                image4.set_alpha(255)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + 100), 920))
                DISPLAYSURF.blit(image4, ((textFader + -800), 960))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 29):
                DISPLAYSURF.fill(BLACK)
                image15.set_alpha(70)
                DISPLAYSURF.blit(image15, (195, 110))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('(Your vision fades more) How pitiful ive become, captured and taken as a slave by the empire.', font5, WHITE, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('If there does exist a god out there, I beg you', font5, WHITE, DISPLAYSURF, halfdisplay, 925)
                image4.set_alpha(255)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + 100), 920))
                DISPLAYSURF.blit(image4, ((textFader + -800), 960))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
                music1 = True
            if (gamescene == 30):
                if(music1):
                    pygame.mixer.music.set_volume(0.7)
                    sound_effect = pygame.mixer.Sound("audio/drowningnoise.mp3")
                    sound_effect.play()
                    music1 = False
                DISPLAYSURF.fill(BLACK)
                image13.set_alpha(200)
                DISPLAYSURF.blit(image4, (100, -100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('please, give me another chance.', font5, WHITE, DISPLAYSURF, halfdisplay, 890)
                image4.set_alpha(255)
                DISPLAYSURF.blit(image4, ((textFader + 500), 880))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 31):
                DISPLAYSURF.fill(BLACK)
                image15.set_alpha(50)
                DISPLAYSURF.blit(image15, (195, 110))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('(Your heartbeat slows)', font5, WHITE, DISPLAYSURF, halfdisplay, 890)
                image4.set_alpha(255)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + 00), 920))
                DISPLAYSURF.blit(image4, ((textFader + -800), 960))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 32):
                DISPLAYSURF.fill(BLACK)
                image15.set_alpha(110)
                DISPLAYSURF.blit(image15, (195, 110))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('its getting cold.. im so cold', font5, WHITE, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('Dammit, is this really the end?', font5, WHITE, DISPLAYSURF, halfdisplay, 925)
                image4.set_alpha(255)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + 100), 920))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 33):
                DISPLAYSURF.fill(BLACK)
                image15.set_alpha(50)
                DISPLAYSURF.blit(image15, (195, 110))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('(Your body begins to goes limp)', font5, WHITE, DISPLAYSURF, halfdisplay, 890)
                image4.set_alpha(255)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 34):
                DISPLAYSURF.fill(BLACK)
                image16.set_alpha(10)
                DISPLAYSURF.blit(image16, (195, 110))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('farewell......', font5, WHITE, DISPLAYSURF, halfdisplay, 890)
                image4.set_alpha(255)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
                music1 = True
            if (gamescene == 35):
                if(music1):
                    pygame.mixer.music.set_volume(0.7)
                    sound_effect = pygame.mixer.Sound("audio/blub.mp3")
                    sound_effect.play()
                    music1 = False
                DISPLAYSURF.fill(BLACK)
                image16.set_alpha(30)
                DISPLAYSURF.blit(image16, (195, 110))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('blub', font5, WHITE, DISPLAYSURF, halfdisplay, 890)
                image4.set_alpha(255)
                DISPLAYSURF.blit(image4, ((textFader + 700), 880))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
                music2 = True
            if (gamescene == 36):
                if(music2):
                    pygame.mixer.music.set_volume(0.7)
                    sound_effect = pygame.mixer.Sound("audio/creaturetrashnoise.mp3")
                    sound_effect.play()
                    music2 = False
                DISPLAYSURF.fill(BLACK)
                image16.set_alpha(40)
                DISPLAYSURF.blit(image16, (195, 110))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('blubbbbbbbb', font5, WHITE, DISPLAYSURF, halfdisplay, 890)
                image4.set_alpha(255)
                DISPLAYSURF.blit(image4, ((textFader + 700), 880))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 37):
                DISPLAYSURF.fill(BLACK)
                image16.set_alpha(60)
                DISPLAYSURF.blit(image16, (195, 110))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('......', font5, WHITE, DISPLAYSURF, halfdisplay, 890)
                image4.set_alpha(255)
                DISPLAYSURF.blit(image4, ((textFader + 700), 880))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
                music1 = True
            if (gamescene == 38):
                if(music1):
                    sound_effect = pygame.mixer.Sound("audio/underwateranimalnoise.mp3")
                    sound_effect.play()
                    pygame.mixer.music.load("audio/heavencalm.mp3")
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.set_volume(0.9)
                    music1 = False
                DISPLAYSURF.fill(BLACK)
                image16.set_alpha(90)
                DISPLAYSURF.blit(image16, (195, 110))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('PwooOOoorrUUuuuHHhhKKkkhh', font5, WHITE, DISPLAYSURF, halfdisplay, 890)
                image4.set_alpha(255)
                DISPLAYSURF.blit(image4, ((textFader + 500), 880))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 39):
                DISPLAYSURF.fill(BLACK)
                image16.set_alpha(120)
                DISPLAYSURF.blit(image16, (195, 110))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('an unknown voice reverbrates throughout the darkness and reaches all around you', font5, SKYBLUE, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('"Where are you, fishyyy~?"', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 925)
                image4.set_alpha(255)
                DISPLAYSURF.blit(image4, ((textFader + 500), 880))
                DISPLAYSURF.blit(image4, ((textFader + 000), 920))
                DISPLAYSURF.blit(image4, ((textFader + -800), 960))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 40):
                DISPLAYSURF.fill(BLACK)
                image16.set_alpha(150)
                DISPLAYSURF.blit(image16, (195, 110))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('"Oh theyre you are!" you hear as the voice gets closer. The words coil around your mind, echoing in the void.', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 890)
                image4.set_alpha(255)
                DISPLAYSURF.blit(image4, ((textFader + 400), 880))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
                music1 = True
            if (gamescene == 41):
                if(music1):
                    sound_effect = pygame.mixer.Sound("audio/humming.mp3")
                    sound_effect.play()
                    music1 = False
                DISPLAYSURF.fill(BLACK)
                image16.set_alpha(180)
                DISPLAYSURF.blit(image16, (195, 110))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('A faint glow flickers in the abyss. "hmmmm, whos this?"', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 890)
                image4.set_alpha(255)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 42):
                DISPLAYSURF.fill(BLACK)
                image17.set_alpha(25)
                DISPLAYSURF.blit(image17, (200, 100))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
                music1 = True
            if (gamescene == 43):
                if(music1):
                    sound_effect = pygame.mixer.Sound("audio/girlgiggle.mp3")
                    sound_effect.play()
                    music1 = False
                DISPLAYSURF.fill(BLACK)
                image17.set_alpha(35)
                DISPLAYSURF.blit(image17, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('"A human? How interesting. Lost, broken... so easy to shatter. How did you end up like this?"', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 890)
                image4.set_alpha(255)
                DISPLAYSURF.blit(image4, ((textFader + 400), 880))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 44):
                DISPLAYSURF.fill(BLACK)
                image17.set_alpha(35)
                DISPLAYSURF.blit(image17, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('(A soft voice whispers near your ear) "I cant just leave you to die like this.."', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 890)
                image4.set_alpha(255)
                DISPLAYSURF.blit(image4, ((textFader + 400), 880))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 45):
                DISPLAYSURF.fill(BLACK)
                image17.set_alpha(25)
                DISPLAYSURF.blit(image17, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('"close your eyes human, leave the rest to me"', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 890)
                image4.set_alpha(255)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 46):
                DISPLAYSURF.fill(BLACK)
                image17.set_alpha(25)
                DISPLAYSURF.blit(image17, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('"everything will be alright"', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 890)
                image4.set_alpha(255)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 47):
                DISPLAYSURF.fill(BLACK)
                image17.set_alpha(15)
                DISPLAYSURF.blit(image17, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('*you fall unconscious to her soothing voice*', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 890)
                image4.set_alpha(255)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 48):
                DISPLAYSURF.fill(BLACK)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 49):
                DISPLAYSURF.fill(BLACK)
                imagemermaid2.set_alpha(50)
                DISPLAYSURF.blit(imagemermaid2, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('"H-, hey… are you awake?"', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 890)
                image4.set_alpha(255)
                DISPLAYSURF.blit(image4, ((textFader + 400), 880))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 50):
                DISPLAYSURF.fill(BLACK)
                imagemermaid2.set_alpha(150)
                DISPLAYSURF.blit(imagemermaid2, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('A violent shudder rips through your body. Your lungs **burn**—but not for air. For something else.', font5, WHITE, DISPLAYSURF, halfdisplay, 880)
                draw_text_center('"can you hear me child?"', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 905)
                image4.set_alpha(255)
                DISPLAYSURF.blit(image4, ((textFader + 500), 880))
                DISPLAYSURF.blit(image4, ((textFader + 000), 910))
                DISPLAYSURF.blit(image4, ((textFader + -500), 937))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 51):
                DISPLAYSURF.fill(BLACK)
                imagemermaid2.set_alpha(255)
                DISPLAYSURF.blit(imagemermaid2, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('"Ah! you are awake finally! Youve been unconscious for 3 days"', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 880)
                draw_text_center('"I was so worried about you"', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 905)
                draw_text_center('"just a bit..."', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 930)
                image4.set_alpha(255)
                DISPLAYSURF.blit(image4, ((textFader + 500), 880))
                DISPLAYSURF.blit(image4, ((textFader + 000), 910))
                DISPLAYSURF.blit(image4, ((textFader + -500), 937))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 52):
                DISPLAYSURF.fill(BLACK)
                imagemermaid2.set_alpha(255)
                DISPLAYSURF.blit(imagemermaid2, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('"Dont panic you are safe now, I brought you somewhere special."', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 880)
                draw_text_center('"You’re in the **Kingdom of Lucidea**"', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 905)
                image4.set_alpha(255)
                DISPLAYSURF.blit(image4, ((textFader + 500), 880))
                DISPLAYSURF.blit(image4, ((textFader + 000), 910))
                DISPLAYSURF.blit(image4, ((textFader + -500), 937))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 53):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(imagemermaid2, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('"You humans have such strange biology, Saving you was… difficult."', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 880)
                draw_text_center('"My only option was to use the innate gift of mermaids,"', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 905)
                draw_text_center('"to have you digest a drop of blood from my heart..."', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 930)
                image4.set_alpha(255)
                DISPLAYSURF.blit(image4, ((textFader + 500), 880))
                DISPLAYSURF.blit(image4, ((textFader + -100), 910))
                DISPLAYSURF.blit(image4, ((textFader + -600), 937))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 54):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(imagemermaid2, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('"Ahhhh, I hope you dont mind that I did it without your blessing..  was difficult for me as well. "', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 880)
                draw_text_center('"You ingested a piece.. of me. But look on the bright side, little human,"', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 905)
                draw_text_center('"Now you can breathe down here. Now you are one of us..."', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 930)
                image4.set_alpha(255)
                DISPLAYSURF.blit(image4, ((textFader + 500), 880))
                DISPLAYSURF.blit(image4, ((textFader + -00), 910))
                DISPLAYSURF.blit(image4, ((textFader + -500), 937))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 55):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(imagemermaid1, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('"Oh, I forgot to introduce myself."', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 880)
                draw_text_center('"How embarassing. My name is Octavia."', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 905)
                draw_text_center('"its a pleasure to meet you"', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 930)
                DISPLAYSURF.blit(image4, ((textFader + 500), 880))
                DISPLAYSURF.blit(image4, ((textFader + -000), 910))
                DISPLAYSURF.blit(image4, ((textFader + -500), 937))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 56):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(imagemermaid1, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('"Whats your name little human?"', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 880)
                image4.set_alpha(255)
                DISPLAYSURF.blit(image4, ((textFader + 400), 880))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 57):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(imagemermaid1, (200, 100))
                image4.set_alpha(160)
                DISPLAYSURF.blit(image4, (0, 0))
                draw_text_center('input username', font4, WHITE, DISPLAYSURF, halfdisplay, 430)
                draw_text_center('[Click to Confirm]', font4, WHITE, DISPLAYSURF, halfdisplay, 810)

                # Font and initial setup
                base_font = pygame.font.Font(None, 70)
                input_rect = pygame.Rect(800, 500, 340, 82)
                color_active = pygame.Color(WHITE)
                color_passive = pygame.Color(111, 236, 247)
                color = color_passive
                active = False

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if (int(len(characterName)) > 1):
                            with open("gamedata.txt", "r") as file:
                                lines = file.readlines()
                                lines[2] = f"name = {characterName}\n"
                            with open("gamedata.txt", "w") as file:
                                file.writelines(lines)  # Write the modified lines back to the file
                            gamescene += 1
                            break
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            characterName = characterName[:-1]
                        else:
                            if(len(characterName) <= 11):
                                characterName += event.unicode

                    # Toggle color based on active state
                    color = color_active if active else color_passive

                # Draw the input box and text outside the event loop
                pygame.draw.rect(DISPLAYSURF, color, input_rect)
                text_surface = base_font.render(characterName, True, (WHITE))
                DISPLAYSURF.blit(text_surface, (input_rect.x + 15, input_rect.y + 15))
                pygame.draw.rect(DISPLAYSURF, (WHITE), input_rect, 2)
                pygame.display.flip()
            if (gamescene == 58):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(imagemermaid1, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 9
                draw_text_center('so your name is, ' + characterName +"!", font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('What a great name!', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 925)
                image4.set_alpha(255)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + 000), 920))
                DISPLAYSURF.blit(image4, ((textFader + -600), 960))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 59):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(imagemermaid1, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 9
                draw_text_center('Us meeting is definitely the work of fate.', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('lets be friends? Thats what you humans call it right?', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 925)
                image4.set_alpha(255)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + 000), 920))
                DISPLAYSURF.blit(image4, ((textFader + -800), 960))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 60):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(imagemermaid1, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 9
                draw_text_center('Ive never had a friend before,', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('this is so exciting.', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 925)
                image4.set_alpha(255)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + 100), 920))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 61):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(imagemermaid1, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 9
                draw_text_center('Oh i know! let me show you around the kingdom!', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('Let me officially welcome you ' + characterName, font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 925)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + 100), 920))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 62):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image19, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('to the grand kingdom of', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('**Lucidea**!', font10, GREY, DISPLAYSURF, halfdisplay, 925)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + 150), 920))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 63):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image19, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('"Here we mermaids rule the seas, protecting it from the everlasting darkness."', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('"Our kingdom has survived for 87 generations as the sole ruler of the 7th Sea!"', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 925)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + -150), 920))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 64):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image19, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('Due to the wisdom and bravery of King Exodus, we learned how to harness mythical beasts', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('and defend our nation from the Nightmares, evil creatures born from darkness.', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 925)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + -150), 920))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 65):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image19, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('Us mermaids once ruled all seven seas, sadly that isnt the case anymore', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('as far as we are aware, the other six nations have been destroyed, wiped from existence..', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 925)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + -150), 920))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 66):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image19, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('All thats left is the four Mermaid factions that rule Lucidea.', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 890)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + 100), 920))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 67):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image19, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('but that is all in the past, now we have the strength to regain our lost land.', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('tell me little human, since you now carry my blood within you, do you wish to join us?', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 925)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + -150), 920))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 68):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image19, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('You need not feel pressured to say yes, It just seems like you have been forgotten, ', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('abandoned... without purpose', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 925)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + -100), 920))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
                music1 = True
            if (gamescene == 69):
                if(music1):
                    sound_effect = pygame.mixer.Sound("audio/chestopen.mp3")
                    sound_effect.play()
                    pygame.mixer.music.set_volume(0.2)
                    music1 = False
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(imagemermaid3, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('Ahh forgive my manners, sorry for saying such things to you so soon.. I have no ill intentions towards you ' +characterName , font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('Please take this gift I prepared for you, Its not much but I believe you will like it.', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 925)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + -150), 920))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 70):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(imagemermaid3, (200, 100))
                DISPLAYSURF.blit(image29, (760, 380))
                DISPLAYSURF.blit(image22, (830, 505))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('Here lies the soul of ', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('of a mythical creature, infact youve met her before', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 925)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + 150), 920))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
                music1 = True
            if (gamescene == 71):
                if(music1):
                    sound_effect = pygame.mixer.Sound("audio/stab.mp3")
                    sound_effect.play()
                    pygame.mixer.music.load("audio/battlemusic2.mp3")
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.set_volume(0.8)
                    music1 = False
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(imagemermaid3, (200, 100))
                DISPLAYSURF.blit(image29, (760, 380))
                DISPLAYSURF.blit(image22, (830, 505))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 13
                draw_text_center('It would surely make me happy if you- ', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('*ShRknC*', font7, RED, DISPLAYSURF, halfdisplay, 925)
                DISPLAYSURF.blit(image4, ((textFader + 1000), 920))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
                music2 = True
            if (gamescene == 72):
                if(music2):
                    sound_effect = pygame.mixer.Sound("audio/gasping.mp3")
                    sound_effect.play()
                    music2 = False
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image23, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('Aeutgh', font9, LIGHTBLUE, DISPLAYSURF, halfdisplay, 890)
                DISPLAYSURF.blit(image4, ((textFader + 700), 880))
                DISPLAYSURF.blit(image4, ((textFader + 100), 920))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
                music1 = True
            if (gamescene == 73):
                if(music1):
                    sound_effect = pygame.mixer.Sound("audio/dragonroar.mp3")
                    sound_effect.play()
                    pygame.mixer.music.set_volume(0.6)
                    music1 = False
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image21, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                draw_text_center('RUEAWRRRRRRRWR', font6, PURPLE, DISPLAYSURF, halfdisplay, 890)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 74):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image23, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('You look over and see the blue haired mermaid leaking blood out of her chest', font5, WHITE, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('dread and panic ignites within you', font5, WHITE, DISPLAYSURF, halfdisplay, 925)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + 100), 920))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
                music2 = True
            if (gamescene == 75):
                if(music2):
                    sound_effect = pygame.mixer.Sound("audio/gasping.mp3")
                    sound_effect.play()
                    music2 = False
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image23, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('"Its a Nightmare creature, RUN '+characterName + "!", font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('"Save yourself..."', font5, LIGHTBLUE, DISPLAYSURF, halfdisplay, 925)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + 200), 920))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
                music1 = True
            if (gamescene == 76):
                if(music1):
                    sound_effect = pygame.mixer.Sound("audio/monsterroar.mp3")
                    sound_effect.play()
                    pygame.mixer.music.set_volume(0.5)
                    music1 = False
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image21, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 15
                draw_text_center('DIE PRINCESS OCTAVIA!', font6, PURPLE, DISPLAYSURF, halfdisplay, 890)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + 100), 925))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
                music2 = True
            if (gamescene == 77):
                if(music2):
                    sound_effect = pygame.mixer.Sound("audio/underwaterimpact.mp3")
                    sound_effect.play()
                    music2 = False
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image21, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('The monster opens its blood filled jaw, inches away from the princesses throat', font5, WHITE, DISPLAYSURF, halfdisplay, 890)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + 100), 920))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 78):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image21, (200, 100))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
                music2 = True
            if (gamescene == 79):
                if(music2):
                    sound_effect = pygame.mixer.Sound("audio/swordsound.mp3")
                    sound_effect.play()
                    music2 = False
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image24, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 9
                draw_text_center('"HALT CREATURE"', font9, GREY, DISPLAYSURF, halfdisplay, 890)
                DISPLAYSURF.blit(image4, ((textFader + 700), 880))
                DISPLAYSURF.blit(image4, ((textFader + 100), 920))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
                music1 = True
            if (gamescene == 80):
                if(music1):
                    sound_effect = pygame.mixer.Sound("audio/marching.mp3")
                    sound_effect.play()
                    pygame.mixer.music.set_volume(0.5)
                    music1 = False
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image24, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('*You look over and see a group of armed mermaids rushing at you from the distance*', font5, WHITE, DISPLAYSURF, halfdisplay, 890)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + 100), 920))
                music2 = True
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 81):
                if(music2):
                    sound_effect = pygame.mixer.Sound("audio/evilmusic.mp3")
                    sound_effect.play()
                    music2 = False
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image25, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 9
                draw_text_center('A bizarre and unnatural voice echoes through the suddenly frigid water,', font5, WHITE, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('filled with a strangely hypnotizing yet dreadful lure', font5, WHITE, DISPLAYSURF, halfdisplay, 925)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + 100), 920))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 82):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image25, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 15
                draw_text_center('"Wretched Guards, always ruining my fun."', font6, PURPLE, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('"Do you even believe you can stop me?"', font6, PURPLE, DISPLAYSURF, halfdisplay, 925)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + 100), 925))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
                music2 = True
            if (gamescene == 83):
                if(music2):
                    pygame.mixer.stop()
                    pygame.mixer.music.load("audio/rebornmusic.mp3")
                    pygame.mixer.music.play(-1)
                    sound_effect = pygame.mixer.Sound("audio/underwaterimpact.mp3")
                    sound_effect.play()
                    sound_effect = pygame.mixer.Sound("audio/scifinoise.mp3")
                    sound_effect.play()
                    music2 = False
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image25, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('A booming voice cuts the Nightmare off', font5, WHITE, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('"I do. "', font11, GOLD, DISPLAYSURF, halfdisplay, 925)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + 00), 920))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
                music1 = True
            if (gamescene == 84):
                if(music1):
                    sound_effect = pygame.mixer.Sound("audio/action.mp3")
                    sound_effect.play()
                    music1 = False
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image28, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('*VRSHHHHM*', font5, YELLOW, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('A flash of gold light descends from the sky, illuminating the entire sea', font5, WHITE, DISPLAYSURF, halfdisplay, 925)
                DISPLAYSURF.blit(image4, ((textFader + 500), 920))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
                music2 = True
            if (gamescene == 85):
                if(music2):
                    sound_effect = pygame.mixer.Sound("audio/warhornblast.mp3")
                    sound_effect.play()
                    sound_effect = pygame.mixer.Sound("audio/explosion.mp3")
                    sound_effect.play()
                    music2 = False
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image28, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 12
                draw_text_center('The pillar of light crashes down on the Nightmare, cracking the land below', font5, WHITE, DISPLAYSURF, halfdisplay, 890)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + 100), 920))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
                music1 = True
            if (gamescene == 86):
                if(music1):
                    sound_effect = pygame.mixer.Sound("audio/monsterscream.mp3")
                    sound_effect.play()
                    music1 = False
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image27, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 15
                draw_text_center('AAEHHEAGHHHGHUAWE GHAEAHHAAAA', font6, PURPLE, DISPLAYSURF, halfdisplay, 890)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
                music2 = True
            if (gamescene == 87):
                if(music2):
                    pygame.mixer.music.load("audio/epicbattle.mp3")
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.set_volume(0.8)
                    music2 = False
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image26, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('you look up to see a golden armored mermaid sitting atop a sea dragon,', font5, WHITE, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('looking down with disdain on the world below*', font5, WHITE, DISPLAYSURF, halfdisplay, 925)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + 000), 920))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 88):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image26, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 14
                draw_text_center('"I am Aurelean, right hand of the king!"', font11, GOLD, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('"Gaze upon the infinite glory and seek retribution in your actions."', font11, GOLD, DISPLAYSURF, halfdisplay, 925)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + 100), 920))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
                music2 = True
            if (gamescene == 89):
                if(music2):
                    sound_effect = pygame.mixer.Sound("audio/die.wav")
                    sound_effect.play()
                    music2 = False
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image26, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 12
                draw_text_center('"Die pathetic Mongrel."', font11, GOLD, DISPLAYSURF, halfdisplay, 890)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + 100), 920))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
                music1 = True
            if (gamescene == 90):
                if(music1):
                    sound_effect = pygame.mixer.Sound("audio/regret.mp3")
                    sound_effect.play()
                    music1 = False
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image36, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 15
                draw_text_center('"You will regret thisss.."', font6, PURPLE, DISPLAYSURF, halfdisplay, 890)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + 100), 925))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
                music2 = True
            if (gamescene == 91):
                if(music2):
                    sound_effect = pygame.mixer.Sound("audio/glassbreaking.mp3")
                    sound_effect.play()
                    music2 = False
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image36, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                DISPLAYSURF.blit(image57, (200, 100))
                if(textFader != 3000):
                    textFader = textFader + 13
                draw_text_center('*Crash*', font5, WHITE, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('the nightmare throws a black orb on the floor and dark tendrels flow out', font5, WHITE, DISPLAYSURF, halfdisplay, 925)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + 100), 920))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
                music1 = True
            if (gamescene ==92):
                if(music1):
                    sound_effect = pygame.mixer.Sound("audio/warp.mp3")
                    sound_effect.play()
                    music1 = False
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image37, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                DISPLAYSURF.blit(image57, (200, 100))
                if(textFader != 3000):
                    textFader = textFader + 15
                draw_text_center('Wrapping around the nightmare and mermaid princess until they dissapeared into the darkness', font5, WHITE, DISPLAYSURF, halfdisplay, 890)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + 100), 920))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 93):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image37, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                DISPLAYSURF.blit(image57, (200, 100))
                if(textFader != 3000):
                    textFader = textFader + 15
                draw_text_center('Right before it dissapeared, you hear a deep voice reverberate your surroundings', font5, WHITE, DISPLAYSURF, halfdisplay, 890)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + 100), 920))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
                music1 = True
            if (gamescene == 94):
                if(music1):
                    sound_effect = pygame.mixer.Sound("audio/dinosaurgrowl.mp3")
                    sound_effect.play()
                    music1 = False
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image37, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                DISPLAYSURF.blit(image57, (200, 100))
                if(textFader != 3000):
                    textFader = textFader + 15
                draw_text_center('"Remember my name scum, I am Galixerous, son of BAag."', font6, PURPLE, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('"ANd just as ive taken your princess, I will one day take your life!"', font6, PURPLE, DISPLAYSURF, halfdisplay, 925)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + 100), 925))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
                music2 = True
            if (gamescene == 95):
                sound_effect = pygame.mixer.Sound("audio/monsterdissapear.mp3")
                sound_effect.play()
                fps = int(capv2.get(cv2.CAP_PROP_FPS))
                clock = pygame.time.Clock()
                while capv2.isOpened():
                    ret, frame = capv2.read()
                    if not ret:
                        break
                    frame = cv2.resize(frame, (1650, 940))
                    frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame = pygame.surfarray.make_surface(frame).convert()
                    DISPLAYSURF.blit(frame, (140, 100))
                    pygame.display.flip()  # Update the display
                    clock.tick(fps)
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            print("stop clicking so much")
                capv2.release()
                gamescene = gamescene + 1
            if (gamescene == 96):
                if(music2):
                    pygame.mixer.stop()
                    pygame.mixer.music.load("audio/dramaticheavenmusic.mp3")
                    pygame.mixer.music.play(-1)
                    music2 = False
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image38, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 9
                draw_text_center('Silence lingers throughout the air as everyone stares at ', font5, WHITE, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('the disappearance of the princess and Nightmare', font5, WHITE, DISPLAYSURF, halfdisplay, 925)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + 00), 920))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 97):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image38, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('Eventually you gaze upon the golden armored knight as he turns his head towards you', font5, WHITE, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('"Human."', font5, GOLD, DISPLAYSURF, halfdisplay, 925)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + 000), 920))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
                music1 = True
            if (gamescene == 98):
                if(music1):
                    sound_effect = pygame.mixer.Sound("audio/sighnoise.mp3")
                    sound_effect.play()
                    music1 = False
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image34, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('"We have shown you something embarrassing, forgive us."', font5, GOLD, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('"But just as I am to blame, you are as well."', font5, GOLD, DISPLAYSURF, halfdisplay, 925)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + 50), 920))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 99):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image34, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('"your sin..."', font5, GOLD, DISPLAYSURF, halfdisplay, 890)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + 100), 920))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 100):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image34, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('"Is being too weak"', font5, GOLD, DISPLAYSURF, halfdisplay, 890)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + 100), 920))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 101):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image34, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('"The capture of our princess is too critical of an error, I must clean up this mess."', font5, GOLD, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('"Normally I would do things differently but the princess has already accepted you as one of our own"', font5, GOLD, DISPLAYSURF, halfdisplay, 925)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + -200), 920))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
                music1 = True
            if (gamescene == 102):
                if(music1):
                    sound_effect = pygame.mixer.Sound("audio/bubbles.mp3")
                    sound_effect.play()
                    music1 = False
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image34, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                draw_text_center('"Tell me human,"', font5, GOLD, DISPLAYSURF, halfdisplay, 890)
                draw_text_center('"Do you desire strength?"', font5, GOLD, DISPLAYSURF, halfdisplay, 925)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + 100), 920))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 103):
                alpha1 = 0
                alpha2 = 0
                radius = 150
                circleCenter1 = (792, 600)
                circleCenter2 = (1135, 600)

                mouse_pos = pygame.mouse.get_pos()
                distance = math.sqrt((mouse_pos[0] - circleCenter1[0]) ** 2 + (mouse_pos[1] - circleCenter1[1]) ** 2)
                if distance <= radius:
                    alpha1 = 200
                distance2 = math.sqrt((mouse_pos[0] - circleCenter2[0]) ** 2 + (mouse_pos[1] - circleCenter2[1]) ** 2)
                if distance2 <= radius:
                    alpha2 = 200
                for event in pygame.event.get():
                    distance = math.sqrt((mouse_pos[0] - circleCenter1[0]) ** 2 + (mouse_pos[1] - circleCenter1[1]) ** 2)
                    if distance <= radius:
                        alpha1 = 200
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            choice1 = True
                            gamescene = gamescene + 1
                    distance2 = math.sqrt((mouse_pos[0] - circleCenter2[0]) ** 2 + (mouse_pos[1] - circleCenter2[1]) ** 2)
                    if distance2 <= radius:
                        alpha2 = 200
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            choice2 = True
                            gamescene = gamescene + 1
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image35, (200, 100))
                image4.set_alpha(100)
                DISPLAYSURF.blit(image4, (0, 0))
                DISPLAYSURF.blit(image32, (610, 250))
                image33.set_alpha(alpha1)
                DISPLAYSURF.blit(image33, (485, 280))
                image33.set_alpha(alpha2)
                DISPLAYSURF.blit(image33, (825, 280))
                draw_text_center('"Choose,"', font4, WHITE, DISPLAYSURF, halfdisplay, 220)
                draw_text_center('"Do you desire strength?"', font4, GOLD, DISPLAYSURF, halfdisplay, 170)
                pygame.display.update()
            if (gamescene == 104):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image35, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                if(choice1):
                    draw_text_center('"Wisdom at you age is not easy to come by."', font5, GOLD, DISPLAYSURF, halfdisplay, 890)
                    draw_text_center('"Follow me child."', font5, GOLD, DISPLAYSURF, halfdisplay, 925)
                if(choice2):
                    draw_text_center('"So you choose mediocrity"', font5, GOLD, DISPLAYSURF, halfdisplay, 890)
                    draw_text_center('"How amusing"', font5, GOLD, DISPLAYSURF, halfdisplay, 925)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + 50), 920))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
                music1 = True
            if (gamescene == 105):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image35, (200, 100))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                if(textFader != 3000):
                    textFader = textFader + 10
                if(choice1):
                    draw_text_center('"I shall take you to the imperial city"', font5, GOLD, DISPLAYSURF, halfdisplay, 890)
                if(choice2):
                    DISPLAYSURF.fill(BLACK)
                    DISPLAYSURF.blit(image40, (200, 100))
                    image4.set_alpha(240)
                    DISPLAYSURF.blit(image4, (0, 880))
                    draw_text_center('You have no choice human, strength is not something you can run away from.', font5, GOLD, DISPLAYSURF, halfdisplay, 890)
                    draw_text_center('You will take responsibility for your actions, follow me to the imperial city', font5, RED, DISPLAYSURF, halfdisplay, 925)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                DISPLAYSURF.blit(image4, ((textFader + -150), 920))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
                music1 = True
            if (gamescene == 106):
                if(music1):
                    sound_effect = pygame.mixer.Sound("audio/bubbles.mp3")
                    sound_effect.play()
                    music1 = False
                music2 = True
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image35, (200, 100))
                image4.set_alpha(100)
                DISPLAYSURF.blit(image4, (0, 0))
                image4.set_alpha(240)
                DISPLAYSURF.blit(image4, (0, 880))
                fps = int(capv4.get(cv2.CAP_PROP_FPS))
                clock = pygame.time.Clock()
                while capv4.isOpened():
                    ret, frame = capv4.read()
                    if not ret:
                        break
                    frame = cv2.resize(frame, (1650, 940))
                    frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame = pygame.surfarray.make_surface(frame).convert()
                    DISPLAYSURF.blit(frame, (140, 100))
                    pygame.display.flip()  # Update the display
                    clock.tick(fps)
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            print("stop clicking so much")
                capv4.release()
                gamescene = gamescene + 1
            if (gamescene == 107):
                DISPLAYSURF.fill(BLACK)
                if(textFader != 3000):
                    textFader = textFader + 12
                if(music2):
                    pygame.mixer.music.load("audio/dramaticheavenmusic.mp3")
                    pygame.mixer.music.play(-1)
                    music2 = False
                draw_text_center('You travel along with the golden knight.', font5, WHITE, DISPLAYSURF, halfdisplay, 890)
                DISPLAYSURF.blit(image4, ((textFader + 600), 880))
                music1 = True
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 108):
                if(music1):
                    textFader = 255
                    music1 = False
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image41, (180, 100))
                image4.set_alpha(textFader)
                DISPLAYSURF.blit(image4, (0, 0))
                if(textFader > 2):
                    textFader = textFader - 2
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 109):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image41, (180, 100))
                DISPLAYSURF.blit(image52, (120, 740))
                DISPLAYSURF.blit(image53, (380, 580))
                draw_text('Welcome to the royal', font5, GOLD, DISPLAYSURF, 475, 620)
                draw_text('capital', font5, GOLD, DISPLAYSURF, 545, 645)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 110):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image41, (180, 100))
                DISPLAYSURF.blit(image52, (120, 740))
                DISPLAYSURF.blit(image53, (380, 580))
                draw_text('let me reintroduce myself,', font5, GOLD, DISPLAYSURF, 465, 620)
                draw_text('I am called Aurelius', font5, GOLD, DISPLAYSURF, 480, 645)
                draw_text('Right hand of the King.', font5, GOLD, DISPLAYSURF, 475, 670)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 111):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image41, (180, 100))
                DISPLAYSURF.blit(image52, (120, 740))
                DISPLAYSURF.blit(image53, (380, 580))
                draw_text('Ive protected this kingdom for,', font5, GOLD, DISPLAYSURF, 450, 620)
                draw_text('300 years and I hope you will', font5, GOLD, DISPLAYSURF, 455, 645)
                draw_text('cherish it as much as I do.', font5, GOLD, DISPLAYSURF, 460, 670)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 112):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image41, (180, 100))
                DISPLAYSURF.blit(image52, (120, 740))
                DISPLAYSURF.blit(image53, (380, 580))
                draw_text('Here we fight as the last hope,', font5, GOLD, DISPLAYSURF, 445, 620)
                draw_text('striving to defeat the darkness', font5, GOLD, DISPLAYSURF, 445, 645)
                draw_text('and take back the whats', font5, GOLD, DISPLAYSURF, 465, 670)
                draw_text('rightfully ours.', font5, GOLD, DISPLAYSURF, 515, 692)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 113):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image41, (180, 100))
                DISPLAYSURF.blit(image52, (120, 740))
                DISPLAYSURF.blit(image53, (380, 580))
                draw_text('Here in the Royal Capital you will', font5, GOLD, DISPLAYSURF, 440, 620)
                draw_text('be able gain the strength necessary', font5, GOLD, DISPLAYSURF, 425, 645)
                draw_text('to fight the Nightmares', font5, GOLD, DISPLAYSURF, 460, 670)
                draw_text('and hopefully..', font5, GOLD, DISPLAYSURF, 505, 695)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 114):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image41, (180, 100))
                DISPLAYSURF.blit(image52, (120, 740))
                DISPLAYSURF.blit(image53, (380, 580))
                draw_text('Rescue princess Aurora', font5, GOLD, DISPLAYSURF, 475, 645)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 115):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image41, (180, 100))
                DISPLAYSURF.blit(image52, (120, 740))
                DISPLAYSURF.blit(image53, (380, 580))
                draw_text('.....', font5, GOLD, DISPLAYSURF, 565, 645)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 116):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image41, (180, 100))
                DISPLAYSURF.blit(image52, (120, 740))
                DISPLAYSURF.blit(image53, (380, 580))
                draw_text('She was a kind princess. Always', font5, GOLD, DISPLAYSURF, 445, 620)
                draw_text('loved by her people and never ', font5, GOLD, DISPLAYSURF, 445, 645)
                draw_text('abusing her power as part of', font5, GOLD, DISPLAYSURF, 460, 670)
                draw_text('the royal family.', font5, GOLD, DISPLAYSURF, 485, 695)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 117):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image41, (180, 100))
                DISPLAYSURF.blit(image52, (120, 740))
                DISPLAYSURF.blit(image53, (380, 580))
                draw_text('I will rescue her no matter what..', font5, GOLD, DISPLAYSURF, 435, 620)
                draw_text('or at the very least,', font5, GOLD, DISPLAYSURF, 490, 645)
                draw_text('die trying!', font7, GOLD, DISPLAYSURF, 520, 680)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 118):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image41, (180, 100))
                DISPLAYSURF.blit(image52, (120, 740))
                DISPLAYSURF.blit(image53, (380, 580))
                draw_text('Enough of that. Let me', font5, GOLD, DISPLAYSURF, 480, 620)
                draw_text('guide you around the capital', font5, GOLD, DISPLAYSURF, 455, 645)
                draw_text('Im sure you will find it most', font5, GOLD, DISPLAYSURF, 455, 670)
                draw_text('interesting.', font5, GOLD, DISPLAYSURF, 520, 695)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 119):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image41, (180, 100))
                DISPLAYSURF.blit(image52, (120, 740))
                DISPLAYSURF.blit(image53, (380, 580))
                draw_text('Follow me', font5, GOLD, DISPLAYSURF, 525, 645)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 120):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image43, (180, 100))
                DISPLAYSURF.blit(image52, (120, 740))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 121):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image43, (180, 100))
                DISPLAYSURF.blit(image52, (120, 740))
                DISPLAYSURF.blit(image53, (380, 580))
                draw_text('First things first,', font5, GOLD, DISPLAYSURF, 485, 620)
                draw_text('as the last standing bastian of', font5, GOLD, DISPLAYSURF, 445, 645)
                draw_text('light, the fear of death hangs', font5, GOLD, DISPLAYSURF, 450, 670)
                draw_text('over us all.', font5, GOLD, DISPLAYSURF, 520, 695)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 122):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image43, (180, 100))
                DISPLAYSURF.blit(image52, (120, 740))
                DISPLAYSURF.blit(image53, (380, 580))
                draw_text('That has led to many', font5, GOLD, DISPLAYSURF, 475, 620)
                draw_text('places of sin to become popular.', font5, GOLD, DISPLAYSURF, 445, 645)
                draw_text('To relieve stress as some', font5, GOLD, DISPLAYSURF, 445, 670)
                draw_text('would say.', font5, GOLD, DISPLAYSURF, 515, 695)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 123):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image43, (180, 100))
                DISPLAYSURF.blit(image52, (120, 740))
                DISPLAYSURF.blit(image53, (380, 580))
                draw_text('The gambling den is by', font5, GOLD, DISPLAYSURF, 465, 620)
                draw_text('far the most popular of them', font5, GOLD, DISPLAYSURF, 445, 645)
                draw_text('all, allowing fortune to decide', font5, GOLD, DISPLAYSURF, 450, 670)
                draw_text('ones fate.', font5, GOLD, DISPLAYSURF, 525, 695)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 124):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image43, (180, 100))
                DISPLAYSURF.blit(image52, (120, 740))
                DISPLAYSURF.blit(image53, (380, 580))
                draw_text('If you were born under a', font5, GOLD, DISPLAYSURF, 460, 620)
                draw_text('lucky star then I suggest', font5, GOLD, DISPLAYSURF, 460, 645)
                draw_text('you take a go at this place.', font5, GOLD, DISPLAYSURF, 460, 670)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 125):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image43, (180, 100))
                DISPLAYSURF.blit(image52, (120, 740))
                DISPLAYSURF.blit(image53, (380, 580))
                draw_text('If not, stay the hell', font5, GOLD, DISPLAYSURF, 485, 620)
                draw_text('away from this place.', font5, GOLD, DISPLAYSURF, 485, 645)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 126):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image44, (180, 100))
                DISPLAYSURF.blit(image52, (120, 740))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 127):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image44, (180, 100))
                DISPLAYSURF.blit(image52, (120, 740))
                DISPLAYSURF.blit(image53, (380, 580))
                draw_text('Next is the best shop', font5, GOLD, DISPLAYSURF, 470, 620)
                draw_text('in town, Paimons Shop.', font5, GOLD, DISPLAYSURF, 470, 645)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 128):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image44, (180, 100))
                DISPLAYSURF.blit(image52, (120, 740))
                DISPLAYSURF.blit(image53, (380, 580))
                draw_text('If you ever need to buy or', font5, GOLD, DISPLAYSURF, 460, 620)
                draw_text('sell things then Paimon is', font5, GOLD, DISPLAYSURF, 465, 645)
                draw_text('your best bet.', font5, GOLD, DISPLAYSURF, 500, 670)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 129):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image45, (180, 100))
                DISPLAYSURF.blit(image52, (120, 740))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 130):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image45, (180, 100))
                DISPLAYSURF.blit(image52, (120, 740))
                DISPLAYSURF.blit(image53, (380, 580))
                draw_text('Ahhh, the Colosseum. It', font5, GOLD, DISPLAYSURF, 460, 620)
                draw_text('brings back old memories.', font5, GOLD, DISPLAYSURF, 460, 645)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 131):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image45, (180, 100))
                DISPLAYSURF.blit(image52, (120, 740))
                DISPLAYSURF.blit(image53, (380, 580))
                draw_text('To fight here is the ultimate', font5, GOLD, DISPLAYSURF, 455, 620)
                draw_text('honor and glory. A place where', font5, GOLD, DISPLAYSURF, 450, 645)
                draw_text('champions are made.', font5, GOLD, DISPLAYSURF, 480, 670)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 132):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image45, (180, 100))
                DISPLAYSURF.blit(image52, (120, 740))
                DISPLAYSURF.blit(image53, (380, 580))
                draw_text('You will also be paid gold', font5, GOLD, DISPLAYSURF, 465, 620)
                draw_text('for every win of course.', font5, GOLD, DISPLAYSURF, 465, 645)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 133):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image46, (180, 100))
                DISPLAYSURF.blit(image52, (120, 740))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 134):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image46, (180, 100))
                DISPLAYSURF.blit(image52, (120, 740))
                DISPLAYSURF.blit(image53, (380, 580))
                draw_text('The labor market is run by the', font5, GOLD, DISPLAYSURF, 455, 620)
                draw_text('union, a group that only cares', font5, GOLD, DISPLAYSURF, 450, 645)
                draw_text('about money.', font5, GOLD, DISPLAYSURF, 505, 670)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 135):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image46, (180, 100))
                DISPLAYSURF.blit(image52, (120, 740))
                DISPLAYSURF.blit(image53, (380, 580))
                draw_text('Come here if you are in', font5, GOLD, DISPLAYSURF, 455, 620)
                draw_text('need of work or resources.', font5, GOLD, DISPLAYSURF, 450, 645)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 136):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image47, (180, 100))
                DISPLAYSURF.blit(image52, (120, 740))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 137):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image47, (180, 100))
                DISPLAYSURF.blit(image52, (120, 740))
                DISPLAYSURF.blit(image53, (380, 580))
                draw_text('The royal castle is where', font5, GOLD, DISPLAYSURF, 460, 620)
                draw_text('I stay. As a celestial Knight', font5, GOLD, DISPLAYSURF, 455, 645)
                draw_text('it is my duty to protect', font5, GOLD, DISPLAYSURF, 465, 670)
                draw_text('the king.', font5, GOLD, DISPLAYSURF, 520, 695)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 138):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image47, (180, 100))
                DISPLAYSURF.blit(image52, (120, 740))
                DISPLAYSURF.blit(image53, (380, 580))
                draw_text('If you are permitted entrance,', font5, GOLD, DISPLAYSURF, 445, 620)
                draw_text('you may visit the royal', font5, GOLD, DISPLAYSURF, 465, 645)
                draw_text('castle for various quests', font5, GOLD, DISPLAYSURF, 475, 670)
                draw_text('and tasks.', font5, GOLD, DISPLAYSURF, 485, 695)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 139):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image48, (180, 100))
                DISPLAYSURF.blit(image52, (120, 740))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 140):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image48, (180, 100))
                DISPLAYSURF.blit(image52, (120, 740))
                DISPLAYSURF.blit(image53, (380, 580))
                draw_text('One of our greatest inventions', font5, GOLD, DISPLAYSURF, 445, 620)
                draw_text('it is called "Tempest"', font5, GOLD, DISPLAYSURF, 470, 645)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 141):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image48, (180, 100))
                DISPLAYSURF.blit(image52, (120, 740))
                DISPLAYSURF.blit(image53, (380, 580))
                draw_text('This ship has capabilities to', font5, GOLD, DISPLAYSURF, 455, 620)
                draw_text('travel anywhere within the ', font5, GOLD, DISPLAYSURF, 455, 645)
                draw_text('known seas.', font5, GOLD, DISPLAYSURF, 515, 670)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 142):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image48, (180, 100))
                DISPLAYSURF.blit(image52, (120, 740))
                DISPLAYSURF.blit(image53, (380, 580))
                draw_text('You cannot hide within', font5, GOLD, DISPLAYSURF, 475, 620)
                draw_text('the arms of safety', font5, GOLD, DISPLAYSURF, 485, 645)
                draw_text('forever.', font5, GOLD, DISPLAYSURF, 510, 670)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 143):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image48, (180, 100))
                DISPLAYSURF.blit(image52, (120, 740))
                DISPLAYSURF.blit(image53, (380, 580))
                draw_text('in order to grow you', font5, GOLD, DISPLAYSURF, 475, 620)
                draw_text('must journey, experience hardship,', font5, GOLD, DISPLAYSURF, 420, 645)
                draw_text('and make new companions.', font5, GOLD, DISPLAYSURF, 465, 670)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 144):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image49, (180, 100))
                DISPLAYSURF.blit(image52, (120, 740))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 145):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image49, (180, 100))
                DISPLAYSURF.blit(image52, (120, 740))
                DISPLAYSURF.blit(image53, (380, 580))
                draw_text('the guild hall gives', font5, GOLD, DISPLAYSURF, 480, 620)
                draw_text('out daily quests to complete.', font5, GOLD, DISPLAYSURF, 450, 645)
                draw_text('A good way to lvl quickly.', font5, GOLD, DISPLAYSURF, 465, 670)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 146):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image49, (180, 100))
                DISPLAYSURF.blit(image52, (120, 740))
                DISPLAYSURF.blit(image53, (380, 580))
                draw_text('do not bite off more then', font5, GOLD, DISPLAYSURF, 465, 620)
                draw_text('you can chew, or you may', font5, GOLD, DISPLAYSURF, 465, 645)
                draw_text('learn the hard way.', font5, GOLD, DISPLAYSURF, 490, 670)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 147):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image50, (180, 100))
                DISPLAYSURF.blit(image52, (620, 740))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 148):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image50, (180, 100))
                DISPLAYSURF.blit(image52, (620, 740))
                DISPLAYSURF.blit(image53, (880, 580))
                draw_text('The stash is run by the', font5, GOLD, DISPLAYSURF, 955, 620)
                draw_text('royal family. It allows', font5, GOLD, DISPLAYSURF, 950, 645)
                draw_text('you to store items and', font5, GOLD, DISPLAYSURF, 975, 670)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 149):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image50, (180, 100))
                DISPLAYSURF.blit(image52, (620, 740))
                DISPLAYSURF.blit(image53, (880, 580))
                draw_text('beasts that you find', font5, GOLD, DISPLAYSURF, 965, 620)
                draw_text('during your journeys', font5, GOLD, DISPLAYSURF, 960, 645)
                draw_text('to the unknown.', font5, GOLD, DISPLAYSURF, 975, 670)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 150):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image51, (180, 100))
                DISPLAYSURF.blit(image52, (620, 740))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 151):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image51, (180, 100))
                DISPLAYSURF.blit(image52, (620, 740))
                DISPLAYSURF.blit(image53, (880, 580))
                draw_text('Last but not least,', font5, GOLD, DISPLAYSURF, 985, 620)
                draw_text('Byrons Black Market.', font5, GOLD, DISPLAYSURF, 975, 645)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 152):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image51, (180, 100))
                DISPLAYSURF.blit(image52, (620, 740))
                DISPLAYSURF.blit(image53, (880, 580))
                draw_text('Do not tell anyone who', font5, GOLD, DISPLAYSURF, 970, 620)
                draw_text('showed you this place,', font5, GOLD, DISPLAYSURF, 970, 645)
                draw_text('however...', font5, GOLD, DISPLAYSURF, 1085, 670)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 153):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image51, (180, 100))
                DISPLAYSURF.blit(image52, (620, 740))
                DISPLAYSURF.blit(image53, (880, 580))
                draw_text('If you are ever in need', font5, GOLD, DISPLAYSURF, 965, 620)
                draw_text('of some more unique items,', font5, GOLD, DISPLAYSURF, 955, 645)
                draw_text('you may consider coming here.', font5, GOLD, DISPLAYSURF, 945, 670)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 154):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image41, (180, 100))
                DISPLAYSURF.blit(image52, (620, 740))
                DISPLAYSURF.blit(image53, (880, 580))
                draw_text('That is all for now,', font5, GOLD, DISPLAYSURF, 980, 620)
                draw_text('I must return to inform', font5, GOLD, DISPLAYSURF, 970, 645)
                draw_text('the king', font5, GOLD, DISPLAYSURF, 1065, 670)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
                music2 = True
            if (gamescene == 155):
                if(music2):
                    sound_effect = pygame.mixer.Sound("audio/backopen.mp3")
                    sound_effect.play()
                    music2 = False
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image41, (180, 100))
                DISPLAYSURF.blit(image52, (620, 740))
                DISPLAYSURF.blit(image53, (880, 580))
                draw_text('Before I leave,', font5, GOLD, DISPLAYSURF, 1005, 620)
                draw_text('take this gift', font5, GOLD, DISPLAYSURF, 1010, 645)
                draw_text('from me', font5, GOLD, DISPLAYSURF, 1050, 670)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
                music1 = True
            if (gamescene == 156):
                if(music1):
                    with open("gamedata.txt", "r") as file:
                        lines = file.readlines()
                        lines[0] = f"gold = {1000}\n"
                    with open("gamedata.txt", "w") as file:
                        file.writelines(lines)
                    sound_effect = pygame.mixer.Sound("audio/itempickup.mp3")
                    sound_effect.play()
                    music1 = False
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image41, (180, 100))
                DISPLAYSURF.blit(image52, (620, 740))
                draw_text_center('You have received *1000 Gold*', font12, YELLOW, DISPLAYSURF, halfdisplay, 470)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 157):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image55, (180, 100))
                DISPLAYSURF.blit(image52, (620, 740))
                DISPLAYSURF.blit(image53, (880, 580))
                draw_text('I see great potential within', font5, GOLD, DISPLAYSURF, 955, 620)
                draw_text('you ' + characterName + '.', font5, GOLD, DISPLAYSURF, 1030, 645)
                draw_text('Do not disappoint me.', font5, GOLD, DISPLAYSURF, 975, 670)
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 158):
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image55, (180, 100))
                DISPLAYSURF.blit(image52, (620, 740))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
                music1 = True
            if (gamescene == 159):
                if(music1):
                    with open("gamedata.txt", "r") as file:
                        lines = file.readlines()
                        lines[3] = f"finishedtutorial = true\n"
                    with open("gamedata.txt", "w") as file:
                        file.writelines(lines)  # Write the modified lines back to the file
                    sound_effect = pygame.mixer.Sound("audio/swoosh.mp3")
                    sound_effect.play()
                    music1 = False
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(image55, (180, 100))
                gamescene = self.xbutton(gamescene)
                pygame.display.update()
            if (gamescene == 160):
                print("starting true game")
                DISPLAYSURF.fill(BLACK)
                pygame.display.update()
                self.menu_active3 = False
                menu3_active = True
                gamescene = 0
#######################################################################################################################
########################################################################################################################
########################################################################################################################
FPS = pygame.time.Clock()
FPS.tick(60)
pygame.display.set_caption("Seven Seas")
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    if menu1_active:
        Menu = StartMenu()
        Menu.StartupScreen()  # Run the first menu screen

    if ((menu2_active != True) & (completetutorial)) :
        print("menu1 false")
        menu2_active = True

    if menu2_active:
        Menu2 = StartMenu2()  # Initialize second menu
        Menu2.ChooseMenu()

        if(completetutorial):
            gameeeeeeintro = gameintro()
            gameeeeeeintro.gameintrocutscene()
    if menu3_active:
        game_instance = game.maingameareas("mainscreen")
    ########################################################################################################################
    pygame.quit()
    sys.exit()
########################################################################################################################