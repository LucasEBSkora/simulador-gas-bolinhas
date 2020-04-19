from OpenGL.GL import glBegin, glEnd, glColor3fv, glVertex3fv, GL_QUADS, glNormal3fv, glMaterialfv, GL_FRONT, GL_AMBIENT_AND_DIFFUSE, GL_SPECULAR, GL_SHININESS, glMateriali, glColor
from math import  sin, cos, pi

from Vetor import Vetor


class Esfera:

  raio = 0.5
  passo_angular = pi/10
  cor = (0.25, 0.25, 0.25, 1)

  def __init__(self, pos, vel):
    self.posicao = pos
    self.velocidade = vel
  
  def mover(self, dt) :
    self.posicao += self.velocidade*dt

  def adquirir_ponto_esfera(self, phi, theta):
    return Vetor(self.posicao.x + self.raio*sin(phi)*cos(theta), 
    self.posicao.y + self.raio*sin(phi)*sin(theta),
    self.posicao.z + self.raio*cos(phi))

  def renderizar(self): 
    glBegin(GL_QUADS)
    phi = 0
    theta = 0
    ponto = None
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, Esfera.cor)
    glMaterialfv(GL_FRONT, GL_SPECULAR, (0.8, 0.8, 0.8, 1.0))
    glMateriali(GL_FRONT, GL_SHININESS, 5)

    while (phi < pi) :
      while (theta < 2*pi) :

        ponto = self.adquirir_ponto_esfera(phi, theta)
        glNormal3fv(ponto.versor().como_tupla())
        glVertex3fv(ponto.como_tupla())

        ponto = self.adquirir_ponto_esfera(phi, theta + self.passo_angular)
        glNormal3fv(ponto.versor().como_tupla())
        glVertex3fv(ponto.como_tupla())
        
        ponto = self.adquirir_ponto_esfera(phi + self.passo_angular, theta + self.passo_angular)
        glNormal3fv(ponto.versor().como_tupla())
        glVertex3fv(ponto.como_tupla())

        ponto = self.adquirir_ponto_esfera(phi + self.passo_angular, theta)
        glNormal3fv(ponto.versor().como_tupla())
        glVertex3fv(ponto.como_tupla())
        
    
        theta += self.passo_angular
      theta = 0
      phi += self.passo_angular
    glEnd()

  