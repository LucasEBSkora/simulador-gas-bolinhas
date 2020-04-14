from OpenGL.GL import glBegin, glEnd, glColor3fv, glVertex3fv, GL_QUADS

from math import  sin, cos, pi

from Vetor import Vetor


class Esfera:

  raio = 0.5
  passo_angular = pi/5
  cor = (0.5, 0.5, 0.5)

  def __init__(self, pos, vel):
    self.posicao = pos
    self.velocidade = vel
  
  def mover(self, dt) :
    self.posicao += self.velocidade*dt

  def adquirir_ponto_esfera(self, phi, theta):
    return (self.posicao.x + self.raio*sin(phi)*cos(theta), 
    self.posicao.y + self.raio*sin(phi)*sin(theta),
    self.posicao.z + self.raio*cos(phi))

  def renderizar(self): 
    glBegin(GL_QUADS)
    phi = 0
    theta = 0
    glColor3fv(Esfera.cor)

    while (phi < pi) :
      while (theta < 2*pi) :
        glVertex3fv(self.adquirir_ponto_esfera(phi, theta))
        glVertex3fv(self.adquirir_ponto_esfera(phi, theta + self.passo_angular))
        glVertex3fv(self.adquirir_ponto_esfera(phi + self.passo_angular, theta + self.passo_angular))
        glVertex3fv(self.adquirir_ponto_esfera(phi + self.passo_angular, theta))
        theta += self.passo_angular
      theta = 0
      phi += self.passo_angular
    glEnd()

  