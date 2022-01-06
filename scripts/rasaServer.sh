#!/usr/bin/env bash

DIR="$(pwd)"
if [[ "$VIRTUAL_ENV" != "" ]]
then
  rasa run --enable-api
else
  # set -e
  echo "Activate your the python environment using command \"source  "./env/bin/activate"\""
  # rasa run --enable-api
fi
