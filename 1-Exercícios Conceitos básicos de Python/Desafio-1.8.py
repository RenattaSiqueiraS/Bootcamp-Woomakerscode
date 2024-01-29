''' Faça um Programa que pergunte quanto você ganha por 
hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
'''

valorh = float(input('Quanto você ganha por hora em R$? '))
horas = float(input('Quantas hrs você trabalha por mês? '))

total = valorh*horas

print(f'O salário total é: R$ {total:.2f}')