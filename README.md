MOTD-API

```BASH
docker build -t flask .
docker run --rm -it -p 5555:5555 --name flask-app -e APP_MESSAGE="Hello World!" -e APP_PORT=5555 flask
```