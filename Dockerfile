FROM alpine:3.6

RUN apt-get update && apt-get install -y \
    python-pip


ADD . /dbPedia

WORKDIR /dbPedia

RUN pip install --default-timeout=100 -r requirements.txt


CMD ["python", “dbPedia.py"]
