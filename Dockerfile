FROM alpine:latest
RUN apk add python3 py3-pip

COPY ./app/ ./app/
WORKDIR app/

RUN python3 -m pip install -r requirements.txt
CMD ["python3", "app.py"]