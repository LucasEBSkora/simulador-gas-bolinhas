from math import sqrt

class Vetor:

  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

  def __str__(self):
    return "(" + str(self.x) + "," + str(self.y) + str(",") + str(self.z) + ")"
  
  def __add__(self, outro):
    return Vetor(self.x + outro.x, self.y + outro.y, self.z + outro.z)

  def __sub__(self, outro):
    return Vetor(self.x - outro.x, self.y - outro.y, self.z - outro.z)

  def __mul__(self, outro):
    if (isinstance(outro, Vetor)):
      return (self.x * outro.x) + (self.y * outro.y) + (self.z * outro.z)
    else :
      return Vetor(self.x * outro, self.y * outro, self.z * outro)

  def modulo(self):
    return sqrt((self.x**2) + (self.y**2) + (self.z**2))
  
  def versor(self):
    return self*(1/self.modulo())
  
  def projecao_ortogonal(self, outro): 
    return outro*(self*outro/(outro*outro))

  def como_tupla(self):
    return (self.x, self.y, self.z)

