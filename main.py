from ursina import *
from parameters import EnhancedFirstPersonController
from environment.materials import Granite
from environment.obstacles import Mur, Barriere, Pyramide
from environment.environments import Axis, Grid, Arbre, Chene, Sol, Boite

def setup_environment(creatif_mode=False):
    # Création des axes pour visualiser les directions
    if creatif_mode:
        Axis()
        Grid()
        
    Sol(scale=(50, 1, 50), position=(0, -0.1, 0))  # Création du sol

    # Création des murs
    Mur(position=(25, 1, 0), scale=(1, 3, 25))  # Mur Est
    Mur(position=(-25, 1, 0), scale=(1, 3, 50)) # Mur Ouest
    Mur(position=(0, 1, 25), scale=(50, 3, 1))  # Mur Nord
    Mur(position=(0, 1, -25), scale=(50, 3, 1)) # Mur Sud

    Barriere(position=(5, 0, 5), scale=(1, 3, 10))  # 
    
    Pyramide(position=(0,0,0))

    Chene(position=(-10, 2, -10))
    Arbre(position=(-15, 2, -10))

    for x in range(10, 20, 5):
        Arbre(position=(x, 2, 10))

    # Dispersion des blocs de granite
    for x in range(0, 21, 5):
        for z in range(-20, 0, 5):
            if (x, z) != (0, 0):
                Granite(position=(x, 0, z))

    Boite(position=(20, 0.5, 10), scale=(2, 1.5, 2))


def main():
    app = Ursina()
    window.fullscreen = True
    creatif_mode = True
    
    setup_environment(creatif_mode)

    if creatif_mode:
        EditorCamera()
    else:
        Sky()
        player_controller = EnhancedFirstPersonController()
        player_controller.gravity = 0.5

    mouse.locked = True  # Verrouille le curseur au centre de l'écran

    app.run()

if __name__ == "__main__":
    main()
