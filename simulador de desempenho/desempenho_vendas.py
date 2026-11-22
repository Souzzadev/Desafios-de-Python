import random
import matplotlib.pyplot as plt

vendas_produtos = [random.randint(500, 5000) for _ in range(7)]
dias = ["Dia 1", "Dia 2", "Dia 3", "Dia 4", "Dia 5", "Dia 6", "Dia 7"]

# Função para calcular o faturamento

def calcular_faturamento(vendas):
    faturamento_total = sum(vendas)
    return faturamento_total


# Função para calcular a média

def calcular_media(vendas_produtos):
    media = sum(vendas_produtos) / len(vendas_produtos)
    return media

# Função para calcular a maior venda

def identificar_maior_venda(vendas_produtos):
    maior_venda = max(vendas_produtos)
    return maior_venda


# Função para classificar desempenho

def classificar_desempenho(media):
    if media >= 3000:
        return "Desempenho excelente"
    elif media >= 1500:
        return "Desempenho satisfatório"
    else:
        return "Desempenho abaixo da meta"

# Chamando as funções

resultado = calcular_faturamento(vendas_produtos)
media_semanal = calcular_media(vendas_produtos)
maior_venda_semanal = identificar_maior_venda(vendas_produtos)
classificacao = classificar_desempenho(media_semanal)


# Visualização de dados

plt.bar(dias, vendas_produtos, color="blue")
plt.title("Desempenho de Vendas Semanal")
plt.xlabel("Dias da semana")
plt.ylabel("Vendas (R$)")
plt.show()


# Relatório

print(f"Faturamento total da semana: R$ {resultado:.2f}")
print(f"Média diária: R$ {media_semanal:.2f}")
print(f"Maior venda da semana: R$ {maior_venda_semanal:.2f}")
print(f"Classificação do desempenho: {classificacao}")

