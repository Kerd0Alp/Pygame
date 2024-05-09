import pygame
pygame.init()

#ekraani seaded
screen = pygame.display.set_mode([640,480])  # Määrame ekraani suuruse
pygame.display.set_caption("Ülesanne2")  # Määrame akna pealkirja
screen.fill([204, 255, 204])  # Täidame ekraani taustavärviga

#Lisame pildid
Shop = pygame.image.load("bg_shop.webp")  # Laeme pildi "bg_shop.webp"
screen.blit(Shop,[0,0])  # Kuvame pildi "bg_shop.webp" ekraanile
Seller = pygame.image.load("seller.webp")  # Laeme pildi "seller.webp"
Seller = pygame.transform.scale(Seller, [230, 320])  # Muudame pildi "seller.webp" suurust
screen.blit(Seller,[110,150])  # Kuvame pildi "seller.webp" ekraanile
Chat = pygame.image.load("chat.webp")  # Laeme pildi "chat.webp"
Chat = pygame.transform.scale(Chat, [250, 190])  # Muudame pildi "chat.webp" suurust
screen.blit(Chat,[250,75])  # Kuvame pildi "chat.webp" ekraanile

# Lisame teksti
font = pygame.font.Font(pygame.font.match_font('arial'), 25)  # Määrame fondi
text = font.render("Tere, olen Kerdo Alp", True, [255,255,255])  # Loome teksti "Tere, olen Kerdo Alp" valge värviga
screen.blit(text, [275,150])  # Kuvame teksti ekraanile

# Lisame Vikk Logo
VikkLogo = pygame.image.load("VIKK logo.png")  # Laeme pildi "VIKK logo.png"
VikkLogo = pygame.transform.scale(VikkLogo, [210, 50])  # Muudame pildi "VIKK logo.png" suurust
screen.blit(VikkLogo,[0,0])  # Kuvame pildi "VIKK logo.png" ekraanile

# Lisame Mõõga pildi
Mõõk = pygame.image.load("Mõõk.png")  # Laeme pildi "Mõõk.png"
Mõõk = pygame.transform.scale(Mõõk, [100, 100])  # Muudame pildi "Mõõk.png" suurust
screen.blit(Mõõk, [530,170])  # Kuvame pildi "Mõõk.png" ekraanile

# Lisame Kooki pildi
kook = pygame.image.load("Kook.png")  # Laeme pildi "Kook.png"
kook = pygame.transform.scale(kook, [100, 100])  # Muudame pildi "Kook.png" suurust
screen.blit(kook, [450,200])  # Kuvame pildi "Kook.png" ekraanile

# Lisa kaarega tekst "TULEVIK 2050"
font = pygame.font.Font(pygame.font.match_font('arial'), 20)  # Määrame fondi
text = font.render("TULEVIK 2050", True, [255, 255, 255])  # Loome teksti "TULEVIK 2050" valge värviga
italic_font = pygame.font.Font(pygame.font.match_font('arial'), 20)  # Määrame kursiivi fondi
italic_font.set_italic(True)  # Aktiveerime kursiivi
text_italic = italic_font.render("TULEVIK 2050", True, [255, 255, 255])  # Loome kursiiviga teksti "TULEVIK 2050" valge värviga
screen.blit(text_italic, [240,20])  # Kuvame kursiiviga teksti ekraanile
pygame.draw.arc(screen,[255,255,255], [220,3,50,45], 0, 3.14*1.5, 5)  # Joonistame kaarega teksti

pygame.display.flip()  # Värskendame akna sisu

running = True  # Määratakse muutujaga "running" mängu käivitamise staatus
while running:  # Peamine mängu tsükkel
    for event in pygame.event.get():  # Otsib kõiki toiminguid, mis mängu aknas on toimunud
        if event.type == pygame.QUIT:  # Kui kasutaja sulgeb akna, lõpetatakse mängu tsükkel
            running = False  # Muudame "running" väärtuseks False, et väljuda tsüklist

    # Mängu akna sisu värskendamine
    pygame.display.flip()

pygame.quit()  # Mängu lõpetamine
