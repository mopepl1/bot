import traceback
from FUNC.defs import *
from FUNC.usersdb_func import *


async def get_charge_resp(result, user_id, fullcc):
    try:

        if type(result) == str:
            status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = result
            hits     = "NO"
        
        elif (
            'success":true' in result.text
            or "success:true" in result.text
            or "Succeeded" in result.text
            or '"status":"success"' in result.text
            or 'Your booking is now confirmed.' in result.text
        ):
            status   = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
            response = "Auth Success ✅"
            hits     = "YES"
            await forward_resp(fullcc, "STRIPE AUTH", response)

        elif "insufficient_funds" in result.text or "card has insufficient funds." in result.text or "Your card has insufficient funds" in result.text:
            status   = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
            response = "Insufficient Funds 💰"
            hits     = "YES"
            await forward_resp(fullcc, "STRIPE AUTH", response)

        elif (
            "incorrect_cvc" in result.text
            or "security code is incorrect." in result.text
            or "Your card's security code is incorrect." in result.text
            or "INVALID SECURITY CODE" in result.text
        ):
            status   = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
            response = "Your card's security code is incorrect ❎"
            hits     = "YES"
            await forward_resp(fullcc, "STRIPE AUTH", response)

        elif ("transaction_not_allowed" in result.text
            or "CURRENCY_COMPLIANCE" in result.text
        ):
            status   = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
            response = "Card Doesn't Support Currency ⚠️"
            hits     = "YES"
            await forward_resp(fullcc, "STRIPE AUTH", response)

        elif '"cvc_check": "pass"' in result.text:
            status   = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
            response = "CVV LIVE 🟢"
            hits     = "YES"
            await forward_resp(fullcc, "STRIPE AUTH", response)

        elif "INVALID_BILLING_ADDRESS" in result.text:
            status   = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
            response = "AVS LIVE🟢"
            hits     = "YES"
            await forward_resp(fullcc, "STRIPE AUTH", response)
    
        
        elif "I Cant Access The Site, Maybe it has cloudflare" in result.text:
            status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Can't Access The Site"
            hits     = "NO"

        elif "failed" in result.text:
            status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "failed ❌"
            hits     = "NO"

        elif "Client-Secret not Found" in result.text:
            status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Client-Secret not Found ❌"
            hits     = "NO"

            
        elif "Your card's security code is invalid." in result.text:
            status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Your card's security code is invalid."
            hits     = "NO"



        
        elif (
            "three_d_secure_redirect" in result.text
            or "card_error_authentication_required" in result.text
            or '"status":"requires_action"' in result.text
            or "requires_action" in result.text
            or "challenge_required" in result.text
            or "#wc-stripe-confirm-pi" in result.text
        ):
            status   = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
            response = "3D Challenge Required ⚠️"
            hits     = "YES"
            await forward_resp(fullcc, "STRIPE AUTH", response)

        elif "stripe_3ds2_fingerprint" in result.text:
            status   = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
            response = "3D Challenge Required ⚠️"
            hits     = "YES"
            await forward_resp(fullcc, "STRIPE AUTH", response)

        elif "Your card does not support this type of purchase." in result.text:
            status   = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
            response = "Card Doesn't Support Purchase ⚠️"
            hits     = "YES"
            await forward_resp(fullcc, "STRIPE AUTH", response)

        elif (
            "generic_decline" in result.text
            or "You have exceeded the maximum number of declines on this card in the last 24 hour period."
            in result.text
            or "card_decline_rate_limit_exceeded" in result.text
            or "CARD_GENERIC_ERROR" in result.text
            or "Your card was declined." in result.text

        ):
            status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Card was declined"
            hits     = "NO"

        elif "do_not_honor" in result.text:
            status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Do Not Honor ❌"
            hits     = "NO"

        elif "fraudulent" in result.text:
            status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Fraudulent ❌"
            hits     = "NO"

        elif "verify the postal code in your billing address" in result.text:
            status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Verify Postal Code ❌"
            hits     = "NO"

        elif "setup_intent_authentication_failure" in result.text:
            status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "setup_intent_authentication_failure ❌"
            hits     = "NO"

        elif "invalid_cvc" in result.text:
            status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "invalid_cvc ❌"
            hits     = "NO"

        elif "stolen_card" in result.text:
            status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Stolen Card ❌"
            hits     = "NO"

        elif "lost_card" in result.text:
            status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Lost Card ❌"
            hits     = "NO"

        elif "pickup_card" in result.text:
            status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Pickup Card ❌"
            hits     = "NO"

        elif "Incorrect Card Number" in result.text:
            status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Incorrect Card Number ❌"
            hits     = "NO"

        elif "Your card has expired." in result.text or "expired_card" in result.text:
            status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Expired Card ❌"
            hits     = "NO"

        elif "intent_confirmation_challenge" in result.text:
            status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "intent_confirmation_challenge ❌"
            hits     = "NO"

        elif "Your card number is incorrect." in result.text:
            status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Incorrect Card Number ❌"
            hits     = "NO"

        elif (
            "Your card's expiration year is invalid." in result.text
            or "Your card's expiration year is invalid." in result.text
        ):
            status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Expiration Year Invalid ❌"
            hits     = "NO"

        elif (
            "Your card's expiration month is invalid." in result.text
            or "invalid_expiry_month" in result.text
        ):
            status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Expiration Month Invalid ❌"
            hits     = "NO"

        elif "card is not supported." in result.text:
            status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Card Not Supported ❌"
            hits     = "NO"

        elif "Invalid account." in result.text:
            status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Invalid Account ❌"
            hits     = "NO"

        elif (
            "Invalid API Key provided" in result.text
            or "testmode_charges_only" in result.text
            or "api_key_expired" in result.text
            or "Your account cannot currently make live charges." in result.text
        ):
            status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "stripe error . contact support@stripe.com for more details ❌"
            hits     = "NO"

        elif "Payment Intent Creation Failed ❌" in result.text:
            status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Payment Intent Creation Failed ❌"
            hits     = "NO"
            await refundcredit(user_id)

        elif "Connection aborted." in result.text:
            status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Proxy Connection Refused ❌"
            hits     = "NO"
            await refundcredit(user_id)

        else:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = await find_between(result.text , "System was not able to complete the payment. ", ".")
            if response is None:
                response = "Card Declined"
                await result_logs(fullcc, "Stripe Charge", result)
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
