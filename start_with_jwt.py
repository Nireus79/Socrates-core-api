#!/usr/bin/env python
"""
Start Socrates API with JWT_SECRET_KEY properly configured.
"""
import os
import secrets
import subprocess
import sys

# Generate and set JWT_SECRET_KEY
jwt_secret = secrets.token_urlsafe(32)
os.environ['JWT_SECRET_KEY'] = jwt_secret
print(f"[INFO] JWT_SECRET_KEY set to: {jwt_secret[:20]}...")

# Now run the API
if __name__ == '__main__':
    from socrates_api.main import app, run
    run()
