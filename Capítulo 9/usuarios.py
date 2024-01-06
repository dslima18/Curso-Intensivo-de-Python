class User():
    def __init__(self, first_name, last_name, idade, sexo, cidade,login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.idade = idade
        self.sexo = sexo
        self.cidade = cidade
        self.login_attempts = login_attempts
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
    def describe_user(self):
        full_name = self.first_name.title() +" "+ self.last_name.title()
        print("O nome do usuário é: " + full_name.title())
        print("A idade do usuário é: "+str(self.idade))
        print("O sexo do usuário é: "+self.sexo)
        print("O usuário mora em: "+self.cidade.title())
        print("O número de tentativa de logins, feitas por esse usuário é de: "+str(self.login_attempts)+"\n")
    def greet_user(self):
        full_name = self.first_name.title() +  " " + self.last_name.title()
        print("Bem vindo, "+full_name+"\n")
class Privileges():
     def __init__(self, privileges = ['can add post','can delete post','can ban user']):
         self.privileges = privileges
     def show_privileges(self):
        print("Os privilégios de um administrador são: "+str(self.privileges))
class Admin(User):
    def __init__(self, first_name, last_name, idade, sexo, cidade, login_attempts):
        super().__init__(first_name, last_name, idade, sexo, cidade, login_attempts)
        self.privileges = Privileges()
#usuario = Admin('donato','souza',22,'masculino','duque de caxias',1)
#usuario.privileges.show_privileges()
#9.5usuario.describe_user()
#9.5usuario.increment_login_attempts()
#9.5usuario.increment_login_attempts()
#9.5usuario.increment_login_attempts()
#9.5usuario.describe_user()
#9.5usuario.reset_login_attempts()
#9.5usuario.describe_user()
#9.3usuario2 = User('ana','souza',56,'feminino','duque de caxias')
#9.3usuario3 = User('manoel','rodrigues',70,'masculino','caucaia')


#9.3usuario.greet_user()
#9.3usuario2.describe_user()
#9.3usuario2.greet_user()
#9.3usuario3.describe_user()
#9.3usuario3.greet_user()