#Ant Spanish
#CS175-L01
#stocks.py



#Input
purchase_commission_rate=float(input("Commission rate percent on purchase: "))
selling_commission_rate=float(input("Commission rate percent on sell: "))
purchase_commission_rate*=.01
selling_commission_rate*=.01
num_shares_bought=int(input("Number of shares purchased: "))
num_shares_sold=int(input("Number of shares sold: "))
purchase_price=float(input("Purchase price per stock: "))
selling_price=float(input("Sell value per stock: "))

#Processing
stock_purchase_price = num_shares_bought * purchase_price
stock_purchase_commission = purchase_commission_rate * stock_purchase_price

stock_sell_value = num_shares_sold * selling_price
stock_sell_commission = selling_commission_rate * stock_sell_value

total_paid = stock_purchase_price + stock_purchase_commission
total_received = stock_sell_value - stock_sell_commission

profit_loss = total_received - total_paid

#Output
print(f"\nAmount paid for the stock: ${stock_purchase_price:,.2f}")
print(f"Commission paid on the purchase: ${stock_purchase_commission:,.2f}")
print(f"Amount the stock sold for: ${stock_sell_value:,.2f}")
print(f"Commission paid on the sale: ${stock_sell_commission:,.2f}")
print(f"Profit (or loss if negative): ${profit_loss:,.2f}")
