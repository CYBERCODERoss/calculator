FROM python:3
FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y \
    sudo \
    python3-tk

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]
