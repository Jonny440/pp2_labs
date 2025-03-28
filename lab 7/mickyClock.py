import pygame
import time
import math

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

background = pygame.image.load("mickey_face.png")
minute_hand = pygame.image.load("right_hand.png")
second_hand = pygame.image.load("left_hand.png")

bg_center = (WIDTH // 2, HEIGHT // 2)

def rotate_hand(image, angle, center):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=center)
    return rotated_image, new_rect.topleft

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    minute_angle = -(minutes * 6)
    second_angle = -(seconds * 6)

    rotated_minute, min_pos = rotate_hand(minute_hand, minute_angle, bg_center)
    rotated_second, sec_pos = rotate_hand(second_hand, second_angle, bg_center)

    screen.blit(rotated_minute, min_pos)
    screen.blit(rotated_second, sec_pos)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(1000)

pygame.quit()
