FROM python:3.9-slim-buster

EXPOSE 5000

WORKDIR /app

RUN apt-get update && apt-get -y install gcc python-dev && apt-get clean

COPY app ./

RUN pip install -r requirements.txt

#CMD ["python3", "app.py"]