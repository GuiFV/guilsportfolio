# Guil's Portfolio

## Build from ground up with no front-end templates

https://gfv.bio/

Contains:
- Material Design with Boostrap framework
- Jazzmin admin template
- Python decouple
- Docker-compose deployment

## Development setup

- requires python >=3.9

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

