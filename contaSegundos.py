segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))
seg = (segundos % 60)
minutoaux = (segundos //60)
minutos = (segundos // 60)% 60
horas = (minutoaux //60 )% 24
dia = (minutoaux//60//24)
print (dia,"dias,",horas,"horas,",minutos,"minutos e",seg,"segundos.")
