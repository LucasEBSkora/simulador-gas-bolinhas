from math import sqrt

class Vetor:

  def __init__(self, x, y, z):
    self.coords = [x, y, z]

  def x(self, arg):
    self.coords[0] = arg
    
  def x(self):
      return self.coords[0]

  def y(self, arg):
    self.coords[1] = arg
    
  def y(self):
      return self.coords[1]

  def z(self, arg):
    self.coords[2] = arg
    
  def z(self):
      return self.coords[2]


  def __str__(self):
    return "(" + str(self.coords[0]) + "," + str(self.coords[1]) + str(",") + str(self.coords[2]) + ")"
  
  def __add__(self, outro):
    return Vetor(self.coords[0] + outro.coords[0], self.coords[1] + outro.coords[1], self.coords[2] + outro.coords[2])

  def __sub__(self, outro):
    return Vetor(self.coords[0] - outro.coords[0], self.coords[1] - outro.coords[1], self.coords[2] - outro.coords[2])

  def __mul__(self, outro):
    if (isinstance(outro, Vetor)):
      return (self.coords[0] * outro.coords[0]) + (self.coords[1] * outro.coords[1]) + (self.coords[2] * outro.coords[2])
    else :
      return Vetor(self.coords[0] * outro, self.coords[1] * outro, self.coords[2] * outro)

  def modulo(self):
    return sqrt((self.coords[0]**2) + (self.coords[1]**2) + (self.coords[2]**2))
  
  def versor(self):
    return self*(1/self.modulo())
  
  def projecao_ortogonal(self, outro): 
    return outro*(self*outro/(outro*outro))

  def como_tupla(self):
    return (self.coords[0], self.coords[1], self.coords[2])

