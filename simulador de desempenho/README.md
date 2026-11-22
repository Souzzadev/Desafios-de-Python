<div align="center">

# Simulador de Desempenho de Vendas

**Programa em Python que simula as vendas de uma equipe durante 7 dias, processa os dados com funções, classifica o desempenho e apresenta o resultado em um relatório e em um gráfico de barras.**

![Python](https://img.shields.io/badge/Python-3-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=plotly&logoColor=white)
![Nível](https://img.shields.io/badge/N%C3%ADvel-Intermedi%C3%A1rio-1F6FEB?style=for-the-badge)

</div>

---

## Índice

- [Sobre o projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Regras de negócio](#regras-de-negócio)
- [Funções do programa](#funções-do-programa)
- [Tecnologias utilizadas](#tecnologias-utilizadas)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Como executar](#como-executar)
- [Exemplo de utilização](#exemplo-de-utilização)
- [Aprendizados](#aprendizados)
- [Melhorias futuras](#melhorias-futuras)

---

## Sobre o projeto

Este projeto simula uma solicitação do gestor comercial de uma empresa de comércio eletrônico: acompanhar o desempenho de vendas de uma equipe ao longo de 7 dias.

**O problema:** o gestor precisa de uma visão rápida do resultado da semana, com o faturamento total, a média diária, a melhor venda e uma avaliação do desempenho, sem analisar os números um a um.

**A solução:** um programa que gera as vendas diárias de forma aleatória, processa os dados com funções específicas, classifica o desempenho da equipe a partir da média diária e apresenta o resultado em um relatório no terminal e em um gráfico de barras.

---

## Funcionalidades

- [x] Gerar 7 valores aleatórios de vendas, um para cada dia
- [x] Armazenar as vendas em uma lista
- [x] Calcular o faturamento total
- [x] Calcular a média diária de vendas
- [x] Identificar a maior venda
- [x] Classificar o desempenho da equipe
- [x] Exibir um relatório com os resultados
- [x] Exibir um gráfico de barras com as vendas por dia

---

## Regras de negócio

**Geração dos dados**

- São geradas vendas para **7 dias**.
- Cada dia tem um valor aleatório entre **R$ 500 e R$ 5.000**.

**Classificação do desempenho** (com base na média diária)

| Média diária | Classificação |
|--------------|---------------|
| Igual ou superior a R$ 3.000 | Desempenho excelente |
| Igual ou superior a R$ 1.500 | Desempenho satisfatório |
| Abaixo de R$ 1.500 | Desempenho abaixo da meta |

---

## Funções do programa

| Função | Recebe | Faz | Retorna |
|--------|--------|-----|---------|
| `calcular_faturamento(vendas)` | Lista de vendas | Soma todas as vendas | Faturamento total |
| `calcular_media(vendas)` | Lista de vendas | Calcula a média diária | Média diária |
| `identificar_maior_venda(vendas)` | Lista de vendas | Identifica a maior venda | Valor da maior venda |
| `classificar_desempenho(media)` | Média diária | Aplica as faixas de desempenho | Classificação em texto |

---

## Tecnologias utilizadas

| Categoria | Tecnologia / Recurso |
|-----------|----------------------|
| Linguagem | Python 3 |
| Geração de dados | Módulo `random`, com `random.randint()` |
| Visualização de dados | [Matplotlib](https://matplotlib.org/) (`matplotlib.pyplot`, gráfico de barras) |
| Organização do código | Funções com `def` e `return` |
| Estruturas de dados | Listas |
| Lógica de decisão | `if`, `elif`, `else` |

Além de `random` e `matplotlib`, o projeto não utiliza outras bibliotecas e não usa `lambda`.


---

## Estrutura do projeto

```text
.
├── desempenho_vendas.py
└── README.md
```

| Arquivo | Descrição |
|---------|-----------|
| `desempenho_vendas.py` | Programa com a geração dos dados, as funções de cálculo, o relatório e o gráfico |
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
cd desafios-python/desafio-05-simulador-desempenho-vendas
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

O relatório apresenta as vendas dos 7 dias e os indicadores calculados. Como as vendas são aleatórias, os valores mudam a cada execução.

> Exemplo ilustrativo dos indicadores, com valores fictícios.

```text
Faturamento total: R$ 18.500
Média diária: R$ 2.642,86
Maior venda: R$ 4.500
Dias analisados: 7
Classificação: Desempenho satisfatório
```

Em seguida, o programa abre um gráfico de barras com:

- **Título:** Desempenho de vendas semanal
- **Eixo X:** dias da semana (Dia 1 até Dia 7)
- **Eixo Y:** valor das vendas

---

## Aprendizados

- Geração de dados aleatórios com `random.randint()`.
- Armazenamento e processamento de dados em listas.
- Criação de funções com `def`, cada uma com uma responsabilidade bem definida.
- Uso de `return` para devolver resultados e reaproveitá-los em outras partes do programa.
- Aplicação de regras de negócio com estruturas condicionais.
- Construção de um relatório no terminal e de um gráfico de barras com Matplotlib.
- Integração de vários conceitos (listas, funções, condicionais e visualização) em um único projeto.

---

## Melhorias futuras

> Ideias para evolução. **Ainda não implementadas.**

- [ ] Permitir que o usuário escolha o número de dias simulados
- [ ] Destacar no gráfico o dia da maior venda
- [ ] Exibir a média diária como linha de referência no gráfico
- [ ] Salvar o gráfico como imagem
- [ ] Exibir os valores no formato brasileiro (R$ com vírgula)