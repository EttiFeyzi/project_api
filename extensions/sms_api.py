import requests
from django.conf import settings

def send_otp(otp):
    url = 'https://api.ghasedak.me/v2/verification/send/simple'
    # headers = {'apikey': settings.GHASEDAK_API_KEY}
    body = {
        'receptor': otp.phone,
        'template': '',
        'type': 1,
        'param1': otp.code
    }
    print(body)
    return requests.post(
        url=url,
        data=body,
        # headers=headers
    )
GHASEDAK_API_KEY = '*'





