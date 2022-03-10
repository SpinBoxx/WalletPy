FROM python:3.8-slim
RUN pip install --upgrade pip==22.0.4
RUN pip -V
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r WalletPy/requirements.txt  --ignore-installed
COPY . /code/