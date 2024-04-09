import pygame
pygame.init()

screen=pygame.display.set_mode([640,480],pygame.RESIZABLE)
pygame.display.set_caption("My Screen")
screen.fill([204, 255, 255])
pygame.draw.line(screen, [255,0,0], [100,100], [200,200], 2)
pygame.draw.rect(screen, [0, 225, 0], [50, 80, 200, 300], 2)
pygame.draw.circle(screen, [0, 0, 255], [150,200], 100, 1)
pygame.draw.polygon(screen, [255, 0, 255], [[50,50],[100,50],[100,150],[250,50],[350,250],[50,250]], 2)
pygame.draw.ellipse(screen, [0, 225, 0], [50, 80, 200, 300], 2)
pygame.draw.arc(screen,[0,0,0], [100,100,250,200], 0, 3.14*1.5, 1)

running = True # Määratakse muutujaga "running" mängu käivitamise staatus
while running: # Peamine mängu tsükkel
    for event in pygame.event.get(): # Otsib kõiki toiminguid, mis mängu aknas on toimunud
        if event.type == pygame.QUIT: # Kui kasutaja sulgeb akna, lõpetatakse mängu tsükkel
            running = False  # Set running to False to exit the loop

    # Mängu akna sisu värskendamine
    pygame.display.flip()

pygame.quit() # Mängu lõpetamine
