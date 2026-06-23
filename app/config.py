from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional

class Settings(BaseSettings):
    app_name: str = "AI Teaching Assistant"
    gemini_api_key: Optional[str] = Field(default=None, env="GEMINI_API_KEY")
    default_llm_provider: str = "gemini"
    class Config:
        env_file = ".env"

settings = Settings()