FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/proposal

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./