# A2A + Nous Hermes Agent Container

This container image packages Nous Hermes Agent with A2A protocol integration.

## Usage

Mount your working directory containing `.env` to `/workspace`:

```bash
docker run -d \
  --name a2a-hermes \
  -v $(pwd):/workspace \
  -p 8000:8000 \
  ghcr.io/msampathkumar/a2a-hermes:latest
```

## Environment Configuration

Create a `.env` in your mounted folder:

```dotenv
OPENAI_API_KEY=your_key
HERMES_MODEL=nousresearch/hermes-3-llama-3.1-8b
A2A_PORT=8000
```
