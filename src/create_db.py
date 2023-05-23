from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

engine = create_engine('postgresql://postgres:12345@localhost:5432/pav')
Base.metadata.create_all(engine)