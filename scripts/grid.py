import numpy as np
import pygame


class Grid:

  def __init__(self, width=100, height=100):
    self.width = width
    self.height = height

    self.cell_width = 1
    self.cell_height = 1

    self.alive_color = (180, 180, 180)
    self.dead_color = (0, 0, 0)

    self.p = 0.1
    self.neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)]

    self.grid = (np.random.rand(self.width, self.height) < self.p).astype(int)

  def update(self):

    neighbor_count = sum(np.roll(self.grid, dir, (0, 1)) for dir in self.neighbors)
    for i in range(self.grid.shape[0]):
      for j in range(self.grid.shape[1]):
       alive = self.grid[i, j]
       neighbors = neighbor_count[i, j]
        # alive and less than two neighbors dies
       if alive and neighbors < 2:
         self.grid[i, j] = 0

       elif alive and neighbors > 3:
         self.grid[i, j] = 0

       elif not alive and neighbors == 3:
         self.grid[i, j] = 1


  def render(self, surf, offset=(0, 0)):

    for i in range(self.grid.shape[0]):
      for j in range(self.grid.shape[1]):

        # position
        left = i * self.cell_width + offset[0]
        top = j * self.cell_height + offset[1]

        color = self.alive_color if self.grid[i, j] else self.dead_color
        rect = (left, top, self.cell_width, self.cell_height)

        pygame.draw.rect(surf, color, rect)