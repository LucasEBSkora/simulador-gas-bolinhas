from OpenGL.GL import glBegin, glEnd, glColor3fv, glVertex3fv, GL_LINES, glPushMatrix, glPopMatrix, glLoadIdentity, glTranslatef

from Vetor import Vetor

class Grafico:
  def __init__(self, pontos, dimensoes, posicao, escala, cor = (1., 1., 1.)):
    self.pontos = pontos
    self.largura = dimensoes[0]
    self.altura = dimensoes[1]
    self.posicao = posicao
    self.escala_x = escala[0]
    self.escala_y = escala[1]
    self.cor = cor
    
  def desenhar(self):

    glPushMatrix()
    glLoadIdentity()
    glTranslatef(*self.posicao)


    glColor3fv(self.cor)
    
    glBegin(GL_LINES)

    #desenha moldura

    glVertex3fv((0, 0, 0))
    glVertex3fv((self.largura, 0, 0))

    glVertex3fv((self.largura, 0, 0))
    glVertex3fv((self.largura, self.altura, 0))

    glVertex3fv((self.largura, self.altura, 0))
    glVertex3fv((0, self.altura, 0))

    glVertex3fv((0, self.altura, 0))
    glVertex3fv((0, 0, 0))

    i = 0
  

    while (i < len(self.pontos) - 1):
      glVertex3fv((self.pontos[i][0]*self.escala_x, self.pontos[i][1]*self.escala_y, 0))
      glVertex3fv((self.pontos[i + 1][0]*self.escala_x, self.pontos[i + 1][1]*self.escala_y, 0))
      i += 1
    glEnd()

    glPopMatrix()