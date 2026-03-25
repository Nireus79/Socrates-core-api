#!/usr/bin/env python
"""
Socrates API Server Startup Script

Sets environment variables BEFORE importing the app to ensure
JWT_SECRET_KEY is available during module initialization.
"""
import os
import sys

# Set environment FIRST
if not os.getenv("JWT_SECRET_KEY"):
    os.environ["JWT_SECRET_KEY"] = "dev-secret-key-change-in-production"
    
if not os.getenv("ENVIRONMENT"):
    os.environ["ENVIRONMENT"] = "development"

print(f"Environment: {os.getenv('ENVIRONMENT')}")
print(f"JWT_SECRET_KEY: {os.getenv('JWT_SECRET_KEY')[:20]}...")

# Now import app
from socrates_api.main import app
import uvicorn

# Verify auth router is loaded
from socrates_api.routers import auth_router
if auth_router:
    print(f"Auth router loaded with {len(auth_router.routes)} routes")
else:
    print("ERROR: Auth router is None!")
    sys.exit(1)

# Run server
print("\nStarting Socrates API Server on http://127.0.0.1:8000")
uvicorn.run(
    app,
    host="127.0.0.1",
    port=8000,
    log_level="info"
)
