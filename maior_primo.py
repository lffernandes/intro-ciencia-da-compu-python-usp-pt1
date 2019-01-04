def primo (num):
  i=1
  divisores = 0
  while i<=num:
    if num%i==0:
      divisores+=1
      i+=1
    else:
      i+=1;
    if divisores ==2:
      p= True
    else:
      p= False
  return p

def maior_primo(x):
  mp=a=1
  while a <= x:
      if primo(a):
        mp=a
        a=a+1
      else:
        a=a+1
  return mp
