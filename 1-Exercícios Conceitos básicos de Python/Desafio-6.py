''' Escreva um programa que calcule o tempo de uma viagem.
Faça um comparativo do mesmo percurso de avião, carro e 
ônibus. Levando em consideração: ●avião=600km/h ●carro=100km/h
●ônibus=80km/h
'''

km = float(input('Digite quantos km a sua viagem possui: '))
taviao = km/600
tcarro = km/100
tonibus = km/80
print('Esse é o comparativo de tempo em relação aos meios de transporte: ')
print(f'Avião: {taviao}h')
print(f'Carro: {tcarro}h')
print(f'Ônibus: {tonibus}h')