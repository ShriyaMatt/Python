# Program to calculate the due amount after payment

def calculate_due_amount(bill_amount, amount_paid):
    """
    Calculate the remaining due amount or change to return.
    Returns a tuple: (status, amount)
    status: 'due' if customer still owes money, 'change' if overpaid, 'paid' if exact.
    """
    if amount_paid < bill_amount:
        return "due", bill_amount - amount_paid
    elif amount_paid > bill_amount:
        return "change", amount_paid - bill_amount
    else:
        return "paid", 0.0


def main():
    try:
        # Get bill amount
        bill_amount = float(input("Enter the total bill amount: "))
        if bill_amount < 0:
            print("Bill amount cannot be negative.")
            return

        # Get amount paid
        amount_paid = float(input("Enter the amount paid by the customer: "))
        if amount_paid < 0:
            print("Amount paid cannot be negative.")
            return

        # Calculate due or change
        status, amount = calculate_due_amount(bill_amount, amount_paid)

        # Display result
        if status == "due":
            print(f"Customer still owes: £{amount:.2f}")
        elif status == "change":
            print(f"Return change to customer: £{amount:.2f}")
        else:
            print("Bill paid in full. No due amount.")

    except ValueError:
        print("Invalid input. Please enter numeric values only.")


if __name__ == "__main__":
    main()