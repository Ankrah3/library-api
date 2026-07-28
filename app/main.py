from fastapi import FastAPI
from app.routers import postgres_router, mysql_router, oracle_router, mongo_router

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