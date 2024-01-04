def describe_pet(pet_name,animal_type='dog'):
    """Exibe informações sobre um animal de estimação."""
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+ pet_name.title()+".")
describe_pet()
#describe_pet('willie','fish')
#describe_pet(pet_name='willie')
#describe_pet(animal_type='hamster',pet_name='harry')
#describe_pet('harry','hamster')
#describe_pet('hamster','harry')
#describe_pet('dog','willie')