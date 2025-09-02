import traceback
from FUNC.defs import *
from FUNC.usersdb_func import *


async def get_charge_resp(result, user_id, fullcc):
    try:

        if type(result) == str:
            status = "Declined ❌"
            response = result
            hits = "NO"

            if (
                "bypassed" in result or
                 "authenticate_successful" in result
                or "authenticate_attempt_successful" in result
                or "authenticate_unavailable" in result
                or "lookup_not_enrolled" in result
                or "authentication_unavailable" in result
                or "authenticate_successful" in result
                or "authenticate_attempt_successful" in result
                or "authenticate_unavailable" in result
                or "lookup_not_enrolled" in result
                or "authentication_unavailable" in result

            ):
                status = "VBV Passed ✅"
                response = "Authenticate Successful"
                hits = "YES"
                await forward_resp(fullcc, "BRAINTREE VBV", response)

            elif (
                "Card Issuer Declined CVV" in result
            ):
                status = "Approved ✅"
                response = "Card Issuer Declined CVV "
                hits = "YES"
                await forward_resp(fullcc, "BRAINTREE AUTH", response)

            elif (
                "Insufficient Funds" in result
            ):
                status = "Approved ✅"
                response = "Insufficient Funds"
                hits = "YES"
                await forward_resp(fullcc, "BRAINTREE AUTH", response)


            elif ("Gateway Rejected: risk_threshold" in result):
                status = "Declined ❌"
                response = "Gateway Rejected: risk_threshold"
                hits = "NO"

            elif ("Declined - Call Issuer" in result):
                status = "Declined ❌"
                response = "Declined - Call Issuer"
                hits = "NO"

            elif ("Cannot Authorize at this time" in result):
                status = "Declined ❌"
                response = "Cannot Authorize at this time!"
                hits = "NO"

            elif ("Processor Declined - Fraud Suspected" in result):
                status = "Declined ❌"
                response = "Fraud Suspected"
                hits = "NO"

            elif "Status code risk_threshold: Gateway Rejected: risk_threshold" in result:
                status = "Declined ❌"
                response = "Gateway Rejected: risk_threshold"
                hits = "NO"

            elif ("Declined - Call Issuer" in result or
                  "Payment failed: Declined - Call Issuer" in result
                  ):
                status = "Declined ❌"
                response = "Declined - Call Issuer"
                hits = "NO"

            elif "ProxyError" in result:
                status = "Declined ❌"
                response = "Proxy Connection Refused"
                hits = "NO"
                await refundcredit(user_id)

            else:
                status = "Declined ❌"
                try:
                    response = result.split('"message": "')[
                        1].split('"')[0] + " ❌"
                except:
                    response = result
                    await result_logs(fullcc, "Braintree Auth", result)
                hits = "NO"

        json = {
            "status": status,
            "response": response,
            "hits": hits,
            "fullz": fullcc,
        }
        return json

    except Exception as e:
        status = "Declined ❌"
        response = str(e) + " ❌"
        hits = "NO"

        json = {
            "status": status,
            "response": response,
            "hits": hits,
            "fullz": fullcc,
        }
        return json
