lista=[]
n=1
while n != 0:
  n = int(input("Digite o número inteiro da sua lista: "))
  print('Para finalizar a lista digite 0: ')
  if n == 0:
    break
  else:
    lista.append(n)
n=0
for i in reversed(lista):
  if n < len(lista)-1:
    print(i)
    n=n+1
  else:
    print(i,end='')
    break
    


