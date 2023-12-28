pizzas = ['calabresa','frango','mussarela']
friend_pizzas = pizzas[:]
pizzas.append('quatro queijos')
for pizza in pizzas:
    print("Minhas pizzas são "+pizza+".\n")
print("As pizzas favoritas do meu amigo são:")
for pizza in friend_pizzas:
    print(pizza)
#print("Eu realmente gosto de "+pizzas[0]+".\n")
#print(pizzas[1]+", é minha preferida.\n")
#print(pizzas[2]+", também é uma das minha favoritas.\n")
#print("Eu realmente gosto de pizza!")