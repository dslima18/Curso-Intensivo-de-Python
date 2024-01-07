while True:
    print("Digite 'q' para sair.")
    num_1 = input("Digite o valor para o primeiro número que será somado: ")
    if(num_1=='q'):
        break
    num_2 = input("Digite o valor para o segundo número que será somado: ")
    if(num_2 == 'q'):
        break
    try:
        num_1 = int(num_1)
        num_2 = int(num_2)
    except ValueError:
        print("Você digitou um texto ao invés de um número.")
    else:
        soma = num_1 + num_2
        print(soma)
