function showIncome() {
    var incomeAdded = parseInt(document.getElementById('addIncome').value);

    return  document.getElementById('incomeAdded').innerHTML = document.getElementById('addIncome').value;
}

function getData() {
    if (input > 10) {
        alert('Danger');
    }
}
function myAlert() {
    window.alert('Alert: Your Expense is too High');
}