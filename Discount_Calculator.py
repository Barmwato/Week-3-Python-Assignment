

#Calculating the Final Price of an item after the discount200

def calculate_discount(price, discount_percent):

    if discount_percent >= 20:
        discount_amount = price * discount_percent / 100
        final_price = price - discount_amount
    else:
        final_price = price

    return final_price

def main():
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)

    print("Final price:", final_price)

if __name__ == "__main__":
    main()