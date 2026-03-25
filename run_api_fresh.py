import os
os.environ["JWT_SECRET_KEY"] = "test-dev-secret"
os.environ["ENVIRONMENT"] = "development"

from socrates_api.main import app
import uvicorn

print("Starting API...")
uvicorn.run(app, host="127.0.0.1", port=8000, log_level="warning")
