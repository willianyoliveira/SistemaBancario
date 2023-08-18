def cadastro (clientes):
    print("Digite seu nome completo: ")
    nome = input()
    print("Digite sua data de nascimento: ")
    data = input()
    print("Digite seu CPF: ")
    cpf = int(input())
    print("Digite seu enfereço: ")
    endereco = input()
    cliente = [nome, data, cpf, endereco]
    return cliente    