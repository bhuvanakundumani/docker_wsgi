
## Command  
```
gunicorn --bind :8888 --workers 1 --threads 8 flask_test:app
```



## API Request format

```python
curl -i -H "Content-Type: application/json" \
      -X POST -d '{"text":"Hi Everyone!!! "}' http://0.0.0.0:8888/hi
```


```python
curl -i -H "Content-Type: application/json" \
      http://0.0.0.0:8888/test
```

``` python
curl -i -H "Content-Type: application/json"  -X \
    POST -d '{"text":"Welcome TO my app "}' http://0.0.0.0:8888/hello

```




```
docker build -t dockertest/flaskapp .
docker images -a
REPOSITORY            TAG                 IMAGE ID            CREATED             SIZE
dockertest/flaskapp   latest              7b47f1d981c8        11 seconds ago      143MB
docker run -p 0.0.0.0:8888:8888 dockertest/flaskapp
```