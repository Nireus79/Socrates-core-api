"""
Local model stubs for API routers

These are minimal placeholder models used by API routers.
Routers should use get_database() and other local modules instead of relying on external model definitions.
"""

from typing import Any, Dict, Optional


class User:
    """Minimal User model stub for API routers"""
    def __init__(self, user_id: str = "", username: str = "", email: str = ""):
        self.id = user_id
        self.username = username
        self.email = email
        self.metadata: Dict[str, Any] = {}

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "metadata": self.metadata
        }


class ProjectContext:
    """Minimal ProjectContext model stub for API routers"""
    def __init__(self, project_id: str = "", name: str = ""):
        self.project_id = project_id
        self.name = name
        self.description = ""
        self.created_at = ""
        self.metadata: Dict[str, Any] = {}
        self.phase_maturity_scores: Dict[str, float] = {}

    def to_dict(self) -> Dict:
        return {
            "project_id": self.project_id,
            "name": self.name,
            "description": self.description,
            "created_at": self.created_at,
            "metadata": self.metadata
        }


class ProjectDatabase:
    """Minimal ProjectDatabase stub - USE get_database() INSTEAD"""
    def __init__(self, db_path: str = ""):
        self.db_path = db_path

    def get_project(self, project_id: str) -> Optional[Dict]:
        return None

    def save_project(self, project: ProjectContext) -> bool:
        return True

    def list_projects(self, user_id: str = "", limit: int = 100) -> list:
        return []


class LearningIntegration:
    """Minimal LearningIntegration stub - USE socratic_learning FROM PyPI"""
    def __init__(self):
        pass

    def log_interaction(self, user_id: str, action: str, data: Dict) -> bool:
        return True

    def get_recommendations(self, user_id: str) -> Dict:
        return {}
