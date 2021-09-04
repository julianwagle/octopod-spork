#!/bin/bash
cd ../
docker-compose -f local.yml down
docker system prune -af
docker volume prune -f
docker container ls
docker image ls
docker volume ls
