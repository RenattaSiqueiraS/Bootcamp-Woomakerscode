''' Crie um dicionário representando contatos (nome,telefone). Permita ao usuário procurar
por um contato pelo nome.
'''

contatos = {'Alice': '123456789', 'Bob': '987654321', 'Charlie': '555555555'}

def procurar_contato():
    nome = input("Digite o nome do contato: ")
    if nome in contatos:
        telefone = contatos[nome]
        print(f"Telefone de {nome}: {telefone}")
    else:
        print(f"Contato {nome} não encontrado.")

# Exemplo de uso
procurar_contato()