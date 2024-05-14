##
# atividade: Calculadora-Hp
# aluno: Apollo
# Data:13/05/2024
##

"""
Esse programa é uma calculadora simples que contém adição, subtração, multiplicação e divisão.
O usuário pode continuar a inserir números para a operação escolhida até que decida parar.

"""

while True:
    print("+ - Adição")
    print("- - Subtração")
    print("* - Multiplicação")
    print("/ - Divisão")
    print("X - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == 'X':
        break  # Conferindo se o usuario parou o loop(programa) ou escolheu uma das opções.

    resultado = float(input("Digite qualquer número ou 'P' para encerrar o calculo: "))

    while True:
        numero = input("Digite 'P' para parar: ")
        if numero == 'P':
            break   # Iniciando outro loop infinito e esperando o usuario escolher uma opção e também lendo os numeros, até o usuario digitar P ou continuar a operação digitando mais um número.
        else:
            numero = float(numero)
                    # Realizando a operação matémica que o usuario escolheu: '+', '-', '*', '/'.
            if opcao == '+':  # Adição
                resultado += numero
            elif opcao == '-':  # Subtração
                resultado -= numero
            elif opcao == '*':  # Multiplicação
                resultado *= numero
            elif opcao == '/':  # Divisão
                resultado /= numero
    # Imprimindo o resultado para o usuario.
    print(f"Resultado: {resultado}")