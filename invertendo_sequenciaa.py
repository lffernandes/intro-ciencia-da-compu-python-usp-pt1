number = []

start = True

while start:

	temp = (int(input('Digite um número: ')))

	if ( temp == 0) :
		break
	else :
		number.append(temp)

x = len(number) - 1

while x >= 0:

	if (number[x] != 0) :
		print(number[x])

	x = x - 1
