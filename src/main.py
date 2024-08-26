import uvicorn

from .config.docs import load_metadata
from .server import app


def main(dev: bool = False) -> None:
    load_metadata(app)

    uvicorn.run(f"{__package__}.main:app", reload=dev)


if __name__ == "__main__":
    main(True)
