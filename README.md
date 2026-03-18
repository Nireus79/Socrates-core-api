# Socrates API

REST API for Socrates AI framework built with FastAPI.

## Features

- **FastAPI Framework** - Modern, fast, and production-ready
- **Comprehensive REST Endpoints** for all Socrates commands
- **OpenAPI/Swagger Documentation** at `/api/docs`
- **Pydantic Validation** for request/response data
- **CORS Support** for web frontend integration
- **Async/Await Support** for high performance
- **Health Check Endpoint** at `/health`

## Installation

```bash
pip install socrates-api
```

## Quick Start

### Running the Server

```bash
# Using uvicorn directly
uvicorn socrates_api:app --host 0.0.0.0 --port 8000

# Or using Python
python -m socrates_api
```

### Using Docker

```bash
docker build -t socrates-api .
docker run -p 8000:8000 socrates-api
```

### API Endpoints

#### Analytics
- `GET /api/analytics/summary` - Get analytics summary
- `GET /api/analytics/analyze` - Analyze categories
- `GET /api/analytics/trends` - Get trends
- `GET /api/analytics/breakdown` - Get detailed breakdown

#### Projects
- `GET /api/projects` - List projects
- `POST /api/projects` - Create project
- `GET /api/projects/{id}` - Get project details
- `PUT /api/projects/{id}` - Update project
- `DELETE /api/projects/{id}` - Delete project

#### Code
- `POST /api/code/generate` - Generate code
- `POST /api/code/explain` - Explain code
- `POST /api/code/review` - Review code
- `POST /api/code/docs` - Generate documentation

#### Sessions
- `GET /api/sessions` - List sessions
- `POST /api/sessions` - Create session
- `GET /api/sessions/{id}` - Get session
- `POST /api/sessions/{id}/save` - Save session
- `POST /api/sessions/{id}/load` - Load session

#### Documents
- `GET /api/documents` - List documents
- `POST /api/documents/import` - Import document
- `POST /api/documents/import-dir` - Import directory
- `GET /api/documents/{id}` - Get document
- `DELETE /api/documents/{id}` - Delete document

#### Collaboration
- `POST /api/collaboration/add` - Add collaborator
- `GET /api/collaboration/list` - List collaborators
- `PUT /api/collaboration/{id}/role` - Set role
- `DELETE /api/collaboration/{id}` - Remove collaborator

#### Workflows
- `GET /api/workflows` - List workflows
- `POST /api/workflows` - Create workflow
- `GET /api/workflows/{id}` - Get workflow
- `PUT /api/workflows/{id}` - Update workflow
- `DELETE /api/workflows/{id}` - Delete workflow

#### Health
- `GET /health` - Health check

## Configuration

### Environment Variables

```bash
# Server
API_HOST=0.0.0.0
API_PORT=8000
API_RELOAD=true

# CORS
CORS_ORIGINS=["*"]

# Logging
LOG_LEVEL=INFO
```

## Development

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest tests/ -v

# Format code
black src/ tests/

# Check types
mypy src/socrates_api --strict

# Lint
ruff check src/ tests/
```

## Architecture

### Main Application

```python
from socrates_api import create_app

app = create_app()
```

### Adding Custom Routes

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/custom")
async def custom_endpoint():
    return {"message": "Custom endpoint"}

app.include_router(router, prefix="/api/custom")
```

## Dependencies

- **fastapi** >= 0.104.0 - Web framework
- **uvicorn** >= 0.24.0 - ASGI server
- **pydantic** >= 2.0.0 - Data validation
- **socrates-cli** >= 0.1.0 - CLI commands
- **socratic-learning** >= 0.1.0 - Learning system
- **socratic-analyzer** >= 0.1.0 - Code analysis
- **socratic-workflow** >= 0.1.0 - Workflow orchestration
- **socratic-conflict** >= 0.1.0 - Conflict detection
- **socratic-agents** >= 0.1.0 - Multi-agent orchestration

## Docker Support

### Dockerfile

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY pyproject.toml .
RUN pip install --no-cache-dir .

EXPOSE 8000

CMD ["uvicorn", "socrates_api:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Docker Compose

```yaml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - API_HOST=0.0.0.0
      - API_PORT=8000
```

## Testing

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src/socrates_api

# Run specific test
pytest tests/test_api.py::test_health_check -v
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting
5. Submit a pull request

## License

MIT - See LICENSE file

## Support

- [GitHub Issues](https://github.com/Nireus79/Socrates-api/issues)
- [Documentation](https://github.com/Nireus79/Socrates-api)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)

---

Part of the Socrates AI Framework ecosystem.
