from ..core import UsuarioInvalidoError


class Usuario:
    def __init__(self, nome, email, ativo=True):
        if not nome or "@" not in email:
            raise UsuarioInvalidoError(f"Usuario invalido: {nome} / {email}")
        self.nome = nome
        self.email = email
        self.ativo = ativo

    def desativar(self):
        self.ativo = False

    def resumo(self):
        estado = "ativo" if self.ativo else "inativo"
        return f"{self.nome} <{self.email}> - {estado}"
