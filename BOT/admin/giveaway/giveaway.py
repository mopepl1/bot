import json
import os
import random
from pyrogram import Client, filters
from FUNC.usersdb_func import *


@Client.on_message(filters.command("join", [".", "/"]))
async def addbrod(Client, message):
    try:
        user_id = str(message.from_user.id)
        user_name = message.from_user.username if message.from_user.username else "NoUsername"
        text = ' '.join(message.command[1:])  # Get the text after the command

        # Ensure join.txt exists
        if not os.path.exists('FILES/join.txt'):
            with open('FILES/join.txt', 'w', encoding="UTF-8") as f:
                pass

        with open("FILES/giveaway_user.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            giveaway_code = data.get("CODE", "")

        # Check if the giveaway code is empty
        if not giveaway_code:
            resp = "⚠️ *The giveaway has ended.*"
            await message.reply_text(resp, reply_to_message_id=message.id)
            return

        # Check if the user ID is already in the file
        with open('FILES/join.txt', 'r', encoding="UTF-8") as f:
            if any(user_id in line for line in f):
                resp = "⚠️ *You have already registered for the giveaway.*"
                await message.reply_text(resp, reply_to_message_id=message.id)
                return

        # Check if the text or giveaway code matches
        if text != giveaway_code:
            resp = "⚠️ *Invalid code or text. Please check the giveaway instructions.*"
            await message.reply_text(resp, reply_to_message_id=message.id)
            return

        # Append user ID, user name, and text to join.txt
        with open("FILES/join.txt", "a", encoding="UTF-8") as f:
            f.write(f"{user_id}: {user_name}: {text}\n")

        # Count the total number of lines in the file
        total_lines_count = sum(1 for line in open('FILES/join.txt', 'r', encoding="UTF-8"))

        resp = f"""
🎉 **Giveaway Participation Confirmed** 🎉
━━━━━━━━━━━━━━
{text}
━━━━━━━━━━━━━━
👥 *Total User Count:* `{total_lines_count}`

✅ *You have successfully registered for the giveaway.*
"""
        await message.reply_text(resp, reply_to_message_id=message.id)
        
    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())





@Client.on_message(filters.command("clear", [".", "/"]))
async def clear_join(Client, message):
    try:
        user_id = str(message.from_user.id)
        with open("FILES/giveaway_user.json", "r", encoding="utf-8") as f:
            OWNER_ID = json.load(f)["ADMIN_ID"]

        # print(OWNER_ID)
        if user_id not in OWNER_ID:

            resp = """<b>You Don't Have Permission To Use This Command.    
Contact Bot Owner @AngelAiSupportBot !</b>"""
            await message.reply_text(resp, reply_to_message_id=message.id)
            return
        # Clear the contents of join.txt
        open('FILES/join.txt', 'w', encoding="UTF-8").close()

        resp = "The join list has been cleared."
        await message.reply_text(resp, reply_to_message_id=message.id)
        
    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())





@Client.on_message(filters.command("draw", [".", "/"]))
async def draw_winner(Client, message):
    try:
        user_id = str(message.from_user.id)
        with open("FILES/giveaway_user.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            OWNER_ID = data["ADMIN_ID"]

        # print(OWNER_ID)
        if user_id not in OWNER_ID:

            resp = """<b>You Don't Have Permission To Use This Command.    
Contact Bot Owner @AngelAiSupportBot !</b>"""
            await message.reply_text(resp, reply_to_message_id=message.id)
            return

        if not os.path.exists('FILES/join.txt') or os.path.getsize('FILES/join.txt') == 0:
            await message.reply_text("No participants in the giveaway yet.", reply_to_message_id=message.id)
            return

        with open('FILES/join.txt', 'r', encoding="UTF-8") as f:
            participants = f.readlines()

        winner_line = random.choice(participants)
        winner_user_name = winner_line.split(':')[1].strip()

        resp = f"""
🎉 Giveaway Winner 🎉
━━━━━━━━━━━━━━
The winner of the giveaway is: @{winner_user_name}
━━━━━━━━━━━━━━
Congratulations!
"""
        await message.reply_text(resp, reply_to_message_id=message.id)

        data["CODE"] = ""
        with open("FILES/giveaway_user.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())










@Client.on_message(filters.command("approve", [".", "/"]))
async def approve_admin(Client, message):
    try:
        user_id = str(message.from_user.id)
        OWNER_ID = json.loads(open("FILES/config.json", "r", encoding="utf-8").read())["OWNER_ID"]

        if user_id not in OWNER_ID:
            resp = """<b>You Don't Have Permission To Use This Command.    
Contact Bot Owner @AngelAiSupportBot !</b>"""
            await message.reply_text(resp, reply_to_message_id=message.id)
            return
        
        ADMIN_ID = json.loads(open("FILES/giveaway_user.json", "r", encoding="utf-8").read())["ADMIN_ID"]

        if len(message.command) != 2:
            resp = "Please provide a user ID to approve."
            await message.reply_text(resp, reply_to_message_id=message.id)
            return
        
        new_admin_id = message.command[1]
        
        if not new_admin_id.isdigit():
            resp = "The user ID should be a valid number."
            await message.reply_text(resp, reply_to_message_id=message.id)
            return
        
        with open("FILES/giveaway_user.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        
        if new_admin_id in data["ADMIN_ID"]:
            resp = "This user is already an admin."
            await message.reply_text(resp, reply_to_message_id=message.id)
            return
        
        data["ADMIN_ID"].append(new_admin_id)
        
        with open("FILES/giveaway_user.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        
        resp = f"User ID {new_admin_id} has been successfully approved as an admin."
        await message.reply_text(resp, reply_to_message_id=message.id)

    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())














@Client.on_message(filters.command("remove", [".", "/"]))
async def remove_admin(Client, message):
    try:
        user_id = str(message.from_user.id)
        OWNER_ID = json.loads(open("FILES/config.json", "r", encoding="utf-8").read())["OWNER_ID"]

        if user_id not in OWNER_ID:
            resp = """<b>You Don't Have Permission To Use This Command.    
Contact Bot Owner @AngelAiSupportBot !</b>"""
            await message.reply_text(resp, reply_to_message_id=message.id)
            return
        
        ADMIN_ID = json.loads(open("FILES/giveaway_user.json", "r", encoding="utf-8").read())["ADMIN_ID"]

        if len(message.command) != 2:
            resp = "Please provide a user ID to remove."
            await message.reply_text(resp, reply_to_message_id=message.id)
            return
        
        admin_id_to_remove = message.command[1]
        
        if not admin_id_to_remove.isdigit():
            resp = "The user ID should be a valid number."
            await message.reply_text(resp, reply_to_message_id=message.id)
            return
        
        with open("FILES/giveaway_user.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        
        if admin_id_to_remove not in data["ADMIN_ID"]:
            resp = "This user is not an admin."
            await message.reply_text(resp, reply_to_message_id=message.id)
            return
        
        data["ADMIN_ID"].remove(admin_id_to_remove)
        
        with open("FILES/giveaway_user.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        
        resp = f"User ID {admin_id_to_remove} has been successfully removed as an admin."
        await message.reply_text(resp, reply_to_message_id=message.id)

    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())


















@Client.on_message(filters.command("create", [".", "/"]))
async def create(Client, message):
    try:
        user_id = str(message.from_user.id)
        
        # Load the owner/admin IDs
        with open("FILES/giveaway_user.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            OWNER_ID = data["ADMIN_ID"]

        # Check if the user has permission
        if user_id not in OWNER_ID:
            resp = """<b>You Don't Have Permission To Use This Command.    
Contact Bot Owner @AngelAiSupportBot !</b>"""
            await message.reply_text(resp, reply_to_message_id=message.id)
            return

        # Generate a new giveaway code
        new_code = ' '.join(message.command[1:]) 

        # Save the new code to the JSON file
        data["CODE"] = new_code
        with open("FILES/giveaway_user.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        # Prepare response message with better UI
        from datetime import datetime
        giveaway_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        creator_username = message.from_user.username or "Unknown"
        
        resp = (
            f"<b>🎉 New Giveaway Created! 🎉</b>\n\n"
            f"<b>🗓 Date:</b> <code>{giveaway_date}</code>\n"
            f"<b>🔑 Giveaway Code:</b> <code>{new_code}</code>\n"
            f"<b>👤 Created by:</b> @{creator_username}\n\n"
            f"<b>📢 How to Join:</b> Use the command <code>/join {new_code}</code> to participate in the giveaway.\n\n"
            f"Good luck to all participants!"
        )
        
        await message.reply_text(resp, reply_to_message_id=message.id)
    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())
