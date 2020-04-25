from OpenGL.GL import * #glBegin, glEnd, glColor3fv, glVertex3fv, GL_QUADS, glNormal3fv, glMaterialfv, GL_FRONT, GL_AMBIENT_AND_DIFFUSE, GL_SPECULAR, GL_SHININESS, glMateriali, GL_DIFFUSE
from OpenGL.GLUT import glutSolidSphere
from math import  sin, cos, pi

from Vetor import Vetor


class Esfera:

  raio = 0.05
  passo_angular = pi/5
  cor = (0.3, 0.3, 0.3, 1)
  pontos_esfera = []
  normais_esfera = []

  def __init__(self, pos, vel):
    self.posicao = pos
    self.velocidade = vel

  def set_N_divisoes(N):
    phi = 0
    theta = 0
    while (phi < pi) :
      while (theta < 2*pi) :

        Esfera.normais_esfera.append(Esfera.adquirir_normal_esfera(phi + (pi/N)/2, theta + (pi/N)))

        Esfera.pontos_esfera.append(Esfera.adquirir_ponto_esfera(phi, theta))
        Esfera.pontos_esfera.append(Esfera.adquirir_ponto_esfera(phi, theta + (pi/N)*2))
        Esfera.pontos_esfera.append(Esfera.adquirir_ponto_esfera(phi + (pi/N), theta + (pi/N)*2))
        Esfera.pontos_esfera.append(Esfera.adquirir_ponto_esfera(phi + (pi/N), theta))

        theta += (pi/N)*2
      theta = 0
      phi += (pi/N)


  def mover(self, dt) :
    self.posicao += self.velocidade*dt

  def adquirir_ponto_esfera(phi, theta):
    return ((sin(phi)*cos(theta)*Esfera.raio, cos(phi)*Esfera.raio, sin(phi)*sin(theta)*Esfera.raio))

  def adquirir_normal_esfera(phi, theta):
    return (sin(phi)*cos(theta), cos(phi), sin(phi)*sin(theta))

  def inicializar_renderizacao():
    glBegin(GL_QUADS)
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, Esfera.cor)
    glMaterialfv(GL_FRONT, GL_SPECULAR, 0.4, 0.4, 0.4, 0.2)
    glMateriali(GL_FRONT, GL_SHININESS, 128)

  def terminar_renderizacao():
    glEnd()

  def renderizar(self):

    glPushMatrix()
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, Esfera.cor)
    glMaterialfv(GL_FRONT, GL_SPECULAR, 0.4, 0.4, 0.4, 0.2)
    glMateriali(GL_FRONT, GL_SHININESS, 128)
    glTranslatef(self.posicao.coords[0], self.posicao.coords[1], self.posicao.coords[2])
    glutSolidSphere(self.raio, 5, 5)
    glPopMatrix()

    # i = 0
    # j = 0
    # glPushMatrix()
    # glBegin(GL_QUADS)
    # glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, Esfera.cor)
    # glMaterialfv(GL_FRONT, GL_SPECULAR, 0.4, 0.4, 0.4, 0.2)
    # glMateriali(GL_FRONT, GL_SHININESS, 128)
    # glTranslatef(*self.posicao.coords)
    # while i < len(Esfera.normais_esfera):
    #   glNormal3fv(Esfera.normais_esfera[i])
    #   i += 1
    #   glVertex3fv(Esfera.pontos_esfera[j])
    #   j += 1
    #   glVertex3fv(Esfera.pontos_esfera[j])
    #   j += 1
    #   glVertex3fv(Esfera.pontos_esfera[j])
    #   j += 1
    #   glVertex3fv(Esfera.pontos_esfera[j])
    #   j += 1
    # glEnd()
    # glPopMatrix()


    # while i < len(Esfera.normais_esfera):
    #   glNormal3fv(Esfera.normais_esfera[i])
    #   i += 1
    #   glVertex3fv((self.posicao.coords[0] + Esfera.pontos_esfera[j][0], self.posicao.coords[1] + Esfera.pontos_esfera[j][1], self.posicao.coords[2] + Esfera.pontos_esfera[j][2]))
    #   j += 1
    #   glVertex3fv((self.posicao.coords[0] + Esfera.pontos_esfera[j][0], self.posicao.coords[1] + Esfera.pontos_esfera[j][1], self.posicao.coords[2] + Esfera.pontos_esfera[j][2]))
    #   j += 1
    #   glVertex3fv((self.posicao.coords[0] + Esfera.pontos_esfera[j][0], self.posicao.coords[1] + Esfera.pontos_esfera[j][1], self.posicao.coords[2] + Esfera.pontos_esfera[j][2]))
    #   j += 1
    #   glVertex3fv((self.posicao.coords[0] + Esfera.pontos_esfera[j][0], self.posicao.coords[1] + Esfera.pontos_esfera[j][1], self.posicao.coords[2] + Esfera.pontos_esfera[j][2]))
    #   j += 1

    # phi = 0
    # theta = 0
    # while (phi < pi) :
    #   while (theta < 2*pi) :

    #     glNormal3fv(self.adquirir_normal_esfera(phi + self.passo_angular/2, theta + self.passo_angular))

    #     glVertex3fv(self.adquirir_ponto_esfera(phi, theta))
    #     glVertex3fv(self.adquirir_ponto_esfera(phi, theta + self.passo_angular*2))
    #     glVertex3fv(self.adquirir_ponto_esfera(phi + self.passo_angular, theta + self.passo_angular*2))
    #     glVertex3fv(self.adquirir_ponto_esfera(phi + self.passo_angular, theta))

    #     theta += self.passo_angular*2
    #   theta = 0
    #   phi += self.passo_angular

#   from OpenGL.GL import glBegin, glEnd, glColor3fv, glVertex3fv, GL_QUADS, glNormal3fv, glMaterialfv, GL_FRONT, GL_AMBIENT_AND_DIFFUSE, GL_SPECULAR, GL_SHININESS, glMateriali, GL_DIFFUSE, glPushMatrix, glPopMatrix, glTranslatef
# from OpenGL.GLUT import glutSolidSphere
# from math import  sin, cos, pi

# from Vetor import Vetor


# class Esfera:

#   raio = 0.05
#   passo_angular = pi/5
#   cor = (0.3, 0.3, 0.3, 1)
#   pontos_esfera = []

#   def __init__(self, pos, vel):
#     self.posicao = pos
#     self.velocidade = vel
#     self.pontos_esfera = []

#   def mover(self, dt) :
#     self.posicao += self.velocidade*dt

#   def adquirir_ponto_esfera(self, phi, theta):
#     return (Vetor(sin(phi)*cos(theta)*self.raio, cos(phi)*self.raio, sin(phi)*sin(theta)*self.raio))

#   def adquirir_normal_esfera(phi, theta):
#     return (sin(phi)*cos(theta), cos(phi), sin(phi)*sin(theta))

#   def inicializar_renderizacao():
#     glBegin(GL_QUADS)
#     glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, Esfera.cor)
#     glMaterialfv(GL_FRONT, GL_SPECULAR, 0.4, 0.4, 0.4, 0.2)
#     glMateriali(GL_FRONT, GL_SHININESS, 128)

#   def finalizar_renderizacao():
#     glEnd()

#   def setDivisoes_esfera(N):
#     self.pontos_esfera = []
#     phi = 0
#     theta = 0
#     while (phi < pi) :
#       while (theta < 2*pi) :

#         Esfera.pontos_esfera.append(adquirir_ponto_esfera(phi + (pi/N)/2, theta + (pi/N)))

#         Esfera.pontos_esfera.append(adquirir_ponto_esfera(phi, theta))

#         Esfera.pontos_esfera.append((phi, theta + (pi/N)*2))
#         Esfera.pontos_esfera.append((phi + (pi/N), theta + (pi/N)*2))
#         Esfera.pontos_esfera.append((phi + (pi/N), theta))

#         theta += (pi/N)*2
#       theta = 0
#       phi += (pi/N)


#   def renderizar(self):

#     # glPushMatrix()
#     # glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, Esfera.cor)
#     # glMaterialfv(GL_FRONT, GL_SPECULAR, 0.4, 0.4, 0.4, 0.2)
#     # glMateriali(GL_FRONT, GL_SHININESS, 128)
#     # glTranslatef(self.posicao.coords[0], self.posicao.coords[1], self.posicao.coords[2])
#     # glutSolidSphere(self.raio, 5, 5)
#     # glPopMatrix()


#     # glPushMatrix()

#     # glTranslatef(self.posicao.x(), self.posicao.y(), self.posicao.z())
#     # glutSolidSphere(Esfera.raio, 5, 5)
#     # glPopMatrix()
#     # # phi = 0
#     # theta = 0
#     # while (phi < pi) :
#     #   while (theta < 2*pi) :

#     #     glNormal3fv(self.adquirir_normal_esfera(phi + self.passo_angular/2, theta + self.passo_angular))

#     #     glVertex3fv(self.adquirir_ponto_esfera(phi, theta))
#     #     glVertex3fv(self.adquirir_ponto_esfera(phi, theta + self.passo_angular*2))
#     #     glVertex3fv(self.adquirir_ponto_esfera(phi + self.passo_angular, theta + self.passo_angular*2))
#     #     glVertex3fv(self.adquirir_ponto_esfera(phi + self.passo_angular, theta))

#     #     theta += self.passo_angular*2
#     #   theta = 0
#     #   phi += self.passo_angular

#     i = 0
#     while i < len(Esfera.pontos_esfera):
#       glNormal3fv((Esfera.pontos_esfera[i][0] + self.posicao.x(), Esfera.pontos_esfera[i][1] + self.posicao.y(), Esfera.pontos_esfera[i][2] + self.posicao.z()))
#       i += 1
#       glVertex3fv((Esfera.pontos_esfera[i][0] + self.posicao.x(), Esfera.pontos_esfera[i][1] + self.posicao.y(), Esfera.pontos_esfera[i][2] + self.posicao.z()))
#       i += 1
#       glVertex3fv((Esfera.pontos_esfera[i][0] + self.posicao.x(), Esfera.pontos_esfera[i][1] + self.posicao.y(), Esfera.pontos_esfera[i][2] + self.posicao.z()))
#       i += 1
#       glVertex3fv((Esfera.pontos_esfera[i][0] + self.posicao.x(), Esfera.pontos_esfera[i][1] + self.posicao.y(), Esfera.pontos_esfera[i][2] + self.posicao.z()))
#       i += 1
#       glVertex3fv((Esfera.pontos_esfera[i][0] + self.posicao.x(), Esfera.pontos_esfera[i][1] + self.posicao.y(), Esfera.pontos_esfera[i][2] + self.posicao.z()))
#       i += 1

