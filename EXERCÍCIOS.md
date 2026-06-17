# Exercícios — Treino POO (Python)

Legenda de dificuldade:
- 🟢 Iniciante
- 🟡 Intermediário

---

## Nível 1 — Aquecimento (🟢)

### 1.1 — Reativar usuário
Objetivo: dar à classe `Usuario` a capacidade de voltar a ficar ativo,
como espelho do método `desativar()` que já existe.
Onde mexer: `models/usuario.py`.
Pronto quando:
- No terminal, `u.desativar()` seguido de `reativar()` faz o `resumo()`
  voltar a mostrar "ativo".

### 1.2 — Quarto usuário
Objetivo: adicionar mais uma pessoa aos dados de exemplo.
Onde mexer: `download/fonte_usuarios.py`.
Pronto quando:
- Rodar `python -m treino_poo.main` mostra 4 linhas no relatório.

### 1.3 — Total no relatório
Objetivo: o relatório deve terminar com uma linha "Total: N usuários".
Onde mexer: `services/relatorio_service.py`.
Pronto quando:
- A última linha da saída mostra o total correto.

---

## Nível 2 — Dando mais vida ao usuário (🟡)

### 2.1 — Campo "idade" com validação
Objetivo: cada usuário passa a ter idade, e ela precisa ser válida.
Idade negativa ou maior que 130 não deve nascer, usando o erro que já
existe (`UsuarioInvalidoError`). O `resumo()` também passa a mostrar a
idade.
Onde mexer: `models/usuario.py` e os dados em `download/fonte_usuarios.py`.
Pronto quando:
- Criar um usuário com idade -5 levanta `UsuarioInvalidoError`.

### 2.2 — Normalizar o e-mail
Objetivo: e-mails devem ser guardados sempre em minúsculas e sem espaços
nas pontas.
Onde mexer: `models/usuario.py`.
Pronto quando:
- `Usuario("Ana", "  ANA@Empresa.com ")` guarda "ana@empresa.com".

---

## Nível 3 — Filtros e estatísticas (🟡)

### 3.1 — Relatório só de ativos
Objetivo: poder gerar um relatório apenas com usuários ativos, sem
duplicar o método `gerar_texto()` (use um parâmetro).
Onde mexer: `services/relatorio_service.py`.
Pronto quando:
- Gerando "apenas ativos", o usuário inativo some da saída.

### 3.2 — Ordenar por nome
Objetivo: o relatório sai em ordem alfabética de nome, independente da
ordem da fonte.
Onde mexer: `services/relatorio_service.py`.
Pronto quando:
- A saída fica em ordem alfabética.

### 3.3 — Estatísticas no rodapé
Objetivo: o relatório termina com "Ativos: X | Inativos: Y", junto ao
total.
Onde mexer: `services/relatorio_service.py`.
Pronto quando:
- Os números batem com os dados reais.

---

## Desafio final — Feature de ponta a ponta

Objetivo: implementar "usuários com perfil" respeitando todas as camadas.
O `Usuario` ganha um campo "perfil" (só aceita "admin" ou "comum", com
validação), os dados de exemplo passam a incluir o perfil, o relatório
agrupa os usuários por perfil, e a lista de perfis válidos vira
configuração em `core/config.py`.
Onde mexer: `models/`, `download/`, `services/`, `core/config.py`.
Pronto quando:
- O relatório mostra os usuários agrupados por perfil, a validação
  recusa perfis inválidos, e nada disso foi parar dentro do `main.py`.

Pergunta de reflexão (responda por escrito, sem código):
- Quantas pastas você precisou tocar? Cada mudança ficou no lugar certo
  segundo a regra "uma pasta, um motivo"?

---

## Apêndice — Auto-checklist antes de considerar um exercício pronto

- O código novo foi para a pasta certa (a do seu papel)?
- O `main.py` continua só coordenando, sem regra de negócio?
- Você modificou um arquivo existente em vez de criar um novo?
- A validação de dados continua acontecendo no `Usuario`?
- O relatório ainda roda com `python -m treino_poo.main`?
