
![Captura de tela 2025-04-09 123351](https://github.com/user-attachments/assets/8f67b29b-9c15-4d3f-b4c6-8881ad4f7d6f)

# TinyLink - Encurtador de URLs

Um projeto simples de encurtador de URLs desenvolvido com Django.

## Funcionalidades

- Encurtamento de URLs longas
- Geração automática de códigos curtos únicos
- Redirecionamento automático para a URL original
- Interface minimalista e responsiva

## Requisitos

- Python 3.8+
- Django 5.2+

## Instalação

1. Clone o repositório
2. Crie um ambiente virtual:
```bash
python -m venv venv
```

3. Ative o ambiente virtual:
```bash
# Windows
.\venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Instale as dependências:
```bash
pip install django
```

5. Execute as migrações:
```bash
python manage.py migrate
```

6. Inicie o servidor:
```bash
python manage.py runserver
```

7. Acesse http://localhost:8000 no seu navegador

## Como usar

1. Acesse a página inicial
2. Cole a URL que deseja encurtar no campo de texto
3. Clique em "Encurtar"
4. Use a URL encurtada gerada

## Estrutura do Projeto

```
tinylink/
├── manage.py
├── tinylink/          # Configurações do projeto
└── shortener/         # App principal
    ├── models.py      # Modelo Link
    ├── views.py       # Views do app
    ├── urls.py        # URLs do app
    └── templates/     # Templates HTML
``` 
