FROM python:3.8
LABEL maintainer="Wi-Feye"
LABEL version="1.0"

# setting the workdir
WORKDIR /app

# copying requirements
COPY ./requirements.txt /app

# installing all requirements
RUN ["pip3", "install", "-r", "requirements.txt"]

# creating the environment
COPY . /app

# exposing the port
EXPOSE 5000/tcp