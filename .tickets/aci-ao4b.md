---
id: aci-ao4b
status: closed
deps: []
links: []
created: 2026-10-18T00:16:06Z
type: task
priority: 1
assignee: Sampath Kumar
parent: aci-vwlr
---
# scripts/validate_image.py + fix existing image READMEs


## Notes

**2026-10-18T00:17:17Z**

Added scripts/validate_image.py (stdlib). First run FAIL 3: a2a-adk-antigravity, a2a-hermes, a2a-opencode READMEs never mention main.py although CMD runs uvicorn main:app -> added one sentence each. Now PASS 4/4. Negative test (compose container port changed) correctly fails.
