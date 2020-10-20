import pygame


def get_tile_surface(num):
    size = 100
    color1 = (255, 0, 0)
    color2 = (255, 255, 255)

    surf = pygame.Surface((size, size))
    surf.fill(color1 if num % 2 else color2)
    draw_text(surf, num)
    return surf


def draw_text(surface, num):
    name = 'consolas'
    size = 42
    color = (0, 0, 0)

    font = pygame.font.SysFont(name, size, bold=True)
    text = font.render(str(num), True, color)  # antialias = True
    rect = text.get_rect()
    rect.center = surface.get_rect().center
    surface.blit(text, rect)


class Puzzle:
    tile_size = 100
    tile_offset = 5
    size = (tile_size * 4) + (tile_offset * 3)

    def __init__(self):
        self.tiles = [get_tile_surface(i) for i in range(1, 16)]
        self.tiles.append(None)  # add empty space

        self.screen_pos = []
        for i in range(1, 17):
            x = ((i - 1) % 4) * (self.tile_size + self.tile_offset)
            y = ((i - 1) // 4) * (self.tile_size + self.tile_offset)
            self.screen_pos.append((x, y))

        # swap last tile and empty space
        temp = self.tiles[14]
        self.tiles[14] = self.tiles[15]
        self.tiles[15] = temp

    def draw(self, screen):
        surf = pygame.Surface((self.size, self.size))
        for i in range(len(self.tiles)):
            if (self.tiles[i]):
                surf.blit(self.tiles[i], self.screen_pos[i])

        rect = surf.get_rect()
        rect.center = screen.get_rect().center

        screen.blit(surf, rect)


if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((500, 500))

    puzzle = Puzzle()

    run = True
    while run:
        clock.tick(30) # fps

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            elif event.type == pygame.QUIT:
                run = False
        
        puzzle.draw(screen)
        pygame.display.flip()

    pygame.quit()