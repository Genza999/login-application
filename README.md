# login-application
This is a login application that demonstrates how to structure the login and logout structure into a web application using python and flask modules to perform various functions.

### Real Live Demo

[Login Application Demo](https://login-application.herokuapp.com/)

### Dependencies, Packages and extensions used

* [Python](https://www.python.org) - 3.3
* [Flask](http://flask.pocoo.org/)

#### Authentication specific packages

* [Flask-Login](https://github.com/maxcountryman/flask-login) - Management of user sessions for logged-in users
* [Werkzeug](http://werkzeug.pocoo.org/) - Password hashing and verification
* [itsdangerous](https://pythonhosted.org/itsdangerous/) - Cryptographically secure token generation and verification

#### General purpose extensions used

* [Flask-Mail](https://github.com/mattupstate/flask-mail) - Sending of authentication-related emails
* [Flask- Bootstrap](https://github.com/mbr/flask-bootstrap) - HTML templates
* [Flask-WTF](https://flask-wtf.readthedocs.io/) - Web forms

### Use the command below to build a perfect replica of the virtual environment by downloading all the dependencies used:

```
pip install -r requirements.txt
```

### create a migration repository with the init subcommand:

```
python manage.py db init
```

### create an automatic migration script

```
python manage.py db migrate -m "initial migration"
```

### Once a migration script has been reviewed and accepted, it can be applied to the database using the db upgrade command:

```
python manage.py db upgrade
```

### After run the following command to start the web application

```
python manage.py runserver
```


### Login page

![Login Image](https://raw.githubusercontent.com/Genza999/login-application/master/img/login.PNG "Login")

### Register page

![Register Image](https://raw.githubusercontent.com/Genza999/login-application/master/img/register.PNG "Register")


### Example of verification email sent after user has registered

![Verification email image](https://raw.githubusercontent.com/Genza999/login-application/master/img/email_verification.PNG "Verification")


### After verification, user is authenticated and logged In.

![Logged In Image](https://raw.githubusercontent.com/Genza999/login-application/master/img/loggedIn.PNG "Logged In")

### Reference

Flask Web Development by Miguel Grinberg



