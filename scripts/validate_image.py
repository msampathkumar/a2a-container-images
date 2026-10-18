#!/usr/bin/env python3
"""Static gate for container image folders (standards/image-standard.md).

Usage:
  python3 scripts/validate_image.py                       # every images/a2a-* folder
  python3 scripts/validate_image.py images/a2a-hermes     # one folder

Prints '<image>: <rule>: <detail>' per violation. Exit 0 = pass, 1 = violations. Stdlib only.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME_RE = re.compile(r"^a2a-[a-z0-9]+(?:-[a-z0-9]+)*$")
SECRET_RE = re.compile(r"^\s*(ENV|ARG)\s+\S*(KEY|TOKEN|SECRET|PASSWORD)\S*\s*=\s*\S+", re.I | re.M)


def check(img: Path) -> list[str]:
    n = img.name
    errs: list[str] = []
    if not NAME_RE.match(n):
        errs.append(f"{n}: naming: folder must be a2a-<lowercase-runtime>")
    df, rd = img / "Dockerfile", img / "README.md"
    for f in (df, rd):
        if not f.is_file():
            errs.append(f"{n}: files: missing {f.name}")
    if errs:
        return errs
    d = df.read_text()
    r = rd.read_text()

    # Dockerfile (standard §2)
    if "COPY common/entrypoint.sh /usr/local/bin/a2a-entrypoint.sh" not in d:
        errs.append(f"{n}: dockerfile: missing 'COPY common/entrypoint.sh /usr/local/bin/a2a-entrypoint.sh'")
    if 'ENTRYPOINT ["/usr/local/bin/a2a-entrypoint.sh"]' not in d:
        errs.append(f"{n}: dockerfile: missing ENTRYPOINT [\"/usr/local/bin/a2a-entrypoint.sh\"]")
    if 'VOLUME ["/workspace"]' not in d:
        errs.append(f"{n}: dockerfile: missing VOLUME [\"/workspace\"]")
    ports = re.findall(r"^EXPOSE\s+(\d+)\s*$", d, re.M)
    if len(ports) != 1:
        errs.append(f"{n}: dockerfile: need exactly one 'EXPOSE <port>', found {len(ports)}")
        return errs
    port = ports[0]
    cmd = next((ln for ln in d.splitlines() if ln.startswith("CMD")), "")
    if port not in cmd:
        errs.append(f"{n}: dockerfile: CMD does not use the EXPOSE port {port}")
    if SECRET_RE.search(d):
        errs.append(f"{n}: dockerfile: ENV/ARG sets a secret-like variable")
    lines = d.splitlines()
    if len(lines) < 2 or not lines[1].startswith("# A2A + "):
        errs.append(f"{n}: dockerfile: line 2 must be a '# A2A + <Runtime>' header comment")

    # README (standard §3)
    if not r.startswith("# A2A + "):
        errs.append(f"{n}: readme: first line must start '# A2A + '")
    for h in ("## Usage", "## Environment Configuration"):
        if h not in r.splitlines():
            errs.append(f"{n}: readme: missing heading '{h}'")
    if "docker run" not in r or ":/workspace" not in r:
        errs.append(f"{n}: readme: needs a 'docker run' with '-v <dir>:/workspace'")
    if f"-p {port}:{port}" not in r:
        errs.append(f"{n}: readme: docker run must publish '-p {port}:{port}'")
    if "```dotenv" not in r:
        errs.append(f"{n}: readme: missing ```dotenv block")
    if "main:app" in cmd and "main.py" not in r:
        errs.append(f"{n}: readme: CMD runs main:app but README never mentions main.py")

    # Repo level (standard §4)
    root = (ROOT / "README.md").read_text()
    row = [ln for ln in root.splitlines() if f"`images/{n}/`" in ln]
    if not row:
        errs.append(f"{n}: root-readme: no row with `images/{n}/`")
    elif f"`{port}`" not in row[0]:
        errs.append(f"{n}: root-readme: row does not show default port `{port}`")
    comp = ROOT / "docker-compose.example.yml"
    ctext = comp.read_text() if comp.is_file() else ""
    m = re.search(rf"dockerfile:\s*images/{re.escape(n)}/Dockerfile\s*\n(.*?)(?=^\S|^  \S|\Z)", ctext, re.S | re.M)
    if not m:
        errs.append(f"{n}: compose: no service builds images/{n}/Dockerfile")
    elif not re.search(rf'-\s*"?\d+:{port}"?', m.group(1)):
        errs.append(f"{n}: compose: ports must map to container port {port}")
    return errs


def main(argv: list[str]) -> int:
    targets = [Path(a).resolve() for a in argv] or sorted(p for p in (ROOT / "images").iterdir() if p.is_dir())
    errs = [e for t in targets for e in check(t)]
    for e in errs:
        print(e)
    print(f"{'FAIL' if errs else 'PASS'}: {len(targets)} image(s), {len(errs)} violation(s)")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
