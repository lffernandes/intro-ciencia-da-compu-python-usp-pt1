def fatorial(x):
  i = x
  fat=1
  while i>0:
    fat = fat*i
    i-=1
  return fat

def numero_binominal(n,p):
   resultado = fatorial(n) // (fatorial(p)*fatorial(n-p))
   return resultado
