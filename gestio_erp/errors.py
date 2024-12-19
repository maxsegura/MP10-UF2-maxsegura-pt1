# Definim una classe d'error personalitzat per quan un producte ja existeix a la comanda
class ProducteJaExisteixError(Exception):
    def __init__(self, producte):
        # Cridem al constructor de la classe base Exception per passar el missatge d'error
        super().__init__(f"El producte {producte} ja existeix a la comanda.")

# Definim una classe d'error personalitzat per quan un producte no existeix a la comanda
class ProducteNoExisteixError(Exception):
    def __init__(self, producte):
        # Cridem al constructor de la classe base Exception per passar el missatge d'error
        super().__init__(f"El producte {producte} no existeix a la comanda.")