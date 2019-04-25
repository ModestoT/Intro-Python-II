# Class to hold item information

class Item:
  def __init__(self, name, desc):
    self.name = name
    self.desc = desc

  def __repr__(self):
    return ''+self.name+' '+self.desc+''

  def __str__(self):
    return ''+self.name+' '+self.desc+''

  def on_take(self):
    print(f'You added the {self.name} to your inventory!')
  
  def on_drop(self):
    print(f'You dropped the {self.name} onto the floor')