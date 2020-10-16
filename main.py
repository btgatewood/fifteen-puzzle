import pygame


def get_tile_surface(index):
    tile_size = 50
    tile_color = (255, 255, 255)
    font_name = 'consolas'
    font_size = 24
    font_color = (0, 0, 0)

    tile = pygame.Surface((tile_size, tile_size))
    tile.fill(tile_color)
    font = pygame.font.SysFont(font_name, font_size, bold=True)
    text = font.render(str(index), True, font_color)  # what is True?!
    rect = text.get_rect()
    rect.center = tile.get_rect().center
    tile.blit(text, (rect.x, rect.y))

    return tile


if __name__ == '__main__':
    screen_size = (500, 500)

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(screen_size)

    # TODO: Create the grid.
    tile = get_tile_surface(15)

    run = True
    while run:
        clock.tick(30)  # fps

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            elif event.type == pygame.QUIT:
                run = False

        screen.blit(tile, (100, 100))
        pygame.display.flip()

    pygame.quit()