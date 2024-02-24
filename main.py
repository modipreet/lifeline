# main.py
from banking_operations import BankingOperations

def main():
    role = input("Enter your role (Banker/Customer): ").capitalize()
    if role == "Banker":
        user = BankingOperations()
    elif role == "Customer":
        user = BankingOperations()
    else:
        print("Invalid role. Exiting.")
        return

    while True:
        user.display_menu()
        option = input("Enter your choice: ")
        user.execute_option(option, role)

if __name__ == "__main__":
    main()
