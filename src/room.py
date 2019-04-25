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
    self.items = []
    self.paths = []
    self.monsters = []
  
  def __repr__(self):
    return ''+self.name+' '+self.desc+''

  def __str__(self):
    return ''+self.name+' '+self.desc+''
  
  def addItem(self, item):
    self.items.append(item)
  
  def removeItem(self, item):
    self.items.remove(item)

  def getItems(self):
    items = [str(i.name) for i in self.items]

    res = '   '.join(items)

    return res 

  def checkPaths(self):
    self.paths = [{ "north": self.n_to, "west":self.w_to, "south":self.s_to, "east":self.e_to }]
    routes = []
    for p in self.paths:
      for r in p:
        if p[r] != '':
          routes.append(r)
    
    return routes

  def printPaths(self, paths):
    string = ', '.join(paths)
    
    return string

  def getPaths(self):
    self.paths = [{ "north": self.n_to, "west":self.w_to, "south":self.s_to, "east":self.e_to }]
    routes = []
    for p in self.paths:
      for r in p:
        if p[r] != '':
          routes.append(p[r])

    return routes

  def addMonsters(self, monsters):
    self.monsters = [m for m in monsters]