#crie um script que leia um salário e informe qual será seu valor com 15% de aumento
salario=float(input('Informe seu salário: '))
aumento= salario*0.15+salario
print('Com 15 por cento de aumento seu novo salário será R${:.2f}!'.format(aumento))