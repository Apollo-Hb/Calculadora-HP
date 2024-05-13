# Iniciando um loop infinito e imprimindo opções disponíveis do menu para o usuario.
while True:
    print("+ - Adição")
    print("- - Subtração")
    print("* - Multiplicação")
    print("/ - Divisão")
    opcao = input("Escolha uma opção: ")

    resultado = float(input("Digite qualquer número ou 'P' para encerrar o calculo: "))

    while True:
        numero = input("Digite 'P' para parar: ")
        if numero == 'P':                                   #Conferindo se o usuario parou o loop(programa) ou escolheu uma das opções.
            break
        else:                                               #Iniciando um outro loop infinito e esperando o usuario escolher uma opção e lendo os numeros e até o usuario digitar P para parar a programação ou continuar a operação digitando mais um numero.
            
            numero = float(numero)

            if opcao == '+':  # Adição
                resultado += numero
            elif opcao == '-':  # Subtração
                resultado -= numero
            elif opcao == '*':  # Multiplicação                                             # Realizando a operação matémica que o usuario escolheu: '+', '-', '*', '/'.
                resultado *= numero
            elif opcao == '/':  # Divisão
                resultado /= numero
    #Imprimindo o resultado para o usuario.
    print(f"Resultado: {resultado}")
