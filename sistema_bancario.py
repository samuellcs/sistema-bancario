import textwrap


def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [n]\tNova Conta
    [u]\tNovo Usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"\nDepósito realizado com sucesso!")

    else:
        print("Operação falhou!\nO valor informado é inválido.")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou!\nVocê não possui saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou!\nO valor do saque excede o limite permitido.")

    elif excedeu_saques:
        print("Operação falhou!\nNúmero máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"\nSaque efetuado com sucesso!")

    else:
        print("Operação falhou!\nO valor informado é inválido.")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):

    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def novo_usuario(usuarios):
    cpf = input("Informe o CPF(somente números):")
    usuario = filtrar_usuario(cpf, usuarios)

    if not cpf.isdigit() or len(cpf) != 11:
        print("CPF inválido! O CPF deve conter exatamente 11 dígitos.")
        return

    if usuario:
        print(f"\nJá existe usuário com esse CPF!")
        return

    nome = input("Informe o seu nome completo: ")
    data_nascimento = input(
        "Informe a sua data de Nascimento:\n(dd-mm-aaaa): ")
    endereco = input("informe o seu endereço(cidade,estado,bairro): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento,
                    "cpf": cpf, "endereco": endereco})

    print("Usuário criado com Sucesso!")


def filtrar_usuario(cpf, usuarios):
    if not cpf.isdigit() or len(cpf) != 11:
        return None

    usuarios_filtrados = [
        usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print(f"\nUsuário não encontrado!\nVolte e crie uma conta!")


def main():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "u":
            novo_usuario(usuarios)

        elif opcao == "n":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

        elif opcao == "q":
            print("Operação finalizada!\nVolte sempre")
            break

        else:
            print(
                "Operação inválida!\npor favor selecione novamente a operação desejada.")


main()
