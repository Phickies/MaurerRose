import sys
import math
import pygame

n = 0
d = 0
color1 = pygame.Color(255, 255, 255)
color2 = pygame.Color(255, 0, 0)

pygame.init()
window_size = (800, 800)
pygame.display.set_caption("Maurer Rose Example")

screen = pygame.display.set_mode(window_size, pygame.HWSURFACE | pygame.DOUBLEBUF & pygame.SRCALPHA)
clock = pygame.time.Clock()

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    # Drawing the maurerRose
    points = []
    for i in range(361):
        k = i * d
        radius = 200 * math.sin(math.radians(n * k))
        radians_angle = math.radians(k)
        x = radius * math.cos(radians_angle) + screen.get_width() / 2
        y = radius * math.sin(radians_angle) + screen.get_height() / 2
        points.append((x, y))

    # Drawing another less complicated line
    another_points = []
    for i in range(361):
        k = i
        radius = 200 * math.sin(math.radians(n * k))
        radians_angle = math.radians(k)
        x = radius * math.cos(radians_angle) + screen.get_width() / 2
        y = radius * math.sin(radians_angle) + screen.get_height() / 2
        another_points.append((x, y))

    # Display the draw
    for i in range(len(points)-1):
        if i+1 == len(points)-1:
            i = 0
        pygame.draw.line(screen, color1, points[i], points[i+1], 1)
        pygame.draw.line(screen, color2, another_points[i], another_points[i + 1], 2)

    # Animation by time
    if n < 100:
        n += 0.001
    else:
        n -= 0.001
    if d < 100:
        d += 0.003
    else:
        d -= 0.001

    pygame.display.flip()
    clock.tick(60)
