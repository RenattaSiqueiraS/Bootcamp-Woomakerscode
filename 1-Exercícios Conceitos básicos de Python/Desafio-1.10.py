''' Faça um Programa que utilize 4 variáveis como preferir 
e no final print uma mensagem amigável utilizando as 
variáveis criadas.
Exemplos de variáveis: nome, idade, lugar, profissão....
Exemplo de retorno: Olá Maria, prazer te conhecer. Sou 
de São Paulo também e estou migrando de área.'''

nome = input('Qual o seu nome? ')
cidade = input('Qual a sua cidade? ')
idade = int( input('Qual a sua idade? '))
migrando = input('Qual nova área de trabalho deseja atuar? ')

print(f'Olá {nome}, prazer te conhecer. Eu também sou de {cidade} e desejo migrar para a mesma área que a sua, que é {migrando}. A única diferença é que tenho 29 anos e não {idade}, como você.')