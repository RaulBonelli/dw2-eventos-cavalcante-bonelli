# Sistema Web de Gestão de Eventos Acadêmicos — Aula 6 (DW2)

Projeto-exemplo da **Aula 6**. Etapa 2 do Projeto Integrador: os dados deixam de viver em uma lista na memória e passam a ser **gravados em um banco de dados**, com SQL escrito à mão.

> A diferença para a Aula 4: cadastre um evento, **encerre o servidor**, execute novamente — e o evento continua lá.

O código usa **apenas os comandos apresentados nos Anexos de Python das Aulas 2 a 6**. Nada além disso.

## Integrantes da dupla

- Integrante 1: _(nome)_
- Integrante 2: _(nome)_

---

## Estrutura

```
projeto_aula06/
├── app.py                        # cria o app, registra o Blueprint e as tabelas
├── database.py                   # conexão + criação das tabelas (DER da Aula 5)
├── consultar.py                  # "prova dos nove": só consulta, sem subir o servidor
├── models/
│   └── evento.py                 # Model: entidade Evento
├── dao/
│   └── evento_dao.py             # DAO: todo o SQL fica aqui
├── controllers/
│   └── evento_controller.py      # Controller: usa o DAO, não conhece SQL
├── templates/
│   └── index.html                # View: lista + formulário
├── instance/                     # (gerado) eventos.db — ignorado pelo Git
├── requirements.txt
├── .gitignore
└── README.md
```

| Camada | Arquivo | Responsabilidade |
| --- | --- | --- |
| Model | `models/evento.py` | Representa a entidade Evento. |
| View | `templates/index.html` | Apresenta os dados e coleta o formulário. |
| Controller | `controllers/evento_controller.py` | Coordena a requisição; pede ao DAO. |
| Acesso a dados | `dao/evento_dao.py` | Concentra o SQL (INSERT e SELECT). |
| Infraestrutura | `database.py` | Conexão e criação das tabelas. |

---

## Como executar

Sempre a partir da **raiz do projeto** (a pasta que contém `app.py`).

**Windows (cmd):**

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

**macOS / Linux:**

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Abra: http://127.0.0.1:5000

---

## A prova dos nove (o ponto central da aula)

1. Rode `python app.py` e **cadastre alguns eventos**.
2. Encerre o servidor com **Ctrl+C**.
3. Execute:

```
python consultar.py
```

4. Os eventos aparecem — porque foram **gravados no banco**, não em uma lista na memória.

---

## O que observar no código

- **`?` nos comandos SQL** (`dao/evento_dao.py`): os valores nunca são colados dentro do texto do comando — isso protege contra SQL Injection.
- **`conexao.commit()`**: sem ele, o `INSERT` não é confirmado e **nada é gravado**, sem gerar erro algum. É o tropeço mais comum da aula.
- **Tuplas → objetos**: o banco devolve tuplas; o DAO percorre as linhas com um `for` e monta objetos `Evento`, para que a View escreva `e.nome` em vez de `linha[1]`. Na Aula 7, o ORM fará isso automaticamente.
- **O Controller não conhece SQL**: ele só chama `EventoDAO.salvar()` e `EventoDAO.listar()`. É essa separação que permitirá trocar a tecnologia de acesso a dados na próxima aula.
- **`os.makedirs`** em `database.py`: o SQLite cria o *arquivo*, mas não a *pasta*.

## Comandos de Python utilizados

Todos já vistos nos anexos:

| Comando | Anexo |
| --- | --- |
| `import`, `from ... import`, `def`, `return`, `if`, `@decorador` | Aula 2 |
| listas, `append`, `for ... in`, classes (`class`, `__init__`, `self`), `request.form["x"]`, `render_template`, `redirect`, `{{ }}` e `{% for %}` | Aula 4 |
| valor padrão de parâmetro (`id=None`) | Aula 5 |
| `import sqlite3`, `connect`, `cursor`, `execute`, `?`, tuplas, aspas triplas, `fetchall`, `commit`, `close`, `@staticmethod`, `os.makedirs` | Aula 6 |

## Esquema criado (a partir do DER da Aula 5)

| Tabela | Colunas |
| --- | --- |
| evento | id (PK), nome, data, local, vagas |
| participante | id (PK), nome, email |
| inscricao | id (PK), participante_id, evento_id, data_inscricao |

> Nesta aula a aplicação usa a tabela `evento` (inserção e consulta). As demais já ficam criadas para as próximas etapas. O CRUD completo é o conteúdo da Aula 8.

## Próximos passos

| Etapa | Conteúdo | Aula |
| --- | --- | --- |
| 2 (em curso) | Persistência com SQL direto | 6 |
| 2 | O mesmo DAO, agora com ORM | 7 |
| 2 | CRUD completo integrado à interface | 8 |

---

*Desenvolvimento Web II — CST em Desenvolvimento de Software Multiplataforma — Fatec Porto Ferreira*
*Professor: Vagner dos Santos*
