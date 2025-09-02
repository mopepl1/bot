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
                "succeeded" in result
                or "thank you" in result
                or "Thank you" in result
                or "Thank You" in result
                or "Thank You!" in result
                or "Thank you!" in result
                or "thank You!" in result
                or "thank you!" in result
                or "Thank you for your order" in result
                or "Thank You for your order" in result
                or "Thank You For Your Order" in result
                or "Thank you for your order!" in result
                or "Thank You for your order!" in result
                or "Thank You For Your Order!" in result
                or "Thank you for your order." in result
                or "Thank You for your order." in result
                or "Thank You For Your Order." in result
                or "Thank you for your order," in result
                or "Thank You for your order," in result
                or "Thank You For Your Order," in result
                or "Thank you for your order!" in result
                or "Thank You for your order!" in result
                or "Thank You For Your Order!" in result
                or "Thank you for your order," in result
                or "Thank You for your order," in result
                or "Thank You For Your Order," in result
                or "You have received a payout" in result
                or "success:true" in result
                or "transaction_status:SUCCESS" in result
                or "CHARGED 0.01$ SUCCESSFULLY" in result
            ):
                status   = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
                response = "Successful Card Payment 🔥"
                hits     = "YES"
                await forward_resp(fullcc, "Paypal Charge 0.01$", response)

            elif "insufficient_funds" in result or "card has insufficient funds." in result or "INSUFFICIENT_FUNDS" in result:
                status   = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
                response = "Insufficient Funds ❎"
                hits     = "YES"
                await forward_resp(fullcc, "Paypal Charge 0.01$", response)

            elif (
                "incorrect_cvc" in result or
                " CVV2_FAILURE_POSSIBLE_RETRY_WITH_CVV." in result
                or "security code is incorrect." in result
                or "Your card's security code is incorrect." in result
                or "INVALID SECURITY CODE" in result
                or "CVV2_FAILURE" in result
            ):
                status   = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
                response = "CCN Live ❎"
                hits     = "YES"
                await forward_resp(fullcc, "Paypal Charge 0.01$", response)


            elif (
                "TRANSACTION_CANNOT_BE_COMPLETED.." in result

            ):
                status   = "TRY TRIAL❎"
                response = "TRANSACTION_CANNOT_BE_COMPLETED."
                hits     = "YES"
                await forward_resp(fullcc, "Paypal Charge 0.01$", response)





            elif (
                "SECURITY_VIOLATION." in result

            ):
                status   = "TRY TRIAL❎"
                response = "SECURITY_VIOLATION"
                hits     = "YES"
                await forward_resp(fullcc, "Paypal Charge 0.01$", response)

            elif ("transaction_not_allowed" in result
                or "CURRENCY_COMPLIANCE" in result
            ):
                status   = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
                response = "Card Doesn't Support Currency ❎"
                hits     = "YES"
                await forward_resp(fullcc, "Paypal Charge 0.01$", response)

            elif( '"Toggjg": "pass"' in result or
                '"issue":"ORDER_NOT_APPROVED"' in result
                ):
                status   = "ORDER_NOT_APPROVED 😢"
                response = "Payer has not yet approved the Order for payment."
                hits     = "YES"
                await forward_resp(fullcc, "Paypal Charge 0.01$", response)

            elif "INVALID_BILLING_ADDRESS" in result:
                status   = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
                response = "AVS LIVE🟢"
                hits     = "YES"
                await forward_resp(fullcc, "Paypal Charge 0.01$", response)
        
            
            
            elif (
                "three_d_secure_redirect" in result
                or "card_error_authentication_required" in result
                or "is3DSecureRequired" in result
            ):
                status   = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
                response = "3D Challenge Required ❎"
                hits     = "YES"
                await forward_resp(fullcc, "Paypal Charge 0.01$", response)

            elif "stripe_3ds2_fingerprint" in result:
                status   = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
                response = "3D Challenge Required ❎"
                hits     = "YES"
                await forward_resp(fullcc, "Paypal Charge 0.01$", response)

            elif "Your card does not support this type of purchase." in result:
                status   = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
                response = "Card Doesn't Support Purchase ❎"
                hits     = "YES"
                await forward_resp(fullcc, "Paypal Charge 0.01$", response)

            elif (
                "EXISTING_ACCOUNT_RESTRICTED" in result
                or "OAS_VALIDATION_ERROR" in result
                or "RESTRICTED_OR_INACTIVE_ACCOUNT." in result
            ):
                status   = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
                response = "CVV LIVE - RESTRICTED_OR_INACTIVE_ACCOUNT"
                hits     = "YES"
                await forward_resp(fullcc, "Paypal Charge 0.01$", response)

            elif (
                "generic_decline" in result
                or "You have exceeded the maximum number of declines on this card in the last 24 hour period."
                in result
                or "card_decline_rate_limit_exceeded" in result
                or "CARD_GENERIC_ERROR" in result
                or "PAYMENT_DENIED" in result
                or "GENERIC_DECLINE." in result
            ):
                status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
                response = "CARD_GENERIC_ERROR"
                hits     = "NO"

            elif "DO_NOT_HONOR." in result:
                status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
                response = "Do Not Honor"
                hits     = "NO"

            elif "fraudulent" in result:
                status   = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
                response = "Fraudulent ❌"
                hits     = "NO"

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
