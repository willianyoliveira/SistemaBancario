def ext (saldo, extrato):
    if extrato == "":
        print("Ainda não foi realizada nenhuma operação")
    else: 
        print(f'''{extrato}
              --------------------------------
              Saldo atual: {saldo}''')