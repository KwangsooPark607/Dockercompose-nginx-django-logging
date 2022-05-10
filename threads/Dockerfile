FROM python:3.9.12-slim

WORKDIR /app 

COPY ./threads/requirements.txt ./ 

#COPY requirements.txt ./ 

RUN pip install -r requirements.txt

RUN apt-get update

COPY . .

EXPOSE 8080