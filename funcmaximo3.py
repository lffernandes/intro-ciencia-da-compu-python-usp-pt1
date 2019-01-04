def maximo(x,y,z):
  maior = 0
  if x>=y and x>=z:
    maior=x
  if y>=x and y>=z:
    maior=y
  if z>=x and z>=y:
    maior=z
    
  return maior

