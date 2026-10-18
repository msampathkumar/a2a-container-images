# A2A + ADK + Antigravity Harness Model Container

This container image packages the Agent2Agent (A2A) protocol interface with Google Agent Development Kit (ADK) and Antigravity harness capabilities.

## Usage

Mount your working directory containing `.env` and your A2A app to `/workspace`.
The default `CMD` runs `uvicorn main:app`, so the folder needs a `main.py` that defines `app`:

```bash
docker run -d \
  --name a2a-adk-antigravity \
  -v $(pwd):/workspace \
  -p 8000:8000 \
  ghcr.io/msampathkumar/a2a-adk-antigravity:latest
```

## Environment Configuration

Create a `.env` in your mounted folder:

```dotenv
GOOGLE_API_KEY=your_gemini_api_key
A2A_AGENT_NAME=AntigravityHarnessAgent
A2A_PORT=8000
```
