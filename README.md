# Site-Ass.-Advogados

Projeto Django para a Associação Jurídica Pricila Cheida & Fred Alvão.

## 🚀 Como rodar localmente

1. Clone o repositório:
bash
   git clone https://github.com/RerissonHRS/Site-Ass.-Advogados.git
   cd Site-Ass.-Advogados
Crie o ambiente virtual:

bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac
Instale as dependências:

bash
pip install -r requisitos.txt
Configure o .env:

bash
cp .env.example .env
Execute as migrações:

bash
python manage.py migrate
Inicie o servidor:

bash
python manage.py runserver
📁 Estrutura do projeto
site_associacao/ — núcleo do projeto Django

essencial/, régia/, notícias/ — apps internos

estático/ — arquivos estáticos (CSS, JS, imagens)

modelos/ — templates HTML

📦 Requisitos
Python 3.10+

Django 4.x

Git