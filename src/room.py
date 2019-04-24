# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, desc):
    self.name = name
    self.desc = desc
    self.n_to = ''
    self.s_to = ''
    self.w_to = ''
    self.e_to = ''
  
  def __repr__(self):
    return ''+self.name+': '+self.desc+''

  def __str__(self):
    return ''+self.name+': '+self.desc+''