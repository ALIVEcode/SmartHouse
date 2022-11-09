from time import sleep
from maison.core.maison import Maison

maison = Maison()


# Fonctions de retour (callback)
def appuieSonnette():
    print("Sonnette appuyée")
    maison.porteEntre.sonnette.ding()



def setup():
    maison.porteEntre.sonnette.surClic(appuieSonnette)

def loop():
    maison.salon.lumiere.allumer()
    print("on")
    sleep(2)
    maison.salon.lumiere.eteindre()
    print("off")
    sleep(1)


maison.board.start(setup, loop)
