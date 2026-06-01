while True:

    print("1. Add Customer")
    print("2. Create Account")
    print("3. Transfer Money")
    print("4. View Transactions")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        import add_customer

    elif choice == "2":
        import create_account

    elif choice == "3":
        import transfer_money

    elif choice == "4":
        import view_transactions

    elif choice == "5":
        break