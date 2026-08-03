import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Centralized application configuration, loaded from environment variables."""

    # Application
    APP_NAME: str = os.getenv("APP_NAME", "CodeSense AI")
    APP_VERSION: str = os.getenv("APP_VERSION", "0.1.0")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"
    HOST: str = os.getenv("HOST", "127.0.0.1")
    PORT: int = int(os.getenv("PORT", "8000"))

    # Database
    DATABASE_URL: str | None = os.getenv("DATABASE_URL") or None

    # Security
    SECRET_KEY: str | None = os.getenv("SECRET_KEY") or None
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60")
    )

    # AI Providers
    OPENAI_API_KEY: str | None = os.getenv("OPENAI_API_KEY") or None
    ANTHROPIC_API_KEY: str | None = os.getenv("ANTHROPIC_API_KEY") or None
    GOOGLE_API_KEY: str | None = os.getenv("GOOGLE_API_KEY") or None

    # GitHub
    GITHUB_CLIENT_ID: str | None = os.getenv("GITHUB_CLIENT_ID") or None
    GITHUB_CLIENT_SECRET: str | None = os.getenv("GITHUB_CLIENT_SECRET") or None

    # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")


settings = Settings()
