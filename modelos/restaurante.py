class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._status = False # o underline transforma esse atributo em um atributo privado (apenas em convenção então ele ainda é acessivel), ou seja, não é esperado que oo usuario mude o vlaor dele

        Restaurante.restaurantes.append(self)
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
        
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(25)}|{restaurante.categoria.ljust(25)}|{restaurante.status}')

    @property
    def status(self):
        return '1' if self._status else '0'

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza', 'Italiana')

Restaurante.listar_restaurantes()

