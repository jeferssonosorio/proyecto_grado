# proyecto_grado
Repositorio para proyecto de grato "Physio Story"

Repositorio creado para desarrollo proyecto de grato "Physio Story"

Setup The first thing to do is to clone the repository:

HTTP
$ git clone https://github.com/jeferssonosorio/proyecto_grado.git

or
SSH
$ git clone git@github.com:jeferssonosorio/proyecto_grado.git

$ cd Prueba-tecnica-metgroup/ Create a virtual environment to install dependencies in and activate it:

$ virtualenv env 
$ source env/bin/activate Then install the dependencies:

(env)$ pip install -r requirements.txt Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv.

The file requimiens.txt does not contain libraries necessary to connect to the DB.

Once pip has finished downloading the dependencies:

(env)$ cd project (env)$ python manage.py runserver And navigate to http://127.0.0.1:8000/.
