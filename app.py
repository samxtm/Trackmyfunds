from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory database to store expenses
expenses = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_expense', methods=['POST'])
def add_expense():
    category = request.form['category']
    amount = float(request.form['amount'])
    date = request.form['date']
    
    # Convert date to a standard format (optional)
    date_obj = datetime.strptime(date, '%Y-%m-%d').strftime('%B %d, %Y')
    
    # Add to in-memory database
    expenses.append({
        'category': category,
        'amount': amount,
        'date': date_obj
    })
    
    return jsonify({'status': 'success', 'message': 'Expense added successfully'})

@app.route('/get_expenses', methods=['GET'])
def get_expenses():
    return jsonify(expenses)

@app.route('/delete_expense', methods=['POST'])
def delete_expense():
    expense_id = int(request.form['id'])
    
    if expense_id < len(expenses):
        expenses.pop(expense_id)
        return jsonify({'status': 'success', 'message': 'Expense deleted successfully'})
    else:
        return jsonify({'status': 'error', 'message': 'Expense not found'})

@app.route('/get_total', methods=['GET'])
def get_total():
    total = sum(expense['amount'] for expense in expenses)
    return jsonify({'total': total})

if __name__ == '__main__':
    app.run(debug=True)
