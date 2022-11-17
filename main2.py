from time import sleep
from alimata.core.board import Board
from alimata.sensors.motion import Motion
from alimata.sensors.button import Button

board = Board()

# Fonctions de retour (callback)
def mouvement_salle_de_bain(data):
    if data.pin == 23 and data.data == True:
        print("mouvement salle de bain")

def mouvement_salon(data):
    # print("mouvement salon")
    pass

def mouvement_cuisine(data):
    # print("mouvement cuisine")
    pass

def setup():
    # detecteur_mouvement = Motion(board=maison.board, pin=6, on_change=mouvement_salle_de_bain)
    # maison.sonnette_entre.sur_clic(mouvement_salle_de_bain)
    list = []
    for i in range(22, 40):
        motion = Button(board, i, on_change=mouvement_salle_de_bain)
        list.append(motion)

    
    # motion1 = Motion(board, "22", on_change=mouvement_salle_de_bain)
    # motion2 = Motion(board, "23", on_change=mouvement_salon)
    # motion3 = Motion(board, "25", on_change=mouvement_cuisine)
    


    

def loop():
    # maison.salle_de_bain.lumiere.allumer()
    # sleep(1)
    # maison.salle_de_bain.lumiere.eteindre()
    sleep(1)
    # print(maison.salle_de_bain.detecteur_mouvement.data)
    pass

board.start(setup, loop)
