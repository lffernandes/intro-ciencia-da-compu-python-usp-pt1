def éPrimo(n):
  i=1
  divisores = 0
  while i<=n:
    if n%i==0:
      divisores+=1
      i+=1
    else:
      i=i+1;
  if divisores ==2:
    return True
  else:
    return False
      
def n_primos(n):
  lista_primos = []
  i=2
  while i>=2 and i<=n:
    if éPrimo(i):
      lista_primos.append(i);  
    i=i+1

  return (lista_primos)
