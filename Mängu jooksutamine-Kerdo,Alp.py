import pygame  # Impordib pygame'i raamatukogu, mis võimaldab mänguakna loomist ja interaktsiooni kasutajaga
import sys  # Impordib sys mooduli, mis võimaldab meil kasutada operatsioonisüsteemi funktsioone
pygame.init()  # Initsialiseerib pygame'i raamatukogu, et saaksime seda kasutada

# Värvid
lRed = [255, 0, 0]  # Defineerib heleda punase värvi RGB-väärtuse
lBlue = [153, 204, 255]  # Defineerib heleda sinise värvi RGB-väärtuse

# Ekraani seaded
screen = pygame.display.set_mode([640, 480])  # Loob mänguakna laiuse ja kõrgusega 640x480 pikslit
pygame.display.set_caption("Harjutamine")  # Määrab mänguakna pealkirjaks "Harjutamine"
screen.fill(lRed)  # Täidab mänguakna heleda punase värviga

gameover = False  # Määrab muutuja "gameover" väärtuseks False, mis näitab, et mäng pole veel lõpetatud


while not gameover:  # Tsükkel, mis jookseb seni kuni "gameover" muutuja väärtus on False


    # Lisame pildid
    youWin = pygame.image.load("seller.webp")  # Laeb pildi "seller.webp" failist
    youWin = pygame.transform.scale(youWin, [300, 180])  # Muudab pildi suurust mõõtudeks 300x180 pikslit
    screen.blit(youWin, [180, 100])  # Kuvab pildi mänguaknale koordinaatides (180, 100)

    pygame.display.flip()  # Värskendab mänguakna sisu


    #mängu sulgemine ristist
    for i in pygame.event.get():
       if i.type == pygame.QUIT:
           sys.exit()

pygame.quit()