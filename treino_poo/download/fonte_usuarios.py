class FonteUsuarios:
    def __init__(self, registros):
        self.registros = registros

    @classmethod
    def exemplo(cls):
        return cls([
            {"nome": "Ana", "email": "ana@empresa.com", "ativo": True},
            {"nome": "Bruno", "email": "bruno@empresa.com", "ativo": False},
            {"nome": "Carla", "email": "carla@empresa.com", "ativo": True},
        ])

    def buscar(self):
        return list(self.registros)
