def calculate_discount(price,discount_percent):
    if discount_percent >= 20:
       discount_amount = (price * discount_percent) / 100
       final_price = price - discount_amount
       return final_price
    else:
       return price
final_price = calculate_discount(1000, 20)
print(f"Final price after discount: {final_price}")
    

    

       