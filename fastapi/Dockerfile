FROM python:3.9

WORKDIR /app
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY app /app/app

#CMD ["uvicorn", "app.main:olympiapp", "--host", "0.0.0.0", "--port", "5000"]
CMD ["uvicorn", "app.main:olympiapp", "--host", "127.0.0.1", "--port", "8000"]