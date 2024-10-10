#from math import hypot
#cat = float(input('Comprimento do Cateto Oposto: '))
#catadj = float(input('Comprimento do Cateto Adjacente: '))
#print(f'A Hipotenusa vai medir: {hypot(cat,catadj):.2f}')

cat = float(input('Comprimento do Cateto Oposto: '))
catadj = float(input('Comprimento do Cateto Adjacente: '))

print(f'A Hipotenusa é {(cat**2 + catadj**2)**(1/2):.2f}')