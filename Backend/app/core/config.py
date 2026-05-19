from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL:str
    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_EMAIL: str
    SMTP_PASSWORD: str
    OTP_EXPIRY_SECONDS: int
    SERPAPI_KEY:str

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
