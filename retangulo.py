def retangulo(width, heigh):
	
	a = 0
	b = 0

	for b in range(heigh):
		
		for a in range(width):
			print('#', end = "")

		print()

width = int(input('digite a largura: '))
heigh = int(input('digite a altura: '))

retangulo(width, heigh)
