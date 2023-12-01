from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/get_transactions', methods=['POST'])
def get_transactions():
    data = request.get_json()

    # Read CSV file and filter transactions
    df = pd.read_csv('transactions.csv')
    filtered_transactions = df[(df['user_email'] == data['email']) & 
                                (df['date_of_transaction'] >= data['date1']) & 
                                (df['date_of_transaction'] <= data['date2'])]

    return jsonify(filtered_transactions.to_dict(orient='records'))

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=5001)