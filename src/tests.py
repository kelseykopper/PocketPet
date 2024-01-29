# Tests for classes, mechanics of game

import game_classes
import sys

def test_init(): 
  """ Tests initialization of Pet object. """
  cat = game_classes.Pet("Ramsey")
  print(cat)

  dog = game_classes.Pet("Polly")
  print(dog)

  guineaPig = game_classes.Pet("Squeaker")
  print(guineaPig)

test_init()
sys.exit()