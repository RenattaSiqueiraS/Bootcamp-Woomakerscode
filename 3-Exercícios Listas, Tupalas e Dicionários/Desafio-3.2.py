''' Faça um Programa que peça as quatro notas de 5 alunos,
calcule e armazene numa lista a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0.
'''
'''Nas vezes em que precisamos que determinada variável seja 
incrementado ou decrementada a cada ciclo, a forma mais 
simples, é gerando uma lista com a função range().
'''

medias = [] #lista de medias

for aluno in range(5): #aluna vai de 1 ate 5

    notas = [] #lista de notas
    for nota in range(4): #nota vai de 1 ate 4
        nota = float(input(f'Digite a nota {(nota + 1)} do aluno {aluno + 1}: '))
        notas.append(nota)

    media = sum(notas) / len(notas) #len é a quantidade de notas e sum a soma das notas
    medias.append(media)

contador_alunos_aprovados = 0
for media in medias:
    if media >= 7.0:
        contador_alunos_aprovados += 1

print(f'Número de alunos aprovados: {contador_alunos_aprovados}')