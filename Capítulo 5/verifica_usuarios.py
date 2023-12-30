current_users = ['Donato','Ana','Manoel','Gabriel','Lucca']
new_users = ['Argentina','Donato','Ana','Bruna','Orlando']
for new_user in new_users:
    if new_user.title() in current_users:
        print("A pessoa deve fornecer um novo nome.")
    else:
        print("Nome de usuário disponível.")