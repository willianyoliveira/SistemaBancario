from deposito import depo
from saque import saq
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
        saldoAtual, extrato = depo(saldo, extrato)  
        extrato = extrato + saldoAtual[1]
        saldo = saldo +  saldoAtual[0]
    if operacao == "s": 
         saque = saq(saldo=saldo,
                          saques=saques,
                          limite_saque = LIMITE_SAQUE,
                          extrato = extrato
                          )
    if operacao == "e":
        if extrato == "":
            print("Ainda não foi realizada nenhuma operação")
        else: 
            print(extrato)
    if operacao == "q":
        break
    if (operacao != "s") and (operacao != "e") and (operacao != "d") and (operacao != "q"):
        print("Operação inválida")