# agent2 — The Refactorer

Clean, maintainable foundation for code quality, structural improvements, performance, and complexity reduction.

## Structure

```
src/agent2/     # Application code
tests/          # Tests
pyproject.toml  # Project config + tool settings
```

## Tools (ready for refactoring work)

- **Ruff** — fast linter + formatter
- **Black** — code formatter (compatible)
- **pytest** — testing

## Quick start

```bash
pip install -e ".[dev]"
ruff check .
ruff format .
pytest
```

## Status

Initial bootstrap by Grok (The Refactorer). Ready for real code and continuous improvement.
