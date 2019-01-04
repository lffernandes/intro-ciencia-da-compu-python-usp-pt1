import math
xa = int(input ("Digite o X do ponto A: "))
ya = int(input ("Digite o Y do ponto A: "))
xb = int(input ("Digite o X do ponto B: "))
yb = int(input ("Digite o Y do ponto B: "))
Dab = math.sqrt((xa-xb)**2 + (ya-yb)**2)
if Dab >= 10:
  print("longe");
else:
  print("perto");
