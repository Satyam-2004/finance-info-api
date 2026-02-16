from sqlalchemy import create_engine, String, Integer, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker

engine = create_engine("sqlite:///mydb.db", echo=True)

SessionLocal = sessionmaker(bind=engine)
    