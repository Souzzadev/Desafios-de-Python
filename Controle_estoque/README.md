<div align="center">

# Relatório de Controle de Estoque

**Programa em Python que recebe os dados de um produto, classifica o nível do estoque, orienta o setor de compras e exibe um gráfico comparando o estoque atual com o mínimo.**

![Python](https://img.shields.io/badge/Python-3-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=plotly&logoColor=white)
![Nível](https://img.shields.io/badge/N%C3%ADvel-B%C3%A1sico-2EA44F?style=for-the-badge)

</div>

---

## Índice

- [Sobre o projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Regras de negócio](#regras-de-negócio)
- [Tecnologias utilizadas](#tecnologias-utilizadas)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Como executar](#como-executar)
- [Exemplo de utilização](#exemplo-de-utilização)
- [Aprendizados](#aprendizados)
- [Melhorias futuras](#melhorias-futuras)

---

## Sobre o projeto

Este projeto simula um módulo de controle de estoque, no qual é possível acompanhar a situação de um produto e decidir se há necessidade de reposição.

**O problema:** para saber se um produto precisa ser reabastecido, é preciso comparar a quantidade disponível com o mínimo desejado e calcular o valor imobilizado em estoque.

**A solução:** um programa que recebe os dados do produto pelo teclado, calcula o valor total em estoque, classifica a situação do estoque, indica a orientação para o setor de compras, imprime um relatório no terminal e exibe um gráfico de barras com a quantidade atual e a mínima.

---

## Funcionalidades

- [x] Receber nome, ID, quantidade em estoque, quantidade mínima e preço unitário do produto
- [x] Calcular o valor total em estoque (quantidade × preço unitário)
- [x] Classificar a situação do estoque em quatro níveis
- [x] Indicar a orientação para o setor de compras
- [x] Exibir um relatório formatado no terminal
- [x] Exibir um gráfico de barras comparando estoque atual e estoque mínimo

---

## Regras de negócio

**Classificação do estoque**

| Condição | Classificação |
|----------|---------------|
| Quantidade em estoque igual a zero | Sem estoque |
| Quantidade em estoque menor que a mínima | Estoque crítico |
| Quantidade em estoque igual à mínima | Estoque no limite |
| Quantidade em estoque maior que a mínima | Estoque adequado |

**Orientação para o setor de compras**

| Condição | Orientação |
|----------|------------|
| Quantidade em estoque menor ou igual à mínima | Solicitar reposição ao setor de compras. |
| Quantidade em estoque maior que a mínima | Manter o estoque atual. |

**Cálculo:** `total em estoque = quantidade em estoque × preço unitário`

---

## Tecnologias utilizadas

| Categoria | Tecnologia / Recurso |
|-----------|----------------------|
| Linguagem | Python 3 |
| Visualização de dados | [Matplotlib](https://matplotlib.org/) (`pyplot`, gráfico de barras) |
| Entrada de dados | `input()`, com conversão para `int` e `float` |
| Lógica de decisão | `if`, `elif`, `else` |
| Formatação de texto | `f-string`, `.center()`, multiplicação de strings e `:.2f` |
| Estruturas de dados | Listas |

---



## Estrutura do projeto

```text
.
├── <nome-do-arquivo>.py
└── README.md
```

| Arquivo | Descrição |
|---------|-----------|
| `<nome-do-arquivo>.py` | Programa com entrada de dados, classificação do estoque, relatório e gráfico |
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
cd desafios-python/desafio-04-relatorio-estoque
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

## Exemplo de utilização

> Exemplo ilustrativo, com dados fictícios.

**Entradas:**

```text
Digite o nome do produto: Teclado
Digite o ID do produto: 1001
Digite a quantidade em estoque: 8
Digite a quantidade mínima em estoque: 10
Digite o preço unitário do produto: 250
```

**Relatório exibido:**

```text
========================================
          RELATÓRIO DE ESTOQUE
========================================
Produto: Teclado
ID do produto: 1001
Quantidade disponível: 8
Quantidade mínima: 10
Preço unitário: R$ 250.00
Total em estoque: R$ 2000.00
Classificação: Estoque crítico
Orientação: Solicitar reposição ao setor de compras.
========================================
```

Em seguida, o programa abre um gráfico de barras com as colunas **Estoque atual** e **Estoque mínimo**.

---

## Aprendizados

- Entrada de dados com `input()` e conversão de tipos para `int` e `float`.
- Cálculos a partir dos dados informados pelo usuário.
- Estruturas condicionais encadeadas para classificar situações de negócio.
- Formatação de relatórios no terminal com `f-string`, `.center()` e `:.2f`.
- Uso de listas para organizar os dados de um gráfico.
- Criação de um gráfico de barras com Matplotlib, com título, rótulos de eixos e cores.

---

## Melhorias futuras

> Ideias para evolução. **Ainda não implementadas.**

- [ ] Validar as entradas (valores negativos ou texto no lugar de números)
- [ ] Cadastrar e comparar vários produtos na mesma execução
- [ ] Exibir o preço no formato brasileiro (R$ com vírgula)
- [ ] Salvar o relatório em arquivo