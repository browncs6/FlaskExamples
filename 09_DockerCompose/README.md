# Dockerizing a Flask application

In this example we use the postgres image from dockerhub and package our flask app in a container too.

Start postgres via

```
mkdir db-data

docker run --name postgres -e POSTGRES_PASSWORD=docker \
                  --rm -p 5432:5432 -v db-data:/var/lib/postgresql/data postgres
```


Start then flask app via

```
docker run --name login -p 8000:5000 --link postgres:dbserver -e DBURI='postgresql://postgres:docker@dbserver/postgres' -e APP_SECRET='test' --rm login:latest
```

Make sure to add users etc. via flask shell e.g.
