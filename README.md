# yt-video-fetcher
A Git repository that fetches latest video based on keyword `technology` and store it locally in postgres database.

## Running Locally 🖥️

The `compose.yaml` file includes all the components (database, backend, message queue, and worker) required for this microservice.

The `.env.sample` file contains sample env variable that need to be added in `.env` file.

### Create and start containers

To build and start the containers, run:

```
$ docker compose up --build
```

To run the containers in the background, use:

```
$ docker compose up --build -d
```

To apply migrations:

```
$ docker exec -it backend /bin/sh

$ ./manage.py migrate
```

### Stop and remove containers

To stop and remove the containers, run:

```
$ docker compose down
```

### To test APIs locally

Start containers and hit following apis:

#### Listing api

```
GET http://localhost:8000/videos/
```

#### Search api

```
GET http://localhost:8000/videos/search/?query=tech
```
