# Importem les classes i errors necessaris des dels fitxers de la nostra aplicació
from gestio_erp.clients import Client
from gestio_erp.comandes import Comanda
from gestio_erp.errors import ProducteJaExisteixError, ProducteNoExisteixError

# Creem clients amb el seu ID, nom i correu electrònic
anna = Client(1, "Anna", "anna@example.com")
pere = Client(2, "Pere", "pere@example.com")
joan = Client(3, "Joan", "joan@example.com")

# Creem comandes per a diferents clients i afegim productes
comanda1 = Comanda(101)
comanda1.afegir_producte("bicicleta", 1)
comanda1.afegir_producte("casc", 2)

comanda2 = Comanda(102)
comanda2.afegir_producte("guants", 1)

comanda3 = Comanda(103)
comanda3.afegir_producte("maillot", 1)
comanda3.afegir_producte("roda", 2)

comanda4 = Comanda(104)
comanda4.afegir_producte("guants", 2)

# Assignem les comandes als clients
anna.afegir_comanda(comanda1)
anna.afegir_comanda(comanda2)
pere.afegir_comanda(comanda3)
pere.afegir_comanda(comanda4)

# Modifiquem l'estat de la comanda i les quantitats dels productes
comanda1.modificar_estat("Enviada")
comanda1.modificar_quantitat("bicicleta", 1)
comanda1.modificar_quantitat("casc", 2)
comanda1.afegir_producte("pantalons", 1)

# Funció per mostrar les comandes d'un client
def mostrar_comandes(client):
    print(f"Comandes del client {client.nom}: {len(client.consultar_comandes())}")
    for comanda in client.consultar_comandes():
        print(comanda.consultar_resum())

# Mostrem les comandes dels clients
mostrar_comandes(anna)
mostrar_comandes(pere)
mostrar_comandes(joan)

# Gestionem errors per afegir productes duplicats o inexistents a les comandes
try:
    comanda1.afegir_producte("bicicleta")
except ProducteJaExisteixError as e:
    print(e)

try:
    comanda1.modificar_quantitat("patinet", 1)
except ProducteNoExisteixError as e:
    print(e)