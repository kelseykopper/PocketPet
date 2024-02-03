# # Main driver of game.
# # @Author Kelsey Kopper

from game_classes import *
import pygame 
import sys 
import constant

class Game: 
  """ Represents an instance of the game. """
  def __init__(self):
    # initialize pygame
    pygame.init()
    self.time_elapsed = 0

    self.width = constant.SCREEN_WIDTH 
    self.height = constant.SCREEN_HEIGHT

     # create game environment
    self.screen = pygame.display.set_mode((self.width, self.height))
    self.clock = pygame.time.Clock()
    self.is_running = True
    self.level = 0

    # set window title
    pygame.display.set_caption("Pocket Pet Simulator")

  def run(self):
    """ Function for handling actual game framework. """
    start_time = pygame.time.get_ticks()

    while self.is_running: 

      # check for quit 
      for event in pygame.event.get():
        if event.type == pygame.QUIT: 
          self.is_running = False 

      # fill screen black to wipe away last frame 
      self.screen.fill("black")

      image = pygame.image.load(constant.ICONS["hungry"])

      (image_width, image_height) = image.get_size()

      # Calculate the position for the image to be centered
      image_x = (self.width - image_width) // 2
      image_y = (self.height - image_height) // 2

      self.screen.blit(image, (image_x, image_y))


      # run each object's process function every frame
      for object in game_objects: 
        object.process(self)

      # update display 
      pygame.display.flip()

      # limit 120 fps 
      self.time_elapsed += 1
      self.clock.tick(120)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
  # create instance of game, pet object
  game = Game()
  cat = Pet("Ramsey")

  # establish other objects for game 
  need_buttons = {
    "feed" : Button(0, 0, 600, 40, "Feed", cat.feed),
    "drink" : Button(0, 40, 600, 40, "Drink", cat.drink),
    "clean" : Button(0, 80, 600, 40, "Clean litter box", cat.clean)
  }

  notifications = {
    "dead" : "Your Pocket Pet has died. You are a terrible owner.",
    "overfed" : "Your Pocket Pet is already full."
  }

  game.run()

