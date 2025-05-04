
import requests

def send_otp(phone_number, code):
    api_key = "YOUR_KAVENEGAR_API_KEY"
    url = f"https://api.kavenegar.com/v1/{api_key}/verify/lookup.json"

    params = {
        'receptor': phone_number,
        'token': code,
        'template': 'your_template_name'  
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()
        if data.get("return", {}).get("status") != 200:
            print("Kavenegar Error:", data)
    except Exception as e:
        print("Failed to send SMS:", str(e))
