from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings

# Postgres
pg_engine = create_engine(settings.postgres_url)
PgSession = sessionmaker(bind=pg_engine)

# MySQL
mysql_engine = create_engine(settings.mysql_url)
MysqlSession = sessionmaker(bind=mysql_engine)

# Oracle
oracle_engine = create_engine(settings.oracle_url)
OracleSession = sessionmaker(bind=oracle_engine)

def get_pg_db():
    db = PgSession()
    try:
        yield db
    finally:
        db.close()

def get_mysql_db():
    db = MysqlSession()
    try:
        yield db
    finally:
        db.close()

def get_oracle_db():
    db = OracleSession()
    try:
        yield db
    finally:
        db.close()