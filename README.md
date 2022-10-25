# Guil's Portfolio

## Build from ground up with no front-end templates

https://gfv.bio/

Contains:
- Material Design with Boostrap framework
- Jazzmin admin template
- Python decouple
- Heroku deployment setup

## Development setup

- requires python3

1. clone repository
2. create virtual environment with python3
3. activate venv
4. install dependencies
5. configure .env file with credentials
6. run makemigrations/migrate
7. create superuser
8. run tests


````console
git clone https://github.com/GuiFV/guilsportfolio guilsportfolio
cd guilsportfolio
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements-dev.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py test
````

## Heroku deploy

1. Create your app under Heroku (use heroku toolbelt)
2. Send configs to Heroku 
3. Define secure SECRET_KEY
4. Define DEBUG=False
5. Define ALLOWED_HOSTS=.herokuapp.com
6. Push code to Heroku

````console
heroku create your_app_name
heroku config:push
heroku config:set SECRET_KEY='secret_key_here'
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS='.herokuapp.com'
git push heroku master --force
````
