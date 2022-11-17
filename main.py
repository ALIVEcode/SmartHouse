from time import sleep
from maison.core.maison import Maison
from alimata.sensors.motion import Motion

maison = Maison()


# Fonctions de retour (callback)
def mouvement_salle_de_bain(etat):
    if etat:
        print("mouvement salle bain")
        maison.salle_de_bain.lumiere.allumer()
    else:
        maison.salle_de_bain.lumiere.eteindre()

def sonner_sonnette(etat):
    if etat:
        print("sonner")
        maison.sonnette_entre.sonner()

# def mouvement_salon():
#     pass
#     print("mouvement salon")

# def mouvement_cuisine():
#     print("mouvement cuisine")
#     pass

def setup():

    maison.salle_de_bain.sur_mouvement(mouvement_salle_de_bain)
    maison.sonnette_entre.sur_clic(sonner_sonnette)
    # maison.salon.sur_mouvement(mouvement_salon)
    # maison.cuisine.sur_mouvement(mouvement_cuisine)
    

def loop():
    print("Temp : " + str(maison.salle_de_bain.capteur_dht.temperature))
    print("Hum : " + str(maison.salle_de_bain.capteur_dht.humidite))

    if maison.salle_de_bain.capteur_dht.humidite >= 50:
        maison.son.sonner()
    else:
        maison.son.stop()
        
    sleep(1)


maison.start(setup, loop)
