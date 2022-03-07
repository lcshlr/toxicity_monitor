# Toxicity monitor

Final project of Data Engineering course

Goal of this project is to build a web app with an api developped in Python with Flask and a simple js front-end to interact with api. Docker is used to build and run project.

## Team members : BERNARD Bastien - NORINDR Alexis - HILAIRE Lucas

## Task management :

Go to project tab on this repo or click on this [link](https://github.com/lcshlr/toxicity_monitor/projects/2)

## Prerequisites

- Docker and docker-compose installed

## Run project

Run the following command at root of the project :

```
docker-compose up
```

## Run tests

### Backend

After starting the API, run :

```
pip3 install -r api/tests/requirements.txt
pytest
```

### Frontend

After starting the API, run :

```
npx cypress run
```

### Dockerhub images

- Frontend : https://hub.docker.com/r/lcs95/toxicity_monitor_frontend
- Backend : https://hub.docker.com/r/alexisnorindrefrei/toxicity_monitor
