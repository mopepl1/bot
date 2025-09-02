from FUNC.usersdb_func import *
import time
from FUNC.defs import *



async def check_all_thingtemp(Client, message):
    try:
        from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

        user_id = str(message.from_user.id)
        chat_type = str(message.chat.type)
        chat_id = str(message.chat.id)
        regdata = await getuserinfo(user_id)
        regdata = str(regdata)

        gate_active = json.loads(open("FILES/deadsk.json", "r", encoding="utf-8").read())["gate_active"]

        with open("FILES/banuser.txt", "r", encoding="UTF-8") as file:
            banned_users = file.read().splitlines()

        if user_id in banned_users:
            await message.reply_text(
                "<b>You are banned from using this bot. Contact support for assistance. @AngelAiSupportBot</b>",
                reply_to_message_id=message.id
            )
            return False, False, False

        if regdata == "None":
            resp = f"""<b>
Unregistered Users ⚠️

Message: You Can't Use Me Unless You Register First.

Type /register to Continue
</b>"""
            await message.reply_text(resp, reply_to_message_id=message.id)
            return False, False, False

        if any(command in message.text for command in gate_active):
            resp = "<b>This gate not available now, please try later 👍</b>"
            await message.reply_text(resp, reply_to_message_id=message.id)
            return False, False, False

        getuser = await getuserinfo(user_id)
        status = getuser["status"]
        credit = int(getuser["credit"])
        antispam_time = int(getuser["antispam_time"])
        now = int(time.time())
        count_antispam = now - antispam_time
        checkgroup = await getchatinfo(chat_id)
        checkgroup = str(checkgroup)

        supertgroup = await getsuperchatinfo(chat_id)
        supertgroup = str(supertgroup)
        await plan_expirychk(supertgroup)

        # Handle supergroups (superchat) for FREE users
        if chat_type in ["ChatType.GROUP", "ChatType.SUPERGROUP"] and supertgroup != "None":
            if status == "FREE":
                # Check antispam for FREE users in supergroups
                if count_antispam < 20:
                    after = 20 - count_antispam
                    resp = f"""<b>
Antispam Detected ⚠️

Message: You Are Acting Too Quickly. Please Try Again After {after}s.

Reduce Antispam Time by /buy Using a Paid Plan.
</b>"""
                    await message.reply_text(resp, reply_to_message_id=message.id)
                    return False, False, False

                # Update antispam_time for FREE users after passing the check
                await setantispamtime(user_id)

            # PREMIUM users in supergroups can proceed without antispam restrictions
            return True, status, credit

        else:
            # Handle private chats for FREE users
#             if chat_type == "ChatType.PRIVATE" and status == "FREE":
#                 resp = """<b>
# Premium Users Required ⚠️

# Message: Only Premium Users are Allowed to use the bot in Personal Chats. However, you can use the bot for free here: https://t.me/freeangelai
# Buy a Premium Plan using /buy to continue.
# </b>"""
#                 await message.reply_text(resp, reply_to_message_id=message.id)
#                 return False, False, False

            # Handle unauthorized groups
            if chat_type in ["ChatType.GROUP", "ChatType.SUPERGROUP"] and checkgroup == "None":
                resp = """<b>
Unauthorized Chats ⚠️

Message: Only Chats Approved By My Master Can Use Me. To Get Your Chat Approved, Follow These Steps:

Type /howgp to Know the Steps.
</b>"""
                await message.reply_text(resp, reply_to_message_id=message.id)
                return False, False, False

            # Check credits
            if credit < 5:
                resp = """<b>
Insufficient Credits ⚠️

Message: You Have Insufficient Credits to Use Me. Recharge Your Credits to Continue Using the Bot.

Type /buy to Recharge.
</b>"""
                await message.reply_text(resp, reply_to_message_id=message.id)
                return False, False, False

            # Check antispam for PREMIUM users
            if status == "PREMIUM" and count_antispam < 5:
                after = 5 - count_antispam
                resp = f"""<b>
Antispam Detected ⚠️

Message: You Are Acting Too Quickly. Please Try Again After {after}s.

Reduce Antispam Time by /buy Using a Paid Plan.
</b>"""
                await message.reply_text(resp, reply_to_message_id=message.id)
                return False, False, False

            # Check antispam for FREE users (non-supergroup)
            if status == "FREE" and count_antispam < 20:
                after = 20 - count_antispam
                resp = f"""<b>
Antispam Detected ⚠️

Message: You Are Acting Too Quickly. Please Try Again After {after}s.

Reduce Antispam Time by /buy Using a Paid Plan.
</b>"""
                await message.reply_text(resp, reply_to_message_id=message.id)
                return False, False, False

            # Update antispam_time for FREE users after passing the check (non-supergroup)
            if status == "FREE":
                await setantispamtime(user_id)

        # If all checks pass, return True, status, and credit
        return True, status, credit

    except Exception:
        # Handle unexpected errors
        import traceback
        await error_log(traceback.format_exc())
        try:
            await message.reply_text("Try Again Later.", reply_to_message_id=message.id)
        except:
            pass
        return False, False, False









async def check_some_thing(Client , message):
    try:
        user_id   = str(message.from_user.id)
        chat_type = str(message.chat.type)
        chat_id   = str(message.chat.id)
        regdata   = await getuserinfo(user_id)
        regdata   = str(regdata)
        if regdata == "None":
            resp = f"""<b>
Unregistered Users ⚠️

Message: You Can't Use Me Unless You Register First .

Type /register to Continue
</b>"""
            await message.reply_text(resp ,  reply_to_message_id = message.id)
            return False , False

        getuser    = await getuserinfo(user_id)
        status     = getuser["status"]
        checkgroup = await getchatinfo(chat_id)
        checkgroup = str(checkgroup)
        await plan_expirychk(user_id)

        if chat_type == "ChatType.PRIVATE" and status == "FREE":
            resp = """<b>
Premium Users Required ⚠️

Message: Only Premium Users are Allowed to use bot in Personal . Although You Can Use Bot Free Here https://t.me/AngelAi_Stuffs
Buy Premium Plan Using /buy to Continue
</b>"""
            await message.reply_text(resp , message_id=message.id)
            return False , False

        if (
            chat_type == "ChatType.GROUP"
            or chat_type == "ChatType.SUPERGROUP"
            and checkgroup == "None"
        ):
            resp = f"""<b>
Unauthorized Chats ⚠️

Message: Only Chats Approved By My Master Can Only Use Me . To Get Approved Your Chats Follow The Steps .

Type /howgp to Know The Step
</b>"""
            await message.reply_text(resp ,  reply_to_message_id = message.id)
            return False , False

        return True , status

    except:
        import traceback
        await error_log(traceback.format_exc())
        try:
            await message.reply_text("Try Again later" ,  reply_to_message_id = message.id)
        except:
            pass
        return False , False


