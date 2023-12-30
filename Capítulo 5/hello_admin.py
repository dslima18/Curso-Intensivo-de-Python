usuarios=[]
if not(usuarios):
    print("Precisamos de alguns usuários.")
usuarios = ['Donato','Ana','Manoel','Lucca','Gabriel']
for usuario in usuarios:
    if(usuario=='admin'):
        print("Olá admin, gostaria de ver um relatório de status?")
    else:
        print("Olá "+usuario+", obrigado por fazer login novamente.")
    