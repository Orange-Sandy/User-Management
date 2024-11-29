from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configuration settings for the application."""

    model_config = SettingsConfigDict(env_file="./.env", env_file_encoding="utf-8", case_sensitive=True, extra="allow")

    # MONGODB
    MONGODB_URL: str
    MONGODB_DB: str
    MONGO_HOST: str
    MONGO_PORT: str
    
    SECRET_KEY: str


def get_settings(env: str = "local") -> Settings:
    """
    Return the settings object based on the environment.

    Parameters
    ----------
        env (str): The environment to retrieve the settings for. Defaults to "dev".

    Returns
    -------
        Settings: The settings object based on the environment.

    Raises
    ------
        ValueError: If the environment is invalid.
    """
    return Settings()  # type: ignore  # noqa: PGH003


settings = get_settings()
CONFIG_SETTINGS = Settings()
