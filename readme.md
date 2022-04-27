# War Game

## Requirements

The latest versions of docker and docker-compose are required for this build.

## Clone the repository

```
git clone https://github.com/crprado/sre.wargame.git
```

## Pull the docker images


```
docker pull maomoa/wargamehistoryapi
docker pull maomoa/wargameweb
docker pull maomoa/wargameapi
```
## Run the containers


```
docker-compose up -d
```
## Open the application

```
http://localhost:5000/simulate
```
