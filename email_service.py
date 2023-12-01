from flask import Flask, request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

app = Flask(__name__)

#@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.get_json()

    # Send email with PDF attachment
    msg = MIMEMultipart()
    msg['From'] = 'weareinfinite2002@gmail.com'  # Replace with your email
    msg['To'] = data['email']
    msg['Subject'] = 'Bank Statement'

    msg.attach(MIMEText("Please find your bank statement attached."))

    pdf_attachment = MIMEApplication(data['pdf_data'])
    pdf_attachment.add_header('Content-Disposition', 'attachment', filename='bank_statement.pdf')
    msg.attach(pdf_attachment)

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('weareinfinite2002@gmail.com', 'zan20021998')  # Replace with your email and password
        server.sendmail('weareinfinite2002@gmail.com', data['email'], msg.as_string())

    return "Email sent successfully!"

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=5003)
