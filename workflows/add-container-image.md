# Workflow: add or repair one container image

**Produces:** `images/a2a-<runtime>/Dockerfile` + `images/a2a-<runtime>/README.md` + one root README row + one compose service   **Runs per invocation:** 1 image
**Skill(s):** none   **Standards:** standards/image-standard.md

## Preconditions
- [ ] `git status --porcelain` prints nothing; `git pull --rebase` exits 0.
- [ ] `python3 scripts/validate_image.py` exits 0 on the current tree (else fix that first in its own ticket).

## Inputs
| Input | Path / Command |
|-------|----------------|
| Next unit | `tk ready` → first line whose title starts `Build A2A +` (open child of epic `aci-vwlr`) |
| Rules | `standards/image-standard.md` |
| Templates | `templates/image/Dockerfile`, `templates/image/README.md` |
| Golden example | `images/a2a-adk-antigravity/` |
| Entrypoint (do not change in this workflow) | `common/entrypoint.sh` |

## Steps
1. **Select unit.** `tk ready | grep 'Build A2A +' | head -1`. No line → milestone reached, STOP. Else `tk start <id>`. `<runtime>` = the lowercase runtime name in the title, spaces → `-` (existing folder wins if one matches).
2. **Read context.** `standards/image-standard.md`, the golden example, the existing `images/a2a-<runtime>/` if present, `tk show <id>`.
3. **Draft.** If the folder does not exist, copy both templates into it. Fill every `{{slot}}`; `grep -n '{{' images/a2a-<runtime>/*` prints nothing. Install commands must come from the runtime's official docs; write the doc URL as a comment above the `RUN` line. No URL found → write `# UNVERIFIED install command` and say so in the ticket.
4. **Register.** Add/update the root `README.md` "Available Images" row and the `docker-compose.example.yml` service (container port = `EXPOSE` port; pick an unused host port).
5. **Validate (Layer A).** `python3 scripts/validate_image.py images/a2a-<runtime>` → exit 0 (max 2 fix loops).
6. **Build (if Docker exists).** `command -v docker && docker build -f images/a2a-<runtime>/Dockerfile -t a2a-<runtime>:dev .`. No Docker → record `BUILD: UNVERIFIED (no docker)`; do not close the ticket.
7. **Rubric (Layer B).** Answer in `tk add-note <id>`.
8. **Record.** `tk add-note <id> "validate_image PASS; build <PASS|UNVERIFIED>; rubric 5/5"`. Close (`tk close <id>`) only if build PASS.
9. **Commit.** `git add images/a2a-<runtime> README.md docker-compose.example.yml .tickets/ && git commit -m "feat(images): <add|fix> a2a-<runtime> (<id>)" && git push`.

## Rubric (all must be YES)
1. Does the `RUN` install the runtime named in the title (not only `a2a-sdk`)? (quote the line)
2. Is every install command backed by a doc URL comment or marked UNVERIFIED?
3. Are all `.env` values placeholders (`your_...`)? (quote the dotenv block)
4. Does the `CMD` listen on `0.0.0.0` and the `EXPOSE` port? (quote)
5. Is the README `docker run` image name one you can build locally, or a ghcr tag that is marked UNVERIFIED in standard §5?

## Failure handling
- Validator fails after 2 loops → `tk add-note <id> "BLOCKED: <line>"`, do not commit, STOP.
- `docker build` fails → note the failing step in the ticket, commit only if the static gate passes and the README says nothing is published, leave the ticket open.
- Runtime has no documented container install → BLOCKED with the reason.

## Definition of Done
- `validate_image.py` exit 0, rubric 5/5, commit pushed; ticket closed only after a successful `docker build`.
