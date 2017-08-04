FROM alpine:3.6



ADD . /dbPedia

WORKDIR /dbPedia

RUN pip install --default-timeout=100 -r requirements.txt


CMD ["python", “dbPedia.py"]
