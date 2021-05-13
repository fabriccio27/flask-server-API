# restAPI using python micro-framework Flask

## Quickstart
Extract zip file cd, into it and run
```
docker build -t myproj:latest .
docker-compose -f docker.compose.yml up
```
`flask-app` and `rq-worker` are located at `./src`
## Docker containers

This applications uses a pulled MongoDb image, a pulled Redis image (meant to work as a message broker) and one reused image to spin up the flask-server and an rq worker (connects to Redis image and takes care of the background tasks), accounting to 4 containers. The built image from comes from `./Dockerfile,` which install a lightweight version of python and the requirements both to the flask-app and the rq worker (PyMongo, rq, Redis, etc).

The whole applications is orchestrated via `./docker-compose.yml`, setting the ports and links needed.

## Testing

The server was tested using Postman, sending both GET and POST request successfully to indicated endpoints. Output is generated using `os`.