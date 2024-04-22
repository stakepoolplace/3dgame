from ursina import Mesh, Entity, Vec3, color, load_texture

class Axis(Entity):
    def __init__(self):
        super().__init__()
        # Axe X en rouge
        self.x_axis = Entity(model='cube', scale=(4, 0.1, 0.1), color=color.red, x=2)
        # Axe Y en vert
        self.y_axis = Entity(model='cube', scale=(0.1, 4, 0.1), color=color.green, y=2)
        # Axe Z en bleu
        self.z_axis = Entity(model='cube', scale=(0.1, 0.1, 4), color=color.blue, z=2)

# Ajouter une grille pour mieux voir le positionnement sur le plan XZ
class Grid(Entity):
    def __init__(self):
        super().__init__(model='quad', 
                         scale=50, 
                         rotation_x=90, 
                         color=color.color(0, 0, 0.1, 0.1))


class Arbre(Entity):
    def __init__(self, position=(0,0,0), texture=None):
        if texture is None:
            texture = load_texture('assets/textures/tree_texture.jpg')
        
        super().__init__(
            model='cube',  # Utiliser un modèle de cube pour le tronc, ou 'cylinder' si disponible
            texture=texture,  # Appliquer la texture chargée
            scale=(1, 4, 1),  # Échelle pour faire ressembler à un tronc
            position=position,
            color=color.brown  # Couleur par défaut au cas où la texture n'est pas trouvée
        )
        
        # Ajouter la canopée
        self.canopy = Entity(
            model='sphere',  # Un modèle de sphère pour la canopée
            parent=self,
            y=1.4,  # Positionnement au sommet du tronc
            scale=(3, 2, 3),  # Canopée large
            color=color.green  # Couleur verte pour la canopée
        )

# un chêne
class Chene(Arbre):
    def __init__(self, position):
        super().__init__(
            position=position, 
            texture=load_texture('assets/textures/mature-oak-tree/mature-oak-tree-albedo.png')
        )


# Créer le sol
class Sol(Entity):
    def __init__(self, scale, position=(0,0,0)):
        super().__init__(
            model='plane',  # Utiliser un plan
            scale=(100, 1, 100),  # Définir la taille du sol
            texture=load_texture('assets/textures/sol.png'),  # Assurez-vous d'avoir cette texture dans votre dossier textures
            texture_scale=(10, 10),  # Répéter la texture pour couvrir tout le sol
            color= color.rgb(153, 101, 51),  # Vous pouvez changer ceci pour une texture plus tard
            collider='box',  # Ajouter un collider si nécessaire
            position=(0, 0, 0)  # Positionner le sol dans la scène
        )

class Boite(Entity):
    def __init__(self, position=(0,0,0), scale=(1,1,1)):
        super().__init__(
            model='cube',  # Modèle simple pour la structure de base
            position=position,
            scale=scale,
            texture='white_cube',  # Texture de base, peut être personnalisée
            collider='box',
            color=color.rgb(255, 250, 240)  # Couleur crème
        )

        # Création du couvercle
        self.couvercle = Entity(
            parent=self,
            model='cube',
            scale=(1.1, 0.3, 1.1),  # Le couvercle est légèrement plus large que la base
            position=Vec3(0, 0.65, 0),  # Positionnement au-dessus de la base
            color=color.rgb(150, 75, 0)  # Couleur marron pour le haut
        )
        
class Toit(Entity):
    def __init__(self, position=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__()
        self.position = position
        self.scale = scale

        # Définir les vertices de l'objet pour un toit à deux pentes
        vertices = [
            Vec3(-5, 0, -5),  #0 Point arrière gauche de la base
            Vec3(5, 0, -5),   #1 Point arrière droit de la base
            Vec3(-5, 0, 5),   #2 Point avant gauche de la base
            Vec3(5, 0, 5),    #3 Point avant droit de la base
            Vec3(0, 4, 0)     #4 Pointe du toit
        ]

        # Définir les triangles en utilisant les indices des vertices
        triangles = [
            (1, 0, 4),  # Triangle de droite Attention: L'ordre affecte la visibilité du triangle face interieure ou exterieure
            (2, 3, 4),   # Triangle de gauche
            (0, 2, 4),   # Triangle 
            (3, 1, 4)   # Triangle 
        ]


        # Créer le mesh avec les vertices et triangles, mode 'line' pour voir les arêtes
        mesh = Mesh(vertices=vertices, triangles=triangles, mode='triangle')
        self.model = mesh
        self.color = color.blue

class Maison(Entity):
    def __init__(self, position=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__()
        self.position = position
        self.scale = scale
        self.build_walls()
        self.build_furniture()
        self.build_roof()

    def build_walls(self):
        # Créer les murs de la maison
        floor = Entity(model='cube', scale=(10, 0.1, 10), color=color.light_gray, collider='box', parent=self)
        wall1 = Entity(model='cube', scale=(10, 12, 0.1), position=(0, 6, 5), color=color.rgb(255, 250, 240), parent=self)
        wall2 = Entity(model='cube', scale=(10, 12, 0.1), position=(0, 6, -5), color=color.rgb(255, 250, 240), parent=self)
        wall3 = Entity(model='cube', scale=(0.1, 12, 10), position=(5, 6, 0), color=color.rgb(255, 250, 240), parent=self)
        wall4 = Entity(model='cube', scale=(0.1, 12, 10), position=(-5, 6, 0), color=color.rgb(255, 250, 240), parent=self)

    def build_roof(self):
        # Utiliser la classe Toit pour créer le toit
        self.roof = Toit(position=(0, 12, 0), scale=(1.5, 4, 1.5))  # Position et échelle ajustées pour la maison
        self.roof.parent = self

    def build_furniture(self):
        # Ajouter des meubles
        self.sofa = Entity(model='cube', scale=(2, 0.5, 1), position=(2, 0.25, 3), color=color.brown, parent=self)
        self.tv = Entity(model='cube', scale=(0.5, 1, 1.5), position=(-3, 0.5, 3), color=color.black, parent=self)
        self.table = Entity(model='cube', scale=(2, 0.5, 1), position=(0, 0.25, -3), color=color.dark_gray, parent=self)
        self.bed = Entity(model='cube', scale=(2, 0.5, 2), position=(-2, 0.25, -3), color=color.blue, parent=self)
