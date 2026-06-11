
# FinTech Fraud Detection & Transaction Ledger

## Project Overview   

This project is a simple FinTech application built using **Python** and **MySQL**. It allows users to manage customers, create accounts, perform money transfers, maintain a transaction ledger, and detect potentially fraudulent transactions based on predefined rules.                      

## Features

* Add new customers           
* Create customer accounts   
* Transfer money between accounts
* Store transaction history in a ledger   
* Detect high-value transactions as potential fraud
* Record fraud alerts in a separate table        
* View transaction records    
* View fraud alerts   

## Technology Stack

* Python
* MySQL
* MySQL Connector for Python

## Database Tables

### Customers

Stores customer information.

### Accounts

Stores account details and balances.

### Transactions

Stores all money transfer records.

### Fraud Alerts

Stores suspicious transaction alerts.

## Project Structure

```text  
FinTech_Fraud_Detection/
│
├── database.py
├── main.py
├── add_customer.py
├── create_account.py
├── transfer_money.py
├── view_transactions.py
├── fraud_alerts.py
└── README.md
```

## Setup Instructions

### 1. Create Database

```sql
CREATE DATABASE fintech_db;
USE fintech_db;
```

### 2. Create Required Tables

Execute the SQL scripts available in the project.

### 3. Install Dependency

```bash
pip install mysql-connector-python
```

### 4. Configure Database Connection

Update the MySQL credentials in `database.py`.

```python
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="fintech_db"
)
```

### 5. Run the Application

```bash
python main.py     
```

## Fraud Detection Rule

A transaction is flagged as suspicious when:

* Transaction amount exceeds ₹50,000

When detected, a fraud alert is stored in the `fraud_alerts` table.

## Sample Transaction Flow

1. Add a customer
2. Create an account
3. Transfer money
4. Store transaction in ledger
5. Detect fraud if amount exceeds ₹50,000
6. Record fraud alert

## Learning Outcomes

Through this project, I learned:

* Database design using MySQL
* Python-MySQL integration
* CRUD operations
* Transaction management
* Basic fraud detection logic
* Project organization and modular coding

## Future Enhancements

* User authentication
* Account balance updates
* Multiple fraud detection rules
* Transaction reports
* FastAPI REST APIs
* Dashboard and visualization

## Author

Nandini

Python Backend Developer.
