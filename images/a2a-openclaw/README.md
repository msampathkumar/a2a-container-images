# A2A + OpenClaw Container

This container image packages the OpenClaw agent platform with A2A protocol interoperability.

## Usage

Mount your working directory containing `.env` to `/workspace`:

```bash
docker run -d \
  --name a2a-openclaw \
  -v $(pwd):/workspace \
  -p 18789:18789 \
  ghcr.io/msampathkumar/a2a-openclaw:latest
```

## Environment Configuration

Create a `.env` in your mounted folder:

```dotenv
OPENCLAW_GATEWAY_TOKEN=your_secure_token
ANTHROPIC_API_KEY=your_key
OPENAI_API_KEY=your_key
```
