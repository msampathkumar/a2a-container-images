# a2a-container-images

Container images for [Agent2Agent (A2A)](https://github.com/msampathkumar/A2A) protocol runtimes, harnesses, and agent frameworks.

## Architecture & Mounting Pattern

All containers in this repository adhere to a standardized runtime pattern:

- **Isolated State & Configuration**: Instead of baking secrets or environment variables into images, you pass environment variables by mounting a local working directory containing a `.env` file to `/workspace`:
  ```bash
  -v /path/to/my-agent-folder:/workspace
  ```
- **Automatic Discovery**: An entrypoint script (`common/entrypoint.sh`) discovers `/workspace/.env` (or `/config/.env` or `$ENV_FILE`), loads and exports variables, changes the working directory to `/workspace`, and launches the agent runtime.

---

## Available Images

| Directory | Image Description | Default Port |
| :--- | :--- | :--- |
| `images/a2a-adk-antigravity/` | A2A + Google ADK + Antigravity Harness Model | `8000` |
| `images/a2a-openclaw/` | A2A + OpenClaw Gateway runtime | `18789` |
| `images/a2a-opencode/` | A2A + OpenCode development agent | `8080` |
| `images/a2a-hermes/` | A2A + Nous Hermes Agent runtime | `8000` |

---

## Quickstart

### 1. Run a container with mounted workspace
```bash
# Prepare your local agent workspace
mkdir -p ./my-agent-workspace
cat <<EOF > ./my-agent-workspace/.env
GOOGLE_API_KEY=your_gemini_api_key
A2A_AGENT_NAME=AntigravityHarnessAgent
EOF

# Build & Run
docker build -t a2a-adk-antigravity -f images/a2a-adk-antigravity/Dockerfile .
docker run -d \
  --name a2a-agent \
  -v $(pwd)/my-agent-workspace:/workspace \
  -p 8000:8000 \
  a2a-adk-antigravity
```

### 2. Multi-Agent Compose
See [`docker-compose.example.yml`](docker-compose.example.yml) for orchestrating multiple A2A agents together on a shared network.

---

## Task & Milestone Tracking

All task tracking, features, and dependencies for this repository are managed using [`tk`](https://github.com/msampathkumar/ticket).
Run `tk ready` inside the repository to see available work items.
