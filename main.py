import pygame


def get_tile_surface(index):
    tile_size = 100
    tile_color1 = (255, 255, 255)
    tile_color2 = (255, 0, 0)
    font_name = 'consolas'
    font_size = 42
    font_color = (0, 0, 0)

    tile = pygame.Surface((tile_size, tile_size))
    if (index % 2):
        pygame.draw.rect(tile, (tile_color1), tile.get_rect())
    else:
        pygame.draw.rect(tile, (tile_color2), tile.get_rect())
    font = pygame.font.SysFont(font_name, font_size, bold=True)
    text = font.render(str(index), True, font_color)  # what is True?!
    rect = text.get_rect()
    rect.center = tile.get_rect().center
    tile.blit(text, rect)
    return tile


def get_tiles():
    # could this be a list comprehension?
    tiles = []
    for i in range(1, 16):
        tiles.append(get_tile_surface(i))
    return tiles


def draw_grid(tiles, screen):
    tile_size = 100
    offset = 5
    n = 4

    grid_size = (tile_size * n) + (offset * (n - 1))
    grid = pygame.Surface((grid_size, grid_size))

    for i in range(len(tiles)):
        x = (i % n) * (tile_size + offset)
        y = (i // n) * (tile_size + offset)
        grid.blit(tiles[i], (x, y))

    rect = grid.get_rect()
    rect.center = screen.get_rect().center
    screen.blit(grid, rect)


if __name__ == '__main__':
    screen_size = (500, 500)

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(screen_size)

    tiles = get_tiles()

    run = True
    while run:
        clock.tick(30) # fps

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            elif event.type == pygame.QUIT:
                run = False
        
        draw_grid(tiles, screen)
        pygame.display.flip()

    pygame.quit()