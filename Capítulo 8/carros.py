def make_car(nome,modelo,**infos_extras):
    carros = {}
    carros['nome']=nome
    carros['modelo']=modelo
    for key,value in infos_extras.items():
        carros[key]=value
    return carros

car = make_car('subaru','outback',color='blue',tow_package=True)
print(car)