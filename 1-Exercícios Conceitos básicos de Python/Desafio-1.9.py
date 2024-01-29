''' Solicite ao usuário o número de horas de exercício 
físico por semana. Calcule o total de calorias queimadas em
um mês, considerando uma média de 5calorias por minuto de 
exercício.'''

hrs = float(input('Quantas hrs de exercício físico você faz por semana? '))
tmin = hrs*60
caloriasmin = 5*tmin
caloriasmes = caloriasmin*43800

print(f'o seu gasto calórico mensal é de: {caloriasmes}')