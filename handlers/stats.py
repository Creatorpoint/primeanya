from pyrogram import filters
from db.database import stats

def register(app):

    @app.on_message(filters.command("stats"))
    async def show_stats(client, message):
        data = await stats.find_one({"group_id": message.chat.id})

        if not data:
            return await message.reply("No data yet")

        text = f"""
📊 Group Stats:

👥 Joins: {data.get('joins',0)}
🚪 Leaves: {data.get('leaves',0)}
"""

        await message.reply(text)
