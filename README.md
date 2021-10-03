# MusicReleases
SaaS to help indie record labels to promote their releases and facilitate trades

### Installation

First install Postgres to your system and run it 

Create ```.env``` file and copy paste there content from ```.env.example```. Change username,
password and dbname for DATABASE_URl to ones you use for the local Postgres instance.
```bash
SECRET_KEY=secret
DEBUG_MODE=True
DATABASE_URL=postgres://username:password@localhost:5432/dbname
```

Install project dependencies via pipenv:
```bash
pipenv install
```
If you run into ```ERROR: Couldn't install package: psycopg2``` error, export the following variables
```bash
export LDFLAGS="-L/usr/local/opt/openssl/lib"
export CPPFLAGS="-I/usr/local/opt/openssl/include"
```

After that, activate your pipenv environment, migrate the database and run the server:
```bash
pipenv shell
./manage.py migrate
./manage.py runserver
```

Optionally, you can fill up a database with a dummy user and few releases via:
```bash
./manage.py seed_db
```

### Tests

To run test suite:
```bash
./manage.py test
```

To check test coverage run:
```bash
coverage run manage.py test
coverage report
```

### Docker

To run the app in the docker environment, run
```bash
docker compose up
```
and it will be available under `http:/localhost:8888`. To stop all containers and remove artifacts:
```bash
docker compose down --remove-orphans
```

To run test suite:
```bash
docker compose run app test
```
