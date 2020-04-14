import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import ceil, sin, cos, pi

add = 0.02
K = 2
N = 1

def draw_axis():
  glBegin(GL_LINES)

  glColor3fv( ( 1, 0, 0)) #eixo x: vermelho
  glVertex3fv(( 0, 0, 0))
  glVertex3fv((10, 0, 0))
  
  glColor3fv( ( 0, 1, 0)) #eixo y: verde
  glVertex3fv(( 0, 0, 0))
  glVertex3fv(( 0,10, 0))
  
  glColor3fv( ( 0, 0, 1)) #eixo z: azul
  glVertex3fv(( 0, 0, 0))
  glVertex3fv(( 0, 0,10))

  glEnd()
  
angular_step = pi/20

def get_ball_point(phi, theta, K, N) :
  r = K*(abs(sin(phi)*cos(theta))**N + abs(sin(phi)*sin(theta))**N + abs(cos(phi))**N)**(-1.0/N)
  return (r*sin(phi)*cos(theta), r*sin(phi)*sin(theta), r*cos(phi))

def draw_ball(K, N): #K -> raio da bola; N-> norma N-ésima usada
  glBegin(GL_QUADS)
  phi = 0
  theta = 0
  glColor4fv((0.5, 0.5, 0.5, 0.25))

  while (phi < pi) :
    while (theta < 2*pi) :
      glVertex3fv(get_ball_point(phi, theta, K, N))
      glVertex3fv(get_ball_point(phi, theta + angular_step, K, N))
      glVertex3fv(get_ball_point(phi + angular_step, theta + angular_step, K, N))
      glVertex3fv(get_ball_point(phi + angular_step, theta, K, N))
      theta += angular_step
    theta = 0
    phi += angular_step
  glEnd()

  glBegin(GL_LINES)
  phi = 0
  theta = 0
  glColor4fv((0.75, 0.75, 0.75, 0.75))

  while (theta < 2*pi) :
    while (phi < pi) :
      glVertex3fv(get_ball_point(phi, theta, K, N))
      glVertex3fv(get_ball_point(phi + angular_step, theta, K, N))
      phi += angular_step
    phi = 0
    theta += pi/4
  glEnd()

def render_ui():


  glPushMatrix()
  glLoadIdentity()

  render_text("||V||    = (|x|   + |y|   + |z|    )    = K", (-0.95, 0.9), GLUT_BITMAP_TIMES_ROMAN_24)

  n = "{:.2f}".format(N)

  render_text(n, (-0.88, 0.88), GLUT_BITMAP_TIMES_ROMAN_10)
  render_text(n, (-0.765, 0.94), GLUT_BITMAP_TIMES_ROMAN_10)
  render_text(n, (-0.67, 0.94), GLUT_BITMAP_TIMES_ROMAN_10)
  render_text(n, (-0.575, 0.94), GLUT_BITMAP_TIMES_ROMAN_10)
  
  render_text("1", (-0.511, 0.955), GLUT_BITMAP_TIMES_ROMAN_10)
  render_text("_", (-0.525, 0.95), GLUT_BITMAP_TIMES_ROMAN_10)
  render_text("_", (-0.518, 0.95), GLUT_BITMAP_TIMES_ROMAN_10)
  render_text("_", (-0.511, 0.95), GLUT_BITMAP_TIMES_ROMAN_10)
  render_text("_", (-0.504, 0.95), GLUT_BITMAP_TIMES_ROMAN_10)
  render_text("_", (-0.496, 0.95), GLUT_BITMAP_TIMES_ROMAN_10)
  render_text(n, (-0.520, 0.915), GLUT_BITMAP_TIMES_ROMAN_10)

  glPopMatrix()

def render_text(text, text_pos, font, color=(1., 1., 1.)):
  glColor(*color)
  glRasterPos2f(*text_pos)
  for char in text:
    glutBitmapCharacter(font, ord(char))


def main(): 
  global N 
  global add
  pygame.init()
  glutInit(sys.argv)
  display = (1280, 720)
  pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
  glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
  glEnable(GL_BLEND)
  gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
  glTranslatef(.0, .0, -10)
  glRotatef(-80, 1, 0, 0)
  glRotatef(-135, 0, 0, 1)
  
  input("aperte enter para começar")
  while True:
    if (N <= 1) :
      N = 1
      add *= -1
    elif (N >= 10):
      N = 10
      add *= -1

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
    glRotatef(-0.25, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    draw_axis()
    draw_ball(K, N)
    render_ui()
    pygame.display.flip()
    pygame.time.wait(10)
    N += add*(N**2)

main()

# vertices = (
#   ( 1, -1, -1),
#   ( 1,  1, -1),
#   (-1,  1, -1),
#   (-1, -1, -1),
#   ( 1, -1,  1),
#   ( 1,  1,  1),
#   (-1, -1,  1),
#   (-1,  1,  1),
# )

# edges = (
#   (0,1),
#   (0,3),
#   (0,4),
#   (2,1),
#   (2,3),
#   (2,7),
#   (6,3),
#   (6,4),
#   (6,7),
#   (5,1),
#   (5,4),
#   (5,7),
# )

# surfaces = (
#   (0,1,2,3),
#   (3,2,7,6),
#   (6,7,5,4),
#   (4,5,1,0),
#   (1,5,7,2),
#   (4,0,3,6),
  
# )

# def CubeLines() :
#   glBegin(GL_LINES)
#   for edge in edges:
#     for vertex in edge:
#       glVertex3fv(vertices[vertex])
#   glEnd()

# def Cube() :
#   glBegin(GL_TRIANGLES)
#   for surface in surfaces:
#     glColor3fv((0.5, 0.5, 0.5))
#     for vertex in surface:
#       glVertex3fv(vertices[vertex])
#   glEnd()
