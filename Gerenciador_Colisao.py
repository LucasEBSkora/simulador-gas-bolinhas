from Esfera import Esfera
from Vetor import Vetor

class Gerenciador_Colisao:

  def colisao_entre_esferas(esfera_atual, esfera): 
    direcao_impacto = esfera_atual.posicao - esfera.posicao #pega o vetor entre os centros das esferas
    if (direcao_impacto.modulo() < 2*Esfera.raio): #se a distância for menor q 2*raio, as esferas estão colidindo
          
      #calcula as componentes da velocidade de cada esfera na direção do impacto e na direção perpendicular

      velocidade_esfera_atual_imp = esfera_atual.velocidade.projecao_ortogonal(direcao_impacto)
      velocidade_esfera_atual_perp = esfera_atual.velocidade - velocidade_esfera_atual_imp

      velocidade_esfera_imp = esfera.velocidade.projecao_ortogonal(direcao_impacto)
      velocidade_esfera_perp = esfera.velocidade - velocidade_esfera_imp

      #as esferas trocam as componentes na direção do impacto, mas mantém as na direção perpendicular

      esfera_atual.velocidade = velocidade_esfera_imp + velocidade_esfera_atual_perp
      esfera.velocidade = velocidade_esfera_atual_imp + velocidade_esfera_perp

      #tira uma esfera de dentro da outra, para evitar problemas com muitas colisões consecutivas

      #uma esfera precisa ser tirada da outra de forma que a distância entre as duas seja maior ou igual ao dobro do raio, ou seja

      sobreposicao = direcao_impacto.versor()*(2*Esfera.raio - direcao_impacto.modulo())

      esfera_atual.posicao += sobreposicao*(1/2)
      esfera.posicao -= sobreposicao*(1/2)

  def colisao_esfera_cubo(esfera, lado_cubo, centro_cubo = Vetor(0, 0, 0)):

    i = 0
    while (i < 3):
      if esfera.posicao.coords[i] - Esfera.raio <= centro_cubo.coords[i] - lado_cubo/2:
        esfera.posicao.coords[i] = centro_cubo.coords[i] - lado_cubo/2 + Esfera.raio 
        esfera.velocidade.coords[i] *= -1
      elif esfera.posicao.coords[i] + Esfera.raio >= centro_cubo.coords[i] + lado_cubo/2:
        esfera.posicao.coords[i] = centro_cubo.coords[i] + lado_cubo/2 - Esfera.raio
        esfera.velocidade.coords[i] *= -1
      i += 1