# Exchange rates dictionary
exchange_rates = {
    'PKR': 305.0, 
    'EUR': 0.85,
    'INR': 83.0,
    'JPY': 146.0,
    'USD': 1.0
}

# Get user input for currency conversion
choice = input("Which currency would you like to convert from? (USD, EUR, PKR, INR, JPY): ").upper()   
convert = input("Which currency would you like to convert to? (USD, EUR, PKR, INR, JPY): ").upper()
amount = float(input("Enter the amount you want to convert: "))

# Perform conversion
amount_in_usd = amount / exchange_rates[choice]  # Convert the amount to USD first
converted_amount = amount_in_usd * exchange_rates[convert]  # Convert from USD to the desired currency

# Display the result
print(f"{amount} {choice} is equivalent to {converted_amount:.2f} {convert}")
