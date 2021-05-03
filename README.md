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

Enter the pipenv shell and run pipenv intall to install dependencies from Pipfile.lock
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
python manage.py runserver
```