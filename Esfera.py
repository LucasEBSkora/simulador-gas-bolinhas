from OpenGL.GL import glBegin, glEnd, glColor3fv, glVertex3fv, GL_QUADS, glNormal3fv, glMaterialfv, GL_FRONT, GL_AMBIENT_AND_DIFFUSE, GL_SPECULAR, GL_SHININESS, glMateriali, GL_DIFFUSE
from math import  sin, cos, pi

from Vetor import Vetor


class Esfera:

  raio = 0.05
  passo_angular = pi/5
  cor = (0.25, 0.25, 0.25, 1)

  def __init__(self, pos, vel):
    self.posicao = pos
    self.velocidade = vel
  
  def mover(self, dt) :
    self.posicao += self.velocidade*dt

  def adquirir_ponto_esfera(self, phi, theta):
    return self.posicao + Vetor(sin(phi)*cos(theta), sin(phi)*sin(theta), cos(phi))*self.raio
  
  def adquirir_normal_esfera(self, phi, theta):
    return (sin(phi)*cos(theta), sin(phi)*sin(theta), cos(phi))

  def inicializar_renderizacao():
    glBegin(GL_QUADS)
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, Esfera.cor)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.25, 0.25, 0.25, 1.0))
    glMaterialfv(GL_FRONT, GL_SPECULAR, 0.5, 0.5, 0.5, 1.0)
    glMateriali(GL_FRONT, GL_SHININESS, 100)

  def terminar_renderizacao():
    glEnd()

  def renderizar(self): 

    phi = 0
    theta = 0
    while (phi < pi) :
      while (theta < 2*pi) :

        glNormal3fv(self.adquirir_normal_esfera(phi + self.passo_angular/2, theta + self.passo_angular/2))

        glVertex3fv(self.adquirir_ponto_esfera(phi, theta).coords)
  
        glVertex3fv(self.adquirir_ponto_esfera(phi, theta + self.passo_angular).coords)
          
        glVertex3fv(self.adquirir_ponto_esfera(phi + self.passo_angular, theta + self.passo_angular).coords)

        glVertex3fv(self.adquirir_ponto_esfera(phi + self.passo_angular, theta))
        
    
        theta += self.passo_angular
      theta = 0
      phi += self.passo_angular

  