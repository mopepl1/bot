import traceback
from FUNC.defs import *
from FUNC.usersdb_func import *

async def get_charge_resp(result, user_id, fullcc):
    # Initialize variables with default values
    status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
    response = ""
    hits = "NO"

    try:
        # Check if the result has a 'text' attribute (e.g., result is an object)
        result_text = result.text if hasattr(result, 'text') else str(result)

        if "APPROVED" in result_text:
            status = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
            response = "Approved"
            hits = "YES"
            await forward_resp(fullcc, "BRAINTREE AUTH 1", response)

        elif "Invalid postal code or street address." in result_text:
            status = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
            response = "Approved"
            hits = "YES"
            await forward_resp(fullcc, "BRAINTREE AUTH 1", response)

        elif "Duplicate card exists in the vault" in result_text:
            status = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
            response = "Approved"
            hits = "YES"
            await forward_resp(fullcc, "BRAINTREE AUTH 1", response)

        elif "Card Issuer Declined CVV" in result_text:
            status = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
            response = "Card Issuer Declined CVV"
            hits = "YES"
            await forward_resp(fullcc, "BRAINTREE AUTH 1", response)

        elif "Insufficient Funds" in result_text:
            status = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
            response = "Insufficient Funds"
            hits = "YES"
            await forward_resp(fullcc, "BRAINTREE AUTH 1", response)

        elif "Reason: CVV" in result_text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Gateway Rejected: CVV"

        elif "Reason: Closed Card" in result_text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Closed Card"

        elif "Reason: Processor Declined - Call Issuer" in result_text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Declined - Call Issuer"

        elif "Reason: Processor Declined" in result_text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Processor Declined"

        elif "Reason: Call Issuer. Pick Up Card." in result_text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Pickup Card"

        elif "Reason: No Account" in result_text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "No Account"

        elif "Reason: Cannot Authorize at this time" in result_text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Cannot Authorize at this time"

        elif "Reason: Processor Declined - Fraud Suspected" in result_text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Fraud Suspected"

        elif "You cannot add a new payment method so soon after the previous one. Please wait for 20 seconds." in result_text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Please Wait 20 Seconds"

        elif "Reason: Card Not Activated" in result_text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Card Not Activated"

        elif "Reason: Card Account Length Error" in result_text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Card Account Length Error"
        
        elif "Reason: Invalid Authorization Code" in result_text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Invalid Authorization Code"

        elif "Reason: Issuer or Cardholder has put a restriction on the card" in result_text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Restricted Card"

        elif "Reason: Transaction amount exceeds the transaction division limit" in result_text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Transactions Limit Exceeds"

        elif "Reason: Processor Declined - Possible Stolen Card" in result_text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Stolen Card"

        elif "Reason: Error - Do Not Retry, Call Issuer" in result_text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Don Not Retry"

        elif "Reason: Invalid Client ID" in result_text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Invalid Client ID"

        elif "Reason: Declined - Call For Approval" in result_text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Call For Approval"

        elif "Reason: Expired Card" in result_text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Expired Card"

        elif "Reason: Limit Exceeded" in result_text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Limit Exceeded"

        elif "Reason: Cardholder's Activity Limit Exceeded" in result_text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Limit Exceeded"

        elif "Reason: Invalid Credit Card Number" in result_text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Invalid Credit Card Number"

        elif "Reason: Invalid Expiration Date" in result_text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Invalid Expiration Date"

        elif "Reason: No Such Issuer" in result_text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "No Such Issuer"

        elif "Reason: Duplicate Transaction" in result_text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Duplicate Transaction"

        elif "Reason: Transaction Not Allowed" in result_text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Transaction Not Allowed"

        elif "Reason: Processor Declined Possible Lost Card" in result_text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Lost Card"

        elif "Reason: Invalid Transaction" in result_text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Invalid Transaction"

        elif "Reason: Card Type Not Enabled" in result_text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Invalid Transaction"

        elif "Reason: Voice Authorization Required" in result_text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Voice Authorization Required"

        elif "Reason: Cardholder Stopped Billing" in result_text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Cardholder Stopped Billing"

        elif "Reason: Cardholder Stopped All Billing" in result_text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Cardholder Stopped All Billing"

        elif "Reason: Gateway Rejected: risk_threshold" in result_text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Gateway Rejected: risk_threshold"

        elif ("Reason: We're sorry, but the payment validation failed. Declined - Call Issuer" in result_text or
              "Reason: Declined - Call Issuer" in result_text):
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Declined - Call Issuer"

        elif "ProxyError" in result_text:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = "Proxy Connection Refused"
            await refundcredit(user_id)

        else:
            status = "Declined ❌"
            try:
                response = result.split('"message": "')[1].split('"')[0] + " ❌"
            except:
                response = result
                await result_logs(fullcc, "BRAINTREE AUTH 2", result)
                hits = "NO"

        json_resp = {
            "status": status,
            "response": response,
            "hits": hits,
            "fullz": fullcc,
        }
        return json_resp

    except Exception as e:
        # Handle any other exceptions that occur
        status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
        response = f"Error: {str(e)} ❌\n{traceback.format_exc()}"
        hits = "NO"

        json_resp = {
            "status": status,
            "response": response,
            "hits": hits,
            "fullz": fullcc,
        }
        return json_resp
