def saq(saldo, saques, limite_saque, extrato):
    if saques < limite_saque:
        print("Qual valor deseja sacar?")
        s = float(input())
        if (s <= saldo) and (s<=500):
            saldo = saldo - s
            print(f"Saque realizado. Novo saldo: {saldo}")
            extrato = extrato + (f'''Foi realizado um saque no valor de {s:.2f}
''')
            saques = saques + 1
        else:
            print("Não á limite disponível para o saldo")
    else:
            print("O número de saques diários permitidos foi alcançado")   