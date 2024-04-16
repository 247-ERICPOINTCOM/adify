# adify
https://jobbookads.pythonanywhere.com/


# To setup 

Make sure you're in the project directory:

``` bash
cd /path/to/adify
```

Set up your environment to have python-3.10. At the time of writing this
python-3.12 is out and Python anywhere only has 3.10 available. So ideally
your environment should also reflect that. I would recommend that you just
install a seperate version of python on your system because you might break
something on your system. 


``` bash
path/to/python-3.10 -m venv venv
```


then run the env: 

``` bash
source ./venv/bin/activate 
```


if you want to turn it off you can run:

``` bash
deactivate
```

You can then install all the required files with:

``` bash
# Assuming python env is on & in root folder
pip install -r requirements.txt
```


Create/Acquire the .env file which houses all the GLOBAL variables which
contains the following variables that you need.

``` env
DEBUG=                  <your-value>
SECRET_KEY=             <your-value>

DATABASE_ENGINE=        <your-value>
DATABASE_NAME=          <your-value>
DATABASE_USER=          <your-value>
DATABASE_PASS=          <your-value>
DATABASE_HOST=          <your-value>
DATABASE_PORT=          <your-value>

DEV_DATABASE_ENGINE=    <your-value>
DEV_DATABASE_NAME=      <your-value>
DEV_DATABASE_USER=      <your-value>
DEV_DATABASE_PASS=      <your-value>
DEV_DATABASE_HOST=      <your-value>
DEV_DATABASE_PORT=      <your-value>

EMAIL_BACKEND=          <your-value>
EMAIL_HOST=             <your-value>
EMAIL_USE_TLS=          <your-value>
EMAIL_PORT=             <your-value>
EMAIL_HOST_USER=        <your-value>
EMAIL_HOST_PASSWORD=    <your-value>
DEFAULT_FROM_EMAIL=     <your-value>

PAYPAL_RECEIVER_EMAIL<your-value>
```

Ideally, you should set up the database env to be MySQL. PythonAnywhere Free tier
only allows mysql database connection. 


Make sure you have mysqlclient installed [Here](https://github.com/PyMySQL/mysqlclient) is a resource.


My `sqlclient` required the system to already have `mysql-client` installed and
available on the path, the same goes for pkg-config. Don't forget to refresh
or resouce the exported variables.


Alternately you can also run it using sqlite3 default configuation. For
development purposes. Check the Django Docs for more information. You're
pretty much just changeing DATABASES variable in Jba/settings.py to the
default.

Thereafter, you can run the project: 

``` bash
# For Dev 
# If it's the first time you're running 
python manage.py makemigrations
python manage.py migrate
# then run the dev server
python manage.py runserver
```



