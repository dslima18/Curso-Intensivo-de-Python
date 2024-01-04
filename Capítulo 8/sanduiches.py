def make_sandwich(itens):
    print("O Sanduíche é composto por :")
    for item in itens:
        print("- "+item)

itens1 = ['queijo','mortadela']
itens2 = ['manteiga']
itens3 = ['maionese','ovo frito','hamburguer']
make_sandwich(itens1)
make_sandwich(itens2)
make_sandwich(itens3)