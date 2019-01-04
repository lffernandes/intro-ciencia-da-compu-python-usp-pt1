num = int(input("Digite um número: "))
adjacenteigual = False
while num != 0:
      digitoa = num % 10
      num = num // 10
      digitob = num % 10
      if digitoa == digitob:
        adjacenteigual = True
if not adjacenteigual :
  print("não")
else:
  print("sim")
