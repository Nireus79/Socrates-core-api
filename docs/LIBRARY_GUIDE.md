# socrates-core-api Library Guide

## Overview

**socrates-core-api** is a production-ready REST API server for the Socrates AI platform. It exposes all Socratic method functionality through HTTP endpoints, enabling CLI tools, web applications, and integrations to interact with Socrates.

**Current Version**: 0.1.0
**Package Name**: `socrates-core-api`
**Python Support**: 3.8+
**License**: MIT
**Status**: Production Ready

## What This Library Does

socrates-core-api provides:

### 1. RESTful API Endpoints (25+)
- Project management (create, list, read, update, delete)
- Code generation
- Socratic guidance and questioning
- Knowledge management
- Artifact generation and storage
- GitHub synchronization
- Configuration management

### 2. Authentication & Security
- JWT-based token authentication
- Multi-Factor Authentication (TOTP/2FA)
- Account lockout protection (progressive lockout)
- Token fingerprinting (IP + User-Agent validation)
- Password breach detection (HaveIBeenPwned)
- Comprehensive audit logging
- OWASP-compliant security headers
- Rate limiting (5 requests/minute default)

### 3. Database Management
- User management and authentication
- Project storage and retrieval
- Session management
- Refresh token handling
- API key management
- Database encryption for sensitive fields

### 4. Real-Time Features
- Event streaming (via event emitter)
- Activity tracking
- Performance monitoring
- Metrics collection

### 5. Production Features
- Uvicorn ASGI server
- Prometheus metrics endpoint
- Structured logging
- Health checks
- Error handling and recovery

## Architecture

```
socrates-core-api
    │
    ├── auth/          # Authentication & MFA
    ├── routers/       # API endpoints
    ├── models/        # Pydantic request/response models
    ├── middleware/    # Rate limiting, CSRF, audit logging
    ├── database/      # Database operations
    └── services/      # Business logic services
```

## Key Endpoints

### Authentication
- `POST /auth/register` - User registration
- `POST /auth/login` - User login with MFA support
- `POST /auth/refresh` - Refresh access token
- `POST /auth/logout` - User logout
- `PUT /auth/change-password` - Change password (with breach checking)
- `POST /auth/mfa/enable` - Enable MFA (setup phase)
- `POST /auth/mfa/verify-enable` - Verify and enable MFA
- `GET /auth/mfa/status` - Check MFA status
- `POST /auth/mfa/disable` - Disable MFA
- `GET /auth/csrf-token` - Get CSRF token

### Projects
- `GET /projects` - List user's projects
- `POST /projects` - Create new project
- `GET /projects/{project_id}` - Get project details
- `PUT /projects/{project_id}` - Update project
- `DELETE /projects/{project_id}` - Delete project

### Code Generation
- `POST /code/generate` - Generate code
- `POST /code/analyze` - Analyze code
- `POST /code/test` - Generate tests

### Knowledge Management
- `POST /knowledge/import` - Import knowledge
- `GET /knowledge` - List knowledge
- `DELETE /knowledge/{knowledge_id}` - Delete knowledge

### System
- `GET /health` - Health check
- `GET /metrics` - Prometheus metrics
- `GET /config` - Get configuration

## Installation

```bash
# Install from PyPI
pip install socrates-core-api

# Install with optional features
pip install socrates-core-api[full]

# Install for development
pip install socrates-core-api[dev]
```

## Quick Start

### 1. Set Environment Variables
```bash
# Required
export ANTHROPIC_API_KEY="sk-..."
export JWT_SECRET_KEY="your-secret-key-here"
export SOCRATES_ENCRYPTION_KEY="your-encryption-key"

# Optional
export DATABASE_URL="postgresql://user:pass@localhost/socrates"
export REDIS_URL="redis://localhost:6379"
export API_PORT="8000"
```

### 2. Run the Server
```bash
# Using uvicorn directly
uvicorn socrates_api.main:app --host 0.0.0.0 --port 8000

# Using docker
docker run -e ANTHROPIC_API_KEY="sk-..." socrates-core-api:latest

# Using Kubernetes
kubectl apply -f k8s/
```

### 3. Access the API
```bash
# Health check
curl http://localhost:8000/health

# Interactive docs (Swagger UI)
open http://localhost:8000/docs

# OpenAPI schema
curl http://localhost:8000/openapi.json
```

## Authentication

### Register User
```bash
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "password": "secure_password_123",
    "email": "john@example.com"
  }'
```

### Login
```bash
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "password": "secure_password_123"
  }'

# Response includes access_token
```

### Use Access Token
```bash
curl -H "Authorization: Bearer {access_token}" \
  http://localhost:8000/projects
```

## Multi-Factor Authentication (MFA)

### Enable MFA
```bash
# Step 1: Setup MFA
curl -X POST http://localhost:8000/auth/mfa/enable \
  -H "Authorization: Bearer {access_token}"

# Response includes QR code URI for authenticator app

# Step 2: Verify with TOTP code from authenticator
curl -X POST http://localhost:8000/auth/mfa/verify-enable \
  -H "Authorization: Bearer {access_token}" \
  -H "Content-Type: application/json" \
  -d '{"totp_code": "123456"}'
```

### Login with MFA
```bash
# Login as normal
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "john_doe", "password": "..."}'

# If MFA enabled, use recovery code or TOTP code from authenticator
```

## Security Features

### 1. Password Requirements
- Minimum 8 characters
- Mix of uppercase, lowercase, digits, and special characters
- Not found in HaveIBeenPwned database (100+ occurrences)

### 2. Account Lockout
- Progressive lockout after failed login attempts
- Configurable thresholds (default: 5 attempts)
- Progressive durations: 30min → 1hr → 2hrs

### 3. Token Security
- Short-lived access tokens (15 minutes)
- Refresh tokens for long-term access
- Token fingerprinting (IP + User-Agent validation)
- Token revocation support

### 4. Data Protection
- Field-level encryption for sensitive data
- Password hashing using bcrypt
- CSRF protection for web frontend
- SQL injection prevention
- XSS protection

### 5. Audit Logging
All operations logged with:
- User ID
- IP address
- Timestamp
- Action type
- Resource accessed
- Success/failure status
- Error messages

## Database

### Supported Databases
- **SQLite** (development, default)
- **PostgreSQL** (production recommended)

### Environment Variables
```bash
# SQLite (default)
DATABASE_URL="sqlite:///./socrates.db"

# PostgreSQL
DATABASE_URL="postgresql://user:password@localhost:5432/socrates"

# Encryption
DATABASE_ENCRYPTION_KEY="fernet-key-base64"

# Connection pooling
SQLALCHEMY_POOL_SIZE=20
SQLALCHEMY_POOL_RECYCLE=3600
```

### Migrations
```bash
# Apply migrations
alembic upgrade head

# Create migration
alembic revision --autogenerate -m "Add new column"
```

## Caching with Redis

### Optional Redis Support
```bash
# Enable caching
export REDIS_URL="redis://localhost:6379/0"

# Caching configuration
REDIS_MAX_CONNECTIONS=50
REDIS_SOCKET_TIMEOUT=5
REDIS_CONNECTION_TIMEOUT=5
```

### Cached Items
- Session tokens
- User data
- Project metadata
- Rate limit counters
- Embedding cache

## Rate Limiting

### Default Limits
- Authentication endpoints: 5/minute
- API endpoints: 100/minute (per user)
- Metrics endpoint: 1000/minute

### Configure Rate Limiting
```bash
# Global rate limit
export RATE_LIMIT_PER_MINUTE=100

# Auth rate limit
export AUTH_RATE_LIMIT_PER_MINUTE=5
```

## Metrics & Monitoring

### Prometheus Metrics
```bash
# Get metrics in Prometheus format
curl http://localhost:8000/metrics
```

### Key Metrics
- `http_request_duration_seconds` - Request latency
- `http_request_total` - Total requests by method/endpoint
- `socrates_agent_duration_seconds` - Agent execution time
- `socrates_token_usage_total` - Claude API token usage
- `socrates_errors_total` - Error count by type

### Grafana Integration
Pre-configured Grafana dashboard available in `/deployment/grafana/`

## Logging

### Log Configuration
```bash
# Log level
export LOG_LEVEL="INFO"

# Log format
export LOG_FORMAT="json"  # or "text"

# Log file
export LOG_FILE="/var/log/socrates-api.log"
```

### Log Fields
```json
{
  "timestamp": "2026-03-21T10:00:00Z",
  "level": "INFO",
  "logger": "socrates_api.main",
  "message": "User logged in",
  "user_id": "user123",
  "ip_address": "192.168.1.100",
  "trace_id": "abc123",
  "request_id": "req456"
}
```

## Deployment

### Docker
```bash
# Build image
docker build -t socrates-core-api:latest .

# Run container
docker run -e ANTHROPIC_API_KEY="sk-..." \
  -e JWT_SECRET_KEY="secret" \
  -p 8000:8000 \
  socrates-core-api:latest
```

### Kubernetes
```bash
# Deploy
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

# Scale replicas
kubectl scale deployment socrates-api --replicas=3

# Check status
kubectl get pods -l app=socrates-api
```

### Docker Compose
```bash
# Start services
docker-compose up -d

# View logs
docker-compose logs -f socrates-api

# Stop services
docker-compose down
```

## Testing

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=socrates_api --cov-report=html

# Run specific test
pytest tests/test_auth.py::test_login -v

# Run with markers
pytest -m "integration" tests/
```

## Configuration

### Environment Variables

#### Required
- `ANTHROPIC_API_KEY` - Claude API key
- `JWT_SECRET_KEY` - Secret for signing JWT tokens
- `SOCRATES_ENCRYPTION_KEY` - Key for field-level encryption

#### Optional
- `DATABASE_URL` - Database connection string
- `REDIS_URL` - Redis connection string
- `LOG_LEVEL` - Logging level (default: INFO)
- `LOG_FORMAT` - Logging format (default: text)
- `API_PORT` - Server port (default: 8000)
- `RATE_LIMIT_PER_MINUTE` - Rate limit (default: 100)

### Via Code
```python
from socrates_api.config import APIConfig

config = APIConfig(
    database_url="sqlite:///./socrates.db",
    jwt_secret_key="your-secret",
    log_level="DEBUG"
)
```

## Common Tasks

### Create a Project Programmatically
```bash
curl -X POST http://localhost:8000/projects \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "My Project",
    "description": "A test project",
    "language": "python"
  }'
```

### Export Project to GitHub
```bash
curl -X POST http://localhost:8000/projects/{id}/export \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/json" \
  -d '{
    "repository_url": "https://github.com/user/repo",
    "branch": "main"
  }'
```

### View Audit Logs
```bash
curl http://localhost:8000/audit/logs \
  -H "Authorization: Bearer {token}" \
  | jq '.'
```

## Troubleshooting

### Server Won't Start
```bash
# Check all required env vars are set
env | grep -E "ANTHROPIC|JWT|ENCRYPTION"

# Check port is available
lsof -i :8000

# Run with verbose logging
LOG_LEVEL=DEBUG uvicorn socrates_api.main:app --reload
```

### Authentication Errors
```bash
# Check JWT secret is set
echo $JWT_SECRET_KEY

# Check tokens are valid
curl -X POST http://localhost:8000/auth/verify \
  -H "Authorization: Bearer {token}"
```

### Database Issues
```bash
# Check database connection
psql $DATABASE_URL

# Run migrations
alembic upgrade head

# Reset database (dev only!)
alembic downgrade base
alembic upgrade head
```

## Version History

### v0.1.0 (Current)
- Complete REST API
- JWT authentication
- MFA support (TOTP)
- Account lockout
- Token fingerprinting
- Password breach detection
- Audit logging
- Rate limiting
- Prometheus metrics

## Contributing

When modifying socrates-core-api:
1. Add tests for new endpoints
2. Update API documentation
3. Update this guide
4. Follow security best practices
5. Ensure backward compatibility

## Related Documentation

- [Socrates Ecosystem Architecture](../../docs/SOCRATES_ECOSYSTEM_ARCHITECTURE.md)
- [Security Architecture](./SECURITY.md) (if exists)
- [API Reference](./API_REFERENCE.md) (available at /docs on running server)

## Support

For issues or questions:
- GitHub Issues: https://github.com/Nireus79/Socrates-api/issues
- Documentation: https://github.com/Nireus79/Socrates-api/tree/main/docs
- API Docs: http://localhost:8000/docs (when server running)
