import math

class Esfera:
  def __init__(self, cor, raio):
    self.cor = cor
    self.raio = raio

vol = (4/3)*math.pi*(self.raio**3)
return vol

def area(self):
  ar = 4*math.pi*(self.raio**2)
  return ar

bola1 = Esfera("vermelha",4)
bola2 = Esfera("azul",7)

print(f"o volume da bola 1 é "{bola1.vol()}cm^3)
print(f"a área Superficial da bola 1 é "{bola.ar()}cm^3)

print(bola1.vol())
print(Esfera.vol(bola1))
