import pet

def test_init(): 
  """ Tests initialization of Pet object. """
  cat = pet.Pet("Ramsey")
  print(cat)

  dog = pet.Pet("Polly")
  print(dog)

  guineaPig = pet.Pet("Squeaker")
  print(guineaPig)
