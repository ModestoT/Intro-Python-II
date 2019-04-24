# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, current_room):
    self.name = name
    self.current_room = current_room
    self.inventory = []

  def __repr__(self):
    return ''+self.name+''

  def __str__(self):
    return ''+self.name+''

  def addItem(self, item):
    self.inventory.append(item)