import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    color = (0, 0, 255)
    points = []
    draw_mode = 'line'  # line, rect, circle, erase

    start_pos = None

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_r:
                    color = (255, 0, 0)
                elif event.key == pygame.K_g:
                    color = (0, 255, 0)
                elif event.key == pygame.K_b:
                    color = (0, 0, 255)
                elif event.key == pygame.K_1:
                    color = (255, 0, 0)
                elif event.key == pygame.K_2:
                    color = (0, 255, 0)
                elif event.key == pygame.K_3:
                    color = (0, 0, 255)
                elif event.key == pygame.K_e:
                    draw_mode = 'erase'
                elif event.key == pygame.K_c:
                    draw_mode = 'circle'
                elif event.key == pygame.K_l:
                    draw_mode = 'line'
                elif event.key == pygame.K_r:
                    draw_mode = 'rect'
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if draw_mode == 'rect':
                        rect = pygame.Rect(event.pos[0] - 25, event.pos[1] - 25, 50, 50)
                        pygame.draw.rect(screen, color, rect, width=radius)
                    elif draw_mode == 'circle':
                        pygame.draw.circle(screen, color, event.pos, 30, width=radius)
                    elif draw_mode == 'erase':
                        pygame.draw.circle(screen, (0, 0, 0), event.pos, radius)
                    elif draw_mode == 'line':
                        points = points + [event.pos]
                        points = points[-256:]
                elif event.button == 3:
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                if event.buttons[0]:
                    if draw_mode == 'erase':
                        pygame.draw.circle(screen, (0, 0, 0), event.pos, radius)
                    elif draw_mode == 'line':
                        points = points + [event.pos]
                        points = points[-256:]

        if draw_mode == 'line':
            i = 0
            while i < len(points) - 1:
                drawLineBetween(screen, i, points[i], points[i + 1], radius, color)
                i += 1

        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = i / iterations
        x = int(start[0] * (1 - progress) + end[0] * progress)
        y = int(start[1] * (1 - progress) + end[1] * progress)
        pygame.draw.circle(screen, color, (x, y), width)

main()
