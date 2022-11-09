from time import sleep
from maison.core.maison import Maison

maison = Maison()


# Fonctions de retour (callback)
def appuieSonnette():
    print("Sonnette appuyée")
    maison.porte_entre.sonnette.ding()



def setup():
    maison.porte_entre.sonnette.sur_clic(appuieSonnette)

def loop():
    maison.salon.lumiere.allumer()
    print("Lumiere salon allumée")
    sleep(5)
    maison.salon.lumiere.eteindre()
    print("Lumiere salon Eteinte")
    sleep(1)


maison.board.start(setup, loop)
