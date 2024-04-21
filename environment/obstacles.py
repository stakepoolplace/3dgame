from ursina import Vec3, Mesh, Entity, color, load_texture

# File: environment/obstacles.py

class Mur(Entity):
    def __init__(self, position, scale=(1, 1, 1)):
        super().__init__(
            model='cube',
            scale=scale,
            position=position,
            texture=load_texture('assets/textures/mur.png'),  # Assurez-vous d'avoir cette texture dans votre dossier textures
            texture_scale=(0.75, 0.5),  # Répéter la texture pour couvrir tout le mur
            collider='box'
        )
        
class Barriere(Entity):
    def __init__(self, position, scale=(1, 1, 1), alpha=0.5):  # Ajout du paramètre alpha avec une valeur par défaut
        super().__init__(
            model='cube',
            scale=scale,
            position=position,
            color=color.white33,  # Utilisez une couleur prédéfinie avec transparence ou créez la vôtre
            collider='box'
        )
        self.color = color.rgba(255, 255, 255, int(alpha * 255))  # Définir la transparence ici, alpha doit être entre 0 et 1

class Pyramide(Entity):
    def __init__(self, position=(0,0,0)):
        super().__init__()

        # Définir les vertices de l'objet
        vertices = [
            Vec3(position[0], position[1], position[2]),   # Vertex 0
            Vec3(position[0] + 1, position[1], position[2]),   # Vertex 1
            Vec3(position[0] + 0.5, position[1] + 0, position[2] + 1), # Vertex 2
            Vec3(position[0] + 0.5, position[1] + 1, position[2] + 0.5)# Vertex 3 (sommet de la pyramide)
        ]

        # Définir les triangles en utilisant les indices des vertices
        triangles = [
            (0, 1, 2),  # Base triangle 1
            (0, 1, 3),  # Side triangle 2
            (1, 2, 3),  # Side triangle 3
            (2, 0, 3)   # Side triangle 4
        ]

        # Créer le mesh avec les vertices et triangles
        mesh = Mesh(vertices=vertices, triangles=triangles, mode='line')
        self.model = mesh
        self.color = color.white
