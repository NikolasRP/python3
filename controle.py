from funcionalidade import *

tv = televisor ("SONY","sony-123")
controle = ControleRemoto(tv)
contole.sintonizaCanal("SBT")
controle.trocaCanal("SBT")
print(tv.canal_atual)
