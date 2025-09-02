import traceback
from FUNC.defs import *
from FUNC.usersdb_func import *

def gets(s, start, end):
    try:
        start_index = s.index(start) + len(start)
        end_index = s.index(end, start_index)
        return s[start_index:end_index]
    except ValueError:
        return None
    

async def get_charge_resp(result, user_id, fullcc):
    try:
        

        if type(result) == str:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = result
            hits = "NO"

       


        elif (
            "SUCCESS" in result.text or
            "ThankYou" in result.text or
            "Thank you" in result.text or
            "thank_you" in result.text or
            "success" in result.text or
            "Your order is confirmed" in result.text or
            "your order is confirmed" in result.text or
            "classicThankYouPageUrl" in result.text or
            '"__typename":"ProcessedReceipt"' in result.text
        ):
            status = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
            response = "order is confirmed 🔥"
            hits = "YES"

            await forward_resp(fullcc, "SHOPIFY CHARGE [SH]", response)

        elif "insufficient_funds" in result.text or "card has insufficient funds." in result.text or "2001 Insufficient Funds" in result.text:
            status = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
            response = "Insufficient Funds"
            hits = "YES"
            await forward_resp(fullcc, "SHOPIFY CHARGE [SH]", response)

        elif (
                "INCORRECT_CVC" in result.text
                or "INVALID_CVC" in result.text
                or "2010 Card Issuer Declined CVV" in result.text
                or "Your card's security code is incorrect." in result.text
                or "Security code was not matched by the processor" in result.text


        ):
            status = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
            response = "Your card's security code is incorrect"
            hits = "YES"
            await forward_resp(fullcc, "SHOPIFY CHARGE [SH]", response)

        elif "transaction_not_allowed" in result.text:
            status = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
            response = "Card Doesn't Support Purchase"
            hits = "YES"
            await forward_resp(fullcc, "SHOPIFY CHARGE [SH]", response)

        elif 'INSUFFICIENT_FUNDS' in result.text:
            status = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
            response = "INSUFFICIENT_FUNDS"
            hits = "YES"
            await forward_resp(fullcc, "SHOPIFY CHARGE [SH]", response)

        elif (
            "ActionRequiredReceipt" in result.text
            or "card_error_authentication_required" in result.text
            or "3ds cc" in result.text
            or "stripe_3ds2_fingerprint" in result.text
            or "stripe/authentications" in result.text
            or "3d_secure_2" in result.text
            or "CompletePaymentChallenge" in result.text
            or "AUTHENTICATION_ERROR" in result.text
            or "ActionRequiredReceipt" in result.text
            or "stripe_3ds2_fingerprint" in result.text
        ):
            status = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
            response = "CVV MATCH - 3ds cc"
            hits = "YES"
            await forward_resp(fullcc, "SHOPIFY CHARGE [SH]", response)

        elif "Your card does not support this type of purchase." in result.text:
            status = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
            response = "Card Doesn't Support Purchase"
            hits = "YES"
            await forward_resp(fullcc, "SHOPIFY CHARGE [SH]", response)

        elif "Access to this resource on the server is denied!" in result.text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Server Error"
            hits = "NO"
            await refundcredit(user_id)


        elif "EXPIRED_CARD" in result.text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Card Expire"
            hits = "NO"


        elif "PICK_UP_CARD" in result.text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "PICK_UP_CARD"
            hits = "NO"






        elif "PROCESSING_ERROR" in result.text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "PROCESSING_ERROR"
            hits = "NO"














        elif "EXPIRED_CARD" in result.text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Card Expire"
            hits = "NO"

        elif ("Card was declined" in result.text
                or "CARD_DECLINED" in result.text
                or "PAYMENTS_CREDIT_CARD_GENERIC" in result.text
                or "Card number is incorrect" in result.text
                or "The shipping options have changed for your order. Review your selection and try again" in result.text

              ):
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "CARD_DECLINED"
            hits = "NO"

        elif ("GENERIC_ERROR" in result.text
                or "GENERIC_ERROR" in result.text
              ):
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "GENERIC_ERROR"
            hits = "NO"



        elif ("thank_you" in result.text
                or "thank_you" in result.text
              ):
            status = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
            response = "order is confirmed 🔥"
            hits = "YES"

            await forward_resp(fullcc, "SHOPIFY CHARGE [SHD]", response)

        elif "Cloudflare Bypass Failed" in result.text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Cloudflare Bypass Failed"
            hits = "NO"
            
        elif "INCORRECT_NUMBER" in result.text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "INCORRECT_NUMBER"
            hits = "NO"


        elif "PAYMENTS_CREDIT_CARD_BASE_EXPIRED" in result.text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "CARD EXPIRE"
            hits = "NO"

        elif "Receipt ID is empty" in result.text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Receipt ID is empty"
            hits = "NO"

            
        elif 'INSUFFICIENT_FUNDS' in result.text:
            status = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
            response = "INSUFFICIENT_FUNDS"
            hits = "YES"
            await forward_resp(fullcc, "SHOPIFY CHARGE [SH]", response)




        elif "Verifying that you are not a robot" in result.text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Captcha Error"
            hits = "NO"


        elif "AUTHORIZATION_ERROR" in result.text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "AUTHORIZATION ERROR"
            hits = "NO"

        elif "FRAUD_SUSPECTED" in result.text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "FRAUD_SUSPECTED"
            hits = "NO"

        elif "Try Again" in result.text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Try Again"
            hits = "NO"

            
        elif "Proxy Dead" in result.text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Proxy Dead"
            hits = "NO"




        else:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = await find_between(result.text, "System was not able to complete the payment. ", ".")
            if response is None:
                response = "Card Declined"
                await result_logs(fullcc, "Stripe Charge 10$", result)
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
        status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
        response = str(e) + " ❌"
        hits = "NO"

        json = {
            "status": status,
            "response": response,
            "hits": hits,
            "fullz": fullcc,
            
        }
        return json
