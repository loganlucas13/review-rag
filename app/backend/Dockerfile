# slim for quicker setup
FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# setup python libraries
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 4196

CMD ["python", "main.py"]