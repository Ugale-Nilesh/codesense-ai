from fastapi import FastAPI

app = FastAPI(
    title="CodeSense AI",
    description="AI-powered developer assistant backend",
    version="0.1.0",
)


@app.get("/health")
def health_check() -> dict[str, str]:
    """Basic liveness check - confirms the API is running."""
    return {"status": "ok"}