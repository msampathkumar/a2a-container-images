# Standard: A2A container image

Single source of truth for what an image folder must contain. Checked by
`python3 scripts/validate_image.py` (stdlib; exit 0 = pass).

## 1. Folder and names

- One image per folder: `images/a2a-<runtime>/` (`<runtime>` = lowercase `a-z0-9-`).
- Required files: `images/a2a-<runtime>/Dockerfile`, `images/a2a-<runtime>/README.md`.
- Build context is the repo root: `docker build -f images/a2a-<runtime>/Dockerfile .`

## 2. Dockerfile rules (V = checked by the validator)

1. (V) `COPY common/entrypoint.sh /usr/local/bin/a2a-entrypoint.sh`.
2. (V) `ENTRYPOINT ["/usr/local/bin/a2a-entrypoint.sh"]`.
3. (V) `VOLUME ["/workspace"]`.
4. (V) Exactly one `EXPOSE <port>` line; that port is the image's **default port**.
5. (V) The `CMD` line contains the default port.
6. (V) No secret values: no `ENV`/`ARG` whose name contains `KEY`, `TOKEN`, `SECRET` or `PASSWORD` with a value.
7. (V) A comment header `# A2A + <Runtime> ...` on line 2.
8. Prefer pinned versions (`pkg==X.Y.Z`, `pkg@X.Y.Z`). Existing images use unpinned
   installs (`openclaw@latest`, unpinned pip packages); pinning is open work (ticket notes),
   not a validator failure yet.

## 3. README rules (all V)

1. First line `# A2A + <Runtime> ...`.
2. Headings `## Usage` and `## Environment Configuration`.
3. A `docker run` command with `-v <dir>:/workspace` and `-p <port>:<port>` using the default port.
4. A `dotenv` code block listing the variables; values are placeholders (`your_...`), never real keys.
5. If the `CMD` runs `main:app`, the README contains `main.py` (the user's app in `/workspace`).

## 4. Repo-level rules (all V)

1. Root `README.md` "Available Images" table has a row with `` `images/a2a-<runtime>/` `` and `` `<default port>` ``.
2. `docker-compose.example.yml` has a service whose `dockerfile:` is `images/a2a-<runtime>/Dockerfile`
   and whose `ports:` entry ends with `:<default port>` (host port may differ).

## 5. Verification levels

- **Static**: `validate_image.py` passes. Possible on any machine.
- **Built**: `docker build -f images/a2a-<runtime>/Dockerfile -t a2a-<runtime>:dev .` exits 0.
  Needs Docker. UNVERIFIED for all four images as of 2026-10-18 (no Docker on oss-vm).
- **Published**: the README's `ghcr.io/msampathkumar/a2a-<runtime>:latest` tag exists.
  UNVERIFIED as of 2026-10-18; no publish workflow exists in this repo.
