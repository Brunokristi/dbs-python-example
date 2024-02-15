from fastapi import APIRouter
import asyncpg

from dbs_assignment.config import settings

router = APIRouter()


@router.get("/v1/status")
async def get_database_status():
    conn = await asyncpg.connect(
        user=settings.DATABASE_USER,
        password=settings.DATABASE_PASSWORD,
        database=settings.DATABASE_NAME,
        host=settings.DATABASE_HOST,
        port=settings.DATABASE_PORT
    )
    version = await conn.fetchval("SELECT version();")
    await conn.close()

    return {"version": version}