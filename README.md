# Sistema Bancário em Python

Este é um projeto de um sistema bancário simples desenvolvido durante o bootcamp de Python AI Backend Developer da Digital Innovation One (DIO). 

O sistema permite que o usuário realize operações básicas como depósito, saque, criação de novos usuários e criação de novas contas, além da visualização de extrato.

## Funcionalidades

- **Depósito:** Permite que o usuário deposite um valor em sua conta.
- **Saque:** Permite que o usuário saque um valor de sua conta, respeitando um limite diário de R$500,00 e um máximo de 3 saques por dia.
- **Extrato:** Exibe o saldo atual e todas as transações realizadas.
- **Novo Usuário:** Permite cadastrar um novo usuário no sistema.
- **Nova Conta:** Permite criar uma nova conta bancária vinculada a um usuário existente.
- **Sair:** Encerra o programa.

## Como usar

Ao executar o programa, um menu será exibido com as seguintes opções:

[d] Depositar

[s] Sacar

[e] Extrato

[n] Nova Conta

[u] Novo Usuário

[q] Sair

O usuário deve selecionar uma opção digitando a letra correspondente:

- **Depósito (`d`)**
  - O usuário será solicitado a informar o valor do depósito.
  - Se o valor for positivo, ele será adicionado ao saldo e registrado no extrato.

- **Saque (`s`)**
  - O usuário será solicitado a informar o valor do saque.
  - O saque será permitido se:
    - O valor do saque não exceder o saldo disponível.
    - O valor do saque não exceder o limite diário de R$500,00.
    - O número de saques realizados no dia não exceder 3.
  - Se todas as condições forem atendidas, o valor será subtraído do saldo e registrado no extrato.

- **Extrato (`e`)**
  - Exibe todas as transações realizadas e o saldo atual.
  - Se não houver transações, será exibida uma mensagem informando que não foram realizadas movimentações.

- **Novo Usuário (`u`):**
  - Permite cadastrar um novo usuário no sistema.
  - O usuário deve informar CPF, nome completo, data de nascimento e endereço.

- **Nova Conta (`n`):**
  - Permite criar uma nova conta bancária vinculada a um usuário existente.
  - O usuário deve informar o CPF do titular da conta.

- **Sair (`q`)**
  - Encerra o programa.

## Requisitos

- Python 3.6 ou superior

## Como executar

1. Certifique-se de ter o Python 3.6 ou superior instalado em seu sistema.
2. Faça o download do código-fonte do projeto.
3. Navegue até o diretório onde o código-fonte está localizado.
4. Execute o script Python:

```bash
python sistema_bancario.py
