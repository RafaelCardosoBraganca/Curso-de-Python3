#crie um script que leia quantos reais uma pessoa tem na carteira e quantos dólares ela pode comprar com esse valor
#condsiderando 1USD = 5.06BRL em 9 de abril de 2023
reais=float(input('Informe o valor que você possui em reais: '))
dolares= reais/5
print('com R${:.2f} você pode comprar US${:.2f}'.format(reais, dolares))