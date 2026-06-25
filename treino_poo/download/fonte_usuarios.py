class FonteUsuarios:
    def __init__(self, registros):
        self.registros = registros

    @classmethod
    def exemplo(cls):
        return cls([
            {"nome": "Ana", "email": "ana@empresa.com","idade": 28, "ativo": True},
            {"nome": "Bruno", "email": "bruno@empresa.com", "idade": 35, "ativo": False},
            {"nome": "Carla", "email": "carla@empresa.com", "idade": 22, "ativo": True},
            {"nome": "Alvaro", "email": "alvaro@empresa.com", "idade": 41, "ativo": True}, # 1.2 Adicionar um usuário
        ])

    def buscar(self):
        return list(self.registros)
