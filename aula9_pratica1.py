#fatiando a string
frase = str('Curso em Video Python')
print('Fatiando a Frase!')
print(frase)
print(frase[9])
print(frase[5:])
print(frase[9::3])
print('-'*40)

#analisando a string
print('Analisando a Frase!')
print('O comprimento da frase é {}\n'.format(len(frase)))
print('Quantas vezes a letra "o" aparece? \nA letra "o" aparece {} vezes\n'.format(frase.count('o')))
print('Em que posição começam os caracteres "deo"?\nNa posição {}\n'.format(frase.find('deo')))
print('Existe a palavra "Curso" na frase? {}!\n'.format('Curso' in frase))
print('-'*40)

#transformando a string
print('Transformando a Frase!\n')
print('Usando a função replace: {}\n'.format(frase.replace('Python', 'Android')))
print('Usando o método upper: {}\n'.format(frase.upper()))
print('Usando o método lower: {}\n'.format(frase.lower()))
print('Usando a função capitalize: {}\n'.format(frase.capitalize()))
print('Usando a função title: {}\n'.format(frase.title()))
frase2= str('   Aprenda Python  ')
print('Testando a função strip na frase: \n{}\n'.format(frase2))
print(frase2.strip())
print(' ')
print('Testando a função rstrip: \n{}\n'.format(frase2.rstrip()))
print('Testando a função lstrip: \n{}\n'.format(frase2.lstrip()))
print('-'*40)

#dividindo a string
print('Dividindo a Frase!\n')
print('Utilizando o split: {}\n'.format(frase.split()))
frase3 = ['Curso', 'em', 'Video', 'Python']
print('-'.join(frase3))
