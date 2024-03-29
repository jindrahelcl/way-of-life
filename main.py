import sys
import pygame

from scripts.grid import Grid

class Game:
  def __init__(self):
    pygame.init()
    pygame.display.set_caption("Way of life")

    # create screen and clock
    self.screen = pygame.display.set_mode((640, 480))
    self.display = pygame.Surface((320, 240))
    self.clock = pygame.time.Clock()

    # set up the app layout
    self.grid_update_freq = 1
    self.grid = Grid(320, 240)
    self.grid_update_timer = self.grid_update_freq

  def run(self):
    while True:

      self.grid_update_timer -= 1
      if self.grid_update_timer <= 0:
        self.grid_update_timer = self.grid_update_freq
        self.grid.update()

      self.grid.render(self.display)

      self.handle_input()

      self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
      pygame.display.update()
      self.clock.tick(60)

  def handle_input(self):
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()

if __name__ == "__main__":
  Game().run()