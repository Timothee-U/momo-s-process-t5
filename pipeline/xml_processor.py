import json
import re
from datetime import datetime
from pathlib import Path
import xmltodict

def detect_transaction_type(text: str) -> str:
    """Infer a simple transaction type from SMS text."""
    lowered = text.lower()
    if "your payment of" in lowered or "payment of" in lowered:
        return "PAYMENT"
    if "you have received" in lowered or "received from" in lowered:
        return "RECEIVE"
    if "withdrawal" in lowered or "cash out" in lowered:
        return "WITHDRAWAL"
    if "deposit" in lowered or "cash in" in lowered:
        return "DEPOSIT"
    if "airtime" in lowered:
        return "AIRTIME"
    if "cash power" in lowered or "electricity" in lowered or "utility" in lowered:
        return "UTILITY"
    return "UNKNOWN"


def parse_transaction_text(transaction_text: str) -> dict:
    """
    Extract structured fields from a transaction SMS body.

    Example:
    "TxId: 37832903831. Your payment of 24,900 RWF to Robert Brown 23478 has been completed at 2025-01-16 00:13:22. Your new balance: 4,900 RWF. Fee was 0 RWF."
    """

    tx_id_match = re.search(r"TxId:\s*(\d+)", transaction_text)
    transaction_id = int(tx_id_match.group(1)) if tx_id_match else None

    amount_match = re.search(r"payment of ([\d,]+)\s*([A-Z]{3})", transaction_text, re.IGNORECASE)
    amount = float(amount_match.group(1).replace(",", "")) if amount_match else None
    currency = amount_match.group(2).upper() if amount_match else "RWF"

    recipient_match = re.search(r"to ([^0-9]+)\s+(\d+)", transaction_text)
    recipient_name = recipient_match.group(1).strip() if recipient_match else None
    recipient_phone = recipient_match.group(2) if recipient_match else None

    timestamp_match = re.search(r"at (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})", transaction_text)
    timestamp_str = timestamp_match.group(1) if timestamp_match else None
    timestamp_iso = None
    if timestamp_str:
        dt = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        timestamp_iso = dt.strftime("%Y-%m-%dT%H:%M:%SZ")

    balance_match = re.search(r"new balance:\s*([\d,]+)\s*[A-Z]{3}", transaction_text, re.IGNORECASE)
    new_balance = float(balance_match.group(1).replace(",", "")) if balance_match else None

    fee_match = re.search(r"Fee was\s*([\d,]+)\s*[A-Z]{3}", transaction_text, re.IGNORECASE)
    fee = float(fee_match.group(1).replace(",", "")) if fee_match else None

    tx_type = detect_transaction_type(transaction_text)

    transaction = {
        "transactionId": transaction_id,
        "amount": amount,
        "currency": currency,
        "timestamp": timestamp_iso,
        "status": "COMPLETED",
        "type": tx_type,
        "recipient": {
            "name": recipient_name,
            "phoneNumber": recipient_phone,
        },
        "balance": {"newBalance": new_balance},
        "fee": fee,
        "rawText": transaction_text,
    }

    return transaction


def write_transactions_json(transactions: list[dict], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        json.dump({"transactions": transactions}, f, indent=2)


if __name__ == "__main__":
    # Read and parse XML file
    with open('../storage/input/modified_sms_v2.xml', mode="r") as file:
        raw_data = file.read()
        print(f"Raw data type: {type(raw_data)}")

    sms_dict = xmltodict.parse(raw_data)
    print(f"Parsed dict type: {type(sms_dict)}")
    
    # Access the body from the XML structure
    # Based on your XML structure, the body is in sms_dict['smses']['sms'][index]['@body']
    if 'smses' in sms_dict and 'sms' in sms_dict['smses']:
        sms_messages = sms_dict['smses']['sms']
        
        # If it's a single message, it might not be a list
        if isinstance(sms_messages, dict):
            sms_messages = [sms_messages]
        
        # Find the message with the transaction body
        transaction_body = None
        for sms in sms_messages:
            if '@body' in sms and 'TxId:' in sms['@body']:
                print("I am in here ")
                transaction_body = sms['@body']
                print(f"Found transaction body: {transaction_body}")
                break
        
        if transaction_body:
            body = transaction_body
        else:
            # Fallback to example body if not found
            body = (
                "TxId: 37832903831. Your payment of 24,900 RWF to Robert Brown 23478 has been completed "
                "at 2025-01-16 00:13:22. Your new balance: 4,900 RWF. Fee was 0 RWF."
            )
    else:
        # Fallback to example body if XML structure is different
        body = (
            "TxId: 37832903831. Your payment of 24,900 RWF to Robert Brown 23478 has been completed "
            "at 2025-01-16 00:13:22. Your new balance: 4,900 RWF. Fee was 0 RWF."
        )

    tx = parse_transaction_text(body)
    project_root = Path(__file__).resolve().parents[1]
    output_file = project_root / "storage" / "output" / "transactions.json"
    write_transactions_json([tx], output_file)
    print(f"Wrote 1 transaction with type '{tx.get('type')}' to {output_file}")
