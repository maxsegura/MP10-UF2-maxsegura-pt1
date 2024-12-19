# Importem els errors personalitzats per a la gestió d'errors relacionats amb productes
from gestio_erp.errors import ProducteJaExisteixError
from gestio_erp.errors import ProducteNoExisteixError

# Definim una classe Comanda per representar una comanda realitzada per un client
class Comanda:
    
    # Mètode constructor (__init__) per inicialitzar un objecte Comanda
    def __init__(self, id_comanda):
        # Inicialitzem l'identificador de la comanda (id_comanda)
        self.id_comanda = id_comanda
        # Inicialitzem un diccionari per emmagatzemar els productes de la comanda, amb la seva quantitat
        self.productes = {}
        # Inicialitzem l'estat de la comanda com a "Pendent"
        self.estat = "Pendent"

    # Mètode per afegir un producte a la comanda amb una quantitat determinada
    def afegir_producte(self, producte, quantitat=1):
        # Comprovem si el producte ja està a la comanda
        if producte in self.productes:
            # Si ja existeix, llançem un error personalitzat ProducteJaExisteixError
            raise ProducteJaExisteixError(producte)
        # Afegim el producte amb la quantitat especificada al diccionari de productes
        self.productes[producte] = quantitat

    # Mètode per modificar la quantitat d'un producte ja present a la comanda
    def modificar_quantitat(self, producte, quantitat):
        # Comprovem si el producte existeix a la comanda
        if producte not in self.productes:
            # Si no existeix, llançem un error personalitzat ProducteNoExisteixError
            raise ProducteNoExisteixError(producte)
        # Modifiquem la quantitat del producte
        self.productes[producte] += quantitat

    # Mètode per modificar l'estat de la comanda (Pendent o Enviada)
    def modificar_estat(self, nou_estat):
        # Comprovem que l'estat proporcionat sigui vàlid
        if nou_estat not in ["Pendent", "Enviada"]:
            # Si l'estat no és vàlid, llançem un error de tipus ValueError
            raise ValueError("Estat no vàlid")
        # Assignem el nou estat a la comanda
        self.estat = nou_estat

    # Mètode per consultar un resum de la comanda
    def consultar_resum(self):
        # Retornem una cadena de text amb un resum de la comanda, incloent-hi l'estat i els productes amb les quantitats
        return f"Comanda {self.id_comanda} [{self.estat}]: " + ", ".join(
            [f"{prod}: {qty}" for prod, qty in self.productes.items()]
        )