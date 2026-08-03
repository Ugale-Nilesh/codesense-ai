from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    description="AI-powered developer assistant backend",
    version=settings.APP_VERSION,
)


@app.get("/health")
def health_check() -> dict[str, str]:
    """Basic liveness check - confirms the API is running."""
    return {"status": "ok", "environment": settings.ENVIRONMENT}
