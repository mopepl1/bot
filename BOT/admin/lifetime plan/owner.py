import json
from pyrogram import Client, filters
from FUNC.usersdb_func import *
from mongodb import client, usersdb


async def owner(user_id, amt):
    try:
        prev = {"id": f"{user_id}"}
        nextt = {"$set": {f"status": f"OWNER"}}
        usersdb.update_one({"id": user_id}, {
                       "$set": {"plan": "OWNER ∞"}})
        update = usersdb.update_one(prev, nextt)
        prev = {"id": f"{user_id}"}
        nextt = {"$set": {f"credit": f"{amt}"}}
        update = usersdb.update_one(prev, nextt)
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")


@Client.on_message(filters.command("ow", [".", "/"]))
async def cmd_owner(Client, message):
    try:
        user_id = str(message.from_user.id)
        OWNER_ID = json.loads(
            open("FILES/config.json", "r", encoding="utf-8").read())["OWNER_ID"]
        if user_id not in OWNER_ID:
            resp = """<b>You Don't Have Permission To Use This Command.    
Contact Bot Owner @AngelAiSupportBot !</b>"""
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
        else:
            await owner(user_id, 1000000)
            resp = f"""<b>
Owner Plan Successfully ✅ 
━━━━━━━━━━━━━━
User ID : <a href="tg://user?id={user_id}"> {user_id}</a> 
Role : Owner

Status : Successfull
    </b> """
            await message.reply_text(resp, message.id)

            user_resp = f"""<b>
Owner Plan Successfully ✅ 
━━━━━━━━━━━━━━ 
User ID: {user_id} 
Role: Owner

Message: Congratz ! Your Account Successfully Promoted To "Owner" User . Enjoy Yourself on the Bot .
    </b> """
            await Client.send_message(user_id, user_resp)

    except Exception as e:
        await message.reply_text(e, message.id)
        import traceback
        await error_log(traceback.format_exc())
