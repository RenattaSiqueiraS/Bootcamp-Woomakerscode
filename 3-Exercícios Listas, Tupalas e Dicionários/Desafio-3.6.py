''' Faça um programa que permita ao usuário digitar o seu nome e
em seguida mostre o nome do usuário de trás para frente
utilizando somente letras maiúsculas. Dica: lembre-se que ao
informar o nome o usuário pode digitar letras maiúsculas ou
minúsculas '''

nome = input('Digite seu nome: ')
novo_nome = nome[::-1].upper() #upper é p/ ficar maiusculo e #a[::-1], começa do final em direção ao primeiro pegando cada elemento. Então isso inverte a. Isso também se aplica a listas/tuplas.
print(novo_nome)