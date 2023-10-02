n_produtos = int(input())
produtos = {}

# Cadastro dos produtos
for _ in range(n_produtos):
    codigo_produto = int(input())
    descricao = input()
    preco = float(input())
    produtos[codigo_produto] = (descricao, preco)

pedidos = {}
soma_dos_pedidos = 0

# Leitura dos pedidos
while True:
    codigo_produto = int(input())
    
    if codigo_produto == 0:
        break
    
    quantidade = int(input())
    
    # Verifica se o código do produto existe
    if codigo_produto not in produtos:
        continue
    
    # Verifica se a quantidade é negativa ou igual a zero
    if quantidade <= 0:
        continue
    
    # Calcula o valor do pedido
    descricao, preco = produtos[codigo_produto]
    valor_pedido = preco * quantidade
    soma_dos_pedidos += valor_pedido

# Imprime o valor total da conta
print(f"{soma_dos_pedidos:.2f}")
