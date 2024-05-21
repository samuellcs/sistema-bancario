print("""
=========Escolha uma operação=========    
        ->[d] Depositar
        ->[s] Sacar
        ->[e] Extrato
        ->[q] Sair
--------------------------------------     
      """)

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou!\nO valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

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

        else:
            print("Operação falhou!\nO valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        print("Operação finalizada!\nVolte sempre")
        break

    else:
        print(f"Operação inválida!\npor favor selecione novamente a operação desejada.")