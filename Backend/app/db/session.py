from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
# Create the SQLAlchemy engine
engine=create_engine(settings.DATABASE_URL)
# Create a configured "Session" class
Session_Local=sessionmaker(autocommit=False,autoflush=False,bind=engine)
# Dependency to get DB session
def get_db():
    db=Session_Local()
    try: 
        yield db
    finally:
        db.close()