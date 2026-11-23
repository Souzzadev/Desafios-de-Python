
import matplotlib.pyplot as plt


# Análise de desempenho financeiro com desconto

produtos = ["Notebook", "Mouse", "Teclado", "Monitor", "Headset"]
faturamento = [8500, 2300, 4100, 7200, 1800]

com_desconto = list(map(lambda p: p * 0.9, faturamento))

# Calcular faturamento total e médio com desconto
def calcular_faturamento_total(com_desconto):
    return sum(com_desconto)

def calcular_faturamento_medio(com_desconto):
    return sum(com_desconto) / len(com_desconto)

#chamadas
faturamento_total = calcular_faturamento_total(com_desconto)
faturamento_medio = calcular_faturamento_medio(com_desconto)

# Exibir resultados
print(f"Faturamento total com desconto: R$ {faturamento_total:.2f}")
print(f"Faturamento médio com desconto: R$ {faturamento_medio:.2f}")

print(30*"=")
print("RELATÓRIO FINANCEIRO".center(30))
print(30*"=")
print()
print(f"Notebook")
print(f"faturamento original: R$ {faturamento[0]:.2f}")
print(f"Faturamento com desconto: R$ {com_desconto[0]:.2f}")
print()
print(f"Mouse")
print(f"faturamento original: R$ {faturamento[1]:.2f}")
print(f"Faturamento com desconto: R$ {com_desconto[1]:.2f}")
print(30*"=")



# Visualização dos dados
plt.bar(produtos, com_desconto, color='pink')
plt.title("Faturamento com Desconto por Produto")
plt.xlabel("Produtos")  
plt.ylabel("Faturamento com Desconto (R$)")
plt.show()