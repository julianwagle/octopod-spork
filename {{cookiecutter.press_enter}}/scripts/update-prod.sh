#!/bin/bash
cd ../
cd ../
rsync -avz --exclude-from=backend/exclude.txt backend/ root@{{cookiecutter.server_ip}}:/root/backend/
sshpass -p "<SERVER PASSWORD HERE>" ssh -o StrictHostKeyChecking=no root@{{cookiecutter.server_ip}} "cd backend; docker-compose -f production.yml down; docker-compose -f production.yml up --build"
