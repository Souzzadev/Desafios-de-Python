<div align="center">

# Comprovante de processamento de pedidos

**Script em Python que armazena os dados de um pedido em variáveis e listas, processa as informações dos produtos e gera um comprovante organizado no terminal.**

![Python](https://img.shields.io/badge/Python-3-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Terminal](https://img.shields.io/badge/Interface-Terminal-4D4D4D?style=for-the-badge&logo=gnubash&logoColor=white)
![Nível](https://img.shields.io/badge/N%C3%ADvel-B%C3%A1sico-2EA44F?style=for-the-badge)

</div>

---

## Índice

- [Sobre o projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Dados do pedido](#dados-do-pedido)
- [Tecnologias e recursos utilizados](#tecnologias-e-recursos-utilizados)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Como executar](#como-executar)
- [Exemplo de utilização](#exemplo-de-utilização)
- [Aprendizados](#aprendizados)
- [Melhorias futuras](#melhorias-futuras)

---

## Sobre o projeto

Este projeto simula uma tarefa de estágio em Engenharia de Dados em uma empresa de comércio eletrônico: a equipe de operações precisa de um pequeno programa para organizar as informações dos pedidos feitos pelos clientes.

**O problema:** os dados de um pedido (número, cliente, produtos, preços e status) ficam separados e precisam ser reunidos em um documento fácil de conferir.

**A solução:** um script que armazena esses dados em variáveis e listas, calcula a quantidade de produtos e o valor total do pedido, seleciona o status atual e exibe tudo em um comprovante formatado no terminal.

---


## Funcionalidades

- [x] Armazenar número do pedido e nome do cliente em variáveis
- [x] Armazenar produtos, preços e status possíveis em listas
- [x] Calcular a quantidade de produtos do pedido
- [x] Calcular o valor total do pedido
- [x] Selecionar o status atual do pedido ("Em Separação")
- [x] Exibir a relação de produtos com seus respectivos preços
- [x] Exibir valores em reais, com duas casas decimais e vírgula decimal
- [x] Exibir o título centralizado e divisórias entre as seções

---

## Dados do pedido

| Campo | Valor |
|-------|-------|
| Número do pedido | 1202 |
| Cliente | MARCOS VILAR |
| Status atual | Em Separação |

**Produtos e preços**

| Produto | Preço |
|---------|------:|
| Notebook | R$ 3.500,00 |
| Mouse | R$ 120,00 |
| Teclado | R$ 250,00 |

**Status disponíveis:** Aguardando Pagamento, Em Separação, Enviado e Entregue.

---

## Tecnologias e recursos utilizados

| Categoria | Recurso |
|-----------|---------|
| Linguagem | Python 3 |
| Armazenamento de dados | Variáveis e listas |
| Acesso aos dados | Índices de listas |
| Processamento | `len()` e `sum()` |
| Formatação de texto | `f-string`, `.center()`, multiplicação de strings e `.replace()` |
| Formatação numérica | `:.2f` (duas casas decimais) |
| Saída de dados | `print()` |

O projeto usa apenas recursos nativos do Python, sem bibliotecas externas.

---

## Estrutura do projeto

```text
.
├── processamento_pedidos.py
└── README.md
```

| Arquivo | Descrição |
|---------|-----------|
| `processamento_pedidos.py` | Script que armazena os dados do pedido, processa as informações e imprime o comprovante |
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
cd desafios-python/desafio-03-sistema-comprovante-pedido
```

3. Execute o programa:

```bash
python <nome-do-arquivo>.py
```

> Em alguns sistemas, o comando pode ser `python3`.

Não há dependências para instalar nem variáveis de ambiente para configurar.

---

## Exemplo de utilização

Resultado esperado ao executar o programa:

```text
======== COMPROVANTE =========
Pedido: #1202
Cliente: MARCOS VILAR

PRODUTOS:
Notebook - R$ 3500,00
Mouse - R$ 120,00
Teclado - R$ 250,00

Quatidade: 3 Produtos
Total: R$3870.0
Status: Em Separação
==============================

```

> No terminal, o título aparece centralizado e as seções são separadas por divisórias.

---

## Aprendizados

- Armazenamento de dados em variáveis e listas.
- Acesso a elementos de listas por índice.
- Uso de `len()` para contar elementos e de `sum()` para somar valores.
- Formatação de texto com `f-string`, `.center()` e multiplicação de strings.
- Formatação de números com `:.2f` e ajuste do separador decimal com `.replace()`.
- Organização de dados e saída em um fluxo simples: armazenar, processar e exibir.

---

## Melhorias futuras

> Ideias para evolução. **Ainda não implementadas.**

- [ ] Receber os dados do pedido pelo teclado
- [ ] Permitir escolher o status entre as opções disponíveis
- [ ] Exibir o preço junto ao produto percorrendo as listas com um laço de repetição
- [ ] Salvar o comprovante em arquivo