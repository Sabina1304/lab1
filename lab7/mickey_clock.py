import pygame
import math
import datetime

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Mickey Clock")
clock = pygame.time.Clock()

def draw_hand(surface, angle, length, width, color):
    end_x = 200 + length * math.sin(math.radians(angle))
    end_y = 200 - length * math.cos(math.radians(angle))
    pygame.draw.line(surface, color, (200, 200), (end_x, end_y), width)

running = True
while running:
    screen.fill((255, 255, 255))
    now = datetime.datetime.now()
    minute_angle = now.minute * 6
    second_angle = now.second * 6

    # Микки правая рука (минутная)
    draw_hand(screen, minute_angle, 80, 8, (0, 0, 0))
    # Микки левая рука (секундная)
    draw_hand(screen, second_angle, 120, 4, (255, 0, 0))

    pygame.draw.circle(screen, (0, 0, 0), (200, 200), 10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
