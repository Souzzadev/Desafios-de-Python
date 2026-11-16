<div align="center">

# Comprovante de Processamento de Pedidos

**Programa em Python que gera, no terminal, um comprovante textual organizado para um pedido de loja virtual.**

![Python](https://img.shields.io/badge/Python-3-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Terminal](https://img.shields.io/badge/Interface-Terminal-4D4D4D?style=for-the-badge&logo=gnubash&logoColor=white)
![Nível](https://img.shields.io/badge/N%C3%ADvel-B%C3%A1sico-2EA44F?style=for-the-badge)

</div>

---

## Índice

- [Sobre o projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Regras de negócio](#regras-de-negócio)
- [Dados do pedido](#dados-do-pedido)
- [Tecnologias utilizadas](#tecnologias-utilizadas)
- [Estrutura do comprovante](#estrutura-do-comprovante)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Como executar](#como-executar)
- [Exemplo de utilização](#exemplo-de-utilização)
- [Aprendizados](#aprendizados)
- [Melhorias futuras](#melhorias-futuras)

---

## Sobre o projeto

Este projeto simula a saída de um módulo de processamento de pedidos de um sistema de e-commerce.

**O problema:** depois que um pedido é processado, os funcionários da loja precisam visualizar rapidamente os dados da compra, sem procurar informações espalhadas pelo sistema.

**A solução:** um programa que exibe um comprovante textual com o número do pedido, o cliente, os produtos adquiridos, a quantidade, o valor total em reais e o status do pedido, separados em seções para facilitar a leitura.

---

## Funcionalidades

- [x] Exibir o número do pedido
- [x] Exibir o nome do cliente
- [x] Exibir cada produto adquirido em uma linha, com seu valor
- [x] Exibir a quantidade de produtos
- [x] Exibir o valor total da compra em reais
- [x] Exibir o status do pedido em destaque

---

## Regras de negócio

- O comprovante possui **cabeçalho**.
- Os produtos aparecem **individualmente**, um por linha.
- Os valores são identificados em **reais (R$)**.
- O status aparece **em destaque textual**, em letras maiúsculas.
- As seções são separadas por **caracteres decorativos**.

---

## Dados do pedido

O comprovante é gerado a partir de um pedido fictício:

| Campo | Valor |
|-------|-------|
| Pedido | #20261145 |
| Cliente | Lucas Ferreira |
| Status | Aprovado |

| Produto | Valor |
|---------|------:|
| Notebook | R$ 3.500,00 |
| Mouse | R$ 120,00 |
| Teclado | R$ 250,00 |
| **Total (3 produtos)** | **R$ 3.870,00** |

---

## Tecnologias utilizadas

| Categoria | Tecnologia / Recurso |
|-----------|----------------------|
| Linguagem | Python 3 |
| Saída de dados | `print()`, com múltiplas chamadas |
| Formatação visual | Caracteres de separação (`=`) para dividir as seções |

O projeto usa apenas recursos nativos do Python, sem bibliotecas externas.

---

## Estrutura do projeto

```text
.
├── <nome-do-arquivo>.py
└── README.md
```

| Arquivo | Descrição |
|---------|-----------|
| `processamento_pedidos.py` | Programa que imprime o comprovante do pedido |
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
cd desafios-python/desafio-02-comprovante-pedidos
```

3. Execute o programa:

```bash
python <nome-do-arquivo>.py
```

> Em alguns sistemas, o comando pode ser `python3`.

Não há dependências para instalar nem variáveis de ambiente para configurar.

---

## Exemplo de utilização

Saída esperada ao executar o programa:

```text
========== COMPROVANTE ==========
Pedido: #20261145
Cliente: Lucas Ferreira

PRODUTOS:
Notebook - R$ 3.500,00
Mouse - R$ 120,00
Teclado - R$ 250,00

Quantidade: 3 produtos
Total: R$ 3.870,00
Status: APROVADO
================================
```

---

## Aprendizados

- Uso de `print()` para montar uma saída completa, com múltiplas chamadas.
- Organização de um texto em seções (cabeçalho, produtos, resumo e rodapé).
- Uso de caracteres para separar seções e dar identidade visual a uma saída de terminal.
- Apresentação de valores monetários em reais.
- Destaque textual de informações importantes, como o status do pedido.

---

## Melhorias futuras

> Ideias para evolução. **Ainda não implementadas.**

- [ ] Receber os dados do pedido pelo teclado
- [ ] Calcular automaticamente o total e a quantidade de produtos
- [ ] Gerar o comprovante para pedidos com quantidades variadas de produtos
- [ ] Salvar o comprovante em arquivo
