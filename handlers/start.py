from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def register(app):

    @app.on_message(filters.command("start"))
    async def start(client, message):
        buttons = InlineKeyboardMarkup([
            [InlineKeyboardButton("📊 Dashboard", callback_data="dashboard")],
            [InlineKeyboardButton("➕ Add Group", callback_data="add_group")]
        ])

        await message.reply_text(
            "👋 Welcome to Prime Analytics Bot",
            reply_markup=buttons
        )
