# Definim una classe Client que representa un client amb les seves dades personals
class Client:
    
    # Mètode constructor (__init__) per inicialitzar un objecte Client
    def __init__(self, id_client, nom, email):
        # Inicialitzem l'identificador del client (id_client), el nom i l'email
        self.id_client = id_client  # Identificador únic per al client
        self.nom = nom  # Nom del client
        self.email = email  # Correu electrònic del client
        self.comandes = []  # Inicialitzem una llista buida per emmagatzemar les comandes del client

    # Mètode per afegir una comanda a la llista de comandes del client
    def afegir_comanda(self, comanda):
        # Afegim una nova comanda a la llista 'comandes' del client
        self.comandes.append(comanda)

    # Mètode per consultar totes les comandes associades al client
    def consultar_comandes(self):
        # Retornem la llista de comandes emmagatzemada
        return self.comandes