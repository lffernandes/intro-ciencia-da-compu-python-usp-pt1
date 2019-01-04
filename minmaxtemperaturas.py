def mintemperatura (temperaturas):
  minima=1000
  for i in temperaturas:
    if i < minima:
      minima = i
  return minima  


def maxtemperatura (temperaturas):

  maxima=0
  for i in temperaturas:
    if i > maxima:
      maxima = i
  return maxima 

def minmax(temperaturas):
  print("A menor temperatura do mês foi: ", mintemperatura(temperaturas), "C.")
  print("A menor temperatura do mês foi: ", maxtemperatura(temperaturas), "C.")
