''' Solicite ao usuário o peso em kg e a altura em metros.
Calcule e imprima o Índice de Massa Corporal(IMC) usando a
fórmula:IMC=peso/(alturaxaltura).'''

peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em m: '))

imc = peso/(altura*altura)

print(f'Seu IMC é: {imc:.2f}')