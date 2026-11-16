<div align="center">

# Cadastro e Classificação de Funcionários

**Módulo de RH em Python que padroniza o cadastro de funcionários e classifica a faixa salarial pelo terminal.**

![Python](https://img.shields.io/badge/Python-3-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Terminal](https://img.shields.io/badge/Interface-Terminal-4D4D4D?style=for-the-badge&logo=gnubash&logoColor=white)
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

Este projeto simula um módulo de cadastro de um sistema de Recursos Humanos.

**O problema:** sem um padrão, os cadastros de funcionários chegam com nomes digitados de formas diferentes (espaços sobrando, letras minúsculas ou maiúsculas misturadas) e sem uma categoria salarial definida, o que dificulta a organização das informações.

**A solução:** um programa que recebe os dados do funcionário pelo teclado, padroniza o nome, formata o salário com duas casas decimais e classifica o funcionário em uma de três faixas salariais, exibindo tudo em um relatório organizado.

---

## Funcionalidades

- [x] Solicitar nome completo, cargo, departamento e salário
- [x] Remover espaços desnecessários nas extremidades do nome
- [x] Exibir o nome com as iniciais maiúsculas
- [x] Exibir o salário com duas casas decimais
- [x] Classificar a faixa salarial (A, B ou C)
- [x] Exibir os dados cadastrados em formato de relatório

---

## Regras de negócio

| Faixa | Condição salarial |
|:-----:|-------------------|
| **A** | Salário inferior a R$ 2.000,00 |
| **B** | Salário entre R$ 2.000,00 e R$ 4.000,00 |
| **C** | Salário superior a R$ 4.000,00 |

Regras de padronização:

- O nome é exibido sem espaços nas extremidades.
- O nome é exibido com a inicial de cada palavra em maiúscula.
- O salário é exibido com duas casas decimais.

---

## Tecnologias utilizadas

| Categoria | Tecnologia / Recurso |
|-----------|----------------------|
| Linguagem | Python 3 |
| Entrada de dados | `input()` |
| Saída de dados | `print()` |
| Tratamento de texto | Métodos de manipulação de strings |
| Lógica de decisão | `if`, `elif`, `else` |
| Formatação | `.format()` e formatação de casas decimais |

O projeto usa apenas recursos nativos do Python, sem bibliotecas externas.

---

## Estrutura do projeto

```text
.
├── bd_employee.py
└── README.md
```

| Arquivo | Descrição |
|---------|-----------|
| `bd_employee.py` | Programa com a entrada de dados, a padronização do nome e a classificação salarial |
| `README.md` | Documentação do projeto |

---

## Como executar

**Pré-requisito:** [Python 3](https://www.python.org/downloads/) instalado.

1. Clone o repositório:

```bash
git clone <url-do-repositorio>
```

2. Acesse a pasta do projeto:

```bash
cd <nome-da-pasta>
```

3. Execute o programa:

```bash
python <nome-do-arquivo>.py
```

> Em alguns sistemas, o comando pode ser `python3`.

Não há dependências para instalar nem variáveis de ambiente para configurar.

---

## Exemplo de utilização

Saída esperada para um funcionário com salário de R$ 3.500,00:

```text
================================
       CADASTRO DE FUNCIONÁRIO
================================
Nome: Mariana Oliveira
Cargo: Analista de Dados
Departamento: Tecnologia
Salário: R$ 3500.00

CLASSIFICAÇÃO SALARIAL: FAIXA B
================================
```

---

## Aprendizados

Este projeto reúne fundamentos de Python aplicados a um cenário de negócio:

- Entrada e saída de dados com `input()` e `print()`.
- Manipulação de strings para padronizar texto digitado pelo usuário.
- Estruturas condicionais (`if`, `elif`, `else`) para implementar regras de negócio.
- Formatação de texto e de números com `.format()`, incluindo casas decimais.
- Tradução de requisitos de negócio em código.

---

## Melhorias futuras

> Ideias para evolução. **Ainda não implementadas.**

- [ ] Validar os dados informados (campos vazios e salário inválido)
- [ ] Cadastrar vários funcionários na mesma execução
- [ ] Salvar os cadastros em arquivo
- [ ] Organizar o código em funções
