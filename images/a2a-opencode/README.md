# A2A + OpenCode Container

This container image packages OpenCode with A2A protocol integration for agentic code generation and execution.

## Usage

Mount your working directory containing `.env` to `/workspace`:

```bash
docker run -d \
  --name a2a-opencode \
  -v $(pwd):/workspace \
  -p 8080:8080 \
  ghcr.io/msampathkumar/a2a-opencode:latest
```

## Environment Configuration

Create a `.env` in your mounted folder:

```dotenv
LLM_API_KEY=your_key
A2A_PORT=8080
```
