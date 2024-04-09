import pygame #Imporditakse Pygame raamatukogu
pygame.init() #Initialiseeritakse Pygame
screen=pygame.display.set_mode([300,300]) # Määratakse mängu akna suurus
pygame.display.set_caption("Floor-Kerdo.Alp") # Määratakse mängu akna pealkiri
screen.fill([0, 0, 0]) # Taustavärvi määramine mustaks
pygame.draw.circle(screen, [255, 0, 0], [150,100], 30, 0)# Punase ringi joonistamine, värv (255, 0, 0) - punane, asukoht (150, 100), raadius 30 ja täisringi tähistav väärtus 0
pygame.draw.circle(screen, [255, 255, 0], [150,160], 30, 0) # Kollase ringi joonistamine, värv (255, 255, 0) - kollane, asukoht (150, 160), raadius 30 ja täisringi tähistav väärtus 0
pygame.draw.circle(screen, [0, 255, 0], [150,220], 30, 0) # Rohelise ringi joonistamine, värv (0, 255, 0) - roheline, asukoht (150, 220), raadius 30 ja täisringi tähistav väärtus 0
pygame.draw.rect(screen, [255, 255, 255], [111, 60, 80, 200], 2)# Halli posti joonistamine, värv (255, 255, 255) - hall, asukoht (111, 60), suurus (80 laius, 200 kõrgus) ja joonuse paksus 
pygame.display.flip() # Mängu akna sisu värskendamine

running = True # Määratakse muutujaga "running" mängu käivitamise staatus
while running: # Peamine mängu tsükkel
    for event in pygame.event.get(): # Otsib kõiki toiminguid, mis mängu aknas on toimunud
        if event.type == pygame.QUIT: # Kui kasutaja sulgeb akna, lõpetatakse mängu tsükkel
            running = False  # Set running to False to exit the loop

    # Mängu akna sisu värskendamine
    pygame.display.flip()

pygame.quit() # Mängu lõpetamine