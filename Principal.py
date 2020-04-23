import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import glutInit, glutBitmapCharacter, GLUT_BITMAP_TIMES_ROMAN_24

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
    self.porcentagem_volume_ocupado = 0.010
    
    self.tempo_passado = 0
    
    self.lado_cubo = 1
    self.K_total = Vetor(0, 0, 0)
    self.pressao_ideal = 0
    self.pressao = 0
    self.n_colisoes = 0
    self.modulo_momento_linear_transferido_paredes = 0
    self.n_colisoes_por_segundo_area_ideal = 0
    self.n_colisoes_por_segundo_area = 0
    self.velocidade_media = 0
    
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
        Vetor(random.uniform(-limite, limite), random.uniform(-limite, limite), random.uniform(-limite, limite)),
        #usa a energia cinética sorteada pra pegar uma velocidade
        Vetor(sqrt(kx*2), sqrt(ky*2), sqrt(kz*2))
      ))
      i += 1

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
    glTranslatef(0.5*self.lado_cubo, 0, -2.5*self.lado_cubo)
    #glRotate(-85, 1, 0, 0)
    glRotate(-15, 0, 1, 0)


  def executar(self):
    self.relogio.reiniciar()
    dt = 0
    while (not self.parar):
      dt = self.relogio.tempo_passado()
      self.tempo_passado += dt

      glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #limpa o buffer para começar novo frame
      self.mover_esferas(dt)
      self.checar_colisoes()
      self.calcular_grandezas()
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
        Gerenciador_Colisao.colisao_entre_esferas(esfera_atual, esfera)

      momento_linear_transferido_paredes = Gerenciador_Colisao.colisao_esfera_cubo(esfera_atual, self.lado_cubo)
      self.modulo_momento_linear_transferido_paredes += momento_linear_transferido_paredes
      if momento_linear_transferido_paredes != 0:
        self.n_colisoes += 1
  
    
  def mover_esferas(self, dt) :
    for esfera in self.esferas:
      esfera.mover(dt)

  def renderizar_texto(self, texto, posicao_texto, fonte, cor = (1., 1., 1.)):
    glColor(*cor)
    glRasterPos2f(*posicao_texto)
    for char in texto:
      glutBitmapCharacter(fonte, ord(char))


  def renderizar_ui(self) :
    self.cubo.renderizar()
    
    textos = [
      "K  = " + "{:.10f}".format(self.K_total*Vetor(1,1,1)) + " u.e.",
      "Vm = " + "{:.10f}".format(self.velocidade_media.modulo()) + " m/s",
      "Kx = " + "{:.10f}".format(self.K_total.x()) + " u.e.",
      "Kx = " + "{:.10f}".format(self.K_total.x()) + " u.e.",
      "Ky = " + "{:.10f}".format(self.K_total.y()) + " u.e.",
      "Kz = " + "{:.10f}".format(self.K_total.z()) + " u.e.",
      "Pi = " + "{:.10f}".format(self.pressao_ideal) + " u.p.",
      "P  = " + "{:.10f}".format(self.pressao) + " u.p.",
      "Ni = " + "{:.10f}".format(self.n_colisoes_por_segundo_area_ideal) + " colisoes/(s*m^2)",
      "N  = " + "{:.10f}".format(self.n_colisoes_por_segundo_area) + " colisoes/(s*m^2)"
    ]
    
    posicao_y = 1

    for texto in textos:
      self.renderizar_texto(texto, (-2.3, posicao_y, 0), GLUT_BITMAP_TIMES_ROMAN_24)
      posicao_y -= 0.1

  def calcular_grandezas(self):
    self.K_total = Vetor(0, 0, 0)
    self.velocidade_media = Vetor(0, 0, 0)
    media_modulo_velocidade = 0
    

    for esfera in self.esferas:
      self.K_total += esfera.velocidade.multiplicar_coords_uma_a_uma(esfera.velocidade)*0.5
      self.velocidade_media += esfera.velocidade
      media_modulo_velocidade += esfera.velocidade.modulo()

    self.velocidade_media *= 1/self.n_esferas
    media_modulo_velocidade *= 1/self.n_esferas
    # usando a equação 19-21 do Halliday volume 2, temos
    # Pi = n*M*Vrms²/(3V). Como V = L³ = 1m³, e n*M*Vrms²é 2*K, Pi = 2*K/3V
    self.pressao_ideal = self.K_total*Vetor(1,1,1)*(2/3)

    #como Pr = F/A e F = dP/dt, Pr =  dP/(a*dt), onde P é o momento linear das paredes.
    self.pressao = self.modulo_momento_linear_transferido_paredes/(self.tempo_passado*6)

    self.n_colisoes_por_segundo_area_ideal = sqrt(self.n_esferas*6*(self.K_total*Vetor(1,1,1)))

    self.n_colisoes_por_segundo_area = self.n_colisoes/(self.tempo_passado*6) #a área superficial de um cubo é 6*l² = 6m², nesse caso.




  def renderizar_esferas(self) :
    Esfera.inicializar_renderizacao()
    for esfera in self.esferas:
      esfera.renderizar()
    Esfera.terminar_renderizacao()

principal = Principal()

principal.executar()