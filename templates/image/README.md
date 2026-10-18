# A2A + {{Runtime}} Container

This container image packages {{Runtime}} with Agent2Agent (A2A) protocol integration.

## Usage

Mount your working directory containing `.env` to `/workspace`:
{{If CMD runs `uvicorn main:app`, add: The default `CMD` runs `uvicorn main:app`, so the folder needs a `main.py` that defines `app`.}}

```bash
docker run -d \
  --name a2a-{{runtime}} \
  -v $(pwd):/workspace \
  -p {{port}}:{{port}} \
  a2a-{{runtime}}:dev
```

Build it first from the repo root: `docker build -t a2a-{{runtime}}:dev -f images/a2a-{{runtime}}/Dockerfile .`

## Environment Configuration

Create a `.env` in your mounted folder:

```dotenv
{{VAR_NAME}}=your_{{value}}
A2A_PORT={{port}}
```
