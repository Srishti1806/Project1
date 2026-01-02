import sys

def calculate_final_price(price, discount):
    """Calculate final price after discount"""
    return price - (discount / 100) * price

def classify_product(final_price):
    """Classify product based on final price"""
    if final_price > 10000:
        return "Premium"
    elif final_price >= 5000:
        return "Standard"
    elif final_price >= 2000:
        return "Budget"
    else:
        return "Economy"

if __name__ == "__main__":

    script_name = sys.argv[0]

    # Check if user provided product details via command-line
    if len(sys.argv) > 5:
        product_id = sys.argv[1]
        product_name = sys.argv[2]
        category = sys.argv[3]
        price = float(sys.argv[4])
        discount = float(sys.argv[5])
        print("User provided product details:")
    else:
        # Default values if no command-line input
        product_id = "P101"
        product_name = "Smartphone"
        category = "Electronics"
        price = 12000
        discount = 10
        print("No input given - using default values:")

    # Calculate final price and classification
    final_price = calculate_final_price(price, discount)
    classification = classify_product(final_price)

    # Display product details
    print("\n========== Product Details ==========")
    print("Script Name      :", script_name)
    print("Product ID       :", product_id)
    print("Product Name     :", product_name)
    print("Category         :", category)
    print("Original Price   : ₹", price)
    print("Discount         :", discount, "%")
    print("Final Price      : ₹", final_price)
    print("Product Category :", classification)
