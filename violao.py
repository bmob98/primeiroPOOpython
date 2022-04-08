# Criei uma classe chamada violão, aqui tera caracteristicas de um v
class Violao:
    modelo = None
    cor = None
    tamanho = None
    cordas = None
    uso = None

    # O __init__ é um metodo especial usado sempre na primeira função da classe
    # criei os atributos de um violao
    def __init__(self, cor, tamanho, cordas, modelo, uso):
        try:
            self.modelo = modelo
            self.cor = cor
            self.cordas = cordas
            self.tamanho = tamanho
            self.uso = uso
        except Exception as e:
            print(str(e))

    # São os gets e sets para poder ser instanciado em outra classe
    def set_modelo(self, modelo):
        try:
            self.modelo = modelo
        except Exception as e:
            print(str(e))

    def get_modelo(self):
        try:
            return self.modelo
        except Exception as e:
            print(str(e))

    def set_cor(self, cor):
        try:
            self.cor = cor
        except Exception as e:
            print(str(e))

    def get_cor(self):
        try:
            return self.cor
        except Exception as e:
            print(str(e))

    def set_cordas(self, cordas):
        try:
            self.cordas = cordas
        except Exception as e:
            print(str(e))

    def get_cordas(self):
        try:
            return self.cordas
        except Exception as e:
            print(str(e))

    def set_tamanho(self, tamanho):
        try:
            self.tamanho = tamanho
        except Exception as e:
            print(str(e))

    def get_tamanho(self):
        try:
            return self.tamanho
        except Exception as e:
            print(str(e))

    def set_uso(self, uso):
        try:
            self.uso = uso
        except Exception as e:
            print(str(e))

    def get_uso(self):
        try:
            return self.uso
        except Exception as e:
            print(str(e))
