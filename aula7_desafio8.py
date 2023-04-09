#crie um script que leia o preço de um produto e informe qual o preço liquido com 5% de desconto
price=float(input('informe o preço do produto: '))
d= price-price*0.05
print('O produto custa R${:.2f}, porém com desconto fica R${:.2f}'.format(price, d))