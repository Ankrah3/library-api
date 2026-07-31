import time
import statistics
from sqlalchemy import create_engine, text
import os

def time_query(fn, runs=10):
    times = []
    for _ in range(runs):
        start = time.perf_counter()
        try:
            fn()
        except Exception as e:
            print(f"  Error during run: {e}")
            continue
        times.append((time.perf_counter() - start) * 1000)  # ms
    if not times:
        return {"error": "all runs failed"}
    return {
        "min_ms": round(min(times), 2),
        "max_ms": round(max(times), 2),
        "avg_ms": round(statistics.mean(times), 2),
        "runs_completed": len(times)
    }

# Read from environment (same vars your app uses)
POSTGRES_URL = os.environ.get("POSTGRES_URL")
MYSQL_URL = os.environ.get("MYSQL_URL")

if POSTGRES_URL:
    pg_engine = create_engine(POSTGRES_URL)
    def pg_query():
        with pg_engine.connect() as conn:
            conn.execute(text("SELECT 1"))
    print("PostgreSQL (Supabase):", time_query(pg_query))
else:
    print("POSTGRES_URL not set")

if MYSQL_URL:
    mysql_engine = create_engine(MYSQL_URL, connect_args={"ssl": {"ssl_disabled": False}})
    def mysql_query():
        with mysql_engine.connect() as conn:
            conn.execute(text("SELECT 1"))
    print("MySQL (Aiven):", time_query(mysql_query))
else:
    print("MYSQL_URL not set")