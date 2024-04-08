
class Usuario:
    def __init__(self, name, lastname, email, password):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password
        self.phone = "X"
        self.foto = ""
        self.nationality = ""

    def __str__(self):
        return self.name, self.lastname, self.email, self.password, self.phone, self.foto, self.nationality
    
