class Monster:
  def __init__(self, name, attack, defense, health):
    self.name = name
    self.attack = attack
    self.defense = defense
    self.health = health

  def __repr__(self):
    return f'Name: '+self.name+'\nAttack: '+str(self.attack)+'\nDefense: '+str(self.defense)+'\nHealth: '+str(self.health)+''

  def __str__(self):
    return f'Name: '+self.name+'\nAttack: '+str(self.attack)+'\nDefense: '+str(self.defense)+'\nHealth: '+str(self.health)+''