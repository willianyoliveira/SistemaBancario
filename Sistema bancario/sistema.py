from deposito import depo
from saque import saq
from extrato import ext
from menu import menu
saldo = 0
deposito = ""
saques = 0
LIMITE_SAQUE = 500
extrato = '''EXTRATO
'''
while True:
    menu()
    operacao = input()
    if operacao == "3":
        saldo, extrato = depo(saldo, extrato)  
    elif operacao == "4": 
         saque = saq(saldo=saldo,
                          saques=saques,
                          limite_saque = LIMITE_SAQUE,
                          extrato = extrato
                          )
    elif operacao == "5":
        ext(saldo, extrato = extrato)
    elif operacao == "6":
        break
    elif (operacao != "1" or "2" or "3" or "4" or "5" or "6"):
        print('''
              Operação inválida
              ''')