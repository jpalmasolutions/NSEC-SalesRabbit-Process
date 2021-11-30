#!/bin/bash
export PYTHONPATH="${PYTHONPATH}:${PWD}"
pipenv run python-lambda-local \
-f lambda_handler \
-e local/local-environment-variables.json \
src/main/driver.py \
local/local-event.json