# ==============================================================================
# A2A + {{Runtime}} Container Image
# ==============================================================================
# Golden example: images/a2a-adk-antigravity/Dockerfile. Rules: standards/image-standard.md §2.
FROM {{base image, e.g. python:3.11-slim}}

ENV PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install the runtime ({{pin versions: pkg==X.Y.Z}})
RUN {{install command}}

# Copy common entrypoint
COPY common/entrypoint.sh /usr/local/bin/a2a-entrypoint.sh
RUN chmod +x /usr/local/bin/a2a-entrypoint.sh

# Mount target for user runtime files and .env
VOLUME ["/workspace"]

EXPOSE {{port}}

ENTRYPOINT ["/usr/local/bin/a2a-entrypoint.sh"]
CMD [{{command that listens on 0.0.0.0:{{port}}}}]
