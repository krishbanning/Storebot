from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_DB_URI
from ..logging import LOGGER
import asyncio

LOGGER(__name__).info("Connecting to your Mongo Database...")

try:
    # serverSelectionTimeoutMS: Agar 5 seconds me connect nahi hua toh error de dega
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI, serverSelectionTimeoutMS=5000)
    
    # Connection ko verify karne ke liye 'ping' karna zaroori hai
    _mongo_async_.admin.command('ping')
    
    mongodb = _mongo_async_.Anon
    LOGGER(__name__).info("Success: Connected to your Mongo Database.")

except Exception as e:
    LOGGER(__name__).error(f"Failed to connect to Mongo Database!")
    LOGGER(__name__).error(f"Error Details: {e}")
    
    # Hosting pe aksar IP whitelist ka issue hota hai
    if "selection timeout" in str(e).lower():
        LOGGER(__name__).error("Tip: Check if your IP is whitelisted on MongoDB Atlas (Allow access from 0.0.0.0/0)")
    
    exit()
