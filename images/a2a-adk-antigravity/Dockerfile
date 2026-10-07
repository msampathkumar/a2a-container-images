# ==============================================================================
# A2A + Google ADK + Antigravity Harness Model
# ==============================================================================
FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    curl \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install A2A SDK and Google ADK
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir \
    google-adk \
    a2a-sdk \
    fastapi \
    uvicorn \
    pydantic \
    python-dotenv

# Copy common entrypoint
COPY common/entrypoint.sh /usr/local/bin/a2a-entrypoint.sh
RUN chmod +x /usr/local/bin/a2a-entrypoint.sh

# Mount target for user runtime files and .env
VOLUME ["/workspace"]

EXPOSE 8000

ENTRYPOINT ["/usr/local/bin/a2a-entrypoint.sh"]
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
