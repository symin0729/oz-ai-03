# Configuration(구성, 설정) 파일
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str

    class Config:
        # 환경변수 파일(.env)에서 설정값을 읽어올 수 있게 해주는 옵션
        env_file = ".env"
    
settings = Settings()
# 바로 .env 파일에서 openai_api_key 값을 읽어올 수 있다.
settings.openai_api_key