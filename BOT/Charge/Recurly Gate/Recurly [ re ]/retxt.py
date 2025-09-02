# import time
# import httpx
# import threading
# import asyncio
# import json
# from pyrogram import Client, filters
# from datetime import timedelta
# from .gate import *
from .response import *
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton# from .response import *
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
# - 𝐆𝐚𝐭𝐞𝐬: RECURLY CHARGE [/re]

# - 𝐓𝐨𝐭𝐚𝐥 𝐂𝐂 𝐈𝐧𝐩𝐮𝐭: {len(ccs)}
# - 𝐇𝐢𝐭𝐬: {hits_count} 
# - 𝐃𝐞𝐚𝐝: { chk_done - hits_count }
# - 𝐓𝐨𝐭𝐚𝐥 𝐂𝐡𝐞𝐜𝐤𝐞𝐝: {chk_done}
# - 𝐒𝐞𝐜𝐫𝐞𝐭 𝐊𝐞𝐲: <code>{key}</code>
# - 𝐒𝐭𝐚𝐭𝐮𝐬: Checked All ✅

# - 𝐓𝐢𝐦𝐞: {hour} Hours {min} Minutes {sec} Seconds
# """
#             await message.reply_document(document=hitsfile, caption=text, reply_to_message_id=message.id)

#         else:
#             text = f"""
# - 𝐆𝐚𝐭𝐞𝐬: RECURLY CHARGE [/re]

# - 𝐓𝐨𝐭𝐚𝐥 𝐂𝐂 𝐈𝐧𝐩𝐮𝐭: {len(ccs)}
# - 𝐇𝐢𝐭𝐬: {hits_count} 
# - 𝐃𝐞𝐚𝐝: { chk_done - hits_count }
# - 𝐓𝐨𝐭𝐚𝐥 𝐂𝐡𝐞𝐜𝐤𝐞𝐝: {chk_done}
# - 𝐒𝐞𝐜𝐫𝐞𝐭 𝐊𝐞𝐲: <code>{key}</code>
# (𝐆𝐞𝐭 𝐘𝐨𝐮𝐫 𝐇𝐢𝐭𝐬 𝐊𝐞𝐲 𝐁𝐲 <code>/gethits {key}</code> )
# - 𝐒𝐭𝐚𝐭𝐮𝐬: Checked All ✅

# - 𝐓𝐢𝐦𝐞: {hour} Hours {min} Minutes {sec} Seconds
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
# - 𝐆𝐚𝐭𝐞𝐬: RECURLY CHARGE [/re]

# <code>{cc}</code>
# - 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {response}

# - 𝐓𝐨𝐭𝐚𝐥 𝐂𝐂 𝐈𝐧𝐩𝐮𝐭: {len(ccs)}
# - 𝐇𝐢𝐭𝐬: {hits_count} 
# - 𝐃𝐞𝐚𝐝: { chk_done - hits_count }
# - 𝐓𝐨𝐭𝐚𝐥 𝐂𝐡𝐞𝐜𝐤𝐞𝐝: {chk_done}
# - 𝐒𝐞𝐜𝐫𝐞𝐭 𝐊𝐞𝐲: <code>{key}</code>
# (𝐆𝐞𝐭 𝐘𝐨𝐮𝐫 𝐇𝐢𝐭𝐬 𝐊𝐞𝐲 𝐁𝐲 <code>/gethits {key}</code> )
# - 𝐒𝐭𝐚𝐭𝐮𝐬: Checking...

# - 𝐓𝐢𝐦𝐞: {hour} Hours {min} Minutes {sec} Seconds

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
#             f.write(f"{cc}\n- 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {response}\n")
#     except:
#         pass


# @Client.on_message(filters.command("retxt", [".", "/"]))
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
#         if checkall[0] == False:
#             return

#         role = checkall[1]
#         try:
#             random_text = await gcgenfunc(len=8)
#             key = f"retxt_{message.from_user.id}_{random_text}"
#             file_name = f"{key}.txt"
#             hitsfile = f"HITS/{file_name}"
#             await message.reply_to_message.download(file_name=file_name)
#         except:
#             resp = """
# 𝐆𝐚𝐭𝐞 𝐍𝐚𝐦𝐞: RECURLY CHARGE [/re]
# 𝐂𝐌𝐃: /schtxt

# 𝐌𝐞𝐬𝐬𝐚𝐠𝐞: 𝐍𝐨 𝐂𝐂 𝐅𝐨𝐮𝐧𝐝 𝐢𝐧 𝐲𝐨𝐮𝐫 𝐢𝐧𝐩𝐮𝐭 ❌

# 𝐔𝐬𝐚𝐠𝐞: /schtxt [ in reply to txt file ]
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
# 𝐈𝐧𝐬𝐮𝐟𝐟𝐢𝐜𝐢𝐞𝐧𝐭 𝐂𝐫𝐞𝐝𝐢𝐭𝐬 ⚠️

# 𝐌𝐞𝐬𝐬𝐚𝐠𝐞: 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 𝐈𝐧𝐬𝐮𝐟𝐟𝐢𝐜𝐢𝐞𝐧𝐭 𝐂𝐫𝐞𝐝𝐢𝐭𝐬, 𝐘𝐨𝐮 𝐭𝐫𝐢𝐞𝐝 𝐭𝐨 𝐂𝐡𝐞𝐜𝐤 {len(ccs)} 𝐂𝐂 𝐰𝐢𝐭𝐡 𝐨𝐧𝐥𝐲 {credit} 𝐂𝐫𝐞𝐝𝐢𝐭𝐬.

# 𝐘𝐨𝐮 𝐧𝐞𝐞𝐝 𝐦𝐨𝐫𝐞 𝐭𝐡𝐚𝐧 {need_crt} 𝐂𝐫𝐞𝐝𝐢𝐭𝐬.

# 𝐓𝐲𝐩𝐞 /buy 𝐭𝐨 𝐑𝐞𝐜𝐡𝐚𝐫𝐠𝐞
# """
#                 await message.reply_text(resp, message.id)
#                 return

#         if role != "OWNER":
#             if len(ccs) > 250:
#                 resp = """
# 𝐋𝐢𝐦𝐢𝐭 𝐑𝐞𝐚𝐜𝐡𝐞𝐝 ⚠️

# 𝐌𝐞𝐬𝐬𝐚𝐠𝐞: 𝐘𝐨𝐮 𝐜𝐚𝐧'𝐭 𝐜𝐡𝐞𝐜𝐤 𝐦𝐨𝐫𝐞 𝐭𝐡𝐚𝐧 𝟏𝟎𝟎 𝐂𝐂𝐬 𝐚𝐭 𝐚 𝐭𝐢𝐦𝐞.
#                 """
#                 await message.reply_text(resp)
#                 return

#         text = f"""
# - 𝐆𝐚𝐭𝐞𝐬: RECURLY CHARGE [/re]

# - 𝐂𝐂 𝐀𝐦𝐨𝐮𝐧𝐭: {len(ccs)}
# - 𝐌𝐞𝐬𝐬𝐚𝐠𝐞: Checking CC For {first_name}
# - 𝐍𝐨𝐭𝐞: This Pop Up Will Change After 1 CC Checked . So Keep Patient . 

# - 𝐒𝐭𝐚𝐭𝐮𝐬: Processing...⌛️

# - 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲: <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ]
# """
#         stats = await message.reply_text(text, message.id)

#         chk_done = 0
#         hits_count = 0
#         start = time.perf_counter()
#         # bearer_token = await get_bearer_token("AUTH_TOKEN")
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
