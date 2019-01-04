def retangulo(width, heigh):
	
	i = 0
	j = 0

	for j in range(heigh):
		
		for i in range(width):

			if ((j == 0) or (j == heigh-1)):
				print('#', end = "")	
			else :
				if ( i == 0) :
					print(end = '#')
				else :
					if (i == width -1):
						print(end = '#')
					else :
						print(end = ' ')
		print()


width = int(input('digite a largura: '))
heigh = int(input('digite a altura: '))

retangulo(width, heigh)
