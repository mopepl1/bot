from pyrogram import Client, filters

MESSAGE = """<b>
👋 Hey {name}!
Welcome to our group ❤️

📜 Please follow some rules:
1. 🚫 Don't send unwanted links.
2. 🚫 Don't spam.
3. 🚫 Promotion of your channel is prohibited.

✅ Just press /register once to continue using me 🥰
</b>"""

@Client.on_message(filters.new_chat_members)
async def welcome(client, message):
    try:
        new_members = [u.mention for u in message.new_chat_members]
        names = ", ".join(new_members)
        text = MESSAGE.format(name=names)

        await message.reply_text(text, quote=True)
    except Exception:
        pass
