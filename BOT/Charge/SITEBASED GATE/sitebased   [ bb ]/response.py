import traceback
from FUNC.defs import *
from FUNC.usersdb_func import *


async def get_charge_resp(result, user_id, fullcc):
    try:

        if type(result) == str:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = result
            hits = "NO"

            if (
                'success":true' in result
            ):
                status   = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
                response = "Thanks for your Donations!🔥"
                hits     = "YES"
                await forward_resp(fullcc, "sitebase Charge 1$", response)

            elif "insufficient_funds" in result or "card has insufficient funds." in result or "2001 Insufficient Funds" in result:
                status = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
                response = "Insufficient Funds"
                hits = "YES"
                await forward_resp(fullcc, "NONSK CHARGE [bb]", response)

            elif (
                    "INCORRECT_CVC" in result
                    or "INVALID_CVC" in result
                    or "Your card's security code is invalid" in result
                    or "2010 Card Issuer Declined CVV" in result
                    or "Your card's security code is incorrect." in result
                    or "Security code was not matched by the processor" in result


            ):
                status = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
                response = "CCN Live"
                hits = "YES"
                await forward_resp(fullcc, "NONSK CHARGE [bb]", response)

            elif "transaction_not_allowed" in result:
                status = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
                response = "Card Doesn't Support Purchase"
                hits = "YES"
                await forward_resp(fullcc, "NONSK CHARGE [bb]", response)

            elif '"cvc_check": "pass"' in result:
                status = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
                response = "CVV LIVE"
                hits = "YES"
                await forward_resp(fullcc, "NONSK CHARGE [bb]", response)

            elif (
                "ActionRequiredReceipt" in result
                or "card_error_authentication_required" in result
                or "OTP Required" in result
                or "stripe_3ds2_fingerprint" in result
                or "Verifying strong customer authentication." in result
                or "stripe/authentications" in result
                or "3d_secure_2" in result
                or "CompletePaymentChallenge" in result
                or "AUTHENTICATION_ERROR" in result
                or "ActionRequiredReceipt" in result
                or "stripe_3ds2_fingerprint" in result
                or '"redirect":"#wcpay-confirm-pi' in result
            ):
                status = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
                response = "OTP Required"
                hits = "YES"
                await forward_resp(fullcc, "NONSK CHARGE [bb]", response)

            elif "Your card does not support this type of purchase." in result:
                status = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
                response = "Card Doesn't Support Purchase"
                hits = "YES"
                await forward_resp(fullcc, "NONSK CHARGE [bb]", response)

            elif "ProxyError" in result:
                status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
                response = "Proxy Connection Refused"
                hits = "NO"
                await refundcredit(user_id)


            elif ("Card was declined" in result
                    or "Your card was declined." in result
                    or "CARD_DECLINED" in result
                    or "PAYMENTS_CREDIT_CARD_GENERIC" in result
                    or "Card number is incorrect" in result
                    or "The shipping options have changed for your order. Review your selection and try again" in result

                ):
                status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
                response = "Card was declined"
                hits = "NO"


            elif "Your payment details couldn’t be verified. Check your card details and try again." in result:
                status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
                response = "INCORRECT_NUMBER"
                hits = "NO"


            elif "Your card has expired" in result:
                status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
                response = "Your card has expired"
                hits = "NO"

            else:
                status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
                response = await find_between(result, "System was not able to complete the payment. ", ".")
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
