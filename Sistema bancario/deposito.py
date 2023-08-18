def depo (saldo, extrato):
    print(f"Qual valor deseja depositar?")
    d =  float(input())
    saldoAtual = saldo + d
    print((f'''Foi realizado um depósito no valor de {d} 
           Saldo atual: {saldoAtual}'''))
    extratoAtual = extrato + (f'''Foi realizado um depósito no valor de {saldo:.2f}
''')
    return saldoAtual, extratoAtual
