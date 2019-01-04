decrescente = True
valor = int(input("Digite o primeiro numero da sequencia: "))
anterior = valor
while valor != 0 and decrescente == True:
    valor = int(input("Digite o proximo numero da sequencia: "))
    if valor > anterior:
      decrescente = False
      print("A sequencia deixou de ser decrescente")
    anterior  = valor
    
if decrescente:
    print("A sequencia é decrescente =)")
