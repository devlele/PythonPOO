from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._status = False # o underline transforma esse atributo em um atributo privado (apenas em convenção então ele ainda é acessivel), ou seja, não é esperado que oo usuario mude o vlaor dele
        self._avaliacao = []

        Restaurante.restaurantes.append(self)
    def __str__(self):
        return f'{self._nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')

        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)}|{restaurante.categoria.ljust(25)}|{str(restaurante.media_avaliacoes).ljust(25)}|{restaurante._status}')

    @property
    def status(self):
        return '1' if self._status else '0'

    def alternar_estado(self):
        self._status = not self._status

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        
        quantidade_notas = len(self._avaliacao)

        media = round(soma_notas / quantidade_notas, 1)
        return media