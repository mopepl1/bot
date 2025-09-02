import json
from pyrogram import Client, filters

@Client.on_message(filters.command("aban", [".", "/"]))
async def ban_user(client, message):
    try:
        # Get the user ID of the message sender
        user_id = str(message.from_user.id)
        
        # Load the owner IDs from the configuration file
        with open("FILES/config.json", "r", encoding="utf-8") as config_file:
            OWNER_ID = json.load(config_file)["OWNER_ID"]
        
        # Check if the sender is an authorized owner
        if user_id not in OWNER_ID:
            resp = """<b>You don't have permission to use this command.    
Contact the bot owner @AngelAiSupportBot!</b>"""
            await message.reply_text(resp, message.id)
            return

        # Extract the user ID to be banned
        try:
            ban_user_id = message.text.split(" ")[1]
        except IndexError:
            if message.reply_to_message:
                ban_user_id = str(message.reply_to_message.from_user.id)
            else:
                await message.reply_text("<b>Please specify a user ID to ban or reply to a user's message.</b>", message.id)
                return

        # Read the current banned user IDs
        try:
            with open("FILES/banuser.txt", "r", encoding="utf-8") as file:
                banned_users = file.read().splitlines()
        except FileNotFoundError:
            banned_users = []

        # Check if the user ID is already banned
        if ban_user_id in banned_users:
            await message.reply_text(f"<b>User ID {ban_user_id} is already banned.</b>", message.id)
            return

        # Save the banned user ID to a file
        with open("FILES/banuser.txt", "a", encoding="utf-8") as file:
            file.write(f"{ban_user_id}\n")

        # Send confirmation message
        resp = f"""<b>
User ID {ban_user_id} successfully banned ✅
━━━━━━━━━━━━━━
Total Banned Users: {len(banned_users) + 1}
        </b>"""
        await message.reply_text(resp, message.id)
    
    except Exception as e:
        import traceback
        traceback_details = traceback.format_exc()
        await message.reply_text(f"<b>An error occurred:</b>\n<pre>{traceback_details}</pre>", message.id)














import json
from pyrogram import Client, filters

@Client.on_message(filters.command("rban", [".", "/"]))
async def remove_ban_user(client, message):
    try:
        # Get the user ID of the message sender
        user_id = str(message.from_user.id)
        
        # Load the owner IDs from the configuration file
        with open("FILES/config.json", "r", encoding="utf-8") as config_file:
            OWNER_ID = json.load(config_file)["OWNER_ID"]
        
        # Check if the sender is an authorized owner
        if user_id not in OWNER_ID:
            resp = """<b>You don't have permission to use this command.    
Contact the bot owner @AngelAiSupportBot!</b>"""
            await message.reply_text(resp, message.id)
            return

        # Extract the user ID to be unbanned
        try:
            unban_user_id = message.text.split(" ")[1]
        except IndexError:
            if message.reply_to_message:
                unban_user_id = str(message.reply_to_message.from_user.id)
            else:
                await message.reply_text("<b>Please specify a user ID to unban or reply to a user's message.</b>", message.id)
                return

        # Read the current banned user IDs
        try:
            with open("FILES/banuser.txt", "r", encoding="utf-8") as file:
                banned_users = file.read().splitlines()
        except FileNotFoundError:
            await message.reply_text("<b>The ban list is empty. No users to unban.</b>", message.id)
            return

        # Check if the user ID exists in the ban list
        if unban_user_id not in banned_users:
            await message.reply_text(f"<b>User ID {unban_user_id} is not in the ban list.</b>", message.id)
            return

        # Remove the user ID from the ban list
        banned_users.remove(unban_user_id)
        with open("FILES/banuser.txt", "w", encoding="utf-8") as file:
            file.write("\n".join(banned_users) + "\n")

        # Send confirmation message
        resp = f"""<b>
User ID {unban_user_id} successfully unbanned ✅
━━━━━━━━━━━━━━
Total Banned Users: {len(banned_users)}
        </b>"""
        await message.reply_text(resp, message.id)
    
    except Exception as e:
        import traceback
        traceback_details = traceback.format_exc()
        await message.reply_text(f"<b>An error occurred:</b>\n<pre>{traceback_details}</pre>", message.id)
