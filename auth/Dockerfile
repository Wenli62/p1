FROM python:3.11
WORKDIR /app/auth
COPY requirements.txt /app/auth/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/auth
EXPOSE 5000
CMD ["gunicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]