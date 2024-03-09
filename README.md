# Python FastAPI Mariadb Project

## Create MariaDB Database
- https://hub.docker.com/_/mariadb
- https://mariadb.com/resources/blog/using-sqlalchemy-with-mariadb-connector-python-part-1/
## Setup env files
```
sqlalchemy_database_url: mariadb+pymysql://username:password@127.0.0.1:3306/your database
```
To use env, use the credential inputs found in .env.sample. To use a .env file, create one, copy contents found in .env.sample and replace with qualified credentials.

## Start server
```
uvicorn src.main:app --reload
```

## testing
not implemented yet
