FROM python:3.11
WORKDIR /app/results
COPY requirements.txt /app/results/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/results
EXPOSE 5030
CMD ["gunicorn", "app:app", "--host", "0.0.0.0", "--port", "5030"]
