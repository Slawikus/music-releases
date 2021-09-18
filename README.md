# MusicReleases
SaaS to help indie record labels to promote their releases and facilitate trades

## Installation

First install Postgres to your system and run it 

Create ```.env``` file and copy paste there content from ```.env.example```. Change username, password and dbname for DATABASE_URl to ones you use for the local Postgres instance.
```sh
SECRET_KEY=secret
DEBUG_MODE=True
DATABASE_URL=postgres://username:password@localhost:5432/dbname
```

Enter the pipenv shell and install dependencies:
```sh
pipenv install
```
If you run into ```ERROR: Couldn't install package: psycopg2``` error, export the following variables
```sh
export LDFLAGS="-L/usr/local/opt/openssl/lib"
export CPPFLAGS="-I/usr/local/opt/openssl/include"
```

After that, exit your pipenv with ```exit ``` command enter it again and run the server
```sh
exit
pipenv shell
./manage.py migrate
./manage.py runserver
```

### Docker

To run the app in the docker environment, run
```
docker compose up
```
and it will be available under `http:/localhost:8888`. To stop all containers and remove artifacts:
```
docker compose down --remove-orphans
```

To run tests suite:
```
docker compose run app test
```
### Test coverage
to check test coverage run:
```
coverage run manage.py test
coverage report
```