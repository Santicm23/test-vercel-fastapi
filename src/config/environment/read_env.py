import os

from dotenv import load_dotenv

load_dotenv()


def read_env(key: str, default: str | None = None) -> str:
    value = os.getenv(key)
    if value is None:
        if default is None:
            raise ValueError(f"Environment variable {key} is required")
        return default
    return value


ENVIRONMENT = read_env("ENVIRONMENT", "dev")
PORT = int(read_env("PORT", "3000"))
JWT_SECRET = read_env("JWT_SECRET")
DB_URL = read_env("DB_URL")
