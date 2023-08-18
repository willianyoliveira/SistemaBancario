from deposito import depo
from saque import saq
from extrato import ext
from menu import menu
from cadastrarUsuario import cadastro
saldo = 0
saques = 0
deposito = ""
LIMITE_SAQUE = 500
clientes = []
extrato = '''EXTRATO
'''
while True:
    menu()
    operacao = input()
    if operacao == "1":
        clientes.append(cadastro(clientes))
    elif operacao == "2":
        print("Criar conta corrente")
    elif operacao == "3":
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
    