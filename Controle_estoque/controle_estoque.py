
# 1. Biblioteca
import matplotlib.pyplot as plt

# 2. Entrada de dados
produto = input("Digite o nome do produto: ")
id_produto = input("Digite o ID do produto: ")
quant_estoque = int(input("Digite a quantidade em estoque: "))
quant_min = int(input("Digite a quantidade mínima em estoque: "))
preco = float(input("Digite o preço unitário do produto: "))

# 3. Processamento dos dados
total_estoque = quant_estoque * preco

categorias = ["Estoque atual", "Estoque mínimo"]
quantidades = [quant_estoque, quant_min]

# 4. Classificação do estoque
if quant_estoque == 0:
    classificacao = "Sem estoque"
elif quant_estoque < quant_min:
    classificacao = "Estoque crítico"
elif quant_estoque == quant_min:
    classificacao = "Estoque no limite"
else:
    classificacao = "Estoque adequado"

# 5. Orientação para o setor de compras
if quant_estoque <= quant_min:
    orientacao = "Solicitar reposição ao setor de compras."
else:
    orientacao = "Manter o estoque atual."

# 6. Relatório
print("=" * 40)
print("RELATÓRIO DE ESTOQUE".center(40))
print("=" * 40)
print(f"Produto: {produto}")
print(f"ID do produto: {id_produto}")
print(f"Quantidade disponível: {quant_estoque}")
print(f"Quantidade mínima: {quant_min}")
print(f"Preço unitário: R$ {preco:.2f}")
print(f"Total em estoque: R$ {total_estoque:.2f}")
print(f"Classificação: {classificacao}")
print(f"Orientação: {orientacao}")
print("=" * 40)

# 7. Visualização com Matplotlib
plt.bar(categorias, quantidades, color=["blue", "orange"])
plt.title(f"Controle de Estoque - {produto}")
plt.xlabel("Categorias")
plt.ylabel("Quantidade de produtos")
plt.show()
