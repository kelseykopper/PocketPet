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
    
cat = Pet("Ramsey")
print(cat)