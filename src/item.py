# Class to hold item information

class Item:
  def __init__(self, name, desc):
    self.name = name
    self.desc = desc

  def __repr__(self):
    return ''+self.name+'\n'+self.desc+''

  def __str__(self):
    return ''+self.name+'\n'+self.desc+''