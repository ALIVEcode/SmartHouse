from time import sleep
from maison.core.maison import Maison
from alimata.sensors.motion import Motion

maison = Maison()


# Fonctions de retour (callback)
def mouvement_salle_de_bain():
    print("mouvement salle bain")
    maison.salle_de_bain.lumiere.allumer()
    sleep(1)
    maison.salle_de_bain.lumiere.eteindre()

def mouvement_salon():
    pass
    print("mouvement salon")

def mouvement_cuisine():
    print("mouvement cuisine")
    pass

def setup():
    pass
    # detecteur_mouvement = Motion(board=maison.board, pin=6, on_change=mouvement_salle_de_bain)
    # maison.sonnette_entre.sur_clic(mouvement_salle_de_bain)
    maison.salle_de_bain.sur_mouvement(mouvement_salle_de_bain)
    maison.salon.sur_mouvement(mouvement_salon)
    maison.cuisine.sur_mouvement(mouvement_cuisine)
    

def loop():
    # maison.salle_de_bain.lumiere.allumer()
    # sleep(1)
    # maison.salle_de_bain.lumiere.eteindre()
    sleep(1)
    # print(maison.salle_de_bain.detecteur_mouvement.data)
    # print("salle de bain : " + str(maison.salle_de_bain.detecteur_mouvement.data))
    # print("salon : " + str(maison.salon.detecteur_mouvement.data))
    # print("cuisine : " + str(maison.cuisine.detecteur_mouvement.data))
    pass

maison.start(setup, loop)
