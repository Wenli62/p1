FROM python:3.11
WORKDIR /app/grade
COPY requirements.txt /app/grade/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/grade
EXPOSE 5000 
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000", "--log-file", "-", "--access-logfile", "-", "--workers", "4", "--keep-alive", "0"] 