# Repository Guidelines

## Project Structure & Module Organization
- `csskp/` contains Django settings and the brand-specific survey apps (`fit4cybersecurity`, `fit4africa`, etc.).
- `survey/` holds questionnaire models, forms, and APIs; `stats/` provides reporting views and helpers.
- Reusable UI lives in `templates/` and `static/`; running `npm ci` links vendor bundles into `static/npm_components/`.
- Support material is stored in `utils/`, `data/`, and `docs/`.
Keep new logic inside the relevant app, colocate fixtures or templates, and add tests under an app-level `tests/` package.

## Build, Test, and Development Commands
- `poetry install`: create the virtualenv with project and dev dependencies.
- `npm ci`: install front-end packages required by the static pipeline.
- `make run` or `poetry run python manage.py runserver`: launch the local server.
- `make migrate`: apply migrations after generating them with `make migration`.
- `python manage.py collectstatic` and `compilemessages`: refresh assets and translations before packaging.
Use `docker-compose up -d` for a production-like stack when validating deployment paths.

## Coding Style & Naming Conventions
Formatting is enforced through pre-commit (`pyupgrade`, `reorder-python-imports`, `black`, `flake8`, `pip-audit`). Run `pre-commit run --all-files` before pushing. Follow Black’s defaults (4-space indents, 100-character lines), snake_case for Python identifiers, PascalCase for classes, and kebab-case for front-end assets. Name templates after their view path (e.g., `survey/results_detail.html`), and keep serializers, forms, and views in dedicated modules.

## Testing Guidelines
Rely on Django’s test runner: `python manage.py test` or targeted calls like `python manage.py test survey.tests`. Use `TestCase` or `APITestCase`, seed data with fixtures under `data/` or factory utilities in `survey/lib`, and assert on scoring rules, serializers, and report generation. CI executes the default suite, so keep tests deterministic and fast; add regression coverage whenever questionnaire logic changes.

## Commit & Pull Request Guidelines
Commits should be small, imperative, and optionally prefixed (`build(deps): bump django`). Reference issue IDs or tickets in the footer as needed. Pull requests must describe the problem, summarize the fix, list the commands/tests run, and provide screenshots for UI changes. Confirm linting, migrations, and locale updates before requesting review.

## Security & Configuration Tips
Configure secrets via environment variables consumed in `csskp/settings.py`; never commit `.env` files. Run `poetry run pip-audit` after dependency updates, and refresh locales with `python manage.py makemessages -a` followed by `compilemessages`. Before release, ensure `collectstatic` output and translations under `locale/` are up to date.
