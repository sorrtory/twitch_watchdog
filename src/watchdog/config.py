from typing import List, Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Import .env variables
    """

    vk_token: str
    vk_group_id: int
    vk_write_to: List[int]

    twitch_user_login: str
    twitch_access_token: Optional[str] = None
    twitch_app_id: Optional[str] = None

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()  # pyright: ignore
