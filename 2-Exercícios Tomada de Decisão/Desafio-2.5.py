''' Desenvolva um programa que solicite ao usuário os 
comprimentos dos três lados de um triângulo e classifique-o
como equilátero, isósceles ou escaleno. 
equilátero: todos os lados com o mesmo valor 
isósceles: dois lados com o mesmo valor
escaleno: todos os lados com medidas distintas.
'''
print('Informe os 3 lados de um triêngulo: ')
x = float(input('{x: }'))
y = float(input('{y: }'))
z = float(input('{z: }'))

if x == y == z :
    print('Equilátero')
elif x != y != z :
    print('Escaleno')       
elif ((x == y) != z) or ((x == z) != y) or ((z == y) != x) :
    print('Isósceles')
