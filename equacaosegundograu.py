import math
a= float(input("Digite o valor de a: "))
b= float(input("Digite o valor de b: "))
c= float(input("Digite o valor de c: "))
delta = b**2 - (4*a*c)
if delta < 0:
    print("Esta equação não possuí raízes reais");
else: 
    if delta == 0:
        x1 = (-b - math.sqrt(delta)) / (2*a)
        print ("A raiz desta equação é:",x1);
    else:  
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        if x1 < x2:
            print ("As raizes são",x1,"e",x2)
        else:
            print ("As raizes são",x2,"e",x1)
