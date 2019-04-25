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
    item.on_take()
    self.inventory.append(item)

  def removeItem(self, item):
    if item in self.inventory:
      self.inventory.remove(item)
      item.on_drop()
    else:
      print("You don't have that item")
      return False

  def getInventory(self):
    inventory = [str(i.name) for i in self.inventory]

    res = '   '.join(inventory)

    return res 