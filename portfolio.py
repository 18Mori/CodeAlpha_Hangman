stock_prices = {
    "AAPL": 180,
    "SAF":110,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 400,
    "AMZN": 175,
}

def track_portfolio():
    print("--- Stock Portfolio Tracker ---")
    total_value = 0
    portfolio = {}

    # User input loop to add stocks to the portfolio
    while True:
        symbol = input("\nEnter stock symbol (e.g., AAPL) or type 'done' to finish: ").upper().strip()
        if symbol == 'DONE':
            break
        
        if symbol in stock_prices:
            try:
                quantity = int(input(f"How many shares of {symbol} do you own? "))
                
                price = stock_prices[symbol]
                current_value = quantity * price
                total_value += current_value
                
                # Store for the summary
                portfolio[symbol] = {"quantity": quantity, "value": current_value}
                
                print(f"Added: {quantity} shares of {symbol} @ ${price} each.")
                
            except ValueError:
                print("Please enter a valid number for quantity.")
        else:
            print(f"Stock symbol, '{symbol}' not found in our database.")
            
    for stock, data in portfolio.items():
        print(f"{stock}: {data['quantity']} shares | Total: ${data['value']}")
        
    print(f"GRAND TOTAL INVESTMENT: ${total_value}")
        
if __name__ == "__main__":
    track_portfolio()