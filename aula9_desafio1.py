#criar um script que leia o nome completp de uma pessoa, e mostre: O nome com todas as letras maiúsculas, o nome com todas as letras minústulas,
#quantas letras ao todo, desconsiderando os espaços; quantas letras tem o primeiro nome
nome=input('Escreva seu nome completo: ')
print(nome.upper())
print(nome.lower())
space = nome.count(' ')
letras = (len(nome)) - space
dividido = nome.split()
pNome = len(dividido[0])
print('o seu nome possui {} letras'.format(letras))
print('o seu primeiro nome possui {} letras'.format(pNome))

