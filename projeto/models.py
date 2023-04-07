from projeto import database

class Usuario(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String, nullable=False)
    senha =database.Column(database.String, nullable=False)
    sexo =database.Column(database.String, nullable=False)
    email =database.Column(database.String, nullable=False)
    foto =database.Column(database.String )
    data_nascimento =database.Column(database.DATE)
    endereco =database.Column(database.String, nullable=False)
