FROM python:3.11-slim

WORKDIR /api-migrations

# Install system dependencies
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    gettext-base \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and migration files
COPY requirements.txt .
COPY migrations ./migrations/
COPY alembic.ini.template .
COPY start.sh .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make entrypoint script executable
RUN chmod +x start.sh

# Run migrations
ENTRYPOINT ["./start.sh"]