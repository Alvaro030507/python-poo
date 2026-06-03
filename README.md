# Treino POO — Projeto Hands-on

Projeto de apoio ao treinamento de Python POO (2h) do Time Governança.
Materializa exatamente os exemplos dos slides: comunicação entre arquivos,
class/self e organização de pastas por responsabilidade.

## Como rodar

A partir da pasta que CONTÉM `treino_poo/`:

```
python -m treino_poo.main
```

Saída esperada:

```
Treino POO v1.0.0
Ana <ana@empresa.com> - ativo
Bruno <bruno@empresa.com> - inativo
Carla <carla@empresa.com> - ativo
Backup salvo em: .../treino_poo/backup/relatorio_usuarios.txt
```

## Por que NÃO rodar `python treino_poo/main.py`

Os imports são relativos ao pacote (`from ..core import ...`).
Rodar o arquivo solto quebra de propósito — isso reforça o conceito de pacote
ensinado em aula.

## Direção de dependência

```
modules -> services -> models / core
```

O de fora pode importar o de dentro; o de dentro nunca importa o de fora.

## Estrutura

```
treino_poo/
├── __init__.py
├── main.py
├── core/
│   ├── __init__.py
│   ├── config.py
│   └── exceptions.py
├── models/
│   ├── __init__.py
│   └── usuario.py
├── services/
│   ├── __init__.py
│   └── relatorio_service.py
├── modules/
│   ├── __init__.py
│   └── relatorio_usuarios.py
├── download/
│   ├── __init__.py
│   └── fonte_usuarios.py
├── backup/
│   ├── __init__.py
│   ├── backup_service.py
│   └── .gitkeep
└── logs/
    └── .gitkeep
```

## Exercício pós-aula

Adicione a funcionalidade de Produtos respeitando as camadas:

1. `models/produto.py` com a classe `Produto` (nome, preco, `aplicar_desconto`).
2. `services/produto_service.py` que gera um relatório de produtos.
3. `modules/relatorio_produtos.py` que orquestra tudo.
4. Crie a fachada nos `__init__.py` dos pacotes envolvidos.
5. Atualize `main.py` para rodar os dois relatórios.

Regra: `models/produto.py` não importa nada de services nem de modules.