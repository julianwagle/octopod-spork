#!/bin/bash

lines=$(cat users.txt | wc -l)
user=$((1 + $RANDOM % $lines))
x=0
cat 'users.txt' | while read l; do
  x=$(( x+1 ))
  if [ $x -eq "$user" ]; then
    key="email"
    re="\"($key)\": \"([^\"]*)\""
    if [[ $l =~ $re ]]; then
      email="${BASH_REMATCH[2]}"
    fi
    key="password1"
    re="\"($key)\": \"([^\"]*)\""
    if [[ $l =~ $re ]]; then
      password1="${BASH_REMATCH[2]}"
    fi
  fi
  echo "$email"
  echo "$password1"
  USER='{"email": "'$email'", "password": "'$password1'"}'
  curl -H "Content-type: application/json" -X POST -d "$USER" http://localhost:8000/api/users/login/
done
