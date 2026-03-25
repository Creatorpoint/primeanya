from pyrogram import filters
from config import OWNER_ID
from db.database import mods

def register(app):

    @app.on_message(filters.command("addmod") & filters.user(OWNER_ID))
    async def add_mod(client, message):
        user_id = int(message.command[1])
        await mods.insert_one({"user_id": user_id})
        await message.reply("✅ Mod Added")

    @app.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
    async def broadcast(client, message):
        from db.database import groups

        if not message.reply_to_message:
            return await message.reply("Reply to message")

        async for g in groups.find():
            try:
                await message.reply_to_message.copy(g["group_id"])
            except:
                pass

        await message.reply("✅ Broadcast Done")
