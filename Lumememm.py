import pygame #Imporditakse Pygame raamatukogu
pygame.init() #Initialiseeritakse Pygame

screen=pygame.display.set_mode([300,300]) # Määratakse mängu akna suurus
pygame.display.set_caption("Lumemees-Kerdo.Alp") # Määratakse mängu akna pealkiri
screen.fill([153, 204, 255]) # Taustavärvi määramine siniseks

pygame.draw.circle(screen, [255, 255, 255], [150,75], 30, 0)#ringi joonistamine, asukoht (150, 100), raadius 30 ja täisringi tähistav väärtus 0
pygame.draw.circle(screen, [255, 255, 255], [150,140], 40, 0) #ringi joonistamine, asukoht (150, 160), raadius 40 ja täisringi tähistav väärtus 0
pygame.draw.circle(screen, [255, 255, 255], [150,220], 50, 0) #ringi joonistamine, asukoht (150, 220), raadius 50 ja täisringi tähistav väärtus 0
pygame.draw.circle(screen, [0, 0, 0], [140,73], 5, 0)#ringi joonistamine, asukoht (140, 73), raadius 50 ja täisringi tähistav väärtus 0
pygame.draw.circle(screen, [0, 0, 0], [160,73], 5, 0) #ringi joonistamine, asukoht (160, 73), raadius 50 ja täisringi tähistav väärtus 0 
pygame.draw.polygon(screen, [255, 153, 51] , [[150,95], [145,80], [155,80]], 0) #kolmnurga joonistamine
pygame.draw.line(screen,[153, 102, 51], [120,110],[100,150], 5)
pygame.draw.line(screen,[153, 102, 51], [180,110],[200,150], 5)
pygame.draw.circle(screen, [0, 0, 0], [150,140], 3, 0)
pygame.draw.circle(screen, [0, 0, 0], [150,160], 3, 0)
pygame.draw.circle(screen, [0, 0, 0], [150,120], 3, 0)
pygame.draw.rect(screen, [0, 0, 0], [120, 45, 60, 10], 0)
pygame.draw.rect(screen, [0, 0, 0], [130, 10, 40, 45], 0)
pygame.draw.circle(screen, [255, 255, 255], [35,140], 15, 0)
pygame.draw.circle(screen, [255, 255, 255], [55,135], 20, 0)
pygame.draw.circle(screen, [255, 255, 255], [75,140], 15, 0)

pygame.draw.circle(screen, [255, 255, 255], [240,100], 15, 0)
pygame.draw.circle(screen, [255, 255, 255], [220,95], 20, 0)
pygame.draw.circle(screen, [255, 255, 255], [200,100], 15, 0)

pygame.draw.circle(screen, [255, 255, 255], [50,50], 15, 0)
pygame.draw.circle(screen, [255, 255, 255], [70,45], 20, 0)
pygame.draw.circle(screen, [255, 255, 255], [90,50], 15, 0)

pygame.draw.circle(screen, [255, 255, 0], [280,20], 30, 0)
pygame.draw.line(screen,[255, 255, 0], [250,5],[200, 5], 5)
pygame.draw.line(screen,[255, 255, 0], [255,35],[220,60], 5)
pygame.draw.line(screen,[255, 255, 0], [290,55],[290,105], 5)

pygame.draw.line(screen,[102, 51, 0], [205,150],[250,220], 5)

pygame.draw.line(screen,[255, 255, 153], [300,250],[250,220], 5)
pygame.draw.line(screen,[255, 255, 153], [250,270],[250,220], 5)
pygame.draw.line(screen,[255, 255, 153], [275,270],[250,220], 5)







pygame.display.flip() # Mängu akna sisu värskendamine

running = True # Määratakse muutujaga "running" mängu käivitamise staatus
while running: # Peamine mängu tsükkel
    for event in pygame.event.get(): # Otsib kõiki toiminguid, mis mängu aknas on toimunud
        if event.type == pygame.QUIT: # Kui kasutaja sulgeb akna, lõpetatakse mängu tsükkel
            running = False  # Set running to False to exit the loop

    # Mängu akna sisu värskendamine
    pygame.display.flip()

pygame.quit() # Mängu lõpetamine