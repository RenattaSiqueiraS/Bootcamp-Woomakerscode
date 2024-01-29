'''Desenvolver um programa que solicite a idade do usuário e
identifique se ele é uma criança, um adolescente, adulto
ou idoso.'''

idade = int(input('informe sua idade: '))
if 0 < idade < 14 :
    print('Criança')
    
elif 14 <= idade <= 18 :
    print('Adolescente')
    
elif 18 < idade < 60 :
    print('Adulto')
    
else :
    print('Idoso')