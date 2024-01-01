numero = input("Informe o número e te direi se esse número é ou não múltiplo de 10: ")
numero = int(numero)
if numero % 10 == 0:
    print(str(numero)+", é múltiplo de 10.")
else:
    print(str(numero)+", não é múltiplo de 10.")