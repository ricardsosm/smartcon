# Sistema de clientes para smart contract em Python
com Django e Mysql(MariaDB)
## Pré-requisitos do sistema
- [Git](https://git-scm.com)
- Python 3.7.1
```
Para debian 9.7 é necessário instalar antes
sudo apt-get install build-essential checkinstall python-dev python-setuptools python-pip python-smbus
sudo apt-get install zlib1g-dev libffi-dev 
sudo apt-get install libncursesw5-dev libgdbm-dev libc6-dev libsqlite3-dev tk-dev libssl-dev openssl
sudo apt install default-libmysqlclient-dev
```
- Virtualenv
- Django 2.1
- Maria db 10.1

# Instalando o virtalenv
```
sudo pip install virtualenv
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
pip install web3 
pip install eth_account
```
# baixe o projeto
