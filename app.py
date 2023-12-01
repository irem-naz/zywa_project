from flask import Flask, request, render_template, send_file, redirect, url_for
import pandas as pd
from fpdf import FPDF
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


app = Flask(__name__)

data = None

@app.route('/')
def open():
    return render_template('main.html')

@app.route('/', methods=['POST'])
def get_transactions():
    data = request.get_json()
    # Read CSV file and filter transactions
    df = pd.read_csv('transactions.csv')
    filtered_transactions = df[(df['user_email'] == data['email']) &
                               (df['date_of_transaction'] >= data['date1']) &
                               (df['date_of_transaction'] <= data['date2'])]
    
    if filtered_transactions.empty:
        return redirect(url_for('error'),code=302)    
    else:
        pdf_output = "generated_statement.pdf"
        generate_pdf(filtered_transactions, pdf_output)
        return send_file(pdf_output, as_attachment=True)
        

def generate_pdf(filtered_transactions, pdf_output):
    try:
        # Generate PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Times", size=25)
        # Title
        pdf.cell(0, 10, "Transaction History", ln=True, align='C')
        pdf.ln(10)  

        pdf.set_font("Times", size=12)
        # Table header
        pdf.cell(40, 10, "Date", 1)
        pdf.cell(150, 10, "Amount", 1)
        pdf.ln()
        pdf.set_font("Times", size=10)
        # Table rows
        for transaction in filtered_transactions.to_dict(orient='records'):
            pdf.cell(40, 10, str(transaction['date_of_transaction']), 1)
            pdf.cell(150, 10, str(transaction['amount']), 1)
            pdf.ln()

        pdf.output(pdf_output)
        send_email(pdf)
        
    except Exception as e:
        print(f"Error generating PDF: {e}")
        
def send_email(pdf_data):

    # Send email with PDF attachment
    msg = MIMEMultipart()
    msg['From'] = 'weareinfinite2002@gmail.com'  
    msg['To'] = data['email']
    msg['Subject'] = 'Bank Statement'

    msg.attach(MIMEText("Please find your bank statement attached."))
    print("I'm here!")
    pdf_attachment = MIMEApplication(pdf_data)
    pdf_attachment.add_header('Content-Disposition', 'attachment', filename='bank_statement.pdf')
    msg.attach(pdf_attachment)

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.set_debuglevel(1) 
            server.starttls()
            server.login('weareinfinite2002@gmail.com', '12345')  
            server.sendmail('weareinfinite2002@gmail.com', 'weareinfinite2002@gmail.com', msg.as_string())
        print("Email sent successfully!")
        return render_template('confirm.html')
    except Exception as e:
        print("No email :'))")
        return render_template('error.html')


@app.route('/error')
def error():
    return render_template('error.html')    
    
if __name__ == '__main__':
    app.run(debug=True)
    #from waitress import serve
    #serve(app, host="0.0.0.0", port=8080)
