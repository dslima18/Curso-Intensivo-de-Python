from usuarios import User
class Privileges():
     def __init__(self, privileges = ['can add post','can delete post','can ban user']):
         self.privileges = privileges
     def show_privileges(self):
        print("Os privilégios de um administrador são: "+str(self.privileges))
class Admin(User):
    def __init__(self, first_name, last_name, idade, sexo, cidade, login_attempts):
        super().__init__(first_name, last_name, idade, sexo, cidade, login_attempts)
        self.privileges = Privileges()
usuario = Admin('donato','souza',22,'masculino','duque de caxias',1)
usuario.privileges.show_privileges()
