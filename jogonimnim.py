

def computador_escolhe_jogada(n, m):
    print("Vez do computador!")
    if n <= m:
        return n    
    else:
        quantia = n % (m+1)
        if quantia > 0:
            return quantia
        return m

def usuario_escolhe_jogada(n, m):
    print("Sua vez!\n")
    jogada = 0
    while jogada == 0:
        jogada = int(input("Quantas peças irá tirar? "))
        if jogada > n or jogada < 1 or jogada > m:
            jogada = 0
    return jogada
  
def partida():
    print(" ")
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    is_computador_joga = False
    if n % (m+1) == 0:
        is_computador_joga = False
    while n > 0:       
        if not is_computador_joga:
            jogada = usuario_escolhe_jogada(n, m)
            is_computador_joga = True
            print("Você retirou {} peças.".format(jogada))
        else:
            jogada = computador_escolhe_jogada(n, m)
            is_computador_joga = False
            print("Computador retirou {} peças.".format(jogada))        
    n = n - jogada
    print("Restam apenas {} peças em jogo.\n".format(n))
    if is_computador_joga:
        print("Você ganhou!")
        return 1
    else:
        print("O computador ganhou!")
        return 0
    
def campeonato():
    usuario = 0
    computador = 0
    tipo_jogo = 0
    
    # Executa 3 vezes:
    for _ in range(3):
        vencedor = partida()
        if vencedor == 1:
            usuario = usuario + 1
        else:
            computador = computador + 1
    print("Placar final: Você  {} x {}  Computador".format(usuario, computador))
    while tipo_jogo == 0:
      print("Bem-vindo ao jogo do NIM! Escolha:")
      print(" ")
      print("1 - Para jogar uma partida isolada")
      print("2 - Para jogar um campeonato")
      tipo_jogo = int(input("Sua opção: "))
      print(" ")
      if tipo_jogo == 1:
        print("Voce escolheu partida isolada!")
        partida()
        break
      if tipo_jogo == 2:
        print("Voce escolheu um campeonato!")
        campeonato()
        break
      else:
        print("Opção inválida!")
        tipo_jogo = 0

print("Bem vindo!")
escolha = int(input("Digite 1 para partida ou 2 para campeonato: "))
if escolha == 1:
    partida()
    i=0
if escolha == 2:
    campeonato()
    i=0

