# customer.py
from banking_operations import BankingOperations

class Customer(BankingOperations):
    def __init__(self):
        super().__init__()

    def withdraw_amount(self, customer_id):
        # Implement Customer-specific withdraw logic

    def deposit_amount(self, customer_id):
        # Implement Customer-specific deposit logic

    def view_balance(self, customer_id):
        # Implement Customer-specific view balance logic
