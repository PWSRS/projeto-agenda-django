# Iniciar o projeto Django

python -m venv venv
. venv/bin/activate (no MAC)
. \venv\scripts\activate (ativa o ambiente virutal)
pip install django
django-admin startproject project .

# Configurar o git

git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
# Configure o .gitignore
git init
git add . (esse comando adiciona um arquivo no Git)
git commit -m 'Mensagem' (normalmente a primeira mensagem é Initial)
git remote add origin URL_DO_GIT (ver vídeo expplicativo)