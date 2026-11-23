<div align="center">

# Desafios de Python

**Prática de programação em Python, com desafios baseados em cenários profissionais, desenvolvidos à medida que aprendo cada conceito.**

![Python](https://img.shields.io/badge/Python-3-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em%20andamento-F2A900?style=for-the-badge)

</div>

---

## Índice

- [Sobre o repositório](#sobre-o-repositório)
- [Como o repositório funciona](#como-o-repositório-funciona)
- [Desafios](#desafios)
- [Estrutura do repositório](#estrutura-do-repositório)
- [Como executar um desafio](#como-executar-um-desafio)
- [Evolução](#evolução)

---

## Sobre o repositório

Este repositório reúne os desafios de Python que resolvo para praticar o que estou aprendendo. A cada conceito novo estudado, aplico o conteúdo em um exercício, para fixar a teoria e treinar a lógica de programação.

Os desafios partem de situações próximas do ambiente profissional, como cadastros, regras de negócio e classificações. Cada um tem **contexto**, **problema de negócio**, **requisitos funcionais**, **regras de negócio** e **critérios de aceitação**, para que a prática se pareça com um pedido real de trabalho.

---

## Como o repositório funciona

- Cada desafio fica em **uma pasta própria**, numerada na ordem em que foi resolvido.
- Dentro de cada pasta há o **código-fonte** e um **README** que explica o desafio, as regras de negócio, os conceitos praticados e como executar.
- O repositório cresce junto com meu aprendizado: novos desafios são adicionados conforme avanço nos estudos.

---

## Desafios

| # | Desafio | Nível | Conceitos praticados |
|:-:|---------|:-----:|----------------------|
| 01 | [Cadastro e classificação de funcionários](desafio-01-cadastro-funcionarios) | Básico | `input()`, `print()`, strings, `if`/`elif`/`else`, `.format()`, casas decimais |
| 02 | [Comprovante de processamento de pedidos](desafio-02-comprovante-pedidos) | Básico | `print()`, múltiplas chamadas de `print()`, separadores de seção |
| 03 | [Controle de estoque](desafio-03-controle-estoque) | Básico | `input()`, `int`/`float`, `if`/`elif`/`else`, `f-string`, `.center()`, listas, Matplotlib |
| 04 | [Calculadora de faturamento](desafio-04-calculadora-faturamento) | Básico | Funções (`def`), parâmetros, `return`, duas casas decimais |
| 05 | [Simulador de desempenho de vendas](desafio-05-simulador-desempenho-vendas) | Intermediário | `random`, listas, funções (`def`), `return`, Matplotlib |
| 06 | [Análise de desempenho financeiro](desafio-06-analise-desempenho-financeiro) | Intermediário | Listas, `lambda`, `map()`, funções (`def`), `return`, Matplotlib |

> A tabela é atualizada a cada novo desafio concluído.

---

## Estrutura do repositório

```text
desafios-python/
├── README.md
├── desafio-01-cadastro-funcionarios/
│   ├── README.md
│   └── bd_employee.py
├── desafio-02-comprovante-pedidos/
│   ├── README.md
│   └── processamento_pedidos.py
├── desafio-03-controle-estoque/
│   ├── README.md
│   └── controle_estoque.py
└── desafio-04-calculadora-faturamento/
│   ├── README.md
│   └── calculo_faturamento.py
└── desafio-05-simulador-desempenho-vendas/
│   ├── README.md
│   └── desempenho_vendas.py
└── desafio-06-analise-desempenho-financeiro/
    ├── README.md
    └── analise_financeiro.py
```

---

## Como executar um desafio

**Pré-requisito:** [Python 3](https://www.python.org/downloads/) instalado.

1. Clone o repositório:

```bash
git clone <url-do-repositorio>
```

2. Acesse a pasta do desafio desejado (exemplo com o Desafio 01):

```bash
cd desafios-python/desafio-01-cadastro-funcionarios
```

3. Execute o programa:

```bash
python bd_employee.py
```

> Em alguns sistemas, o comando pode ser `python3`.

A maioria dos desafios usa apenas recursos nativos do Python. O **Desafio 03** usa a biblioteca Matplotlib, que deve ser instalada antes de executar:

```bash
pip install matplotlib
```

O README de cada pasta indica as dependências e o arquivo a ser executado.

---

## Evolução

Este repositório mostra o meu progresso na prática de Python. Os primeiros desafios são de nível básico, e novos níveis serão adicionados conforme eu avançar nos estudos.

- [x] Desafio 01: Cadastro e classificação de funcionários
- [x] Desafio 02: Comprovante de processamento de pedidos
- [x] Desafio 03: Controle de estoque
- [x] Desafio 04: Calculadora de faturamento
- [x] Desafio 05: Simulador de desempenho de vendas
- [x] Desafio 06: Análise de desempenho financeiro