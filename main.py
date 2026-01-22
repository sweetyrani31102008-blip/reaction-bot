import random
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

BOT_TOKEN = "8349318064:AAGdBJFyf-9Ll5n3yOTpN3YWqXq1OOe2PeI"

EMOJIS = [
    "🔥", "❤️", "😂", "👍", "😎",
    "👀", "💀", "⚡", "🤯", "👑",
    "👏", "🙌", "😱", "💯", "🤣"
]

async def react(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        reactions = random.sample(EMOJIS, 5)
        await context.bot.set_message_reaction(
            chat_id=update.effective_chat.id,
            message_id=update.message.message_id,
            reaction=reactions
        )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, react))
app.run_polling()
