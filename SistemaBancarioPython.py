menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Digite o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! o Valor informado é invalido.")

    elif opcao == "2":
        if numero_saques < LIMITE_SAQUES:
            valor = float(input("Digite o valor a ser sacado: "))
            if valor < 0:
                print("Informe um valor valido para saque!")

            elif valor <= saldo and valor <= limite:
                saldo -= valor
                extrato.append(f"Saque: R$ {valor:.2f}")
                numero_saques += 1
            else:
                print("Não foi possível realizar o saque.")
        else:
            print("Limite de saques diários atingido.")

    elif opcao == "3":
        print("Extrato:")
        for movimento in extrato:
            print(movimento)
        print(f"Saldo: R$ {saldo:.2f}")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
