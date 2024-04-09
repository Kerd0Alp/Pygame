import pygame
pygame.init()
#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Ülesanne2")
screen.fill([204, 255, 204])

#Lisame pildid
Shop = pygame.image.load("bg_shop.webp")
screen.blit(Shop,[0,0])
Seller = pygame.image.load("seller.webp")
Seller = pygame.transform.scale(Seller, [230, 320])
screen.blit(Seller,[110,150])
Chat = pygame.image.load("chat.webp")
Chat = pygame.transform.scale(Chat, [250, 190])
screen.blit(Chat,[250,75])
font = pygame.font.Font(pygame.font.match_font('arial'), 25)
text = font.render("Tere, olen Kerdo Alp", True, [255,255,255])
screen.blit(text, [275,150])
pygame.display.flip()

running = True # Määratakse muutujaga "running" mängu käivitamise staatus
while running: # Peamine mängu tsükkel
    for event in pygame.event.get(): # Otsib kõiki toiminguid, mis mängu aknas on toimunud
        if event.type == pygame.QUIT: # Kui kasutaja sulgeb akna, lõpetatakse mängu tsükkel
            running = False  # Set running to False to exit the loop

    # Mängu akna sisu värskendamine
    pygame.display.flip()

pygame.quit() # Mängu lõpetamine