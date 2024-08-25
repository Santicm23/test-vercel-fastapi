from importlib.metadata import metadata, version

from fastapi import FastAPI

__project__ = "test-vercel-fastapi"


def load_metadata(app: FastAPI) -> None:
    app.title = metadata(__project__)["name"]
    app.description = metadata(__project__)["description"]
    app.version = version(__project__)