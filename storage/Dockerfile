FROM python:3.11
WORKDIR /app/storage
COPY requirements.txt /app/storage/requirements.txt

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get install -y \
    python3-dev \
    python3-pip \
    default-libmysqlclient-dev \
    build-essential && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/storage
EXPOSE 5020
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5020", "--log-file", "-", "--access-logfile", "-", "--workers", "4", "--keep-alive", "0"]
