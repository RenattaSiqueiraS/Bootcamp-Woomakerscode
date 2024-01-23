''' Escreva um programa que calcule o salário líquido.
Lembrando de declarar o salário bruto e o percentual de 
desconto do Imposto de Renda.
●Renda até R$1.903,98: isento de imposto de renda;
●Renda entre R$1.903,99 e R$2.826,65: alíquota de 7,5%;
●Renda entre R$2.826,66 e R$3.751,05: alíquota de 15%;
●Renda entre R$3.751,06 e R$4.664,68: alíquota de 22,5%;
●Renda acima de R$4.664,68: alíquota máxima de 27,5%
'''

print('\
●Renda até R$1.903,98 - digite 1\
●Renda entre R$1.903,99 e R$2.826,65 - diigite 2\
●Renda entre R$2.826,66 e R$3.751,05 - digite 3\
●Renda entre R$3.751,06 e R$4.664,68 = digite 4\
●Renda acima de R$4.664,68 - digite 5')
valor = (input('Declare a sua renda com base nas opcões apresentadas: '))
salario = input('Digite a opção que corresponde ao seu salário bruto: ')

print(f'O salário líquido é: {salario}')