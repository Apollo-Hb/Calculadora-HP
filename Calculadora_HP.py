# Iniciando o loop do menu com opções para o usuario.
while True:
    print("+ - Adição")
    print("- - Subtração")
    print("* - Multiplicação")
    print("/ - Divisão")
    print("X - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == 'X':
        break                               # Vendo se o usuario parou o programa ou escolheu uma das opções.
    for opcao in ['+', '-', '*', '/']:
        
        resultado = float(input("Digite qualquer número ou 'P' para encerrar o calculo: "))

        while True:
            numero = input("Digite 'P' para parar: ")
            if numero == 'P':
                break                       #Iniciando outro loop e esperando o usuario escolher uma opção e lendo os numeros e até o usuario digitar P ou continuar a operação.
            else:
                numero = float(numero)

                if opcao == '+':  # Adição
                    resultado += numero
                if opcao == '-':  # Subtração
                    resultado -= numero
                if opcao == '*':  # Multiplicação                            # Realizando a operação que o usuario escolher.
                    resultado *= numero
                if opcao == '/':  # Divisão
                    resultado /= numero

        # Imprimindo o resultado para o usuario.
        print(f"Resultado: {resultado}")
