import traceback
from FUNC.defs import *
from FUNC.usersdb_func import *


async def get_charge_resp(result, user_id, fullcc):
    try:

        if type(result) == str:
            status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = result
            hits     = "NO"
        
            if (
                "transaction_status:SUCCESS" in result
                or '"success":true' in result
            ):
                status   = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
                response = "Recurly Payment Complete 🔥"
                hits     = "YES"
                await forward_resp(fullcc, "RECURLY CHARGE [/re]", response)

            elif "insufficient funds" in result or "Your transaction was declined due to insufficient funds in your account" in result or "INSUFFICIENT_FUNDS" in result:
                status   = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
                response = "Insufficient Funds 💰"
                hits     = "YES"
                await forward_resp(fullcc, "RECURLY CHARGE [/re]", response)

            elif (
                "The security code (CVV) or expiration date you entered does not match" in result
                or "Please update the CVV" in result
                or "Your card's security code is incorrect." in result
                or "Please update the CVV" in result
            ):
                status   = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
                response = "CCN Live ❎"
                hits     = "YES"
                await forward_resp(fullcc, "RECURLY CHARGE [/re]", response)

            elif ("transaction_not_allowed" in result
                or "CURRENCY_COMPLIANCE" in result
            ):
                status   = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
                response = "Card Doesn't Support Currency ⚠️"
                hits     = "YES"
                await forward_resp(fullcc, "RECURLY CHARGE [/re]", response)

            elif '"cvc_check": "pass"' in result:
                status   = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
                response = "CVV LIVE 🟢"
                hits     = "YES"
                await forward_resp(fullcc, "RECURLY CHARGE [/re]", response)

            elif "Your billing address does not match the address on your account" in result:
                status   = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
                response = "AVS [Rejected] - LIVE🟢"
                hits     = "YES"
                await forward_resp(fullcc, "RECURLY CHARGE [/re]", response)
        
            
            elif "your session has expired" in result:
                response = "Session has expired"

            elif "Your card number is not valid" in result:
                response = "Your card number is not valid"


            elif "Your account number is not valid" in result:
                response = "Your account number is not valid"

            
            elif (
                "three_d_secure_redirect" in result
                or "card_error_authentication_required" in result
                or "is3DSecureRequired" in result
                or "#wc-stripe-confirm-pi" in result
            ):
                status   = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
                response = "3D Challenge Required ⚠️"
                hits     = "YES"
                await forward_resp(fullcc, "RECURLY CHARGE [/re]", response)

            elif "stripe_3ds2_fingerprint" in result:
                status   = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
                response = "3D Challenge Required ⚠️"
                hits     = "YES"
                await forward_resp(fullcc, "RECURLY CHARGE [/re]", response)

            elif "Your card does not support this type of purchase." in result:
                status   = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
                response = "Card Doesn't Support Purchase ⚠️"
                hits     = "YES"
                await forward_resp(fullcc, "RECURLY CHARGE [/re]", response)

            elif (
                "generic_decline" in result
                or "You have exceeded the maximum number of declines on this card in the last 24 hour period."
                in result
                or "card_decline_rate_limit_exceeded" in result
                or "The transaction was declined" in result
                or "Your card was declined." in result

            ):
                status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
                response = "Transaction declined"
                hits     = "NO"

            elif "do_not_honor" in result:
                status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
                response = "Do Not Honor ❌"
                hits     = "NO"

            elif "fraudulent" in result:
                status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
                response = "Fraudulent ❌"
                hits     = "NO"

            elif "invalid_cvc" in result:
                status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
                response = "invalid_cvc ❌"
                hits     = "NO"

            elif "stolen_card" in result:
                status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
                response = "Stolen Card ❌"
                hits     = "NO"

            elif "lost_card" in result:
                status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
                response = "Lost Card ❌"
                hits     = "NO"

            elif "pickup_card" in result:
                status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
                response = "Pickup Card ❌"
                hits     = "NO"

            elif "incorrect_number" in result:
                status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
                response = "Incorrect Card Number ❌"
                hits     = "NO"

            elif "Your card has expired." in result or "expired_card" in result:
                status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
                response = "Expired Card ❌"
                hits     = "NO"

            elif "Your account number is not valid" in result:
                status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
                response = "Invalid Account Number ❌"
                hits     = "NO"

            elif "Your card number is not valid" in result:
                status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
                response = "Invalid Card Number ❌"
                hits     = "NO"

            elif (
                "Your card's expiration year is invalid." in result
                or "Your card's expiration year is invalid." in result
            ):
                status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
                response = "Expiration Year Invalid ❌"
                hits     = "NO"

            elif (
                "Your card's expiration month is invalid." in result
                or "invalid_expiry_month" in result
            ):
                status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
                response = "Expiration Month Invalid ❌"
                hits     = "NO"

            elif "card is not supported." in result:
                status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
                response = "Card Not Supported ❌"
                hits     = "NO"

            elif "invalid_account" in result:
                status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
                response = "Dead Card ❌"
                hits     = "NO"

            elif (
                "Please validate information and try again" in result
            ):
                status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
                response = "Please validate information and try again ❌"
                hits     = "NO"

            elif "Payment Intent Creation Failed ❌" in result:
                status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
                response = "Payment Intent Creation Failed ❌"
                hits     = "NO"
                await refundcredit(user_id)

            elif "ProxyError" in result:
                status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
                response = "Proxy Connection Refused ❌"
                hits     = "NO"
                await refundcredit(user_id)

            else:
                status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
                response = await find_between(result , "System was not able to complete the payment. ", ".")
                if response is None:
                    response = "Card Declined"
                    await result_logs(fullcc, "Recurly Charge", result)
                response = response + " ❌"
                hits = "NO"

        json = {
            "status": status,
            "response": response,
            "hits": hits,
            "fullz": fullcc,
        }
        return json 

    except Exception as e:
        status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
        response = str(e) + " ❌"
        hits     = "NO"

        json = {
            "status": status,
            "response": response,
            "hits": hits,
            "fullz": fullcc,
        }
        return json
