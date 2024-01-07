filename = 'respostas.txt'
with open(filename, 'a') as file_object:
    nome = ''
    while(nome != 'quit'):
        nome = input("Porque você gosta de Programação? (Digite 'quit' para sair.)")
        if nome == 'quit':
            break
        else:
            file_object.write(nome+"\n")
    #file_object.write((input("Qual o seu nome? ")))