# Tests Pet object methods

import game_classes
import sys

sys.path.append('src/')

import pygame 

def test_needs(): 
  """ Tests need functions (feed, drink, clean) of Pet object. """

  # Arrange
  test_objects = {
    "Ramsey" : game_classes.Pet("Ramsey"),
    "Polly" : game_classes.Pet("Polly")
  }

  # Act
  for obj in test_objects:
    obj.feed()
    obj.clean()
    obj.drink()
  
  # Assert
  for obj in test_objects:
    assert obj.hunger == 0.5
    assert obj.thirst == 0.5
    assert obj.cleanliness == 1.0
