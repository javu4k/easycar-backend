# EasyCar - Sistema de Aluguel de Carros

## Descricao do Projeto
O EasyCar e uma API REST desenvolvida em Django para informatizar o processo de aluguel de veiculos. O sistema permite o cadastro de clientes, gestao de frota e registro de alugueis, com controle de acesso baseado em grupos de usuarios (Funcionarios e Clientes).

Projeto desenvolvido para a disciplina de Back-End Python.

## Integrantes
* Julia (Desenvolvedora 1 - Infraestrutura e Gestao de Usuarios)
* Felipe (Desenvolvedor 2 - Gestao de Frota e Transacoes)

## Tecnologias Utilizadas
* Python 3
* Django & Django REST Framework
* SQLite (Banco de Dados)
* drf-spectacular (Documentacao Swagger/Redoc)

## Pre-requisitos
* Python instalado (versao 3.8 ou superior)
* Git instalado

## Instalacao e Configuracao

1. Clone o repositorio:
   git clone https://github.com/SEU-USUARIO/easycar-backend.git
   cd easycar-backend

2. Crie e ative o ambiente virtual:
   # No Windows:
   python -m venv venv
   venv\Scripts\activate

   # No Linux/Mac:
   python3 -m venv venv
   source venv/bin/activate

3. Instale as dependencias:
   pip install -r requirements.txt

4. Realize as migracoes do banco de dados:
   python manage.py migrate

5. Configuracao Inicial (Criacao de Grupos):
   Para o sistema funcionar corretamente, e necessario criar os grupos de permissao.
   Execute o seguinte comando no terminal para abrir o shell do Django:
   
   python manage.py shell

   Dentro do shell, cole os comandos abaixo e aperte Enter:
   
   from django.contrib.auth.models import