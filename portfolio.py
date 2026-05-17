import csv

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

    print("\n" + "="*30)
    print("      PORTFOLIO SUMMARY")
    print("="*30)
    
    for stock, data in portfolio.items():
        print(f"{stock}: {data['quantity']} shares | Total: ${data['value']}")
    
    print("-" * 30)
    print(f"GRAND TOTAL INVESTMENT: ${total_value}")
    print("="*30)
    
      # Optional - Saving the summary to a file
    while True:
        save_choice = input("\nWould you like to save as .txt file? (y/n): ").lower()
        if save_choice == 'y':
            with open("portfolio_summary.txt", "w") as f:
                f.write("Stock Portfolio Summary\n")
                f.write("="*25 + "\n")
                for stock, data in portfolio.items():
                    f.write(f"{stock}: {data['quantity']} shares - ${data['value']}\n")
                    f.write("_"*25 + "\n")
                f.write(f"\nTotal Investment: ${total_value}\n")
            print("Summary saved to 'portfolio_summary.txt'.")
            break
        elif save_choice == 'n':
            print("Summary not saved.")
            break
                
    save_choice = input("\nWould you like to save as .csv file? (y/n): ").lower()
    if save_choice == 'y':
            filename = "portfolio_summary.csv"
            with open(filename, mode='w', newline='') as f:
                writer = csv.writer(f)
                
                writer.writerow(["Stock Symbol", "Quantity", "Total Value ($)"])
            
                for stock, data in portfolio.items():
                    writer.writerow([stock, data['quantity'], data['value']])
                    print("Summary saved to 'portfolio_summary.csv'.")
                    break
    elif save_choice == 'n':
      print("Summary not saved.")
                

if __name__ == "__main__":
    track_portfolio()