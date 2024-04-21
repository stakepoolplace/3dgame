from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import time

class EnhancedFirstPersonController(FirstPersonController):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.walk_speed = 5  # Vitesse normale de marche
        self.run_speed = 10  # Vitesse de course lors de l'appui sur Shift
        self.speed = self.walk_speed  # Définir la vitesse initiale à la vitesse de marche

        # Éléments de texte pour le débogage
        self.debug_text = Text(text='', position=(-0.7, 0.45), origin=(0, 0), scale=2, color=color.white)

    def update(self):
        super().update()
        
        # Gestion de la touche Shift pour courir
        if held_keys['left shift'] or held_keys['right shift']:
            self.speed = self.run_speed  # Augmenter la vitesse si Shift est maintenu
        else:
            self.speed = self.walk_speed  # Revenir à la vitesse de marche si Shift est relâché
        