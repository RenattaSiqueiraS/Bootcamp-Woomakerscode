''' Criar um programa em Python que solicite três números ao 
usuário, utilize estruturas condicionais para determinar o
maior entre eles e apresente o resultado.
'''

print('Informe os 3 numeros: ')
x = float(input('{x}: '))
y = float(input('{y}: '))
z = float(input('{z}: '))

if x > y and x > z :
    print('{x} é o maior número')
elif y > x and y > z :
    print('{y} é o maior número')  
else :
    print('{z} é o maior número')