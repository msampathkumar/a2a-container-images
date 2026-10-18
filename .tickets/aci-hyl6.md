---
id: aci-hyl6
status: open
deps: [aci-w7yo]
links: []
created: 2026-10-07T00:07:40Z
type: feature
priority: 2
assignee: Sampath Kumar
parent: aci-vwlr
---
# Build A2A + OpenCode container image

Docker image packaging A2A with OpenCode


## Notes

**2026-10-18T00:17:17Z**

2026-10-18 review: passes static validator, but the Dockerfile installs only a2a-sdk/fastapi/uvicorn, not the runtime named in the title. Needs official install command + docker build (workflows/add-container-image.md). Left open.
