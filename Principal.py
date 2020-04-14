import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from Relogio import Relogio
from Esfera import Esfera
from Vetor import Vetor

class Principal :
  def __init__(self):
    self.esferas = [Esfera(Vetor(0, 0, 0), Vetor(0.1, 0.1, 0.1)), Esfera(Vetor(0,1,0), Vetor(0, -0.2, 0))]
    self.parar = False
    self.relogio = Relogio()
    self.dimensoes_janela = (800, 600)
    
    
    pygame.init()
    glutInit(sys.argv)
    pygame.display.set_mode(self.dimensoes_janela, DOUBLEBUF|OPENGL)
    gluPerspective(45, (self.dimensoes_janela[0]/self.dimensoes_janela[1]), 0.1, 50.0)
    glTranslatef(.0, .0, -10)
  
  def executar(self):
    self.relogio.reiniciar()
    while (not self.parar):
      
      #parar se a tela foi fechada
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          self.parar = True
      
      glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #limpa o buffer para começar novo frame
      self.mover_esferas(self.relogio.tempo_passado())
      self.checar_colisoes()
      self.renderizar_ui()
      self.renderizar_esferas()
      pygame.display.flip()
      pygame.time.wait(10)

  

  def checar_colisoes(self) :
    print("des")

  def mover_esferas(self, dt) :
    for esfera in self.esferas:
      esfera.mover(dt)

  def renderizar_ui(self) :
    print("ci")

  def renderizar_esferas(self) :
    for esfera in self.esferas:
      esfera.renderizar()

principal = Principal()

principal.executar()