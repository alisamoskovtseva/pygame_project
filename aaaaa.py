import pygame

pygame.font.init()
screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("SUDOKU SOLVER USING BACKTRACKING")
img = pygame.image.load('судоку.jpg')
pygame.display.set_icon(img)
dif = 550 / 9


class Board:
    def __init__(self, width, height, left=5, top=5, cell_size=60):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 0
        self.top = 0
        self.cell_size = 0
        self.set_view(left, top, cell_size)

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        left, top = self.left, self.top
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, (255, 255, 255), ((left, top), (self.cell_size, self.cell_size)), 1)
                left += self.cell_size
            top += self.cell_size
            left = self.left
        for i in range(10):
            if i % 3 == 0:
                thick = 7
            else:
                thick = 0
            pygame.draw.line(screen, (255, 255, 255), (0, i * dif), (550, i * dif), thick)
            pygame.draw.line(screen, (255, 255, 255), (i * dif, 0), (i * dif, 550), thick)

    # def get_cell(self, mouse_pos):
    # x = (mouse_pos[1] - self.top) // self.cell_size
    # y = (mouse_pos[0] - self.top) // self.cell_size
    # if 0 <= x <= self.height and 0 <= y <= self.width:
    # return x, y
    # return None

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def on_click(self, cell_coords):
        print(cell_coords)

    def get_cell(self, mouse_pos):
        if self.left <= mouse_pos[1] < self.left + self.height * self.cell_size and self.top <= mouse_pos[
            0] < self.top + self.width * self.cell_size:
            return int((mouse_pos[1] - self.left) / self.cell_size), int((mouse_pos[0] - self.top) / self.cell_size)
        else:
            return None

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell != None:
            self.on_click(cell)
        if cell == None:
            print(cell)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 550, 600
    screen = pygame.display.set_mode(size)
    running = True
    fps = 60
    clock = pygame.time.Clock()
    board = Board(9, 9)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)

        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
