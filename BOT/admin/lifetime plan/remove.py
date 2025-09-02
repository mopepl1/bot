import traceback
import json
from pyrogram import Client, filters
from FUNC.usersdb_func import *


async def freeuser(user_id):
    try:
        usersdb.update_one({"id": user_id}, {
            "$set": {
                "status": "FREE",
                "credit": "0",
                "plan": "N/A",
                "expiry": "N/A"
            }
        })

    except Exception as e:
        await error_log(traceback.format_exc())


@Client.on_message(filters.command("rm", [".", "/"]))
async def cmd_rm(Client, message):
    try:
        user_id = str(message.from_user.id)
        OWNER_ID = json.loads(
            open("FILES/config.json", "r", encoding="utf-8").read())["OWNER_ID"]

        if user_id not in OWNER_ID:
            resp = """<b>Privilege Not Found ⚠️

Message: To perform this action, you need admin level power. 

Contact @AngelAiSupportBot For More Info ✅</b>"""
            await message.reply_text(resp, message.id)
            return

        try:
            if message.reply_to_message:
                user_id = str(message.reply_to_message.from_user.id)
            else:
                user_id = str(message.text.split(" ")[1])
        except Exception as e:
            resp = """<b>
Invalid ID ⚠️

Message: Not Found Valid ID From Your Input.
            </b>"""
            await message.reply_text(resp, message.id)
            return

        pm_chk = await getuserinfo(user_id)
        status = str(pm_chk["status"])
        credit = int(pm_chk["credit"])

        resp = f"""<b>
        
User Information ⚙️
━━━━━━━━━━━━
User ID: {user_id}
Status: {status}
Credit Balance: {credit}

Message: This user's information has been retrieved.
</b>"""
        await message.reply_text(resp, message.id)

        if credit > 0:
            await directcredit(user_id, 0)
            resp = f"""
All Credit Removed ✅

User ID: {user_id}

Message: All credit has been removed from the user's account.
            """
            await message.reply_text(resp, message.id)

            user_sms = f"""<b>
Credit Removed ❌
━━━━━━━━━━━━━━
● User ID: {user_id}

Message: Sorry! Due to Some Suspicious or Wrong Behavior, Your all credit has been removed from your account.
            </b>"""
            try:
                await Client.send_message(user_id, user_sms)
            except:
                pass

        if status in ["LIFETIME", "PREMIUM", "OWNER"]:
            await freeuser(user_id)
            resp = f"""
Account Demoted ✅

User ID: {user_id}

Message: Account Demoted to "Free" User Successfully.
            """
            await message.reply_text(resp, message.id)

            user_resp = f"""<b>
Account Demoted ❌
━━━━━━━━━━━━━━
● User ID: {user_id}
● Role: Free

Message: Sorry! Due to Some Suspicious or Wrong Behavior, Your Account got Demoted to "Free" User.
            </b>"""
            try:
                await Client.send_message(user_id, user_resp)
            except:
                pass

    except Exception as e:
        await error_log(traceback.format_exc())
