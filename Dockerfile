FROM tiangolo/uvicorn-gunicorn:python3.10

LABEL maintainer="Angel A. Garcia Gonzalez <angelgarcia@idom.com>"

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH $PWD

RUN apt-get update && apt-get install -y python3-psycopg2

WORKDIR /api

COPY requirements.txt /tmp/requirements.txt

# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# COPY . .
COPY . /api

# RUN ./install.sh

# gunicorn
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
# CMD ["./start.sh"]