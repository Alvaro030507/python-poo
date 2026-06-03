import os
from datetime import datetime

from ..core import PASTA_BACKUP, PASTA_LOGS


class BackupService:
    def __init__(self, raiz):
        self.raiz = raiz
        self.pasta_backup = os.path.join(raiz, PASTA_BACKUP)
        self.pasta_logs = os.path.join(raiz, PASTA_LOGS)

    def salvar(self, nome_arquivo, conteudo):
        os.makedirs(self.pasta_backup, exist_ok=True)
        os.makedirs(self.pasta_logs, exist_ok=True)
        caminho = os.path.join(self.pasta_backup, nome_arquivo)
        with open(caminho, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)
        self._registrar_log(nome_arquivo)
        return caminho

    def _registrar_log(self, nome_arquivo):
        carimbo = datetime.now().isoformat(timespec="seconds")
        linha = f"{carimbo} backup gerado: {nome_arquivo}\n"
        caminho_log = os.path.join(self.pasta_logs, "backup.log")
        with open(caminho_log, "a", encoding="utf-8") as arquivo:
            arquivo.write(linha)
