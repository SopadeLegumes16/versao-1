lista_deposito = list()
lista_retirado = list()
num = 0
soma_deposito = soma_retirar = saldo_conta = 0
limite_saque = 0


while True:
    if limite_saque >= 3:
        break

    resp = str(input('Voce deseja retirar ou adicionar dinheiro?[Retirar/Depositar] '))[0].upper()

    if resp == 'R':
        if num == 0:
            print('deposite algo primeiro!!')
            continue

        else:
            quantidade_Retirar = float(input('Quanto voce Quer retirar? R$'))

            if saldo_conta < quantidade_Retirar:
                print('saldo insuficiente')

            else:
                limite_saque += 1
                soma_retirar += quantidade_Retirar
                lista_retirado.append(quantidade_Retirar)
                pergunta = input('Deseja mais alguma coisa?[S/N] ')[0].upper()
                saldo_conta = soma_deposito - soma_retirar

                if pergunta in 'S':
                    continue

                else:
                    break

    elif resp == 'D':
        num += 1
        quantidade_Depositar = float(input('Quanto voce quer depositar R$'))

        soma_deposito += quantidade_Depositar

        lista_deposito.append(quantidade_Depositar)

        pergunta = input('Deseja mais alguma coisa?[S/N] ')[0].upper()

        saldo_conta = soma_deposito - soma_retirar

        if pergunta in 'S':
            continue
        else:
            break
    else:
        print('Retirar ou depositar!!!!')
        continue

opcao = input('Deseja ver o extrato de sua conta?[S/N]')[0].upper()

if opcao in 'S':

    print('-=' * 30)

    print(f'depositos em sua conta: ',end='')

    for i in lista_deposito:

        print(f'R${i:.2f} - ', end='')

        print()

    print('-=' * 30)
    print(f'Valores retirados de sua conta: ', end='')

    for i in lista_retirado:

        print(f'R${i:.2f} - ', end='')

        print()

    print('-=' * 30)
print(f'Saldo restante na conta R${saldo_conta:.2f}')