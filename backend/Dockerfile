# backend/Dockerfile
FROM python:3.8

WORKDIR /app

# Copy only the requirements file, to cache the pip install step
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy the rest of the application
COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
