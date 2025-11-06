# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Fit4Cybersecurity is a Django-based self-assessment tool by NC3-LU to help business owners implement better cybersecurity strategies. The platform supports multiple branded survey variants (fit4cybersecurity, fit4africa, fit4contract, fit4ehealth, fit4operatorsurvey, fit4privacy) with customizable questionnaires, scoring, and PDF report generation.

## Branch Policy

- The `codex` branch is **exclusively** for AI/GPT-generated content (e.g., Claude Code, GitHub Copilot). **No manual edits or human-written code** may be committed to this branch.
- Only automated, AI-generated documentation updates are permitted; all manual code changes, bug fixes, and features must be committed to a different branch.
- The `master` branch is the main stable branch for production.
- Develop features in separate branches and merge to master.

## Development Setup

```bash
# Install Python dependencies
poetry install

# Install pre-commit hooks (REQUIRED before committing)
pre-commit install

# Install front-end dependencies
npm ci

# Run migrations (after setting up database config)
make migrate

# Start development server
make run
# OR: poetry run python manage.py runserver
```

## Common Commands

### Development
- `make run` - Start the Django development server
- `poetry run python manage.py runserver` - Alternative way to start server
- `make migrate` - Apply database migrations
- `make migration` - Generate new migrations after model changes
- `make superuser` - Create Django superuser for admin access

### Testing
- `poetry run python manage.py test` - Run all tests
- `poetry run python manage.py test survey.tests` - Run specific app tests
- `poetry run python manage.py test survey.tests.TestClassName` - Run specific test class

### Code Quality
- `pre-commit run --all-files` - Run all pre-commit hooks (do this before pushing)
- `poetry run black .` - Format Python code
- `poetry run flake8` - Lint Python code
- `poetry run pip-audit` - Check for security vulnerabilities in dependencies

### Internationalization
- `python manage.py makemessages -a` - Extract translatable strings to .po files
- `python manage.py compilemessages` - Compile .po files to .mo for production
- `make generatepot` - Generate .pot file with all translatable strings

### Question Management
- `python manage.py import_questions data/questions.json` - Import survey questions
- `python manage.py export_questions` - Export questions to JSON
- `make populate path=data/` - Populate database with questions from path

### Static Files
- `python manage.py collectstatic` - Collect static files for production
- `npm ci` - Install and link front-end packages (creates static/npm_components symlink)

### Production Deployment
- `make update` - Full production update (npm, poetry install, collectstatic, compilemessages, migrate)
- `make deploy` - Build and start Docker containers
- `make down` - Stop Docker containers

## Architecture

### Multi-Brand System

The application supports multiple survey brands through a configuration-based architecture:

1. **Brand Configuration**: Each brand (fit4cybersecurity, fit4africa, etc.) is defined in `csskp/fit4*/init__.py` with a `CUSTOM` dictionary containing:
   - Tool name and intro text
   - Language preferences
   - Logo paths
   - Score thresholds
   - Enabled modules (report download, email, diagnostics)
   - Available report sections
   - Stats chart configurations

2. **Settings Resolution**: `csskp/settings.py` imports configuration from `csskp/config.py` (production) or `csskp/config_dev.py` (development). The config file must define `SITE_NAME` which points to the brand module.

3. **Template Hierarchy**: Templates are resolved in this order:
   - `templates/{SITE_NAME}/` (brand-specific)
   - `templates/` (main templates)
   - `templates/parts/` (reusable parts)

### Core Apps

- **survey/**: Core questionnaire functionality
  - `models.py`: Survey data models (SurveyUser, SurveyQuestion, SurveyUserAnswer, etc.)
  - `views.py`: Main survey views (start, questions, results)
  - `viewLogic.py`: Business logic separated from views
  - `forms.py`: Django forms for user input
  - `report.py`: HTML/PDF report generation using WeasyPrint
  - `reporthelper.py`: Score calculation and radar chart generation with matplotlib
  - `api/`: REST API using Django REST Framework

- **stats/**: Analytics and reporting views for survey data

- **admin/**: Custom admin interface beyond Django's default admin

- **utils/**: Shared utilities
  - `notifications.py`: Email sending for reports
  - `utils.py`: General utility functions
  - `radarFactory.py`: Radar chart generation logic

### Key Data Flow

1. **Survey Start** (`survey/views.py:start`): User fills company info → creates SurveyUser with encrypted user_id
2. **Questions** (`survey/views.py:questions`): Loads question sequence → displays one question at a time → saves answers to SurveyUserAnswer
3. **Results** (`survey/views.py:results`): Calculates scores using `reporthelper.calculateResult()` → generates recommendations → displays results or creates PDF report

### Models Overview

- `SurveyUser`: Stores survey participant with company info (sector, size, country)
- `SurveyQuestion`: Question text with type (multiple choice, single choice, slider), section, service category
- `SurveyQuestionAnswer`: Possible answers for each question with scores
- `SurveyUserAnswer`: User's selected answer for a question (many-to-many relationship)
- `SurveySection`: Groups questions into sections
- `SurveyQuestionServiceCategory`: Categorizes questions by service area

### API

REST API available at `/api/` using Django REST Framework:
- OpenAPI schema available via drf-spectacular
- Serializers in `survey/api/serializers.py`
- Views in `survey/api/views.py`
- Authentication: Basic + Session auth

## Configuration Management

**IMPORTANT**: Never commit sensitive configuration files:

1. **Production Config**: Create `csskp/config.py` (gitignored) with:
   - `SECRET_KEY`, `HASH_KEY`: Django secrets
   - `SITE_NAME`: Brand identifier (e.g., "fit4cybersecurity")
   - `DATABASES`: PostgreSQL connection settings
   - `DEBUG`, `LOGGING`, `LOG_DIRECTORY`
   - `ALLOWED_HOSTS`, `PUBLIC_URL`, `OPERATOR_CONTACT`
   - `EMAIL_HOST`, `EMAIL_PORT`
   - `REPORT_TEMPLATE_DIR`
   - Optional: `CORS_ALLOWED_ORIGINS`, `CORS_ALLOWED_ORIGIN_REGEXES`

2. **Development Config**: `csskp/config_dev.py` is a reference example (safe to commit)

## Coding Standards

- **Python Style**: Black formatter with 100-character line length, 4-space indents
- **Naming**: snake_case for functions/variables, PascalCase for classes, kebab-case for templates/static files
- **Imports**: Use reorder-python-imports (handled by pre-commit)
- **Type Hints**: mypy is configured; add type hints for new code
- **Pre-commit**: MUST pass before pushing (pyupgrade, reorder-python-imports, black, flake8, pip-audit)

## Testing

- Use Django's TestCase or APITestCase
- Place tests in `{app}/tests/` directory
- Seed data using fixtures in `data/` or factory utilities in `survey/lib`
- Focus on: scoring rules, serializers, report generation, questionnaire logic
- Keep tests deterministic and fast for CI

## Translations

- Translations stored in `locale/{lang}/LC_MESSAGES/`
- Always run `makemessages` and `compilemessages` after adding translatable strings
- Use `gettext_lazy` for model fields and settings, `gettext` in views
- Translation status tracked at https://translate.monarc.lu

## Front-end

- **Framework**: Vanilla JavaScript (no framework)
- **Dependencies**: Bootstrap 4, jQuery, Chart.js (managed via npm)
- **Static files**: Located in `static/`, npm packages symlinked to `static/npm_components/`
- Bootstrap configuration in `csskp/settings.py` (BOOTSTRAP4 dict)

## Security Notes

- User IDs are encrypted using Fernet (cryptography library) with HASH_KEY
- CORS headers configured for cross-origin API access
- CSRF protection enabled for all forms
- Cookie banner implemented via django-cookiebanner
- Run `pip-audit` after dependency updates
- Never commit `.env`, `config.py`, or files with secrets

## Report Generation

Reports use WeasyPrint for HTML-to-PDF conversion:
- HTML template rendered with survey results
- Radar charts generated as PNG using matplotlib
- Charts encoded as base64 and embedded in HTML
- Report templates in `templates/report/`
- Logos and styling defined per brand in CUSTOM config

## Docker Deployment

- `docker-compose.yml` defines production stack
- Use `make deploy` to build and start containers
- Database runs in separate PostgreSQL container
- Static files must be collected before deployment
