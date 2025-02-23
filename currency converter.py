conversion_rates = {
    "USD": 0.012,
    "EUR": 0.011,
    "GBP": 0.01}
def convert_currency(amount, currency):
    if currency in conversion_rates:
        return round(amount * conversion_rates[currency], 2)
    else:
        return None

# Function to log the transaction
def log_transaction(amount, currency, converted_amount):
    with open("conversion_log.txt", "a") as file:
        file.write(f"INR {amount} -> {currency} {converted_amount}\n")

# Main function
def main():
    print("Welcome to the Currency Converter!")
    
    try:
        amount = float(input("Enter amount in INR: "))
        currency = input("Enter target currency (USD, EUR, GBP): ").upper()
        converted_amount = convert_currency(amount, currency)
        
        if converted_amount is not None:
            print(f"{amount} INR = {converted_amount} {currency}")
            log_transaction(amount, currency, converted_amount)
        else:
            print("Invalid currency. Please choose from USD, EUR, GBP.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
