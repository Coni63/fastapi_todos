import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

import envs

engine = create_engine(os.environ.get("CONNECTION_STR"))
SessionLocal = sessionmaker(autoflush=False, bind=engine)
Base = declarative_base()
