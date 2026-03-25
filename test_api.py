import os
os.environ["JWT_SECRET_KEY"] = "test-dev"
os.environ["ENVIRONMENT"] = "development"

from socrates_api.main import app
import uvicorn

uvicorn.run(app, host="127.0.0.1", port=9001, log_level="error")
