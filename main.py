import pygame


# the grid (puzzle) has 16 cells (spaces) and 15 tiles (pieces)


class Tile:
    size = 100
    color1 = (255, 0, 0)
    color2 = (255, 255, 255)
    font_name = 'consolas'
    font_size = 42
    font_color = (0, 0, 0)

    def __init__(self, num):
        self.surf = pygame.Surface((self.size, self.size))
        self.surf.fill(self.color1 if num % 2 else self.color2)
        font = pygame.font.SysFont(self.font_name, self.font_size, bold=True)
        text = font.render(str(num), True, self.font_color)  # antialias = True
        rect = text.get_rect()
        rect.center = self.surf.get_rect().center
        self.surf.blit(text, rect)


def draw_grid(tiles, screen):
    tile_size = 100
    offset = 5
    n = 4

    grid_size = (tile_size * n) + (offset * (n - 1))
    grid = pygame.Surface((grid_size, grid_size))

    for i in range(len(tiles)):
        x = (i % n) * (tile_size + offset)
        y = (i // n) * (tile_size + offset)
        grid.blit(tiles[i].surf, (x, y))

    rect = grid.get_rect()
    rect.center = screen.get_rect().center
    screen.blit(grid, rect)


if __name__ == '__main__':
    screen_size = (500, 500)

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(screen_size)

    # tiles = get_tiles()  # create the grid
    tiles = [Tile(i) for i in range(1, 16)]

    run = True
    while run:
        clock.tick(30) # fps

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            elif event.type == pygame.QUIT:
                run = False
        
        draw_grid(tiles, screen)  # draw the grid
        pygame.display.flip()

    pygame.quit()