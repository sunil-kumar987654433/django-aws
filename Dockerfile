# ---------- Builder Stage ----------
FROM python:3.12.13-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --prefix=/install -r requirements.txt


# ---------- Final Stage ----------
FROM python:3.12.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Create non-root user
RUN adduser --disabled-password --no-create-home appuser

# Copy installed packages
COPY --from=builder /install /usr/local

# Copy project
COPY . .

# Change ownership
RUN chown -R appuser:appuser /app

# Copy entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Switch user
USER appuser

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]