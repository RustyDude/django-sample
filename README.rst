====================
The Russel Project
====================

A Demo Django Project for application purposes.

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


Contact/Inquires
==========

If you've any questions/inquiries regarding the demo or me pesonally, 
you can send me a message through the demo project's contact function
or via skype/gmail icons in the footer of each pages. Else you may contact 
me at this email address: `rustydude09@gmail.com <mailto:RustyDude09@gmail.com>`_
