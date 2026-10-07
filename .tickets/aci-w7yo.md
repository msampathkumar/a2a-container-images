---
id: aci-w7yo
status: closed
deps: []
links: []
created: 2026-10-07T00:07:40Z
type: task
priority: 1
assignee: Sampath Kumar
parent: aci-vwlr
---
# Define common entrypoint & volume mount convention for .env and workspace

Standardize container entrypoint script that automatically sources .env from a mounted directory and sets up workspace


## Notes

**2026-10-07T00:08:10Z**

Implemented standard entrypoint script supporting mounted volume /workspace/.env, /config/.env, or custom ENV_FILE
