from flask import Flask, request, jsonify
import os
import smtplib
from flask_cors import CORS

app = Flask(__name__)

CORS(app, supports_credentials=True)

@app.route('/sendemail', methods=['POST'])
def sendEmail():
    msg = jsonify("Will it work?")
    
    data = request.json

    contact = data.get('contact')
    email = data.get('email')
    name = data.get('name')
    
    #Gmail SMTP server does not allow for the change of who the email was sent from, this was a built in limitation
    HOST = "smtp.gmail.com"
    PORT = 587
    FROM_EMAIL = "test.t94714808@gmail.com"
    TO_EMAIL = "ryan.haddadi81@gmail.com"
    PASSWORD = os.environ.get('SENDER_PASSWORD')
    MESSAGE = "From: " + FROM_EMAIL + "\r\n" 
    MESSAGE += "To: " + TO_EMAIL + "\r\n"
    MESSAGE += "Reply-To: {name}".format(name=name) + "\r\n"
    MESSAGE += "Subject: " + "Question" + "\r\n"
    MESSAGE += "\r\n"
    MESSAGE += "Hi There Ryan" + "\r\n"
    MESSAGE += " " + "\r\n"
    MESSAGE += contact + "\r\n"
    MESSAGE += "  " + "\r\n"
    MESSAGE += "Thanks, {name}".format(name=name) + "\r\n"
    
    msg = jsonify("Success")

    s = smtplib.SMTP(HOST, PORT)

    #elho() tells the server that the user is a SMTP client
    status_code, response = s.ehlo()
    print(f"[*] Echoing the server: {status_code} {response}")


    #StartTLS is a protocol command used to inform the email server that the email client wants to upgrade 
    # from an insecure connection to a secure one using TLS or SSL. 
    status_code, response = s.starttls()
    print(f"[*] Starting tls connection: {status_code} {response}")


    status_code, response = s.login(FROM_EMAIL, PASSWORD)
    print(f"[*] Logging in: {status_code} {response}")


    s.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
    s.quit() 
    
    msg.headers['Access-Control-Allow-Methods'] = 'POST'
    msg.headers['Access-Control-Allow-Origin'] = '*' 
    
    return msg
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)