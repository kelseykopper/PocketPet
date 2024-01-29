import pygame

class Pet:
  """ A class representing a pet object. """
  
  def __init__(self, name):
    self.name = name
    self.daysLived = 0
    self.hunger = 0.5
    self.satisfaction = 0.5

  def __str__(self):
    stats = self.name + "'s stats:\n"
    stats += f"  -> days lived: {self.daysLived}\n"
    stats += f"  -> hunger level: {self.hunger}\n"
    stats += f"  -> satisfaction level: {self.satisfaction}" 

    return stats
  
  def feed(self):
    self.hunger -= 0.25
  
  def play(self):
    self.satisfaction += .25

  def incr_days_lived(self):
    self.daysLived += 1
  
  def is_dead(self):
    if self.hunger == 0 or self.satisfaction == 0:
      return True 
    else:
      return False

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
run = True

while run:
  # check for quit
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  # fill screen to wipe away anything from last frame
  screen.fill("white")

  # game rendering here
  pygame.draw.polygon(screen, "black", [(300, 25), (100, 400), (500, 500)], 4)
  catImage = pygame.image.load("lib/cat.png")

  # put your work on the screen
  pygame.display.flip()

  # limit 120 fps
  clock.tick(120)

pygame.quit()
