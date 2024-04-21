from ursina import Entity, color, load_texture

class Granite(Entity):
    def __init__(self, position):
        super().__init__(
            model='cube',
            texture=load_texture('assets/textures/granite.jpg'),  # Assurez-vous d'avoir cette texture dans votre dossier textures
            scale=(0.5, 0.5, 0.5),
            position=position,
            color=color.white,  # Vous pouvez changer ceci pour une texture plus tard
            collider='box'
        )
