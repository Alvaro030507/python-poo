from ..models import Usuario


class RelatorioService:
    def __init__(self, fonte):
        self.fonte = fonte

    def gerar_texto(self):
        brutos = self.fonte.buscar()
        usuarios = [Usuario(**b) for b in brutos]
        linhas = [u.resumo() for u in usuarios]
        return "\n".join(linhas)
