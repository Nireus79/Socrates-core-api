# E2E Authentication Test - Quick Reference

## Test Results
- **Status**: ✓ ALL TESTS PASSED
- **Date**: 2026-03-25
- **Duration**: ~6 minutes
- **Environment**: Development

## API Endpoint
```
http://localhost:9003
```

## Test User Credentials
```
Username: e2etest123
Email: e2e123@test.com
Password: E2eTest123!@#
```

## API Endpoints Tested

### 1. Health Check
```bash
GET http://localhost:9003/health
```
**Response**: healthy status, all components ready

### 2. User Registration
```bash
POST http://localhost:9003/auth/register
Content-Type: application/json

{
  "username": "e2etest123",
  "password": "E2eTest123!@#",
  "email": "e2e123@test.com"
}
```
**Response**: User object + access_token + refresh_token

### 3. User Login
```bash
POST http://localhost:9003/auth/login
Content-Type: application/json

{
  "username": "e2etest123",
  "password": "E2eTest123!@#"
}
```
**Response**: User object + access_token + refresh_token

### 4. Token Refresh
```bash
POST http://localhost:9003/auth/refresh
Content-Type: application/json

{
  "refresh_token": "<your_refresh_token>"
}
```
**Response**: New access_token + refresh_token

## JWT Token Details

### Access Token
- **Algorithm**: HS256
- **Expiry**: 900 seconds (15 minutes)
- **Type**: access
- **Contains**: subject, expiry, issued_at, type, fingerprint

### Refresh Token
- **Algorithm**: HS256
- **Expiry**: 604800 seconds (7 days)
- **Type**: refresh
- **Contains**: subject, expiry, issued_at, type

## Frontend Configuration

### Option 1: Environment Variable
```bash
export VITE_API_URL=http://localhost:9003
npm run dev
```

### Option 2: .env.local File
```
VITE_API_URL=http://localhost:9003
```

### Option 3: Auto-Discovery
Frontend automatically detects API on common ports:
- 8000, 8008, 8009, 8010, 8015, 8020
- Can be extended to include 9003 in `/src/api/client.ts`

## Frontend API Client Features
- ✓ Automatic JWT injection
- ✓ Proactive token refresh (2 min before expiry)
- ✓ Automatic error handling
- ✓ localStorage persistence
- ✓ 401 retry mechanism
- ✓ Configurable timeout (60s default)

## Security Summary
- ✓ JWT properly signed with HS256
- ✓ Separate access/refresh tokens
- ✓ Token fingerprinting
- ✓ Rate limiting (in-memory backend)
- ✓ Security headers middleware
- ✓ CORS configured
- ✓ Audit logging enabled

## Important Files
- API Main: `/src/socrates_api/main.py`
- Database: `~/.socrates/api_projects.db`
- Frontend API Client: `/socrates-frontend/src/api/client.ts`
- Frontend Config: `/socrates-frontend/.env.example`

## Database Schema
The API creates users with:
- username (unique)
- email (unique)
- password (hashed)
- subscription_tier (default: free)
- subscription_status (default: active)
- testing_mode (default: true)
- created_at (timestamp)

## Testing Commands

### Test Registration
```bash
curl -X POST http://localhost:9003/auth/register \
  -H "Content-Type: application/json" \
  -d '{"username":"test","password":"Test123!","email":"test@example.com"}'
```

### Test Login
```bash
curl -X POST http://localhost:9003/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"test","password":"Test123!"}'
```

### Test Health
```bash
curl http://localhost:9003/health
```

## Starting the API

### With Custom Port
```bash
export JWT_SECRET_KEY="your-secret-key"
export SOCRATES_API_PORT=9003
export ENVIRONMENT=development
python -m socrates_api.main
```

### Generate JWT Secret
```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

## Troubleshooting

### Port Already in Use
```bash
# Change port in command
export SOCRATES_API_PORT=9004
```

### JWT_SECRET_KEY Missing
```bash
export JWT_SECRET_KEY="$(python -c 'import secrets; print(secrets.token_urlsafe(32))')"
```

### Frontend Can't Connect
1. Check API is running on correct port
2. Set VITE_API_URL environment variable
3. Check CORS is configured (should work on localhost)
4. Verify token is valid JWT format

## Production Checklist
- [ ] Use strong JWT_SECRET_KEY
- [ ] Set ENVIRONMENT=production
- [ ] Enable HTTPS/TLS
- [ ] Configure proper CORS origins
- [ ] Set up external Redis
- [ ] Configure database backup
- [ ] Monitor authentication logs
- [ ] Implement rate limiting properly
- [ ] Set up API key management
- [ ] Test all endpoints thoroughly

## Next Steps
1. Deploy frontend with VITE_API_URL configured
2. Run full integration tests
3. Test token refresh mechanism
4. Monitor authentication logs
5. Set up production environment

---

**Test Report Location**: 
- `/c/Users/themi/PycharmProjects/Socrates-api/E2E_AUTH_TEST_REPORT.md`
- `/c/Users/themi/PycharmProjects/Socrates-api/E2E_AUTH_TEST_SUMMARY.md`
