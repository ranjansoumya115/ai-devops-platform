FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install pandas fastapi uvicorn

CMD ["python3", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
