FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY dog_api/ ./dog_api/

ENV PYTHONUNBUFFERED 1

CMD ["sh", "-c", "python dog_api/manage.py migrate && python dog_api/manage.py runserver 0.0.0.0:8000"]