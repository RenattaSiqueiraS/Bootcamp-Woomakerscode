''' Faça um programa que lê três números inteiros e os 
mostra em ordem crescente.
'''

print('Informe 3 numeros inteiros: ')
x = int(input('{x}: '))
y = int(input('{y}: '))
z = int(input('{z}: '))

numeros = [x, y, z]
numeros.sort() # para lista decrescente: numeros.sort(reverse =True)
print(numeros)
