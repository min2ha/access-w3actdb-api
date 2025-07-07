from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

SQLALCHEMY_DATABASE_URI = "sqlite:///example.db"

SQLALCHEMY_ACTDB_URI = "postgresDB"


#postgresql
enginePostgres = create_engine(
    SQLALCHEMY_ACTDB_URI,
    echo=True
)

#sqlite
engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    # required for sqlite ? 
    # check source code?
    connect_args={"check_same_thread": False}
)

Base = declarative_base()

#postgreSQL
connection = enginePostgres.raw_connection()
cursor = connection.cursor()

Base.metadata.create_all(enginePostgres)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=enginePostgres)
