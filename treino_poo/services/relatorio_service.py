from ..models import Usuario


class RelatorioService:
    def __init__(self, fonte):
        self.fonte = fonte

    def gerar_texto(self, apenas_ativos=False):
        brutos = self.fonte.buscar()
        usuarios = [Usuario(**b) for b in brutos]

        if apenas_ativos: # 3.1
            usuarios = [u for u in usuarios if u.ativo] # 3.1 

        linhas = [u.resumo() for u in usuarios]
        
        total = len(usuarios) # 1.3 Cálculo totas de usuarios
        linhas.append(f"Total: {total} usuários") # 1.3 Linha final exibe o total
        
        return "\n".join(linhas)
