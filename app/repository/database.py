from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/postgres")
SessionLocal = sessionmaker(autoflush=False, bind=engine)
Base = declarative_base()
