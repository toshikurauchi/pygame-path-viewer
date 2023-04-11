import sys

import pygame

from loader import load_data
from constants import BLOCK_WIDTH, BLOCK_HEIGHT
from graphics import draw_maze, draw_breadcrumb


data_path = 'exemplo.txt'
if len(sys.argv) > 1:
    data_path = sys.argv[1]

maze, path = load_data(data_path)

pygame.init()
window = pygame.display.set_mode(
    (
        len(maze[0]) * BLOCK_WIDTH, 
        len(maze) * BLOCK_HEIGHT,
    )
)

simulation_on = True
path_index = 0
while simulation_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            simulation_on = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                path_index += 1
                if path_index >= len(path):
                    simulation_on = False
    
    draw_maze(window, maze)
    for cur, (i, j) in enumerate(path[:path_index + 1]):
        draw_breadcrumb(window, j, i, cur == path_index)
    
    pygame.display.update()
