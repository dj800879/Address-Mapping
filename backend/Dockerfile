# Base image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy files
COPY ./app /app/app
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run FastAPI with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]