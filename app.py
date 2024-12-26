from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Guilherme', 10)
restaurante_praca.receber_avaliacao('Talita', 5)
restaurante_praca.receber_avaliacao('João', 8)
restaurante_praca.receber_avaliacao('Carol', 7)



def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()