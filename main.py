import asyncio
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import register_all_handlers
import web
from web_panel.app import start_web

app = Client(
    "PrimeBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

register_all_handlers(app)

async def main():
    await app.start()
    print("✅ Bot Started")

    start_web()  # web panel start

    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
