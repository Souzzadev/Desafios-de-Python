# Variáveis

quantidade = int(input("Digite a quantidade: "))
preco_unitario = float(input("Digite o preço unitario do produto: "))

# Função que calcula o faturamento
def calcular_faturamento(quantidade, preco_unitario):
  cal_faturamento = quantidade * preco_unitario

  return cal_faturamento

# Chamada da função e exibição do resultado
resultado = calcular_faturamento(quantidade, preco_unitario)
print(f"Faturamento total: R$ {resultado:.2f} ")