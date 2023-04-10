#faça um script que calcule os catetos e hipotenusa de um triângulo 
#usando o teorema de pitágoras e os módulos Math, lendo os comprimentos dos 2 catetos

from math import sqrt
print('Calcule a sua Hipotenusa!!!')
print('-'*20)
co= int(input('Informe o comprimento do Cateto Oposto: '))
ca= int(input('Informe o comprimento do Cateto Adjacente: '))
#hp= pow(ca, 2) + pow(co, 2)
hp= sqrt(pow(ca, 2) + pow(co, 2))
print('-'*20)
print('O comprimento da Hipotenusa é {} !!!'.format(hp))

#print('o Comprimento da Hipotenusa é {:.1f} !!!!'.format(sqrt(hp)))
