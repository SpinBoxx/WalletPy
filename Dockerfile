FROM python:3.8-slim
RUN pip install --upgrade pip==22.0.4
RUN pip -V
RUN apt-get update
RUN  apt-get install -y gcc
RUN apt-get install -y default-libmysqlclient-dev
RUN apt-get install -y python3-dev
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt  --ignore-installed
COPY . /code/