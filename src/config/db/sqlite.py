from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from ..environment.read_env import DB_URL, TURSO_AUTH_TOKEN

engine = create_engine(f"sqlite+{DB_URL}/?authToken={TURSO_AUTH_TOKEN}&secure=true", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
