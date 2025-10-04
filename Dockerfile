FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY pyproject.toml .
RUN pip install --no-cache-dir .

# Download assets
COPY download.sh .
RUN chmod +x download.sh && ./download.sh

# Copy application code
COPY src ./src

# Set the entry point
ENTRYPOINT [ "python", "/app/src/main.py" ]