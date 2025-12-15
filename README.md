# EasyCar - Sistema de Aluguel de Carros

## Descricao do Projeto
O **EasyCar** e uma API REST desenvolvida em Django para informatizar o processo de aluguel de veiculos. Atualmente, muitos registros sao feitos manualmente, dificultando o controle. Este sistema permite o cadastro de clientes, gestao de frota e registro de alugueis, garantindo seguranca e organizacao dos dados.

O projeto implementa autenticacao via Token e controle de acesso baseado em grupos (Funcionarios e Clientes).

## Integrantes
* Julia (Desenvolvedora 1 - Infraestrutura e Gestao de Usuarios)
* Felipe (Desenvolvedor 2 - Gestao de Frota e Transacoes)

## Tecnologias Utilizadas
* Python 3
* Django
* Django REST Framework (DRF)
* SQLite (Banco de Dados)
* drf-spectacular (Documentacao Swagger/Redoc)

## Pre-requisitos
* Python instalado no Windows
* Git instalado

## Instalacao e Configuracao (Windows)

Siga os passos abaixo para rodar o projeto em ambiente Windows:

1. Clone o repositorio:
```bash
git clone [https://github.com/javu4k/easycar-backend.git](https://github.com/javu4k/easycar-backend.git)
cd easycar-backend
Crie e ative o ambiente virtual:

```bash

python -m venv venv
venv\Scripts\activate
Instale as dependencias do projeto:

```bash

pip install -r requirements.txt
Realize as migracoes do banco de dados:

```bash

python manage.py migrate
Configuracao Inicial (Criacao de Grupos): Para o sistema de permissoes funcionar, e necessario criar os grupos "Funcionários" e "Clientes". Execute o comando abaixo para abrir o shell do Django:

```bash

python manage.py shell
Dentro do shell interativo, cole o seguinte codigo Python e aperte Enter:

Python

from django.contrib.auth.models import Group
Group.objects.get_or_create(name='Funcionários')
Group.objects.get_or_create(name='Clientes')
exit()
Crie um superusuario (para acessar o Painel Administrativo):

```bash

python manage.py createsuperuser
Como Rodar a Aplicacao
Execute o comando abaixo para iniciar o servidor de desenvolvimento:

```bash

python manage.py runserver
O sistema estara disponivel em: http://127.0.0.1:8000/

Documentacao da API
A documentacao interativa gerada automaticamente pode ser acessada nos seguintes enderecos:

Swagger UI: http://127.0.0.1:8000/api/docs/

Redoc: http://127.0.0.1:8000/api/docs/redoc/

Principais Rotas e Recursos
O sistema possui as seguintes rotas principais:

Autenticacao
POST /api/auth/token/ - Obtencao de Token de acesso.

Usuarios e Perfis (Apenas Funcionarios)
GET /api/users/ - Listagem de usuarios.

POST /api/perfis-clientes/ - Cadastro de novos perfis de clientes.

Frota (Carros)
GET /api/carros/ - Listar carros disponiveis (Acesso liberado).

POST /api/carros/ - Cadastrar novo carro (Apenas Funcionarios).

Alugueis
POST /api/alugueis/ - Registrar um novo aluguel (Apenas Funcionarios).

GET /api/alugueis/ - Listar alugueis realizados.

Estrutura do Projeto
accounts/: Aplicativo responsavel pela gestao de usuarios, autenticacao e perfil do cliente.

core/: Aplicativo responsavel pela regra de negocio, gestao de carros e alugueis.

cconfig/: Configuracoes globais do projeto Django.