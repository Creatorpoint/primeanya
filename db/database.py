from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL

client = AsyncIOMotorClient(MONGO_URL)
db = client["prime_bot"]

groups = db["groups"]
stats = db["stats"]
