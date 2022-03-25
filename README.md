# AutoZone - Azorian

This is a software program that tracks the Authority to Operate (ATO) for New stores and Mergers IT equipment. 

## A list of technologies used within the project:
***
* [Python](https://www.python.org/downloads/): Version 3.9+
* [PostgreSQL](https://www.postgresql.org/download/): Version 14.2
    * *For demonstration purposes, we used SQLite*
* [Flask](https://pypi.org/project/Flask/): Version 2.0.3
* [psycopg2](https://pypi.org/project/psycopg2/): Version 2.9.3
* [SQLAlchemy](https://pypi.org/project/SQLAlchemy/): Version 1.4.32
* [alembic](https://pypi.org/project/alembic/): Version 1.7.7
* *MORE TO COME*

## Setup & Installation

Make sure that you have the latest PostgreSQL installed
Make sure that you have the latest Python installed

### Grab the repo

```bash
git clone <repo-url>
```

Create a virtual environment

### Linux

```bash
sudo apt-get install python3-venv    # If needed
python3 -m venv .venv
source .venv/bin/activate
```

### macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```bash
py -3 -m venv .venv
.venv\scripts\activate
```

## Install all of the requirements

```bash
pip install -r requirements.txt
```

## Run the App

```bash
python main.py
```
