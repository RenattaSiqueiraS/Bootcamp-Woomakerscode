'''Crie um dicionário representando um carrinho de compras.
Adicione produtos (chaves) e quantidades (valores) ao carrinho.
Calcule o total do carrinho de compra'''


compras = {'tomate': [10, 2.30], 'alface': [ 1, 0.45], 'batata': [4, 1.20]}

total = 0
for produto, info in compras.items():
    quantidade, preco_unitario = info
    
    total += preco_unitario * quantidade

print(f'Total do carrinho: {total:.2f}')