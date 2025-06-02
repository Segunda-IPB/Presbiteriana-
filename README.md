# 🌿 Site da Igreja Presbiteriana

Este é um sistema web desenvolvido com Django para gerenciar a agenda de eventos e as mensagens de contato da Igreja Presbiteriana. O projeto permite o cadastro, visualização, edição e exclusão de eventos e mensagens, com um painel administrativo acessível mediante login.

## 🔧 Tecnologias Utilizadas

- Python 3.11
- Django 5.2.1
- PostgreSQL
- Bootstrap 5
- HTML/CSS
- JavaScript

## 📁 Estrutura do Projeto

- `apps/core/`: App principal com os modelos de `Evento` e `MensagemContato`
- `templates/`: HTML dos templates principais e de autenticação
- `static/`: arquivos estáticos (CSS, imagens, etc.)
- `registration/`: páginas de login/logout do admin
- `painel/`: painel exclusivo para administradores autenticados

## ⚙️ Funcionalidades

- ✅ Cadastro de eventos com título, descrição, data e hora
- ✅ Página de Fale Conosco com formulário para dúvidas
- ✅ CRUD completo para eventos e mensagens de contato
- ✅ Visualização da Agenda com os eventos e visualização das Sociedades da igreja 
