"""Document management API endpoints."""

from fastapi import APIRouter
from typing import Any, Dict

router = APIRouter()


@router.get("")
async def list_documents() -> Dict[str, Any]:
    """List documents."""
    return {"message": "List documents endpoint"}


@router.post("/import")
async def import_document() -> Dict[str, Any]:
    """Import document."""
    return {"message": "Import document endpoint"}


@router.post("/import-dir")
async def import_directory() -> Dict[str, Any]:
    """Import directory of documents."""
    return {"message": "Import directory endpoint"}


@router.get("/{doc_id}")
async def get_document(doc_id: str) -> Dict[str, Any]:
    """Get document details."""
    return {"message": "Get document endpoint", "doc_id": doc_id}


@router.delete("/{doc_id}")
async def delete_document(doc_id: str) -> Dict[str, Any]:
    """Delete document."""
    return {"message": "Delete document endpoint", "doc_id": doc_id}
