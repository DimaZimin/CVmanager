# pull official base image
FROM python:3.8


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT=8000

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app/

COPY . /app/

# install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        tzdata \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        git \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

RUN pip install -r requirements.txt
EXPOSE 8000
CMD gunicorn CVmanager.wsgi:application --bind 0.0.0.0:$PORT
