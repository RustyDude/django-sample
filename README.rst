====================
Project: Django Sample
====================

A Demo Django Project for application purposes.
Developed a personal blog-like site using the Django framework in Python. Serving a multi-page web application with Home, Profile, and Contacts pages. Using Bootstrap, LESS, Django-markdown, etc.

Local Deployment
==================

#. create virtualenv then fork or download project into your virtualenv::
	
	'virtualenv env-name'


#. go the main project directory and install dependecies using requirement::

	'pip install -r requirement.txt'


#. create django migrations:: 

	'manage.py makemigrations'
	'manage.py migrate'


#. load initial data/fixtures::
	
	'manage.py loaddata fixtures/*.json'


#. run the following and check out the site your browser::
  
	'manage.py runserver 8000' and type in 'localhost:8000' in your browser

  

Credits
=========

* This Project is powered by `Django <https://www.djangoproject.com/>`_
