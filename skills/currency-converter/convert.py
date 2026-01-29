import sys
import json
import urllib.request

def convert_currency(amount, from_curr, to_curr):
    try:
        url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_curr}&to={to_curr}"
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            
            result = {
                "amount": amount,
                "from": from_curr.upper(),
                "to": to_curr.upper(),
                "converted_amount": data['rates'][to_curr.upper()],
                "rate": data['rates'][to_curr.upper()] / float(amount),
                "date": data['date']
            }
            return json.dumps(result, ensure_ascii=False)
    except Exception as e:
        return json.dumps({"error": str(e)})

if __name__ == "__main__":
    if len(sys.argv) > 3:
        print(convert_currency(sys.argv[1], sys.argv[2], sys.argv[3]))
    else:
        # Default test: 1 USD to CNY
        print(convert_currency(1, "USD", "CNY"))
