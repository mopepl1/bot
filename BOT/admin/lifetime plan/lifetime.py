import json
from pyrogram import Client, filters
from FUNC.usersdb_func import *


@Client.on_message(filters.command("lifetime", [".", "/"]))
async def cmd_plan2(Client, message):
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

        paymnt_method = "CRYPTO/BINANCE"
        registration_check = await getuserinfo(user_id)
        registration_check = str(registration_check)
        if registration_check == "None":
            resp = f"""<b>
Lifetime Plan Activation Failed ❌
━━━━━━━━━━━━━━
User ID : <a href="tg://user?id={user_id}"> {user_id}</a> 
Plan Name: Lifetime Plan
Reason : Unregistered Users

Status : Failed
</b>"""
            await message.reply_text(resp, message.id)
            return

        await check_negetive_credits(user_id)
        await get_lifetime_plan(user_id)
        receipt_id = await randgen(len=10)
        gettoday = str(date.today()).split("-")
        yy = gettoday[0]
        mm = gettoday[1]
        dd = gettoday[2]
        today = f"{dd}-{mm}-{yy}"

        user_resp = f"""<b>
Thanks For Purchasing Our Lifetime Plan ✅

ID : <code>{user_id}</code>
Plan : Lifetime Plan
Price : 100$
Purchase Date: {today}
Validity: Lifetime
Status : Paid ☑️
Payment Method : {paymnt_method}.
Receipt ID : ANGEL-{receipt_id}

This is a receipt for your plan.saved it in a Secure Place.This will help you if anything goes wrong with your plan purchases .

Have a Good Day .
- @AngelAiSupportBot
</b>"""
        try:
            await Client.send_message(user_id, user_resp)
        except:
            pass

        ad_resp = f"""<b>
Lifetime Plan Activated ✅ 
━━━━━━━━━━━━━━
User ID : <a href="tg://user?id={user_id}"> {user_id}</a> 
Plan Name: Lifetime Plan 
Plan Expiry: Lifetime

Status : Successfull
        </b>"""
        await message.reply_text(ad_resp, message.id)

    except:
        import traceback
        await error_log(traceback.format_exc())
