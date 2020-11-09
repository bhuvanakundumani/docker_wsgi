FROM python:3.7-slim

WORKDIR /app/

ADD requirements.txt /
RUN pip install -r /requirements.txt 
ADD . /app

EXPOSE 8888

COPY nginx.conf /app/nginx.conf

WORKDIR /app

CMD exec gunicorn --bind :8888 --workers 1 --threads 8 flask_test:app

