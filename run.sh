#!/bin/bash

#Set up environnement
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi
source .venv/bin/activate
sudo apt install postgresql
pip install -r requirements.txt

#Start db server
sudo systemctl start postgresql

#Set up db
sudo -u postgres psql --version
sudo -u postgres psql -c "CREATE USER $PG_USER WITH PASSWORD '$PG_PASSWORD';"
sudo -u postgres psql -c "ALTER USER $PG_USER WITH SUPERUSER;"
sudo -u postgres psql -c "CREATE DATABASE $DB OWNER $PG_USER;"

#Run process
python main.py

#Close db server and exit
sudo systemctl stop postgresql
deactivate