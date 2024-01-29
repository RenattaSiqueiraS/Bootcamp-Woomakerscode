''' Escreva um programa que calcule o salário líquido.
Lembrando de declarar o salário bruto e o percentual de 
desconto do Imposto de Renda.
●Renda até R$1.903,98: isento de imposto de renda;
●Renda entre R$1.903,99 e R$2.826,65: alíquota de 7,5%;
●Renda entre R$2.826,66 e R$3.751,05: alíquota de 15%;
●Renda entre R$3.751,06 e R$4.664,68: alíquota de 22,5%;
●Renda acima de R$4.664,68: alíquota máxima de 27,5%
'''

print('Declare a sua renda com base nas opcões apresentadas:\
●Renda até R$1.903,98 isento de imposto de renda;\
●Renda entre R$1.903,99 e R$2.826,65: alíquota de 7,5%;\
●Renda entre R$2.826,66 e R$3.751,05: alíquota de 15%;\
●Renda entre R$3.751,06 e R$4.664,68: alíquota de 22,5%; \
●Renda acima de R$4.664,68: alíquota máxima de 27,5%')

salariob = float(input('Digite o seu salário bruto: R$ '))
aliquota = float(input('Digite a sua alíquota correspondente: '))

salariol = salariob-(aliquota*salariob/100)

print(f'O salário líquido é: {salariol:.2f}')