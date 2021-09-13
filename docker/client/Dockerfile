FROM python:3.8.12-alpine
RUN apk update 
RUN mkdir /usr/src/client
WORKDIR /usr/src/client
COPY ./requirements.txt .
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED 1
COPY . .