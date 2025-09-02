# import time
# import httpx
# import threading
# import asyncio
# import json
# from pyrogram import Client, filters
# from datetime import timedelta
# from .gate import *
from .response import *
# from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from FUNC.usersdb_func import *
# from TOOLS.check_all_func import *
# from TOOLS.getcc_for_txt import *


# async def get_checked_done_response(Client, message, ccs,  key, hitsfile, start, stats, role, hits_count, chk_done):
#     try:
#         taken = str(timedelta(seconds=time.perf_counter() - start))
#         hours, minutes, seconds = map(float, taken.split(":"))
#         hour = int(hours)
#         min = int(minutes)
#         sec = int(seconds)
#         if hits_count != 0:
#             await Client.delete_messages(message.chat.id, stats.id)
#             text = f"""
# - 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 - Stripe Auth♻️

# - 𝐓𝐨𝐭𝐚𝐥 𝐂𝐂 𝐈𝐧𝐩𝐮𝐭 - {len(ccs)}
# - 𝐀𝐩𝐩𝐫𝐨𝐯𝐞: {hits_count} 
# - 𝐃𝐞𝐚𝐝: { chk_done - hits_count }
# - 𝐓𝐨𝐭𝐚𝐥 𝐂𝐡𝐞𝐜𝐤𝐞𝐝: {chk_done}
# - 𝐒𝐞𝐜𝐫𝐞𝐭 𝐊𝐞𝐲: <code>{key}</code>
# - 𝐒𝐭𝐚𝐭𝐮𝐬: Checked All ✅

# - 𝐓𝐢𝐦𝐞: {hour} Hours {min} Minutes {sec} Seconds
# - 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲: <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ]
# """
#             await message.reply_document(document=hitsfile, caption=text, reply_to_message_id=message.id)

#         else:
#             text = f"""
# - 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 - Stripe Auth♻️

# - 𝐓𝐨𝐭𝐚𝐥 𝐂𝐂 𝐈𝐧𝐩𝐮𝐭 - {len(ccs)}
# - 𝐀𝐩𝐩𝐫𝐨𝐯𝐞: {hits_count} 
# - 𝐃𝐞𝐚𝐝: { chk_done - hits_count }
# - 𝐓𝐨𝐭𝐚𝐥 𝐂𝐡𝐞𝐜𝐤𝐞𝐝: {chk_done}
# - 𝐒𝐞𝐜𝐫𝐞𝐭 𝐊𝐞𝐲: <code>{key}</code>
# (𝐆𝐞𝐭 𝐘𝐨𝐮𝐫 𝐇𝐢𝐭𝐬 𝐊𝐞𝐲 𝐁𝐲 <code>/gethits {key}</code> )
# - 𝐒𝐭𝐚𝐭𝐮𝐬: Checked All ✅

# - 𝐓𝐢𝐦𝐞: {hour} Hours {min} Minutes {sec} Seconds
# - 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲: <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ]
# """
#             await Client.edit_message_text(message.chat.id, stats.id, text)
#     except:
#         pass


# async def get_checking_response(Client, message, ccs,  key, i, start, stats, role, hits_count, chk_done):
#     try:
#         taken = str(timedelta(seconds=time.perf_counter() - start))
#         hours, minutes, seconds = map(float, taken.split(":"))
#         hour = int(hours)
#         min = int(minutes)
#         sec = int(seconds)
#         cc = i["fullz"]
#         response = i["response"]
#         text = f"""
# - 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 - Stripe Auth♻️

# <code>{cc}</code>
# - 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {response}

# - 𝐓𝐨𝐭𝐚𝐥 𝐂𝐂 𝐈𝐧𝐩𝐮𝐭 - {len(ccs)}
# - 𝐀𝐩𝐩𝐫𝐨𝐯𝐞: {hits_count} 
# - 𝐃𝐞𝐚𝐝: { chk_done - hits_count }
# - 𝐓𝐨𝐭𝐚𝐥 𝐂𝐡𝐞𝐜𝐤𝐞𝐝: {chk_done}
# - 𝐒𝐞𝐜𝐫𝐞𝐭 𝐊𝐞𝐲: <code>{key}</code>
# (𝐆𝐞𝐭 𝐘𝐨𝐮𝐫 𝐇𝐢𝐭𝐬 𝐊𝐞𝐲 𝐁𝐲 <code>/gethits {key}</code> )
# - 𝐒𝐭𝐚𝐭𝐮𝐬: Checking...


# - 𝐓𝐢𝐦𝐞: {hour} Hours {min} Minutes {sec} Seconds
# - 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲: <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ]
# """
#         await Client.edit_message_text(chat_id=message.chat.id, message_id=stats.id, text=text)
#     except:
#         pass


# async def chktxt2func(fullcc, user_id, bearer_token):
#     result = await create_cvv_charge(fullcc, bearer_token)
#     getresp = await get_charge_resp(result, user_id, fullcc)
#     return getresp


# async def gcgenfunc(len=4):
#     import random
#     chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
#     return "".join(random.choice(chars) for _ in range(len))


# async def save_cc(i, file_name):
#     try:
#         cc = i["fullz"]
#         response = i["response"]
#         hitsfile = f"HITS/{file_name}"
#         with open(hitsfile, "a", encoding="utf-8") as f:
#             f.write(f"{cc}\n- Response: {response}\n")
#     except:
#         pass


# @Client.on_message(filters.command("autxt", [".", "/"]))
# def multi(Client, message):
#     t1 = threading.Thread(target=bcall, args=(Client, message))
#     t1.start()


# def bcall(Client, message):
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     loop.run_until_complete(stripe_mass_txt_auth_cmd(Client, message))
#     loop.close()


# async def stripe_mass_txt_auth_cmd(Client, message):
#     try:
#         user_id = str(message.from_user.id)
#         first_name = str(message.from_user.first_name)
#         checkall = await check_all_thing(Client, message)
#         results = await getuserinfo(user_id)

#         plan = results["plan"]

#         if plan == "OWNER":  
#             return True, True  
#         elif "∞" not in plan: 
#             resp = """<b>
# Sorry!⚠️

# This feature is available only for Premium users.

# Upgrade to Premium using the /buy command to continue enjoying personal access.
#         </b>"""
#             await message.reply_text(resp, message.id)
#             return


#         if checkall[0] == False:
#             return

#         role = checkall[1]
#         try:
#             random_text = await gcgenfunc(len=8)
#             key = f"authtxt{message.from_user.id}_{random_text}"
#             file_name = f"{key}.txt"
#             hitsfile = f"HITS/{file_name}"
#             await message.reply_to_message.download(file_name=file_name)
#         except:
#             resp = """
# - 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 - Stripe Auth ♻️
# CMD: /authtxt

# Message: No CC Found in your input ❌

# Usage: /authtxt [ in reply to txt file ]
# """
#             await message.reply_text(resp, message.id)
#             return

#         getcc = await getcc_for_txt(file_name, role)
#         if getcc[0] == False:
#             await message.reply_text(getcc[1], message.id)
#             return

#         ccs = getcc[1]
#         user_id = str(message.from_user.id)
#         results = await getuserinfo(user_id)
#         credit = int(results["credit"])
#         need_crt = len(ccs) - credit
#         get_user_info = usersdb.find_one({"id": user_id}, {"_id": 0})
#         if "∞" in get_user_info["plan"]:
#             pass
#         else:
#             if credit < len(ccs):
#                 resp = f"""
# You have no credit, so check with less CC.. Try to Check CC under {credit}.
# You need more {need_crt} Credits
# If you Buy credit, then type /buy .
#         </b> """
#                 await message.reply_text(resp, message.id)
#                 return

#         if role != "OWNER":
#             if len(ccs) > 200:
#                 resp = """
# Limit Reached ⚠️

# Message: YOu can't check more than 200 CCs at a time.
#                 """
#                 await message.reply_text(resp)
#                 return

#         text = f"""
# - 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 - Stripe Auth ♻️

# - 𝐂𝐂 𝐀𝐦𝐨𝐮𝐧𝐭 - {len(ccs)}
# - 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 - Checking CC For {first_name}
# - 𝐍𝐨𝐭𝐞 - This Pop Up Will Change After 50 CC Checked . So Keep Patient . 

# - 𝐒𝐭𝐚𝐭𝐮𝐬 - Processing...⌛️
#     """
#         stats = await message.reply_text(text, message.id)

#         chk_done = 0
#         hits_count = 0
#         start = time.perf_counter()
#         session = httpx.AsyncClient(timeout=30)
#         works = [chktxt2func(i, user_id, session) for i in ccs]
#         worker_num = int(json.loads(
#             open("FILES/config.json", "r", encoding="utf-8").read())["THREADS"])

#         while works:
#             a = works[:worker_num]
#             a = await asyncio.gather(*a)
#             for i in a:
#                 chk_done += 1
#                 if i["hits"] == "YES":
#                     hits_count += 1
#                     await save_cc(i, file_name)

#                 if chk_done % 1 == 0:
#                     await get_checking_response(Client, message, ccs,  key, i, start, stats, role, hits_count, chk_done)

#             works = works[worker_num:]

#         await session.aclose()

#         await get_checked_done_response(Client, message, ccs,  key, hitsfile, start, stats, role, hits_count, chk_done)
#         await massdeductcredit(user_id, message ,len(ccs))
#         await setantispamtime(user_id)

#     except:
#         import traceback
#         await error_log(traceback.format_exc())
