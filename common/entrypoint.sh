#!/usr/bin/env bash
# ==============================================================================
# A2A Common Container Entrypoint
# ==============================================================================
# Discovers and sources environment variables from mounted directories:
#   1. $ENV_FILE (if explicitly set)
#   2. /workspace/.env (standard mounted workspace directory)
#   3. /config/.env
# ==============================================================================

set -e

load_env() {
    local env_path="$1"
    if [ -f "$env_path" ]; then
        echo "[a2a-entrypoint] Loading environment variables from: $env_path"
        # Export all variables defined in the .env file
        set -a
        # shellcheck disable=SC1090
        . "$env_path"
        set +a
    fi
}

# 1. Custom ENV_FILE override
if [ -n "$ENV_FILE" ] && [ -f "$ENV_FILE" ]; then
    load_env "$ENV_FILE"
# 2. Mounted workspace .env (default convention)
elif [ -f "/workspace/.env" ]; then
    load_env "/workspace/.env"
# 3. Dedicated /config/.env mount
elif [ -f "/config/.env" ]; then
    load_env "/config/.env"
else
    echo "[a2a-entrypoint] No .env file found at /workspace/.env or /config/.env. Proceeding with existing environment."
fi

# Ensure workspace exists and change directory if present
if [ -d "/workspace" ]; then
    cd /workspace
fi

# Execute the container command or CMD
exec "$@"
