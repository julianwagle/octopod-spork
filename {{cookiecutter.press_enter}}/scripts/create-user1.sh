#!/bin/bash
NAME=$(openssl rand -hex 16)
PASS=$(openssl rand -hex 16)

USER='{"email": "'$NAME'@example.com", "username": "'$NAME'", "password": "'$PASS'"}'

echo "Username:" $NAME
echo "Email:" $NAME"@example.com"
echo "Password:" $PASS

curl -H "Content-type: application/json" -X POST -d "$USER" http://localhost:8000/api/users/

filename='users.txt'

echo ''$USER'' >> $filename
