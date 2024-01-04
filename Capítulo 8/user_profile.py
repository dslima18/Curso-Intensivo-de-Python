def build_profile(first,last,**user_info):
    """Constrói um dicionário contendo tudo que sabemos sobre um usuário."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('donato','souza',location='ribeirão preto',field='computação',hobby='xadrez')
print(user_profile)