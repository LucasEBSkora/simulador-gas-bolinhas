from time import time

class Relogio:
  def __init__(self):
    self._tempo = time()

  def reiniciar(self):
    self._tempo = time()

  def tempo_passado(self):
    tempo_atual = time()
    dt = tempo_atual - self._tempo
    self._tempo = tempo_atual
    return dt