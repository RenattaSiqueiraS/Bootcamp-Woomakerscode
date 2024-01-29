''' Receba do usuário a quantidade de litros de combustível
consumidos e a distância percorrida. Calcule e imprima o 
consumo médio em km/l.
'''

litros = float(input('Digite quantos L foram consumidos: '))
distancia = float(input('Digite a distância percorrida: '))
consumo = distancia/litros

print(f'O consumo médio é: {consumo:.3f}km/l')