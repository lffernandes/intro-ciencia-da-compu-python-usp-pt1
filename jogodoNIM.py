def computador_escolhe_jogada(n,m):
  jogadapc=i=1
  multiplo=False
  while i<=m:
    if (n-i)%(m+1)==0:
      jogadapc=i
      multiplo=True
      i=i+1
    else:
      multiplo=False
      i=i+1
  if not multiplo:
    jogadapc=m
  return jogadapc

def usuario_escolhe_jogada(n,m):
  print("Sua vez!\n")
  jogada = 0
  while jogada == 0:
    jogada = int(input("Quantas peças irá tirar? "))
    if jogada > n or jogada < 1 or jogada > m:
      jogada = 0
  return jogada

def partida():
  n = int(input("Quantas peças? "))
  m = int(input("Limite de peças por jogada? "))
is_computer_turn = True
if x != 0:
    is_computer_turn = True
    print("O computador começa!") 
if x == 0:
    is_computer_turn = False
    print("Você começa!")

while n > 0:
    if is_computer_turn:
      jogada = computador_escolhe_jogada(n, m)
      is_computer_turn = False
      print("Computador retirou {} peças.".format(jogada))
    else:
      jogada = usuario_escolhe_jogada(n, m)
      is_computer_turn = True
      print("Você retirou {} peças.".format(jogada))
n = n - jogada
print("Restam apenas {} peças em jogo.\n".format(n))

if is_computer_turn:
   print("Você ganhou!")
return 1;
else:
    print("O computador ganhou!")
return 0

def campeonato():
  usuario = 0
  computador = 0
for _ in range(3):
    vencedor = partida()
if vencedor == 1:
      usuario = usuario + 1
else:
      computador = computador + 1
print("Placar final: Você  {} x {}  Computador".format(usuario, computador))
  


