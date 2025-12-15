# EasyCar - Sistema de Aluguel de Carros

## 📌 Descrição do Projeto
O **EasyCar** é uma API REST desenvolvida em Django para informatizar o processo de aluguel de veículos. O sistema permite o cadastro de clientes, gestão de frota e registro de aluguéis, com controle de acesso baseado em grupos de usuários (Funcionários e Clientes).

Projeto desenvolvido para a disciplina de Back-End Python.

## 👥 Integrantes
* **Julia** (Desenvolvedora 1 - Infraestrutura e Gestão de Usuários)
* **Felipe** (Desenvolvedor 2 - Gestão de Frota e Transações)

## 🛠 Tecnologias Utilizadas
* Python 3
* Django & Django REST Framework
* SQLite (Banco de Dados)
* drf-spectacular (Documentação Swagger/Redoc)

## ⚙️ Pré-requisitos
* Python instalado (versão 3.8 ou superior)
* Git instalado

## 🚀 Instalação e Configuração

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU-USUARIO/easycar-backend.git](https://github.com/SEU-USUARIO/easycar-backend.git)
   cd easycar-backend

   Crie e ative o ambiente virtual:


# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
Instale as dependências:


pip install -r requirements.txt
Realize as migrações do banco de dados:


python manage.py migrate
Crie os Grupos de Usuários (Configuração Inicial):


# Abra o shell do Django:
python manage.py shell

# Cole os comandos abaixo:
from django.contrib.auth.models import Group
Group.objects.get_or_create(name='Funcionários')
Group.objects.get_or_create(name='Clientes')
exit()
Crie um superusuário (para acessar o Admin):

python manage.py createsuperuser

Como Rodar a Aplicação
Execute o comando abaixo para iniciar o servidor de desenvolvimento:

python manage.py runserver

O sistema estará disponível em http://127.0.0.1:8000/.

Documentação da API
A documentação interativa (Swagger UI) pode ser acessada em:

Swagger: http://127.0.0.1:8000/api/docs/

Redoc: http://127.0.0.1:8000/api/docs/redoc/

Estrutura do Projeto
accounts/: Gestão de usuários, autenticação e perfil do cliente.

core/: Gestão de carros e aluguéis.

cconfig/: Configurações globais do projeto.