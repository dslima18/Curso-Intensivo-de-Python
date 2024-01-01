responses = {}
polling_active = True
while polling_active:
    name = input("Digite seu nome: ")
    resposta = input("Se você pudesse visitaru m lugar do mundo, para onde você iria ?")
    responses[name] = resposta
    repete = input("Você gostaria que outra pessoa respondesse a enquente? (sim/nao)")
    if repete == 'nao':
        polling_active = False

for nome ,resposta in responses.items():
    print(nome.title()+", gostaria de ir a(ao),"+resposta)