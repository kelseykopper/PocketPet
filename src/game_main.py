# # Main driver of game.
# # @Author Kelsey Kopper

from game_classes import *
import pygame 
import sys 
import constant

# create instance of game, pet object
game = Game()
cat = Pet("Ramsey")

# establish other objects for game 
need_buttons = {
  "feed" : Button(0, 0, 200, 40, "Feed", cat.feed),
  "drink" : Button(0, 40, 200, 40, "Drink", cat.drink),
  "clean" : Button(0, 80, 200, 40, "Clean litter box", cat.clean)
}

while game.run:
  # check for quit
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game.run = False

  # fill screen to wipe away anything from last frame
  game.screen.fill("black")

  # if (game.time_elapsed > game.ENGAGE_END_GAME):
  #   print("put the end game here") 
  # else: 
  #   # game rendering here

  #   catImage = pygame.image.load(cat.ICON_HAPPY)

  #   # delete later -- tracks time in game in seconds
  #   ingame_time = game.time_elapsed // 100

  #   # draw cat image at center of screen
  #   # game.screen.blit(catImage, (game.width // 3 - catImage.get_width() // 3, 
  #   #                           game.height // 3 - catImage.get_height() // 3))
  
  #   # draw cat's stats on screen

  #   game_classes.Button(30, 30, 400, 100, "feed", cat.feed())
    
  # run processes every frame 
  for object in game_objects: 
    object.process(game)

  # font = pygame.font.Font(None, 36)
  # text = font.render(str(ingame_time), True, "white")
  # text_pos = text.get_rect(center=(game.width // 2, game.height // 2))
  # game.screen.blit(text, text_pos)

  # put your work on the screen
  pygame.display.flip()

  # limit 120 fps
  game.time_elapsed += 1
  game.clock.tick(120)

pygame.quit()
sys.exit()
