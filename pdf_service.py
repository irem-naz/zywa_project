from flask import Flask, request, send_file
from fpdf import FPDF

app = Flask(__name__)

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    data = request.get_json()

    # Generate PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    for transaction in data:
        pdf.cell(200, 10, txt=f"Date: {transaction['date_of_transaction']}, Amount: {transaction['amount']}", ln=True)

    pdf_output = "generated_statement.pdf"
    pdf.output(pdf_output)

    return send_file(pdf_output, as_attachment=True)

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=5002)
