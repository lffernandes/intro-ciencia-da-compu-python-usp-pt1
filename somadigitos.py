num=int(input("Digite um número inteiro: "))
soma=0
while num!=0:
  soma += num%10
  num=num//10
print(soma)
