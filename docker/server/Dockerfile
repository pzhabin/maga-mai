FROM python:3.8.12-alpine
RUN apk update 
RUN mkdir /usr/src/server
WORKDIR /usr/src/server
COPY ./requirements.txt .
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED 1
COPY . .
EXPOSE 6666/tcp