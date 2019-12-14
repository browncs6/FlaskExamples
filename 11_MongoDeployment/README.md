# Flask + MongoDB example

This here is a simple example on how to deploy flask + mongoDB in two separate containers
and start it via docker-composer.

All commands assume you are in the `11_MongoDeployment` dir.

### Step 1:
You need to create the image for your flask app. Here, the image is called `login`.
To create it, run

```
docker build -t login:latest .
```

You also need to pull the `mongo` docker image, i.e.

```
docker pull mongo
```

### Step 2:
We want to persist data via a volume. To do so, run `mkdir db-data` or change the `DBURI` environment variable in the `docker-compose.yml` file.

### Step 3:
To run everything, use `docker-compose up`. Adding the option `-d` sends it to the background.


### More notes:
This is a basic example. For a more advanced setup, please read https://www.digitalocean.com/community/tutorials/how-to-set-up-flask-with-mongodb-and-docker
