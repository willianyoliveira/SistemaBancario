saldo = 0
deposito = ""
saques = 0
LIMITE_SAQUE = 500
extrato = '''EXTRATO
'''
while True:
    print(''' Sistema Bancário
          Selecione uma operação para iniciar:
          d = Depósito
          s = Saldo
          e = Extrato
          q = Sair''')
    operacao = input()
    if operacao == "d":
        print(f"Qual valor deseja depositar?")
        d =  float(input())
        extrato = extrato + (f'''Foi realizado um depósito no valor de {d:.2f}
''')
        saldo = saldo + d
        print((f'''Foi realizado um depósito no valor de {d}
               Saldo atual: {saldo}'''))
    if operacao == "s": 
        if saques < 3:
            print("Qual valor deseja sacar?")
            s = float(input())
            if (s <= saldo) and (s<=500):
                saldo = saldo - s
                print(f"Saque realizado. Novo saldo: {saldo}")
                extrato = extrato + (f'''Foi realizado um saque no valor de {s:.2f}
''')
                saques = saques + 1
                print(saques)
            else:
                print("Não á limite disponível para o saldo")
        else:
            print("O número de saques diários permitidos foi alcançado")    
    if operacao == "e":
        if extrato == "":
            print("Ainda não foi realizada nenhuma operação")
        else: 
            print(extrato)
    if operacao == "q":
        break
    if (operacao != "s") and (operacao != "e") and (operacao != "d") and (operacao != "q"):
        print("Operação inválida")