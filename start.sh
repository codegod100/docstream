#!/bin/bash
poetry install
FLASK_DEBUG=1 poetry run flask run --host 0.0.0.0