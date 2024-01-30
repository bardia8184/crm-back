# Django Rest Framework
Setup project environment with virtualenv and pip.

$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt

# You may want to change the name `projectname`.
$ django-admin startproject --template https://github.com/juanifioren/django-project-template/archive/master.zip projectname

$ cd projectname/
$ python manage.py migrate
$ python manage.py runserver
