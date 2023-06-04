# Initial Project Setup
### Creating Virtualenv
```sudo pip3 install virtualenv
mkdir ~/loop
cd ~/loop
python3 -m virtualenv loop
source myprojectenv/bin/activate
```
### Installing Dependencies:
```commandline
pip install -r /path/to/requirements.txt
```
### Installing Postgres:
[Postgres installation link.](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-20-04)
```
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql.service
sudo systemctl status postgresql.service
```
### Creating Postgres User:
[Setting postgres with Django.](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-20-04)
```
sudo apt update
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib
sudo -u postgres psql
CREATE DATABASE loop;
CREATE USER loopuser WITH PASSWORD 'password';
ALTER ROLE loopuser SET client_encoding TO 'utf8';
ALTER ROLE loopuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE loopuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE loop TO loopuser;
\q
```
### Creating DjangoAdmin User:
```
Go to project folder, then run:-
python manage.py createsuperuser
```
### Running Migrations:
```commandline
Go to project folder, then run:-
python manage.py makemigrations
python manage.py migrate
```
### Running Server:
```
python manage.py runserver
```