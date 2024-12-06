class Restaurante:
    restaurantes = []

    def __init__(self, Nome, Categoria):
        self.Nome = Nome
        self.Categoria = Categoria
        self.Status = False

        Restaurante.restaurantes.append(self)
    def __str__(self):
        return f'{self.Nome} | {self.Categoria}'
        
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.Nome}|{restaurante.Categoria}|{restaurante.Status}')

    @property
    def Status(self):
        return '1' if self.status else '0'

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza', 'Italiana')

Restaurante.listar_restaurantes()

