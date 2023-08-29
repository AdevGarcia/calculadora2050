#! /usr/bin/env bash
set -e

export PYTHONPATH=$PWD
./install.sh

cd ./app/src/ 
python initial_data.py

uvicorn main:app --host 0.0.0.0 --port 8000 --proxy-headers
