FROM python:3.11

# Set working directory
WORKDIR /app/storage

# Copy requirements and install dependencies
COPY requirements.txt /app/storage/requirements.txt

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get install -y \
    python3-dev \
    python3-pip \
    default-libmysqlclient-dev \
    build-essential && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY . /app/storage

# Expose port
EXPOSE 5010

# Command to run the app
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5010", "--log-file", "-", "--access-logfile", "-", "--workers", "4", "--keep-alive", "0"]
