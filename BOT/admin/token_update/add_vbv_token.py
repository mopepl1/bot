import json
from pyrogram import Client, filters
from FUNC.defs import *



@Client.on_message(filters.command("addvbvtoken", [".", "/"]))
async def addbrod(Client, message):
    try:
        user_id     = str(message.from_user.id)
        OWNER_ID    = json.loads(open("FILES/config.json", "r" , encoding="utf-8").read())["OWNER_ID"]
        if user_id not in OWNER_ID:
            resp = """<b>You Don't Have Permission To Use This Command.    
Contact Bot Owner @AngelAiSupportBot !</b>"""
            await message.reply_text(resp, message.id)
            return

        VBV_TOKEN = str(message.reply_to_message.text).split('"dfReferenceId":"')[1].split('"')[0]
        clear_file = open('FILES/vbv_token.txt', 'w',encoding="UTF-8").close()
        with open("FILES/vbv_token.txt", "a",encoding="UTF-8") as f:
                f.write(VBV_TOKEN)

        # await update_token("VBV_TOKEN", VBV_TOKEN)


        resp = f"""<b>
VBV_TOKEN Successfully Added ✅
━━━━━━━━━━━━━━
{VBV_TOKEN}

Status: Successfull
    </b>"""
        await message.reply_text(resp, message.id)

    except:
        import traceback
        await error_log(traceback.format_exc())










import json
from pyrogram import Client, filters
from FUNC.defs import *



@Client.on_message(filters.command("adddonation", [".", "/"]))
async def adddonation(Client, message):
    try:
        user_id     = str(message.from_user.id)
        OWNER_ID    = json.loads(open("FILES/config.json", "r" , encoding="utf-8").read())["OWNER_ID"]
        if user_id not in OWNER_ID:
            resp = """<b>You Don't Have Permission To Use This Command.    
Contact Bot Owner @AngelAiSupportBot !</b>"""
            await message.reply_text(resp, message.id)
            return

        donation_id_list = str(message.reply_to_message.text)
        clear_file = open('FILES/donation_id_list.txt', 'w',encoding="UTF-8").close()
        with open("FILES/donation_id_list.txt", "a",encoding="UTF-8") as f:
                f.write(donation_id_list)

        # await update_token("VBV_TOKEN", VBV_TOKEN)


        resp = f"""<b>
VBV_TOKEN Successfully Added ✅
━━━━━━━━━━━━━━
{donation_id_list}

Status: Successfull
    </b>"""
        await message.reply_text(resp, message.id)

    except:
        import traceback
        await error_log(traceback.format_exc())
