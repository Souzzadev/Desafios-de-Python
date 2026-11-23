<div align="center">

# Análise de Desempenho Financeiro

**Programa em Python que aplica um desconto ao faturamento de cinco produtos, calcula indicadores com funções e compara os resultados em um gráfico de barras.**

![Python](https://img.shields.io/badge/Python-3-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=plotly&logoColor=white)
![Nível](https://img.shields.io/badge/N%C3%ADvel-Intermedi%C3%A1rio-1F6FEB?style=for-the-badge)

</div>

---

## Índice

- [Sobre o projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Dados e resultados esperados](#dados-e-resultados-esperados)
- [Funções do programa](#funções-do-programa)
- [Tecnologias utilizadas](#tecnologias-utilizadas)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Como executar](#como-executar)
- [Relatório e gráfico](#relatório-e-gráfico)
- [Aprendizados](#aprendizados)
- [Melhorias futuras](#melhorias-futuras)

---

## Sobre o projeto

Este projeto simula uma solicitação do setor financeiro de uma empresa de comércio eletrônico: analisar o desempenho de cinco produtos a partir dos valores de faturamento disponibilizados.

**O problema:** o setor financeiro precisa visualizar o desempenho de cada produto depois de aplicado um desconto de 10% sobre o faturamento, além de conhecer o total e a média do faturamento líquido.

**A solução:** um programa que transforma os valores com uma função `lambda` e `map()`, calcula o total e a média com funções, apresenta um relatório e constrói um gráfico de barras para comparar os cinco produtos.

---

## Funcionalidades

- [x] Armazenar produtos e faturamento em listas
- [x] Aplicar desconto de 10% ao faturamento de cada produto com `lambda` e `map()`
- [x] Armazenar o resultado na lista `faturamento_liquido`
- [x] Calcular o faturamento líquido total
- [x] Calcular a média do faturamento líquido
- [x] Exibir um relatório com os valores originais, os valores após o desconto e os indicadores
- [x] Exibir um gráfico de barras comparando os cinco produtos

---

## Dados e resultados esperados

Os dados de entrada são fixos, definidos em duas listas:

```python
produtos = ["Notebook", "Mouse", "Teclado", "Monitor", "Headset"]
faturamento = [8500, 2300, 4100, 7200, 1800]
```

Aplicando o desconto de 10% (valor após o desconto = 90% do faturamento), os valores esperados são:

| Produto | Faturamento original | Faturamento após desconto |
|---------|---------------------:|--------------------------:|
| Notebook | R$ 8.500,00 | R$ 7.650,00 |
| Mouse | R$ 2.300,00 | R$ 2.070,00 |
| Teclado | R$ 4.100,00 | R$ 3.690,00 |
| Monitor | R$ 7.200,00 | R$ 6.480,00 |
| Headset | R$ 1.800,00 | R$ 1.620,00 |
| **Total** | **R$ 23.900,00** | **R$ 21.510,00** |

| Indicador | Valor |
|-----------|------:|
| Faturamento líquido total | R$ 21.510,00 |
| Média de faturamento líquido | R$ 4.302,00 |

> Valores calculados a partir dos dados do enunciado.

---

## Funções do programa

**Função `lambda`**

| Item | Descrição |
|------|-----------|
| **Recebe** | Um valor de faturamento |
| **Faz** | Calcula o valor após o desconto de 10% |
| **Aplicação** | Usada com `map()` sobre os cinco produtos, com o resultado armazenado em `faturamento_liquido` |

**Funções com `def`**

| Função | Recebe | Faz | Retorna |
|--------|--------|-----|---------|
| `calcular_faturamento_total(valores)` | Lista de faturamento líquido | Soma todos os valores | Total |
| `calcular_media_faturamento(valores)` | Lista de faturamento líquido | Calcula a média | Média |

---

## Tecnologias utilizadas

| Categoria | Tecnologia / Recurso |
|-----------|----------------------|
| Linguagem | Python 3 |
| Estruturas de dados | Listas |
| Programação funcional | Função `lambda` e `map()` |
| Organização do código | Funções com `def` e `return` |
| Visualização de dados | [Matplotlib](https://matplotlib.org/) (`matplotlib.pyplot`, gráfico de barras) |

O projeto não utiliza outras bibliotecas além do Matplotlib.

---

## Estrutura do projeto

```text
.
├── analise_financeiro.py
└── README.md
```

| Arquivo | Descrição |
|---------|-----------|
| `analise_financeiro.py` | Programa com os dados, a função `lambda`, as funções de cálculo, o relatório e o gráfico |
| `README.md` | Documentação do desafio |

---

## Como executar

**Pré-requisitos:** [Python 3](https://www.python.org/downloads/) e a biblioteca Matplotlib.

1. Clone o repositório:

```bash
git clone <url-do-repositorio>
```

2. Acesse a pasta do desafio:

```bash
cd desafios-python/desafio-06-analise-desempenho-financeiro
```

3. Instale a dependência:

```bash
pip install matplotlib
```

4. Execute o programa:

```bash
python <nome-do-arquivo>.py
```

> Em alguns sistemas, os comandos podem ser `python3` e `pip3`.

O gráfico abre em uma janela própria, por isso é necessário um ambiente com interface gráfica.

---

## Relatório e gráfico

Ao final da execução, o programa apresenta:

- O nome dos cinco produtos.
- O faturamento original de cada produto.
- O faturamento após o desconto.
- O faturamento líquido total.
- A média de faturamento líquido.
- Um gráfico comparativo.

O gráfico de barras tem as seguintes características:

- **Título:** Faturamento líquido por produto
- **Eixo X:** nomes dos produtos
- **Eixo Y:** faturamento líquido

---

## Aprendizados

- Armazenamento de dados relacionados em listas paralelas.
- Uso de funções `lambda` para expressar uma regra simples em uma única linha.
- Aplicação de uma função a todos os elementos de uma lista com `map()`.
- Criação de funções com `def`, cada uma com uma responsabilidade definida, e uso de `return`.
- Cálculo de indicadores como total e média.
- Construção de um gráfico de barras comparativo com Matplotlib.
- Integração de vários conceitos (listas, `lambda`, `map()`, funções e visualização) em um único projeto.

---

## Melhorias futuras

> Ideias para evolução. **Ainda não implementadas.**

- [ ] Permitir que o usuário informe o percentual de desconto
- [ ] Destacar no gráfico o produto de maior faturamento
- [ ] Exibir a média como linha de referência no gráfico
- [ ] Salvar o gráfico como imagem
- [ ] Exibir os valores no formato brasileiro (R$ com vírgula)