import pygame


if __name__ == '__main__':
    pygame.init()
    size = (360, 640)
    screen = pygame.display.set_mode(size)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            elif event.type == pygame.QUIT:
                run = False

    pygame.quit()