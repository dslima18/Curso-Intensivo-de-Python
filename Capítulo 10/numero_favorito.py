import json
#numero = input("Qual o seu número favorito?")
filename = 'numero.json'
try:
    with open(filename) as f_obj:
        numero = json.load(f_obj)
        print("Eu sei qual é o seu  número favorito! É "+str(numero))
except FileNotFoundError:
    with open(filename, 'w') as f_obj:
        numero = json.dump(input("Qual o seu número favorito?"),f_obj)

