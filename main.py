from time import sleep
from maison.core.maison import Maison

maison = Maison()


# Fonctions de retour (callback)
def appuieSonnette():
    print("Sonnette appuyée")
    maison.sonnette_entre.sonner()



def setup():
    maison.sonnette_entre.sur_clic(appuieSonnette)

def loop():
    maison.salle_de_bain.lumiere.allumer()
    maison.alarme.sonner()
    print("Lumiere salon allumée")
    sleep(2)
    maison.salle_de_bain.lumiere.eteindre()
    maison.alarme.stop()
    print("Lumiere salon Eteinte")
    sleep(1)


maison.start(setup, loop)
