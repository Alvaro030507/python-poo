import os

from .core import APP_NOME, VERSAO
from .modules import RelatorioUsuarios
from .backup import BackupService


def main():
    print(f"{APP_NOME} v{VERSAO}")
    relatorio = RelatorioUsuarios()
    texto = relatorio.executar()
    print(texto)
    raiz = os.path.dirname(os.path.abspath(__file__))
    backup = BackupService(raiz)
    caminho = backup.salvar("relatorio_usuarios.txt", texto)
    print(f"Backup salvo em: {caminho}")


if __name__ == "__main__":
    main()
