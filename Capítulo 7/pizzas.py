message = ""
while message != 'quit':
    message = input("Qual ingrediente você gostaria de colocar na sua pizza ?\n Digite 'quit', caso queira finalizar o pedido.")
    if message != 'quit':
        print("O ingrediente: "+message+", foi acrescentado a pizza.")
