from OpenGL.GL import glBegin, glEnd, glColor3fv, glVertex3fv, GL_LINES, glNormal3fv, glMaterialfv, GL_FRONT, GL_AMBIENT_AND_DIFFUSE, GL_SPECULAR, GL_SHININESS, glMateriali, glColor

class Cubo:
  cor = (1, 1, 1)
  arestas = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4)
  ]

  def __init__(self, lado, cor): 
    self.cor = cor
    self.lado = lado
    self.vertices = [ 
      (-lado/2, -lado/2, -lado/2),
      ( lado/2, -lado/2, -lado/2),
      ( lado/2,  lado/2, -lado/2),
      (-lado/2,  lado/2, -lado/2),
      (-lado/2, -lado/2,  lado/2),
      ( lado/2, -lado/2,  lado/2),
      ( lado/2,  lado/2,  lado/2),
      (-lado/2,  lado/2,  lado/2)
    ]
  
  def renderizar(self):
    glBegin(GL_LINES)

    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, self.cor)
    glMaterialfv(GL_FRONT, GL_SPECULAR, (1.0, 1.0, 1.0, 1.0))
    glMateriali(GL_FRONT, GL_SHININESS, 128)
    
    for aresta in Cubo.arestas:
      for ponto in aresta:
        glVertex3fv(self.vertices[ponto])
    glEnd()