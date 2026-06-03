from ..services import RelatorioService
from ..download import FonteUsuarios


class RelatorioUsuarios:
    def executar(self):
        service = RelatorioService(FonteUsuarios.exemplo())
        return service.gerar_texto()
