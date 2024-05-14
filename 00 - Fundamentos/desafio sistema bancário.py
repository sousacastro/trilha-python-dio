menu = """

[1] Sacar
[2] Depositar
[3] Transferir
[4] Extrato
[5] Sair 

=> """

saldo = 1000
limite = 1000
extrato = ""
numero_saques = 0
numero_transferencias = 0
LIMITE_SAQUES = 3
LIMITE_TRANSFERENCIAS = 3

while True:

    opcao = input(menu)

    if opcao == "2":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "1":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1



    elif opcao == "3":
        valor = float(input("Informe informe o valor para transferência: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_transferencias = numero_transferencias >= LIMITE_TRANSFERENCIAS

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! Limite de transferencias excedido.")

        elif excedeu_transferencias:
            print("Operação falhou! Número máximo de transferências excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Transferências: R$ {valor:.2f}\n"
            numero_transferencias += 1   

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "4":
        print("\n================ EXTRATO BANCÁRIO ================")
        print("Sem movimentação para o período." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("====================================================")

    elif opcao == "5":
        print("Operação finalizada com sucesso!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
