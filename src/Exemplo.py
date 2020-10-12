class ExemploClass:
  def __init__(self, classe, distancia):
    self._classe = classe
    self._distancia = distancia

  @property
  def getClasse(self):
    return self._classe

  @property
  def getDistancia(self):
    return self._distancia

