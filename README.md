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

> A tabela é atualizada a cada novo desafio concluído.

---

## Estrutura do repositório

```text
desafios-python/
├── README.md
└── desafio-01-cadastro-funcionarios/
    ├── README.md
    └── cadastro_funcionarios.py
└── desafio-02-controle_estoques/
    ├── README.md
    └── processamento_pedidos.py
```
---

## Como executar um desafio

**Pré-requisito:** [Python 3](https://www.python.org/downloads/) instalado.

1. Clone o repositório:

```bash
git clone <url-do-repositorio>
```

2. Acesse a pasta do desafio desejado:

```bash
cd desafios-python/desafio-01-cadastro-funcionarios
```

3. Execute o programa:

```bash
python cadastro_funcionarios.py
```

> Em alguns sistemas, o comando pode ser `python3`.

Os desafios usam apenas recursos nativos do Python. Se algum precisar de dependências, isso estará indicado no README da respectiva pasta.

---

## Evolução

Este repositório mostra o meu progresso na prática de Python. Os primeiros desafios são de nível básico, e novos níveis serão adicionados conforme eu avançar nos estudos.

- [x] Desafio 01: Cadastro e classificação de funcionários
- [x] Desafio 02: Controle de estoque
