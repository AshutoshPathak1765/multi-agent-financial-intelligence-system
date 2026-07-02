from sqlalchemy.ext.asyncio import AsyncSession,async_sessionmaker,create_async_engine
from app.core.config import DATABASE_URL
import ssl
from pathlib import Path

# print("DATABASE_URL =", DATABASE_URL)

BASE_DIR = Path(__file__).resolve().parent.parent


# print("Creating engine...")

engine = create_async_engine(
   DATABASE_URL,
   echo=True,
)


AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# from sqlalchemy import text
# import asyncio


# async def test_connection():
#     async with engine.begin() as conn:
#         result = await conn.execute(text("SELECT 1"))
#         print("Connected:", result.scalar())


# if __name__ == "__main__":
#     asyncio.run(test_connection())