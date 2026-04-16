# Scratch workspace

Use `.scratch/` for disposable local-only work:

- one-off QA probes
- browser/playwright experiments
- temporary debug scripts
- captured notes or artifacts that should not live at repo root

Rules:

- Nothing in `.scratch/` should be required for the product or test suite
- If a script becomes reusable, move it into a real tracked location with a better name
- Prefer subfolders for batches of related probes, for example `.scratch/qa-probes/`
- Keep secrets out of committed files. `.scratch/` is gitignored, but local files can still leak through copy/paste

Current convention:

- root-level disposable scripts should be moved into `.scratch/qa-probes/`
- product code, tests, and docs should stay outside `.scratch/`
