# Dados do pedido
numero_pedido = 1202
nome_cliente = "MARCOS VILAR"
# Listas de produtos, preços e status
produtos = ["Notebook", "Mouse", "Teclado"]
precos = [3500.00, 120.00, 250.00]
# Processamento dos dados
quant_produtos = len(produtos)
valor_total = sum(precos)
status_disponiveis = ["Aguardando Pagamento", "Em Separação", "Enviado", "Entregue"]
status_pedido = status_disponiveis[1]

# Exibição do comprovante
print(" COMPROVANTE ".center(30, "="))
print(f"Pedido: #{numero_pedido}")
print(f"Cliente: {nome_cliente}")
print()
print("PRODUTOS:")
print(f"{produtos[0]} - R$ {precos[0]:.2f}".replace(".", ","))
print(f"{produtos[1]} - R$ {precos[1]:.2f}".replace(".", ","))
print(f"{produtos[2]} - R$ {precos[2]:.2f}".replace(".", ","))
print()
print(f"Quantidade: {quant_produtos} Produtos")
print(f"Total: R$ {valor_total:.2f}".replace(".", ","))
print(f"Status: {status_pedido}")
print(30*"=")
