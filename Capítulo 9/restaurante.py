class Restaurante():
    def __init__(self, restaurant_name, cuisine_type, number_served):
        """Uma tentativa simples de modelar um restaurante."""
        self.number_served = 2
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def set_number_served(self, number_served):
        self.number_served = number_served
    def increment_number_served(self, number_served):
        self.number_served += number_served
    def describe_restaurant(self):
        print("O nome do restaurante é: "+self.restaurant_name.title())
        print("O tipo de cozinha desse restaurante é: "+self.cuisine_type.title())
        print("O número de clientes atendidos por esse restaurante é: "+str(self.number_served)+"\n")
    def open_restaurant(self):
        print("O restaurante está aberto.")
class IceCreamStand(Restaurante):
    def __init__(self, restaurant_name, cuisine_type, number_served):
        super().__init__(restaurant_name,cuisine_type,number_served)
        self.flavors = ['morango','uva','napolitano']
    def describe_flavors(self):
        print("Os sabores que temos são: "+str(self.flavors))
restaurant = Restaurante('Coco Bambu Ribeirao Preto','Brasileira, Frutos do mar', 0)
#9.3restaurant.describe_restaurant()
#9.3restaurant.set_number_served(5)
#9.3restaurant.describe_restaurant()
#9.3restaurant.increment_number_served(5)
#9.3restaurant.describe_restaurant()
sorvete = IceCreamStand('Coco Bambu Ribeirao Preto','Brasileira, Frutos do mar', 0)
sorvete.describe_flavors()
#8.3restaurant2 = Restaurante('La Cucina di Tullio Santini','Italiana, Toscana, Centro da Itália')
#8.3restaurant3 = Restaurante('Ancho','Steakhouse, Churrasco, Argentina, Brasileira, Internacional')
#8.1print("O nome do restaurante é: "+restaurant.restaurant_name.title())
#8.1print("O tipo de cozinha do restaurante é: " + restaurant.cuisine_type.title())

#8.3restaurant2.describe_restaurant()
#8.3restaurant3.describe_restaurant()
#8.1restaurant.open_restaurant()