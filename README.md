# Projeto - Site Institucional (Associação)
Estrutura inicial em Django com páginas:
- Home
- Sobre
- Diretoria (lista e detalhe)
- Notícias (lista e detalhe)
- Contato (form)
- Formulário de Associação (form)

## Como usar (local)
1. Crie um ambiente virtual e instale dependências:
   ```
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate # macOS/Linux
   pip install -r requirements.txt
   ```
2. Rode migrações e crie superuser:
   ```
   python manage.py migrate
   python manage.py createsuperuser
   ```
3. Rode o servidor:
   ```
   python manage.py runserver
   ```
4. Acesse o admin em `/admin/` para cadastrar Áreas, Membros e Notícias.

Observações:
- Substitua `static/img/bg.jpg` por uma imagem de hero de alta qualidade.
- Para enviar e-mails de contato, configure o EMAIL_BACKEND no settings.py.
