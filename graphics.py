import pygame

from constants import BLOCK_WIDTH, BLOCK_HEIGHT


def draw_maze(window, maze):
    for i, row in enumerate(maze):
        for j, block in enumerate(row):
            if block == '#':
                pygame.draw.rect(
                    window, 
                    (0, 0, 0), 
                    (
                        j * BLOCK_WIDTH, 
                        i * BLOCK_HEIGHT, 
                        BLOCK_WIDTH, 
                        BLOCK_HEIGHT,
                    )
                )
            elif block == '.':
                pygame.draw.rect(
                    window, 
                    (255, 255, 255), 
                    (
                        j * BLOCK_WIDTH, 
                        i * BLOCK_HEIGHT, 
                        BLOCK_WIDTH, 
                        BLOCK_HEIGHT,
                    )
                )


def draw_breadcrumb(window, x, y, is_current):
    if is_current:
        color = (255, 0, 0)
    else:
        color = (0, 0, 255)
    
    pygame.draw.circle(
        window, 
        color,
        (x * BLOCK_WIDTH + BLOCK_WIDTH // 2, y * BLOCK_HEIGHT + BLOCK_HEIGHT // 2),
        BLOCK_WIDTH // 4,
    )