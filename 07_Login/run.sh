#!/usr/bin/env bash
# starts up flask app

export APP_SECRET=`openssl rand -base64 32`

export FLASK_APP=login.py
flask run
