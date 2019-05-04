# Sistema de clientes para smart contract em Python
com Django e Mysql(MariaDB)
## Pré-requisitos do sistema
- [Git](https://git-scm.com)
- Python 3.7.1
```

Para Linux debian 9.7 é necessário instalar antes
sudo apt-get install build-essential checkinstall python-dev python-setuptools python-pip python-smbus zlib1g-dev libffi-dev libncursesw5-dev libgdbm-dev libc6-dev libsqlite3-dev tk-dev libssl-dev openssl default-libmysqlclient-dev

```
```
Para Windows é necessário instalar antes
Visual studio >= 2014
```
- Virtualenv
- Django 2.1
- Maria db 10.1

# Instalando o MariaDB
```
apt-get install mariadb-server

# Instalando o virtualenv
```
sudo pip install virtualenv
ou
curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash

```
# Criando o ambiente virtual
```
pyenv install 3.7.1 
pyenv virtualenv 3.7.1 smart 
pyenv activate smart
```
# Instalando Django 2.1
```
pip install django==2.1
```
# Instalando mysqlclient
```
pip install mysqlclient
```
# Instalando web3.py
```
pip install web3 
pip install eth_account
pip install py-solc
python -m solc.install v0.4.25
```
# baixe o projeto
