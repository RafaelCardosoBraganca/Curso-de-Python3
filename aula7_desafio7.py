#crie um scripe que calcule a área de uma parede em m², e informe qts L de tinta são necessários para
#pinta-la. Considere 1 L = 2m² de area pintada

h=float(input('Informe a altura da parede: '))
w=float(input('Informe a largura da parede: '))
a= h*w
tinta= a/2
print('A área da parede é {}m², e serão necessários {} litros de tinta para pinta-la!'.format(a, tinta))