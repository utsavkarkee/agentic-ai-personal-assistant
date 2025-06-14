"""
Configuration management for the AI Personal Assistant.
"""

from pydantic import Field
from pydantic_settings import BaseSettings
from typing import List, Optional
import os
from pathlib import Path


class Settings(BaseSettings):
    """Application settings with environment variable support."""
    
    # Application Settings
    app_name: str = "AI Personal Assistant"
    app_version: str = "1.0.0"
    environment: str = Field(default="development", env="ENVIRONMENT")
    debug: bool = Field(default=True, env="DEBUG")
    secret_key: str = Field(default="your-secret-key-here", env="SECRET_KEY")
    
    # CORS Settings
    cors_origins: List[str] = Field(
        default=["http://localhost:3000", "http://localhost:8000"],
        env="CORS_ORIGINS"
    )
    
    # Database Settings
    database_url: str = Field(
        default="sqlite:///./ai_assistant.db",
        env="DATABASE_URL"
    )
    
    # OpenAI Settings
    openai_api_key: str = Field(..., env="OPENAI_API_KEY")
    ai_model: str = Field(default="gpt-4o-mini", env="AI_MODEL")
    ai_temperature: float = Field(default=0.7, env="AI_TEMPERATURE")
    ai_max_tokens: int = Field(default=1000, env="AI_MAX_TOKENS")
    
    # Google Calendar Settings
    google_credentials_path: str = Field(
        default="credentials/google_credentials.json",
        env="GOOGLE_CREDENTIALS_PATH"
    )
    google_token_path: str = Field(
        default="credentials/google_token.json",
        env="GOOGLE_TOKEN_PATH"
    )
    
    # ChromaDB Settings
    chroma_persist_directory: str = Field(
        default="./chroma_db",
        env="CHROMA_PERSIST_DIRECTORY"
    )
    chroma_collection_name: str = Field(
        default="ai_assistant_memory",
        env="CHROMA_COLLECTION_NAME"
    )
    
    # Logging Settings
    log_level: str = Field(default="INFO", env="LOG_LEVEL")
    log_file: str = Field(default="logs/ai_assistant.log", env="LOG_FILE")
    
    # Redis Settings (for production)
    redis_url: Optional[str] = Field(default=None, env="REDIS_URL")
    
    # Celery Settings (for background tasks)
    celery_broker_url: Optional[str] = Field(default=None, env="CELERY_BROKER_URL")
    celery_result_backend: Optional[str] = Field(default=None, env="CELERY_RESULT_BACKEND")
    
    # Time Zone
    timezone: str = Field(default="America/New_York", env="TIMEZONE")
    
    class Config:
        env_file = ".env"
        case_sensitive = False
        
    @property
    def is_development(self) -> bool:
        """Check if running in development mode."""
        return self.environment.lower() == "development"
    
    @property
    def is_production(self) -> bool:
        """Check if running in production mode."""
        return self.environment.lower() == "production"
    
    def get_database_url(self) -> str:
        """Get the database URL with proper path handling."""
        if self.database_url.startswith("sqlite"):
            # Convert relative path to absolute for SQLite
            db_path = self.database_url.replace("sqlite:///", "")
            if not os.path.isabs(db_path):
                db_path = os.path.join(os.getcwd(), db_path)
            return f"sqlite:///{db_path}"
        return self.database_url
    
    def ensure_directories(self):
        """Ensure required directories exist."""
        directories = [
            os.path.dirname(self.log_file),
            self.chroma_persist_directory,
            os.path.dirname(self.google_credentials_path),
            os.path.dirname(self.google_token_path),
        ]
        
        for directory in directories:
            if directory:
                Path(directory).mkdir(parents=True, exist_ok=True)


# Global settings instance
settings = Settings()

# Ensure directories exist on import
settings.ensure_directories() 