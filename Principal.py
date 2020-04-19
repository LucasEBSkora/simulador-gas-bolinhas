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

import sys
import random
from math import sqrt, floor, pi, sin, cos
from time import time

class Principal :
  


  def __init__(self): 
    


    self.esferas = []
    self.parar = False
    self.relogio = Relogio()
    self.dimensoes_janela = (1000, 700)
    self.lado_cubo = 1

    self.porcentagem_volume_ocupado = 0.01

    self.n_esferas = floor(((self.lado_cubo**3)*self.porcentagem_volume_ocupado) / ((4./3.)*pi*Esfera.raio**3))

    random.seed(time())

    #consideraremos que a energia cinética é medida em "unidades de energia", e que a massa de cada esfera é dada por 2 "unidades de massa", de forma que a equação
    #da energia cinética seja

    #E_c = m*v²/2 = 2(u.m.)*v²(m/s)/2 = v² (u.e.)

    #A energia cinética total do sistema é entre 0.05 e 0.2 vezes o número de esfera, em "unidades de energia"
    energia_cinetica_total = random.uniform(0.05, 0.2)* self.n_esferas 

    limite = self.lado_cubo/2 - Esfera.raio # maior módulo possível da posição inicial de uma esfera sem começar colidindo com paredes

    i = 0
    while (i < self.n_esferas):
      
      kx = random.uniform(0.0, 0.9*energia_cinetica_total)
      energia_cinetica_total -= kx

      ky = random.uniform(0.0, 0.9*energia_cinetica_total)
      energia_cinetica_total -= ky

      kz = random.uniform(0.0, 0.9*energia_cinetica_total)
      energia_cinetica_total -= kz

      self.esferas.append(Esfera(
        #sorteia uma posição dentro do cubo
        Vetor(random.uniform(-self.lado_cubo/2, self.lado_cubo/2), random.uniform(-self.lado_cubo/2, self.lado_cubo/2), random.uniform(-self.lado_cubo/2, self.lado_cubo/2)),
        #usa a energia cinética sorteada pra pegar uma velocidade
        Vetor(sqrt(kx), sqrt(ky), sqrt(kz))
      ))
      i += 1

    # i = -1
    # j = -1
    # k = -1

    # while i < 2:
    #   j = -1
    #   while j < 2:
    #     k = -1
    #     while k < 2:
    #       self.esferas.append(
    #         Esfera(Vetor(i*limite, j*limite, k*limite), Vetor(0, 0, 0))
    #       )
    #       k += 1
    #     j += 1
    #   i += 1

    # self.esferas.append(Esfera(Vetor(0.,0.,0.), Vetor(0.,0.,0.)))

    self.cubo = Cubo(self.lado_cubo, (1, 1, 1))

    pygame.init()

    pygame.display.set_mode(self.dimensoes_janela, DOUBLEBUF|OPENGL)
    glutInit(sys.argv)

    glMatrixMode(GL_MODELVIEW)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_LIGHTING)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHT0)

    luz_ambiente = 0.1
    luz_difusa = 0.20
    luz_especular = 0.1

    #glLightModelfv(GL_LIGHT_MODEL_AMBIENT, (1.0,1.0,1.0,1.0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (luz_ambiente, luz_ambiente, luz_ambiente, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (luz_difusa, luz_difusa, luz_difusa, 1.0))
    glLightfv(GL_LIGHT0, GL_SPECULAR, (luz_especular, luz_especular, luz_especular, 1.0))
    
    glLightfv(GL_LIGHT0, GL_POSITION, (-self.lado_cubo*0.8, 0, -self.lado_cubo*4.9, 1))    




    gluPerspective(45, (self.dimensoes_janela[0]/self.dimensoes_janela[1]), 0.1, 50.0)
    glTranslatef(0, .0, -2.5*self.lado_cubo)
    #glRotate(-85, 1, 0, 0)
    glRotate(-15, 0, 1, 0)


  def executar(self):
    self.relogio.reiniciar()
    # theta = 0
    while (not self.parar):
      
      glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #limpa o buffer para começar novo frame
      self.mover_esferas(self.relogio.tempo_passado())
      self.checar_colisoes()
      self.renderizar_ui()
      self.renderizar_esferas()
      pygame.display.flip()
      pygame.time.wait(10)
      # posicao_luz = Vetor(sin(theta), 0, cos(theta))*self.lado_cubo*5
      # print(posicao_luz)
      # glLightfv(GL_LIGHT0, GL_POSITION, posicao_luz.coords)          

      #parar se a tela foi fechada
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          self.parar = True
        # elif event.type == pygame.KEYDOWN:
        #   if event.key == pygame.K_LEFT:
        #     theta -= 0.1
        #   elif event.key == pygame.K_RIGHT:
        #     theta += 0.1
        
        # elif event.type == pygame.KEYDOWN:
        #   if event.key == pygame.K_LEFT:
        #     glRotate(-10, 0, 1, 0)
        #   elif event.key == pygame.K_RIGHT:
        #     glRotate(10, 0, 1, 0)
        #   elif event.key == pygame.K_UP:
        #     glRotate(10, 1, 0, 0)
        #   elif event.key == pygame.K_DOWN:
        #     glRotate(-10, 1, 0, 0)
            

  def checar_colisoes(self):
    copia_lista = self.esferas.copy()

    esfera_atual = None

    while (len(copia_lista) > 0):
      
      #tira o primeiro elemento da lista
      esfera_atual = copia_lista.pop(0)

      for esfera in copia_lista :
        Gerenciador_Colisao.colisao_entre_esferas(esfera_atual, esfera)

      Gerenciador_Colisao.colisao_esfera_cubo(esfera_atual, self.lado_cubo)
  
    
  def mover_esferas(self, dt) :
    for esfera in self.esferas:
      esfera.mover(dt)

  def renderizar_ui(self) :
    self.cubo.renderizar()
    glBegin(GL_LINES)
    glEnd()

  def renderizar_esferas(self) :
    Esfera.inicializar_renderizacao()
    for esfera in self.esferas:
      esfera.renderizar()
    Esfera.terminar_renderizacao()

principal = Principal()

principal.executar()