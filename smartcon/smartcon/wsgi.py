"""
WSGI config for smartcon project.

apt-get install libapache2-mod-wsgi
sudo gedit  /etc/apache2/sites-available/000-default.conf
sudo gedit /etc/apache2/apache2.conf 
sudo gedit /etc/hosts


    Alias /static /home/Programas/smartcon/smartcon/sistema/static
    <Directory /home/Programas/smartcon/smartcon/sistema/static>
        Require all granted
    </Directory>

    <Directory /home/Programas/smartcon/smartcon/smartcon>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    WSGIDaemonProcess smartcon python-home=/home/Programas/smartcon/smartcon python-path=/home/Programas/smartcon/smartcon
    WSGIProcessGroup smartcon
    WSGIScriptAlias / /home/Programas/smartcon/smartcon/smartcon/wsgi.py

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smartcon.settings')

application = get_wsgi_application()
