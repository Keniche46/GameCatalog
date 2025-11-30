# Catálogo de Jogos - Projeto Final Desenvolvimento Web II

**Instituto Federal do Ceará - Campus Maranguape**  
Curso Técnico Integrado em Informática  
Professor: Thomaz Maia  

---

## 1. Descrição do Projeto
Aplicação web para cadastro e gerenciamento de jogos, permitindo adicionar, visualizar, editar e deletar jogos com informações como nome, gênero, nota, descrição e imagem.

O projeto utiliza **Flask** com integração de HTML, CSS, JavaScript e **SQLAlchemy** para persistência de dados, demonstrando a comunicação entre frontend e backend de forma completa.

---

## 2. Funcionalidades
- **CRUD Completo**: adicionar, editar, deletar e listar jogos; imagens são removidas junto com o registro.  
- **Filtros e Busca**: filtrar jogos por gênero.  
- **Interface Interativa**: botões estilizados, efeitos de hover e layout responsivo.  
- **Persistência de Dados**: SQLAlchemy gerencia o banco de dados SQLite.  
- **Upload de Imagens**: imagens salvas em `core/static/img` com nomes únicos para evitar conflitos.  

---

## 3. Estrutura de Pastas
```bash
/projeto_final
│
├─ /core
│ ├─ /controllers
│ │ └─ views.py
│ ├─ /models
│ │ └─ models.py
│ ├─ /static
│ │ ├─ /css
│ │ │ └─ style.css
│ │ ├─ /js
│ │ │ └─ script.js
│ │ └─ /img
│ └─ /templates
│ ├─ base.html
│ ├─ index.html
│ ├─ add_game.html
│ ├─ edit_game.html
│ └─ view_game.html
│
├─ instance/
│ └─ database.db
│
├─ run.py
└─ README.md
```

---

## 4. Tecnologias Utilizadas
- Python 3  
- Flask  
- SQLAlchemy  
- HTML / CSS / JavaScript  
- Werkzeug (upload seguro de arquivos)  

---

## 5. Como Executar
1. Clone o repositório:

```bash
git clone <link_do_repositorio>
```

2. Crie e ative o ambiente virtual:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute a aplicação:
```bash
python3 run.py
```

5. Acesse a aplicação:
```www
http://127.0.0.1:5000/
```

---

## 6. Considerações Técnicas
- **Flask**: gerencia as rotas, templates e integração com o backend.  
- **SQLAlchemy**: mapeamento objeto-relacional para armazenar os jogos no banco SQLite.  
- **Upload de imagens**: imagens são salvas em `core/static/img` com nomes seguros via `werkzeug.utils.secure_filename()`.  
- **Templates**: `base.html` contém a estrutura principal; `index.html`, `add_game.html`, `edit_game.html` e `view_game.html` herdam da base e utilizam **Jinja2** para renderização dinâmica.  
- **Estilo e Interatividade**: CSS moderno e responsivo; botões estilizados; efeitos de hover; JS usado para interações e validações básicas.  

---

## 7. Autores
- **Heitor Martins**  
- **Rennan Medeiros**  

---
