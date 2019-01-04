qnum= int(input("Quantos numeros deseja somar:"))
valor=0
soma=0
i=0
while i < qnum:
  valor= int(input("Digite um valor: "))
  soma = soma + valor
  i= i+1

print("A soma dos valores é:",soma)
