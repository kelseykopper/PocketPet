# Classes relating to game and objects within the game environment.
# @Author Kelsey Kopper

import pygame
import constant

# any object that might be shown on screen, ex. stats display, buttons, pet object, etc
game_objects = []

class Stats: 
  """ Class to handle representation of Pet stats in-game. """
  def __init__(self, pet_instance):
    self.pet = pet_instance 
    game_objects.append(self)

  def __str__(self):
    stats = self.pet.name + "'s stats:\n"
    stats += f"  -> days lived: {self.pet.daysLived}\n"
    stats += f"  -> hunger level: {self.pet.hunger}\n"
    stats += f"  -> thirst level: {self.pet.thirst}\n"
    stats += f"  -> hygiene level: {self.pet.hygiene}" 

    return stats
  
  def process(self, game):
    """ Display the pet's stats in game. """

    pet_needs = {
      "Fullness" : self.pet.hunger, 
      "Hydration" : self.pet.thirst, 
      "Hygiene" : self.pet.hygiene
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
      full_bar_width = 400
      actual_bar_width = 400 * pet_needs[need]
      bar_outline_pos = pygame.Rect((150, text_pos.top), (full_bar_width, bar_height)) # the bar's outline
      bar_pos = pygame.Rect((150, text_pos.top), (actual_bar_width, bar_height)) # actual stat percentage

      pygame.draw.rect(game.screen, "white", bar_outline_pos, width=2)
      pygame.draw.rect(game.screen, "white", bar_pos)
      text_height -= 25

    # print "days lived" stat outside loop so we don't print a bar with it 
    text = font.render(f"Days lived: {int(self.pet.daysLived)}", True, "white")
    text_pos = text.get_rect(bottom=text_height)
    game.screen.blit(text, text_pos)

class Pet:
  """ A class representing a pet object. """
  
  def __init__(self, name):
    self.name = name
    self.daysLived = 0
    self.hunger = 0.25
    self.thirst = 0.25
    self.hygiene = 0.5

    self.pet_stats = Stats(self)
    game_objects.append(self)

  def __str__(self):
    return str(self.pet_stats)
  
  def feed(self):
    self.hunger += .25
    if (self.hunger) > constant.MAX_NEED_LEVEL:
      self.hunger = constant.MAX_NEED_LEVEL

  def drink(self):
    self.thirst = constant.MAX_NEED_LEVEL
  
  def clean(self):
    self.hygiene = constant.MAX_NEED_LEVEL

  def is_alive(self):
    """ Pet will die if any one need reaches 0. """
    if self.hunger <= 0 or self.thirst <= 0 or self.hygiene <= 0: 
      print("pet is dead")
      return False 
    else:
      print("pet is alive")
      return True 
    
  def decay_needs(self):
    """ Needs should decay .01 every frame. """
    self.hygiene -= constant.NEED_DECAY_RATE
    if self.hygiene < 0:
        self.hygiene = 0

    self.hunger -= constant.NEED_DECAY_RATE
    if self.hunger < 0:
      self.hunger = 0

    self.thirst -= constant.NEED_DECAY_RATE
    if self.thirst < 0: 
      self.thirst = 0

    # also reflect time passing here 
    self.daysLived += constant.DAY_INCR_RATE
    
  def get_mood(self):
    """ TODO: Return the appropriate pet icon for the pet's mood. """
    pass

  def process(self, game):
    """ Update the pet's icon every frame. """
    self.decay_needs()

    if not self.is_alive():
      death_notif = Popup("Your Pocket Pet has died. You are a terrible owner.")
      death_notif.display(game)
    # icon = pygame.image.load(constant.ICON_HAPPY)
    # game.screen.blit(icon, (0, 0))
    
class Button:
  """ Class to represent on-screen buttons.
      @author Maxim Maedem, https://thepythoncode.com/article/make-a-button-using-pygame-in-python """
  def __init__(self, x, y, width, height, label, action=None):
    self.x = x
    self.y = y
    self.width = width
    self.height = height 
    self.label = label 
    self.action = action 

    self.alreadyPressed = False 
    self.onePress = False

    # construct button box
    self.buttonSurface = pygame.Surface((self.width, self.height))
    self.box = pygame.Rect(self.x, self.y, self.width, self.height)

    # construct text on box
    self.font = pygame.font.Font(None, 36)
    self.textSurface = self.font.render(label, True, "white")

    # append to objects list
    game_objects.append(self)
    
    # colors of button background
    self.colors = {
      'normal' : '#1f1f1f',
      'hover' : '#363636'
    }

  def process(self, game):
    """ Checks if the button has been pressed and if so, runs action function. """
    mousePos = pygame.mouse.get_pos()
    self.buttonSurface.fill(self.colors['normal'])

    if self.box.collidepoint(mousePos):
      self.buttonSurface.fill(self.colors['hover'])

      # check if left click (1 mouse press = 1 action ONLY)
      if pygame.mouse.get_pressed(num_buttons=3)[0]: 
        if self.onePress:
          self.action()
        elif not self.alreadyPressed:
          self.action()
          self.alreadyPressed = True 
      else: 
        self.alreadyPressed = False

    # align text to center of button box and display on screen
    self.buttonSurface.blit(self.textSurface, [
      self.box.width/2 - self.textSurface.get_rect().width/2,
      self.box.height/2 - self.textSurface.get_rect().height/2
        ])
    game.screen.blit(self.buttonSurface, self.box)

class Popup: 
  """ Represents any kind of popup in-game message.
      Duration = duration for message to display on screen, in milliseconds.
       Defaults to -1 and displays message indefinitely.
  """
  def __init__(self, msg, duration=-1):
    self.msg = msg 
    self.duration = duration 

   # TODO: fix this shit
  def display(self, game, start_time=pygame.time.get_ticks()):
    """ Display the popup on screen. Start time defaults to time at function call. """

    def word_wrap():
      """ Helper function to break message up into a list of words """
       # split the message into words
    #   words = self.msg.split(' ')
    #   lines = []
    #   current_line = ""
      
    #   # Word wrapping logic
    #   for word in words:
    #       test_line = current_line + word + " "
    #       text_width, text_height = font.size(test_line)
    #       if text_width <= constant.SCREEN_WIDTH:
    #           current_line = test_line
    #       else:
    #           lines.append(current_line)
    #           current_line = word + " "
      
    #   if current_line:
    #       lines.append(current_line)

    #   return lines

    # current_time = pygame.time.get_ticks() 
    # lines = word_wrap()
    # text_height = constant.SCREEN_HEIGHT
    # font = pygame.font.Font(None, 36)

    # if (self.duration == -1) or (current_time - start_time < self.duration):
    #   # Calculate the total height of the text block
    #   total_text_height = len(lines) * text_height
      
    #   # Display each line of text
    #   y = (constant.SCREEN_HEIGHT - total_text_height) / 2  # Starting y position for centered text
    #   for line in lines:
    #       text = font.render(line, True, "white")
    #       text_width, _ = font.size(line)
    #       x = (constant.SCREEN_WIDTH - text_width) / 2  # Center each line
    #       game.screen.blit(text, (x, y))
    #       y += text_height  # Move to the next line

      font = pygame.font.Font(None, 36)
      text = font.render(self.msg, True, "white")
      text_pos = text.get_rect(left=225)
      game.screen.blit(text, text_pos)



