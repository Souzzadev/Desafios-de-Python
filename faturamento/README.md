<div align="center">

# Calculadora de Faturamento

**Função em Python que calcula o valor total de uma venda a partir da quantidade e do preço unitário.**

![Python](https://img.shields.io/badge/Python-3-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Terminal](https://img.shields.io/badge/Interface-Terminal-4D4D4D?style=for-the-badge&logo=gnubash&logoColor=white)

</div>

---

## Índice

- [Sobre o projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [A função calcular_faturamento](#a-função-calcular_faturamento)
- [Tecnologias e recursos utilizados](#tecnologias-e-recursos-utilizados)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Como executar](#como-executar)
- [Exemplo de utilização](#exemplo-de-utilização)
- [Aprendizados](#aprendizados)
- [Melhorias futuras](#melhorias-futuras)

---

## Sobre o projeto

Este projeto simula uma tarefa de assistente de dados em uma empresa de comércio eletrônico: o setor financeiro precisa calcular o faturamento de cada venda.

**O problema:** o cálculo do valor total de uma venda (quantidade vezes preço unitário) é repetido a cada venda registrada, e escrevê-lo de novo em cada ponto do código gera repetição e risco de erros.

**A solução:** uma função reutilizável, `calcular_faturamento`, que recebe a quantidade e o preço unitário, calcula o faturamento, devolve o resultado com `return` e o apresenta com duas casas decimais.

---

## Funcionalidades

- [x] Função `calcular_faturamento` que recebe quantidade e preço unitário
- [x] Cálculo do faturamento da venda
- [x] Devolução do resultado com `return`
- [x] Exibição do resultado com duas casas decimais

---

## A função calcular_faturamento

| Item | Descrição |
|------|-----------|
| **Nome** | `calcular_faturamento` |
| **Parâmetros** | Quantidade vendida e preço unitário |
| **Cálculo** | `faturamento = quantidade × preço unitário` |
| **Retorno** | Valor total da venda, devolvido com `return` |
| **Apresentação** | Resultado exibido com duas casas decimais |

---

## Tecnologias e recursos utilizados

| Categoria | Recurso |
|-----------|---------|
| Linguagem | Python 3 |
| Funções | Definição com `def`, parâmetros e `return` |
| Formatação numérica | Exibição com duas casas decimais |
| Saída de dados | `print()` |

O projeto usa apenas recursos nativos do Python, sem bibliotecas externas.

---

## Estrutura do projeto

```text
.
├── calculo_faturamento.py
└── README.md
```

| Arquivo | Descrição |
|---------|-----------|
| `calculo_faturamento.py` | Programa com a função `calcular_faturamento` e a exibição do resultado |
| `README.md` | Documentação do desafio |

---

## Como executar

**Pré-requisito:** [Python 3](https://www.python.org/downloads/) instalado.

1. Clone o repositório:

```bash
git clone <url-do-repositorio>
```

2. Acesse a pasta do desafio:

```bash
cd desafios-python/desafio-05-calculadora-faturamento
```

3. Execute o programa:

```bash
python <nome-do-arquivo>.py
```

> Em alguns sistemas, o comando pode ser `python3`.

Não há dependências para instalar nem variáveis de ambiente para configurar.

---

## Exemplo de utilização

> Exemplo ilustrativo, com dados fictícios.

Uma venda de **3 unidades** de um produto a **R$ 25,50** cada tem faturamento de 3 × 25,50 = **76,50**, exibido com duas casas decimais.

---

## Aprendizados

- Definição de funções com `def` e uso de parâmetros.
- Retorno de valores com `return`, separando o cálculo da exibição do resultado.
- Reutilização de código: a mesma função atende qualquer venda.
- Formatação de números com duas casas decimais.
- Tradução de uma necessidade do setor financeiro em código.

---

## Melhorias futuras

> Ideias para evolução. **Ainda não implementadas.**

- [ ] Receber quantidade e preço pelo teclado
- [ ] Validar os valores informados (números negativos ou texto)
- [ ] Calcular o faturamento de várias vendas e somar o total
- [ ] Exibir o valor no formato brasileiro (R$ com vírgula)