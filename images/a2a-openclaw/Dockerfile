# ==============================================================================
# A2A + OpenClaw Container Image
# ==============================================================================
FROM node:24-bookworm-slim

ENV NODE_ENV=production \
    DEBIAN_FRONTEND=noninteractive

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    curl \
    git \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install OpenClaw globally
RUN npm install -g openclaw@latest

# Copy common entrypoint
COPY common/entrypoint.sh /usr/local/bin/a2a-entrypoint.sh
RUN chmod +x /usr/local/bin/a2a-entrypoint.sh

# Mount target for user runtime files and .env
VOLUME ["/workspace"]

EXPOSE 18789

ENTRYPOINT ["/usr/local/bin/a2a-entrypoint.sh"]
CMD ["openclaw", "gateway", "--bind", "0.0.0.0", "--port", "18789"]
