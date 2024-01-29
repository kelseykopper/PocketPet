# Classes relating to game and objects within the game environment.
# @Author Kelsey Kopper

import pygame

class Stats: 
  """ Class to handle representation of Pet stats in-game. """
  def __init__(self, pet_instance):
    self.pet = pet_instance 

  def __str__(self):
    stats = self.pet.name + "'s stats:\n"
    stats += f"  -> days lived: {self.pet.daysLived}\n"
    stats += f"  -> hunger level: {self.pet.hunger}\n"
    stats += f"  -> thirst level: {self.pet.thirst}\n"
    stats += f"  -> cleanliness level: {self.pet.cleanliness}" 

    return stats
  
  def display_ingame(self, game):
    """ Display the pet's stats in game. """

    pet_needs = {
      "Fullness" : self.pet.hunger, 
      "Hydration" : self.pet.thirst, 
      "Hygiene" : self.pet.cleanliness
    }

    font = pygame.font.Font(None, 36)
    text_height = game.height

    for need in pet_needs:
      # render the name of the stat
      text = font.render(need, True, "white")
      text_pos = text.get_rect(bottom=text_height)
      game.screen.blit(text, text_pos)

      # render a bar indicating that stat's percentage 
      bar_height = 15
      full_bar_width = 200
      actual_bar_width = 200 * pet_needs[need]
      bar_outline_pos = pygame.Rect((150, text_pos.top), (full_bar_width, bar_height)) # the bar's outline
      bar_pos = pygame.Rect((150, text_pos.top), (actual_bar_width, bar_height)) # actual stat percentage

      pygame.draw.rect(game.screen, "white", bar_outline_pos, width=2)
      pygame.draw.rect(game.screen, "white", bar_pos)
      text_height -= 25

    # print "days lived" stat outside loop so we don't print a bar with it 
    text = font.render(f"Days lived: {self.pet.daysLived}", True, "white")
    text_pos = text.get_rect(bottom=text_height)
    game.screen.blit(text, text_pos)

class Pet:
  """ A class representing a pet object. """

  # pet instance icons
  ICON_HAPPY = "img/cat.png"
  
  def __init__(self, name):
    self.name = name
    self.daysLived = 0
    self.hunger = 0.25
    self.thirst = 0.25
    self.cleanliness = 0.5

    self.pet_stats = Stats(self)

  def __str__(self):
    return str(self.pet_stats)
  
  def feed(self):
    self.hunger += .25

  def drink(self):
    # 1 represents 100% "capacity"; 0 = died from thirst
    self.thirst = 1 
  
  def clean(self):
    self.cleanliness = 1.0

  def incr_days_lived(self):
    self.daysLived += 1
    
class Button:
  def __init__(self, x, y, width, height, label, action):
    self.x = x
    self.y = y
    self.width = width
    self.height = height 
    self.label = label 
    self.action = action 

  # construct button on screen

class Game: 
  """ A class to represent an instance of the game. """
  ENGAGE_END_GAME = 300000 # if player has survived this long, begin end game


  def __init__(self, screen_width, screen_height):
    # initialize pygame
    pygame.init()
    self.time_elapsed = 0

    self.width = screen_width 
    self.height = screen_height 

     # create game environment
    self.screen = pygame.display.set_mode((screen_width, screen_height))
    self.clock = pygame.time.Clock()
    self.run = True
    self.level = 0


