# Inicialização de variáveis
saldo = 0.0
depositos = []
saques = []
saques_diarios = 0

while True:
    # Menu de opções
    print("Sistema Bancário Básico")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Extrato")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        # Depositar
        valor_deposito = float(input("Digite o valor do depósito: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            depositos.append(valor_deposito)
            print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido. Tente novamente.")

    elif opcao == "2":
        # Sacar
        if saques_diarios < 3:
            valor_saque = float(input("Digite o valor do saque: "))
            if valor_saque > 0 and valor_saque <= 500:
                if saldo >= valor_saque:
                    saldo -= valor_saque
                    saques.append(valor_saque)
                    saques_diarios += 1
                    print(f"Saque de R${valor_saque:.2f} realizado com sucesso!")
                else:
                    print("Saldo insuficiente. Não é possível realizar o saque.")
            else:
                print("Valor de saque inválido. Tente novamente.")
        else:
            print("Você já realizou 3 saques diários. Tente novamente amanhã.")

    elif opcao == "3":
        # Extrato
        print("Extrato da Conta:")
        for deposito in depositos:
            print(f"Depósito: R${deposito:.2f}")
        for saque in saques:
            print(f"Saque: R${saque:.2f}")
        print(f"Saldo atual: R${saldo:.2f}")

    elif opcao == "4":
        # Sair
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")