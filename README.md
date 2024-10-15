# django app
## front-end side
go to repo => https://github.com/mohammadx0098/React-front-end
## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/mohammadx0098/Django-backend.git
$ cd Django-backend
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv .venv
$ source .venv/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.
