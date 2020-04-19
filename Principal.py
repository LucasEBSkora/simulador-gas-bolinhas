import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import glutInit

from Relogio import Relogio
from Esfera import Esfera
from Vetor import Vetor
from Cubo import Cubo
from Gerenciador_Colisao import Gerenciador_Colisao

from math import sqrt

class Principal :
  


  def __init__(self):
    self.esferas = [Esfera(Vetor(0, 0, 0), Vetor(5, 3, 2)), Esfera(Vetor(0,1,0), Vetor(0, 3, 1))]
    self.parar = False
    self.relogio = Relogio()
    self.dimensoes_janela = (1000, 700)
    self.lado_cubo = 10

    self.cubo = Cubo(self.lado_cubo, (1, 1, 1))
    self.gerenciador_colisao = Gerenciador_Colisao()
    pygame.init()
    
    
    


    pygame.display.set_mode(self.dimensoes_janela, DOUBLEBUF|OPENGL)
    #glutInit(sys.argv)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.8, 0.8, 0.8, 1.0))
    glLightfv(GL_LIGHT0, GL_SPECULAR, 0.5, 0.5, 0.5, 1.0)
    glLightfv(GL_LIGHT0, GL_POSITION, (3, 0, 0, 1.0))    

    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, (0.1,0.1,0.1,1.0))

    

    gluPerspective(45, (self.dimensoes_janela[0]/self.dimensoes_janela[1]), 0.1, 50.0)
    glTranslatef(4, .0, -25)
    glRotate(-10, 0, 1, 0)


  def executar(self):
    self.relogio.reiniciar()
    while (not self.parar):
      
      glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #limpa o buffer para começar novo frame
      self.mover_esferas(self.relogio.tempo_passado())
      self.checar_colisoes()
      self.renderizar_ui()
      self.renderizar_esferas()
      pygame.display.flip()
      pygame.time.wait(10)
      
      #parar se a tela foi fechada
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          self.parar = True

  def checar_colisoes(self):
    copia_lista = self.esferas.copy()

    esfera_atual = None

    while (len(copia_lista) > 0):
      
      #tira o primeiro elemento da lista
      esfera_atual = copia_lista.pop(0)

      for esfera in copia_lista :
        self.gerenciador_colisao.colisao_entre_esferas(esfera_atual, esfera)
        print("vo chora")
      self.gerenciador_colisao.colisao_esfera_cubo(esfera_atual, self.lado_cubo)
  
    
  def mover_esferas(self, dt) :
    for esfera in self.esferas:
      esfera.mover(dt)

  def renderizar_ui(self) :
    self.cubo.renderizar()

  def renderizar_esferas(self) :
    for esfera in self.esferas:
      esfera.renderizar()

principal = Principal()

principal.executar()