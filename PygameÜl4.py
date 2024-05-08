import pygame
import random

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLUE_CAR_SPEED = 5

class Car(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

def game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Car Game")
    background = pygame.image.load("bg_rally.jpg").convert()

    all_sprites = pygame.sprite.Group()
    blue_cars = pygame.sprite.Group()

    red_car = Car("f1_red.png", SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT - 50)
    all_sprites.add(red_car)

    running = True
    clock = pygame.time.Clock()
    score = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if random.randint(0, 100) < 2:
            blue_car = Car("f1_blue.png", random.randint(120, 470 - 20), random.randint(-500, -50))
            all_sprites.add(blue_car)
            blue_cars.add(blue_car)

        for blue_car in blue_cars:
            blue_car.rect.y += BLUE_CAR_SPEED
            if blue_car.rect.y > SCREEN_HEIGHT:
                blue_car.kill()
                score += 1

        collisions = pygame.sprite.spritecollide(red_car, blue_cars, True)
        if collisions:
            score += len(collisions)

        screen.blit(background, (0, 0))
        all_sprites.draw(screen)

        font = pygame.font.Font(None, 36)
        score_text = font.render("Score: " + str(score), True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    game()
