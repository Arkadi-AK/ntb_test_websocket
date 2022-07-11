import asyncio
import hashlib
import hmac

from flask import Flask, request
from flask import render_template

from produser import produce

app = Flask(__name__)

key_from_server = 'n5AUbpMiEGV1WvAcgvjFdm75vDqrvFlm884ZN9IEBjJshGgOouCuNx'


def get_hmac_from_email(key: str, email: str):
    key = key.encode('utf-8')
    email = email.encode('utf-8')
    email_hmac = hmac.new(key=key, msg=email, digestmod=hashlib.sha256)
    email_hmac = email_hmac.digest()
    return email_hmac


@app.route('/', methods=['POST', 'GET'])
def index():
    message = "E-mail адрес не введен"
    if request.method == 'POST':
        email = request.form.get('email')
        hmac = get_hmac_from_email(key_from_server, email)
        email = email + ":"
        bytes_email = email.encode('utf-8')
        message = asyncio.run(produce(message=bytes_email + hmac, host='46.229.214.188', port=80))

        if message == b'.':
            message = "OK"
    return render_template('index.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)
