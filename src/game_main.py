# # Main driver of game.
# # @Author Kelsey Kopper

import game_classes
import pygame 
import sys 

# create instance of game, pet object
game = game_classes.Game(600, 700)
cat = game_classes.Pet("Ramsey")

while game.run:
  # check for quit
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game.run = False

  # fill screen to wipe away anything from last frame
  game.screen.fill("black")

  if (game.time_elapsed > game.ENGAGE_END_GAME):
    print("put the end game here") 
  else: 
    # game rendering here

    catImage = pygame.image.load(cat.ICON_HAPPY)

    # delete later -- tracks time in game in seconds
    ingame_time = game.time_elapsed // 100

    # draw cat image at center of screen
    # game.screen.blit(catImage, (game.width // 3 - catImage.get_width() // 3, 
    #                           game.height // 3 - catImage.get_height() // 3))
  
    # draw cat's stats on screen

    game_classes.Button(30, 30, 400, 100, "feed", cat.feed())
    
    for object in game_classes.game_objects: 
      object.process(game)

  font = pygame.font.Font(None, 36)
  text = font.render(str(ingame_time), True, "white")
  text_pos = text.get_rect(center=(game.width // 2, game.height // 2))
  game.screen.blit(text, text_pos)

  # put your work on the screen
  pygame.display.flip()

  # limit 120 fps
  game.time_elapsed += 1
  game.clock.tick(120)

pygame.quit()
sys.exit()
