import pygame, random
pygame.init()

# Ekraani seaded
ekraani_laius = 640
ekraani_kõrgus = 480
ekraan = pygame.display.set_mode([ekraani_laius, ekraani_kõrgus])  # Loome mänguakna
pygame.display.set_caption("Ping-Pong")  # Määrame mänguakna pealkirja
kell = pygame.time.Clock()  # Loome kella objekti, et reguleerida mängu värskendussagedust

# Lae pildid
palli_pilt = pygame.image.load("ball.webp")  # Laeme palli pildi
palli_pilt = pygame.transform.scale(palli_pilt, (30, 30))  # Muudame palli pildi suurust

alus_pilt = pygame.image.load("paddle.webp")  # Laeme aluse pildi
alus_pilt = pygame.transform.scale(alus_pilt, (120, 20))  # Muudame aluse pildi suurust

# Palli seaded
palli_rect = palli_pilt.get_rect()  # Loome palli ristküliku objekti
palli_rect.x = random.randint(palli_rect.width, ekraani_laius - palli_rect.width)  # Määrame palli algse x-koordinaadi
palli_rect.y = random.randint(palli_rect.height, ekraani_kõrgus - palli_rect.height)  # Määrame palli algse y-koordinaadi
palli_kiirusX = 3  # Määrame palli algse horisontaalse kiiruse
palli_kiirusY = 4  # Määrame palli algse vertikaalse kiiruse

# Aluse seaded
alus_rect = alus_pilt.get_rect()  # Loome aluse ristküliku objekti
alus_rect.x = ekraani_laius // 2 - alus_rect.width // 2  # Määrame aluse x-koordinaadi, et see oleks ekraani keskel
alus_rect.y = ekraani_kõrgus // 1.5  # Määrame aluse y-koordinaadi

alus_kiirus = 5  # Määrame aluse liikumiskiiruse

# Muutujad skoori jälgimiseks
mängija_skoor = 0  # Mängija skoor
vastase_skoor = 0  # Vastase skoor
eelmine_skoor = mängija_skoor  # Eelmine skoor mängija jaoks, et kontrollida, kas skoor on muutunud

# Font ja teksti seaded
font = pygame.font.Font(None, 36)  # Loome fondi objekti teksti renderdamiseks
valge = (255, 255, 255)  # Määrame valge värvi RGB koodi

# Mängu põhiloop
mäng_läbi = False  # Muutuja, mis näitab, kas mäng on lõppenud või mitte
while not mäng_läbi:
    kell.tick(60)  # Reguleerime mängu värskendussagedust 60 kaadrit sekundis
    for sündmus in pygame.event.get():  # Kontrollime mängusündmusi
        if sündmus.type == pygame.QUIT:  # Kui kasutaja vajutab mänguakna sulgemisnuppu
            mäng_läbi = True  # Lõpetame mängu

    # Aluse liikumine
    klahvid = pygame.key.get_pressed()  # Kontrollime, milliseid klahve kasutaja vajutab
    if klahvid[pygame.K_LEFT]:  # Kui kasutaja vajutab vasakule nooleklahvi
        alus_rect.x -= alus_kiirus  # Liigutame alust vasakule
    if klahvid[pygame.K_RIGHT]:  # Kui kasutaja vajutab paremale nooleklahvi
        alus_rect.x += alus_kiirus  # Liigutame alust paremale

    # Palli liikumine
    palli_rect.x += palli_kiirusX  # Liigutame palli horisontaalselt
    palli_rect.y += palli_kiirusY  # Liigutame palli vertikaalselt

    # Palli põrkumine seintest
    if palli_rect.left <= 0 or palli_rect.right >= ekraani_laius:  # Kui pall puudutab mängu vasakut või paremat serva
        palli_kiirusX = -palli_kiirusX  # Pöörame palli liikumissuuna vastupidiseks
    if palli_rect.top <= 0:  # Kui pall puudutab mängu ülemist serva
        palli_kiirusY = -palli_kiirusY  # Pöörame palli liikumissuuna vastupidiseks
    if palli_rect.bottom >= ekraani_kõrgus:  # Kui pall puudutab mängu alumist serva
        mängija_skoor -= 1  # Vähendame mängija skoori
        palli_rect.x = random.randint(palli_rect.width, ekraani_laius - palli_rect.width)  # Määrame palli uue x-koordinaadi
        palli_rect.y = 0  # Määrame palli uue y-koordinaadi

    # Kokkupõrge alusega
    if palli_rect.colliderect(alus_rect):  # Kui pall puudutab alust
        if palli_kiirusY > 0:  # Kui pall liigub allapoole
            palli_kiirusY = -palli_kiirusY  # Pöörame palli liikumissuuna vastupidiseks
            mängija_skoor += 1  # Suurendame mängija skoori

            # Reguleeri palli nurka vastavalt sellele, kuhu alus tabab
            suhteline_lõikepunkt_x = (alus_rect.x + alus_rect.width / 2) - (palli_rect.x + palli_rect.width / 2)
            normaliseeritud_lõikepunkt_x = suhteline_lõikepunkt_x / (alus_rect.width / 2)
            palli_kiirusX = normaliseeritud_lõikepunkt_x * 8

            # Piira palli maksimaalne kiirus
            if abs(palli_kiirusX) > 8:
                palli_kiirusX = 8 if palli_kiirusX > 0 else -8

    # Palli kaotus ekraani alt
    if palli_rect.top >= ekraani_kõrgus:  # Kui pall puudutab mängu alumist serva
        vastase_skoor -= 1  # Vähendame vastase skoori
        palli_rect.x = random.randint(palli_rect.width, ekraani_laius - palli_rect.width)  # Määrame palli uue x-koordinaadi
        palli_rect.y = 0  # Määrame palli uue y-koordinaadi

    # Kontrolli, kas mäng on läbi
    if mängija_skoor >= 20 or vastase_skoor >= 20:  # Kui mängija või vastane saavutab 20 punkti
        mäng_läbi = True  # Lõpetame mängu

    # Uuenda ekraani
    ekraan.fill((153, 204, 255))  # Täidame ekraani helesinise värviga
    ekraan.blit(alus_pilt, alus_rect)  # Kuvame aluse pildi
    ekraan.blit(palli_pilt, palli_rect)  # Kuvame palli pildi

    # Uuenda teksti ekraanil
    skoori_tekst = font.render("Mängija Skoor: " + str(mängija_skoor), True, valge)  # Loome teksti mängija skoori jaoks
    ekraan.blit(skoori_tekst, (10, 10))  # Kuvame mängija skoori ülemises nurgas

    pygame.display.flip()  # Värskendame ekraani

# Mäng läbi
print("Mäng Läbi")
print("Mängija Skoor:", mängija_skoor)  # Trükime mängija skoori

pygame.quit()  # Sulgeme pygame'i
