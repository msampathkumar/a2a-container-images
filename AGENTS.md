# AGENTS.md

## Mission

Container images that run Agent2Agent (A2A) runtimes, harnesses and agent
frameworks with one convention: secrets and config come from a mounted
`/workspace/.env`, loaded by `common/entrypoint.sh`. Owner: Sampath (msampathkumar).

## Milestone and Definition of Done

Milestone: tk epic `aci-vwlr` (A2A Container Images Suite). Done when all are true:
1. `python3 scripts/validate_image.py` exits 0 for all images in `images/`.
2. Each image's `docker build -f images/<image>/Dockerfile .` exits 0, recorded in its ticket
   (status today: UNVERIFIED for all 4; no Docker on oss-vm).
3. Each image installs the runtime named in its title (today a2a-hermes and a2a-opencode
   install only `a2a-sdk`/FastAPI; see ticket notes).
4. `tk ready | grep 'Build A2A +'` prints nothing (all image tickets closed).

## Workflow index

| Trigger | Workflow file |
|---------|---------------|
| Add a new image, or repair an existing one | `workflows/add-container-image.md` |
| Any edit under `images/`, `README.md`, `docker-compose.example.yml` | run `python3 scripts/validate_image.py` before commit |

Standards: `standards/image-standard.md` (single source of truth for image rules).

## Automation boundary

No automation targets this repo. If one is added it may run only
`workflows/add-container-image.md`, 1 image per run, and stops when step 1 finds no ticket.

## Red lines (testable)

- Never commit when `python3 scripts/validate_image.py` exits non-zero.
- Never put a real key, token or password in a Dockerfile, README or compose file
  (validator rule §2.6; review `git diff --cached`).
- Never commit `.env` files (`.gitignore` covers them; check `git status`).
- Never push images to a registry or claim a `ghcr.io` tag exists without proof (standard §5).
- Never change `common/entrypoint.sh` behaviour without updating standard §2 and every image README.
- Always `git add` explicit paths plus `.tickets/`; never `git add .`/`-A`; never force-push.
- Every work unit has a tk ticket: `tk create` → `tk start` → `tk add-note` → `tk close`.
- Max 2 fix loops per gate, then `tk add-note <id> "BLOCKED: <reason>"` and stop.
