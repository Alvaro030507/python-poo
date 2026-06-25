from ..core import UsuarioInvalidoError


class Usuario:
    def __init__(self, nome, email, idade=0, ativo=True):
        email = email.strip().lower()

        if not nome or "@" not in email:
            raise UsuarioInvalidoError(f"Usuario invalido: {nome} / {email}")
        
        if idade < 0 or idade > 130:
            raise UsuarioInvalidoError(f"Idade inválida: {idade}")

        self.nome = nome
        self.email = email
        self.idade = idade
        self.ativo = ativo

    def desativar(self):
        self.ativo = False

    # 1.1 Reativar usuário
    def reativar(self):
        self.ativo = True

    def resumo(self):
        estado = "ativo" if self.ativo else "inativo"
        return f"{self.nome} <{self.email}> - {self.idade} anos - {estado}"
