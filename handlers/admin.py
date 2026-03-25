from pyrogram import filters
from config import OWNER_ID
from db.database import groups

def register(app):

    @app.on_message(filters.command("addgroup") & filters.user(OWNER_ID))
    async def add_group(client, message):
        try:
            group_id = int(message.command[1])
            await groups.insert_one({"group_id": group_id})

            await message.reply("✅ Group Added")
        except:
            await message.reply("❌ Usage: /addgroup -100xxxx")
