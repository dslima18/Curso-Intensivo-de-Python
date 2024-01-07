import json
filename = 'numero.json'

with open(filename) as f_obj:
    numero = json.load(f_obj)
    print("Eu sei qual é o seu  número favorito! É "+str(numero))