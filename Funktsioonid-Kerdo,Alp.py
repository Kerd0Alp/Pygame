import pygame  # Impordib pygame'i raamatukogu, mis võimaldab mänguakna loomist ja interaktsiooni kasutajaga
import sys  # Impordib sys mooduli, mis võimaldab meil kasutada operatsioonisüsteemi funktsioone
import random  # Impordib random mooduli, mis võimaldab juhuslike arvude genereerimist
pygame.init()  # Initsialiseerib pygame'i raamatukogu, et saaksime seda kasutada

# Värvid
black = [0, 0, 0]  # Defineerib punase värvi RGB-väärtuse
green = [0, 255, 0]  # Defineerib rohelise värvi RGB-väärtuse
blue = [0, 0, 255]  # Defineerib sinise värvi RGB-väärtuse
pink = [255, 153, 255]  # Defineerib roosa värvi RGB-väärtuse
lWhite = [255,255,255]  # Defineerib heleda rohelise värvi RGB-väärtuse

# Ekraani seaded
screen = pygame.display.set_mode([640, 640])  # Loob mänguakna laiuse ja kõrgusega 640x480 pikslit
pygame.display.set_caption("Harjutamine")  # Määrab mänguakna pealkirjaks "Harjutamine"
screen.fill(lWhite)  # Täidab mänguakna heleda rohelise värviga

# Funktsioonid
def drawHouse(x, y, width, height, screen, color):  # Defineerib funktsiooni "drawHouse" maja joonistamiseks
    points = [(x, y - ((3/4.0) * height)), (x, y), (x + width, y), (x + width, y - ((3/4.0) * height)),
              (x, y - ((3/4.0) * height)), (x + width/2.0, y - height), (x + width, y - (3/4.0)*height)]  
    # Loob nimekirja punktidest, mis moodustavad maja seinad ja katuse
    lineThickness = 2  # Määrab joonte paksuse
    pygame.draw.lines(screen, color, False, points, lineThickness)  # Joonistab maja seinad ja katuse ekraanile

#kutsun funktsiooni välja
drawHouse(180,400,300,200,screen, black)
    
pygame.display.flip() # Värskendab mänguakna sisu

running = True # Määratakse muutujaga "running" mängu käivitamise staatus
while running: # Peamine mängu tsükkel
    for event in pygame.event.get(): # Otsib kõiki toiminguid, mis mängu aknas on toimunud
        if event.type == pygame.QUIT: # Kui kasutaja sulgeb akna, lõpetatakse mängu tsükkel
            running = False  # Set running to False to exit the loop

    # Mängu akna sisu värskendamine
    pygame.display.flip()

pygame.quit() # Mängu lõpetamine