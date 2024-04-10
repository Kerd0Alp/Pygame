import pygame  # Impordib pygame'i raamatukogu, mis võimaldab mänguakna loomist ja interaktsiooni kasutajaga
import random  # Impordib random mooduli, mis võimaldab juhuslike arvude genereerimist
pygame.init()  # Initsialiseerib pygame'i raamatukogu, et saaksime seda kasutada

# Värvid
blue = [52, 229, 235]  # Defineerib sinise värvi RGB-väärtuse
lWhite = [255, 255, 255]  # Defineerib valge värvi RGB-väärtuse


# Ekraani seaded
screen = pygame.display.set_mode([640, 480])  # Loob mänguakna laiuse ja kõrgusega 640x480 pikslit
pygame.display.set_caption("Harjutamine")  # Määrab mänguakna pealkirjaks "Harjutamine"
screen.fill(lWhite)  # Täidab mänguakna valge värviga

for i in range(1, 10):  # Tsükkel, mis jookseb 9 korda
    x = random.randint(0, 620)  # Genereerib juhusliku x-koordinaadi mänguakna piires
    y = random.randint(0, 460)  # Genereerib juhusliku y-koordinaadi mänguakna piires
    pygame.draw.rect(screen,  blue, [x, y, 20, 20])  # Joonistab sinise ruudu mänguaknale juhuslikes koordinaatides
    pygame.display.flip()  # Värskendab mänguakna sisu

running = True # Määratakse muutujaga "running" mängu käivitamise staatus
while running: # Peamine mängu tsükkel
    for event in pygame.event.get(): # Otsib kõiki toiminguid, mis mängu aknas on toimunud
        if event.type == pygame.QUIT: # Kui kasutaja sulgeb akna, lõpetatakse mängu tsükkel
            running = False  # Set running to False to exit the loop

    # Mängu akna sisu värskendamine
    pygame.display.flip()

pygame.quit() # Mängu lõpetamine