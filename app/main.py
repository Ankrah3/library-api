from fastapi import FastAPI
from app.routers import postgres_router, mysql_router, oracle_router, mongo_router
from app.database import pg_engine, mysql_engine, oracle_engine
from app.models import Base

app = FastAPI(
    title="Library Multi-DB API",
    description="Demonstrates a single backend reading/writing to PostgreSQL, MySQL, Oracle XE, and MongoDB",
    version="1.0.0"
)

app.include_router(postgres_router.router)
app.include_router(mysql_router.router)
app.include_router(oracle_router.router)
app.include_router(mongo_router.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}

# Create tables on startup if engines are ready
for engine, db_name in [
    (pg_engine, "PostgreSQL"),
    (mysql_engine, "MySQL"),
    (oracle_engine, "Oracle")
]:
    try:
        Base.metadata.create_all(bind=engine)
        print(f"Successfully initialized {db_name} tables.")
    except Exception as e:
        print(f"Skipping {db_name} initialization for now (not ready yet): {e}")
