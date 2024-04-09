import pygame #Imporditakse Pygame raamatukogu
pygame.init() #Initialiseeritakse Pygame
screen=pygame.display.set_mode([300,500]) # Määratakse mängu akna suurus
pygame.display.set_caption("Floor-Kerdo.Alp") # Määratakse mängu akna pealkiri
screen.fill([0, 0, 0]) # Taustavärvi määramine mustaks
pygame.draw.circle(screen, [255, 0, 0], [150,50], 30, 0)# Punase ringi joonistamine, värv (255, 0, 0) - punane, asukoht (150, 100), raadius 30 ja täisringi tähistav väärtus 0
pygame.draw.circle(screen, [255, 255, 0], [150,110], 30, 0) # Kollase ringi joonistamine, värv (255, 255, 0) - kollane, asukoht (150, 160), raadius 30 ja täisringi tähistav väärtus 0
pygame.draw.circle(screen, [0, 255, 0], [150,170], 30, 0) # Rohelise ringi joonistamine, värv (0, 255, 0) - roheline, asukoht (150, 220), raadius 30 ja täisringi tähistav väärtus 0
pygame.draw.rect(screen, [128, 128, 128], [111, 10, 80, 200], 2)# Halli posti joonistamine, värv (255, 255, 255) - hall, asukoht (111, 60), suurus (80 laius, 200 kõrgus) ja joonuse paksus
pygame.draw.rect(screen, [128, 128, 128], [145, 210, 15, 300], 0)
pygame.draw.polygon(screen, [128, 128, 128] , [[135, 445],[168, 445], [200, 500], [100, 500]], 2) #kolmnurga joonistamine
pygame.draw.polygon(screen, [0, 0, 255] , [[135, 445],[168, 445], [180, 470], [122, 470]], 0)
pygame.draw.polygon(screen, [0, 0, 0] , [[180, 470], [122, 470], [135, 485],[168, 485]], 0)
pygame.draw.polygon(screen, [255, 255, 255] , [[115, 485],[188, 485], [198, 500],[105, 500]], 0)
pygame.display.flip() # Mängu akna sisu värskendamine

running = True # Määratakse muutujaga "running" mängu käivitamise staatus
while running: # Peamine mängu tsükkel
    for event in pygame.event.get(): # Otsib kõiki toiminguid, mis mängu aknas on toimunud
        if event.type == pygame.QUIT: # Kui kasutaja sulgeb akna, lõpetatakse mängu tsükkel
            running = False  # Set running to False to exit the loop

    # Mängu akna sisu värskendamine
    pygame.display.flip()

pygame.quit() # Mängu lõpetamine