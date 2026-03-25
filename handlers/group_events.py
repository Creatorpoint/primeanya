from pyrogram import filters
from db.database import stats

def register(app):

    @app.on_message(filters.new_chat_members)
    async def join(client, message):
        await stats.update_one(
            {"group_id": message.chat.id},
            {"$inc": {"joins": 1}},
            upsert=True
        )

    @app.on_message(filters.left_chat_member)
    async def leave(client, message):
        await stats.update_one(
            {"group_id": message.chat.id},
            {"$inc": {"leaves": 1}},
            upsert=True
        )
