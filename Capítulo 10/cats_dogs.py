
"""filename = 'cats.txt'
with open(filename,'a') as f_obj:
    for i in range(1,4):
        nome = input("Digite o nome do gato: ")
        f_obj.write(nome+"\n")
filename2 = 'dogs.txt'
with open(filename2,'a') as f_obj:
    for i in range(1,3):
        nome = input("Digite o nome do cachorro: ")
        f_obj.write(nome+"\n")
"""
filename = 'cats.txt'
filename2 = 'dogs.txt'
try:
    with open(filename) as f_obj:
        for line in f_obj:
            print(line)
    with open(filename2) as f_obj:
        for line in f_obj:
            print(line)
except FileNotFoundError:
    print("O arquivo não foi encontrado.")

