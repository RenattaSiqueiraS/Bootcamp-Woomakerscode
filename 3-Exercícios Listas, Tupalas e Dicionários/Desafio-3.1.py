''' Utilizando listas faça um programa que faça 5 perguntas
para uma pessoa sobre um crime. As perguntas são:
""Telefonou para a vítima?""
""Esteve no local do crime?""
""Mora perto da vítima?""
""Devia para a vítima?""
""Já trabalhou com a vítima?""
O programa deve no final emitir uma classificação sobre a 
participação da pessoa no crime. Se a pessoa responder 
positivamente a 2 questões ela deve ser classificada como
""Suspeita"", entre 3 e 4 como ""Cúmplice"" e 5 como
""Assassino"". Caso contrário, ele será classificado como
""Inocente""
'''
print('Responda as seguintes perguntas com S ou N: ')
p1 = input('Telefonou para a vítima? ')
p2 = input('Esteve no local do crime? ')
p3 = input('Mora perto da vítima? ')
p4 = input('Devia para a vítima? ')
p5 = input('Já trabalhou com a vítima? ')

valorculpa = 0
if p1 == "S":
    valorculpa += 1 #incremento
elif p2 == "S":
    valorculpa += 1
elif p3 == "S":
    valorculpa += 1
elif p4 == "S":
    valorculpa += 1
if p5 == "S":
    valorculpa += 1

if valorculpa < 2:
    print("Inocente")
elif valorculpa == 2:
    print("Suspeita")
elif 3 <= valorculpa <= 4:
    print("Cúmplice")
else:
    print("Assassino")
