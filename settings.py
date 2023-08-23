import os
from environs import Env
from pydantic import BaseModel, BaseSettings, Field

env = Env()
env.read_env()


class TestUser(BaseModel):
    login: str
    password: str


class Settings(BaseSettings):
    base_url: str = os.getenv('BASE_URL')
    user_login: str = os.getenv('TEST_USER_LOGIN')
    user_password: str = os.getenv('TEST_USER_PASSWORD')

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

    @property
    def api_url(self) -> str:
        return f'{self.base_url}/futurama'

    @property
    def user(self) -> TestUser:
        return TestUser(
            login=self.user_login,
            password=self.user_password
        )


base_settings = Settings()
