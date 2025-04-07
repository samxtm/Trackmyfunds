// Sample expenses data array
let expenses = [];

// Function to display the expenses
function displayExpenses() {
    const expenseTableBody = document.getElementById('expense-table-body');
    expenseTableBody.innerHTML = '';

    expenses.forEach((expense, index) => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${expense.category}</td>
            <td>${expense.amount}</td>
            <td>${expense.date}</td>
            <td><button onclick="deleteExpense(${index})">Delete</button></td>
        `;
        expenseTableBody.appendChild(row);
    });

    // Update total amount
    const totalAmount = expenses.reduce((total, expense) => total + expense.amount, 0);
    document.getElementById('total-amount').innerText = totalAmount.toFixed(2);
}

// Function to add a new expense
document.getElementById('add-btn').addEventListener('click', function() {
    const category = document.getElementById('category-search').value;
    const amount = parseFloat(document.getElementById('amount-input').value);
    const date = document.getElementById('date-input').value;

    if (!category || isNaN(amount) || !date) {
        alert('Please fill in all fields!');
        return;
    }

    const newExpense = {
        category: category,
        amount: amount,
        date: new Date(date).toLocaleDateString()
    };

    expenses.push(newExpense);
    displayExpenses();

    // Clear input fields
    document.getElementById('category-search').value = '';
    document.getElementById('amount-input').value = '';
    document.getElementById('date-input').value = '';
});

// Function to delete an expense
function deleteExpense(index) {
    expenses.splice(index, 1);
    displayExpenses();
}

// Initial call to display any existing expenses
displayExpenses();
